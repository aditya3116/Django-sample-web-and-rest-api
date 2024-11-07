import json
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('sample_data/data.js') as file:
            data = json.load(file)
        context['data'] = data
        return context
    
class JSONDataView(APIView):
    def get(self, request, *args, **kwargs):
        with open('sample_data/data.js') as file:
            data = json.load(file)
        return Response(data)
