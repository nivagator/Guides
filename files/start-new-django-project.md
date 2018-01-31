## How To Begin a New Django project

#### Assuptions:
- Ubuntu Linux server environment (or similar)
- virtualenv and virtualenvwrapper installed

### Server-Side Setup
1. Create virtualenv
`mkvirtualenv project-name`

2. Install Django
`pip install django`

3. Start new Django project
`django-admin startproject project-name`

4. Update settings.py
- add host IP address to the `ALLOWED_HOSTS`
- add custom database solution if required

5. Make migrations
`python manage.py makemigrations`

5. Create superuser
`python manage.py createsuperuser`

6. Verify site
`python manage.py runserver 0:8000`

7. Start new Django app
`python manage.py startapp app-name`



### Dev Environment Setup (VSCode)
1. Create folder for project
2. Open folder in VSCode
3. Set up sftp.json file SFTP:Config - point to project folder on remote Server
4. Download project files
5. Profit
