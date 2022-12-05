# DjangoBlog
# django-blog-app
It's django based blog app for posting, commenting, sharing information with others.
  
# Instructions 

1) ### Installations
  Python 3 is required to be installed in your pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/nurali0709/DjangoBlog.git`<br>
  
2) ### Installing dependencies 
  Run this command in order to install all the dependencies.<br>
  ```JavaScript
  pip install -r requirements.txt
  ```
  
3) ### Migrations 
  Then run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
4) ### Create superuser
  After create superuser. <br>
  `python manage.py createsuperuser` <br>
  You can access admin panel from `127.0.0.1:8000/admin/`

4) ### Running locally
  `python manage.py runserver` 
