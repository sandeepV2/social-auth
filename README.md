# social-auth
Project gives a simplest step by step guide to add sign in via goole authentication.

1. Clone this repository.

2. Create vitual env (with python 3) and activate it.
```python
python -m venv login-env
source login-evn/bin/activate # Note this is for Mac/Linux
``` 

4. Install  django and social authentication package. 
```python
pip install django==4.0.5
pip install social-auth-app-django==5.0.0
```
5. Add your google client key and secre key in **login/login/settings.py**

Note : Make sure you added below redirect url in google OAUTH config. 

Autherized redirect URIs : http://localhost:8000/social-auth/complete/google-oauth2/ 

7. Make migrations and run server to deploy it locally.
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

8. Access your server with google auth at http://localhost:8000 

!! HAPPY CODING !!
