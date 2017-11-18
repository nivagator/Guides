[uWSGI](https://www.linode.com/docs/security/backups/backing-up-your-data)  
[Linode](https://www.linode.com/docs/web-servers/nginx/deploy-django-applications-using-uwsgi-and-nginx-on-ubuntu-14-04)  
[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)  

## Deploy with nginx and uwsgi
[Monica Lent](http://monicalent.com/blog/2013/12/06/set-up-nginx-and-uwsgi/)  
[uwsgi-docs](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)  
[stop uwsgi in emperor mode](http://lists.unbit.it/pipermail/uwsgi/2012-February/003560.html)  
[Django docs uwsgi](http://lists.unbit.it/pipermail/uwsgi/2012-February/003560.html)  

1. Import site files.
  - git/ftp

  
#### create virtualenv
#### pip install from requirements.txt


2. Create media and static directories
3. Edit settings.py to set `STATIC_ROOT = os.path.join(BASE_DIR, "static/")` and run `python manage.py collectstatic`
4. Create socket file at `/var/uwsgi/[app].sock` and update permissions/owner
  - `sudo chown www-data /var/uwsgi/[app].sock`
  - `sudo chmod og+rw /var/uwsgi/[app].sock`
5. Create `nginx.conf` file and add file link to `/etc/nginx/sites-enabled`
  - `sudo ln -s /home/[user]/[virtualenv]/[app]_nginx.conf /etc/nginx/sites-enabled`
6. Create `uwsgi.ini` file and add file link to  `/etc/uwsgi/vassals`
  - `sudo ln -s /home/[user]/[virtualenv]/[app]_uwsgi.ini /etc/uwsgi/vassals`
8. Restart Nginx with `sudo service nginx restart`

#### Scenario
For the following files, my environment did not use virtualenvwrapper and my project file path was as follows:

app location:   `/home/[user]/[virtualenv]/src/manage.py`  
wsgi file:      `/home/[user]/[virtualenv]/src/[app]/wsgi.py`  
media:          `/home/[user]/[virtualenv]/media`  
static:         `/home/[user]/[virtualenv]/src/static-serve`  
virtualenv home `/home/[user]/[virtualenv]`  

permissions are key  
emperor mode runs as the www-data user, set permissions accordingly

#### unix socket file
- place file in `/var/uwsgi/[app].sock`
- set og+rw and owner to www-data

#### [nginx.conf file](app_nginx.conf)
```
# [app]_nginx.conf
upstream django {
    server unix:///var/uwsgi/[app].sock; # for a file socket
    # server 127.0.0.1:8001; # for a web port socket
}

# configuration of the server
server {
    listen      80; # the port your site will be served on
    server_name www.example.com example.com; # domain name - substitute your machine's IP address or FQDN
    charset     utf-8;
    client_max_body_size 75M;  # max upload size adjust to taste

    # Django media
    location /media  {
        alias /home/[user]/[project]/media;  # your Django project's media files
    }
    # Django static files
    location /static/ {
        alias /home/[user]/[project]/src/static-serve; # your Django project's static files
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /home/[user]/[project]/uwsgi_params; # nginx uwsgi_params
    }
}
```
#### [uwsgi.ini file](app_uwsgi.ini)
```
# [app]_uwsgi.ini file
[uwsgi]

# Django-related settings
chdir           = /home/[user]/[project]/src # the base directory (full path)
module          = [app].wsgi:application # Django's wsgi file
home            = /home/[user]/[project] # the virtualenv (full path) or Env virtualenvwrapper home

# process-related settings
master          = true
processes       = 10 # maximum number of worker processes

# the socket (use the full path to be safe
# socket          = /home/[user]/[project]/lnkto.sock # used for testing
socket		= /var/uwsgi/lnkto.sock # used for emperor mode

chmod-socket    = 666
vacuum          = true # clear environment on exit
```
