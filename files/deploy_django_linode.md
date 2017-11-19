[uWSGI](https://www.linode.com/docs/security/backups/backing-up-your-data)  
[Linode](https://www.linode.com/docs/web-servers/nginx/deploy-django-applications-using-uwsgi-and-nginx-on-ubuntu-14-04)  
[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)  
[Setting up NGINX + Django + uWSGI](http://blog.richard.do/index.php/2013/04/setting-up-nginx-django-uwsgi-a-tutorial-that-actually-works/)  
[Setting up Nginx, uWSGI & Python3](https://gist.github.com/simoncoulton/2625954)
[Using uwsgi the right way](http://guoqiao.farbox.com/post/2014/0416-use-uwsgi-the-right-way)

## Deploy with nginx and uwsgi
[Monica Lent](http://monicalent.com/blog/2013/12/06/set-up-nginx-and-uwsgi/)  
[uwsgi-docs](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)  
[stop uwsgi in emperor mode](http://lists.unbit.it/pipermail/uwsgi/2012-February/003560.html)  
[Django docs uwsgi](http://lists.unbit.it/pipermail/uwsgi/2012-February/003560.html)  

1. Import site files
  - Destination: `/home/[user]/[project]/src`
  - [git](auto-deploy-github.md)/ftp
2. Create virtualenv
  - using virtualenvwrapper, `mkvirtualenv [project]`
  - create and load using requirements file using `mkvirtualenv -r /path/to/project/requirements.txt [project]`
  - force python3 if necessary `mkvirtualenv --python=/usr/bin/python3 -r /home/[user]/[project]/src/[app]/requirements.txt [project]`
3. pip install from requirements.txt
  - this can be done as part of the virtualenv deployment or manually after
  - be careful to install through the correct python pip version
  - Make sure you have uWSGI installed `pip install uwsgi`
4. Create media and static directories
  - Option 1: part of the project folder at `/home/[user]/[project]/`
  - Option 2: part of the typical webserver deployment at `/var/www/[project]`
  - Option 3: as part of a CDN like AWS S3 (need content)
5. Edit settings.py to set `STATIC_ROOT = os.path.join(BASE_DIR, "static/")` and run `python manage.py collectstatic`
  - You can also use an explicit file path: `/var/www/example.com/static/` or `/home/[user]/[project]/static`
6. Create socket file at `/var/uwsgi/[app].sock` and update permissions/owner
  - `sudo chown www-data /var/uwsgi/[app].sock`
  - `sudo chmod og+rw /var/uwsgi/[app].sock`
7. If not already created, make a uwsgi directory at `/var/log/` and update permissions
  - `sudo chmod og+rw /var/log/uwsgi`
7. Create `nginx.conf` file and add file link to `/etc/nginx/sites-enabled`
  - `sudo ln -s /home/[user]/[project]/[app]_nginx.conf /etc/nginx/sites-enabled`
8. Create `uwsgi.ini` file and add file link to  `/etc/uwsgi/vassals`
  - `sudo ln -s /home/[user]/[project]/[app]_uwsgi.ini /etc/uwsgi/vassals`
9. Restart Nginx with `sudo service nginx restart`
10. Reload uwsgi pid file `uwsgi --reload /tmp/[app].pid`


### Note: if serving multiple apps on the same server, each must have a unique `upstream` designation in the nginx.conf file.

#### Scenario
For the following files, my environment did use virtualenvwrapper and my project file path was as follows:

app location:   `/home/[user]/[project]/src/manage.py`  
wsgi file:      `/home/[user]/[project]/src/[app]/wsgi.py`  
media:          `/home/[user]/[project]/media`  
static:         `/home/[user]/[project]/src/static-serve`  
virtualenv home `/home/[user]/Env/[project]`  

#### permissions are key  
uWSGI Emperor mode runs as the www-data user, set permissions accordingly.  
This applies to the socket file, pid file, log file and specifically the sqlite db file.  

#### unix socket file
- place file in `/var/uwsgi/[app].sock`
- set og+rw and owner to www-data

#### [nginx.conf file](app_nginx.conf)
```
# [app]_nginx.conf
upstream django-[app] {
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
    location /static {
        alias /home/[user]/[project]/static; # your Django project's static files
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django-[app];
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
pidfile         = /tmp/[app].pid # including a pid file allows you to reload this app easily
daemonize       = /var/log/uwsgi/[app].log # log file allows for debugging prod
```
#### Troubleshooting
- 502 Bad Gateway
  - nginx is working but uwsgi is not  
- 500 Server Error
  - check recursive file permissions for the src folder, specifically the db.sqlite3 file if using sqlite
