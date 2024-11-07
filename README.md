# Steps to Run the Project
### 1. Clone the Project and Navigate Inside
```
git clone https://github.com/rs077/django-sample-web-and-rest-api.git
cd django-sample-web-and-rest-api
```
### 2. Create a Virtual Environment
```
python3 -m venv .venv
```
### 3. Activate the Virtual Environment
```
source .venv/bin/activate
```
### 4. Install Required Packages
```
pip install -r requirements.txt
```
### 5. Apply Database Migrations
```
python manage.py migrate
```
### 6. Run the Django Development Server
```
python manage.py runserver
```
### 7. Access the Web App
Open your browser and go to http://localhost:8000/. Sign up and log in to view the D3 chart on the website.

### 8. Access the Browsable API
You can explore the browsable API at http://localhost:8000/api/data/.
