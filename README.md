
# Uptime Checker by Pulsely

![Uptime Checker Screenshot](https://pulsely.github.io/products/uptime-checker/images/screenshot.png)

__Uptime Checker__ is a Django powered app developed by [Pulsely](https://www.pulsely.com/). __Uptime Checker__ monitors your websites for any downtime, as well as SSL expiration dates.

Any down times can be notified by:
- E-mails
- <strike>Websocket Notifications</strike> (Coming soon!)
- <strike>Slack channel notifications</strike> (Coming soon!)
- <strike>Push Notifications</strike> (Coming soon!)
- <strike>SMS Notifications</strike> (Coming soon!)

For more information, please refer to the [Uptime Checker](https://www.pulsely.com/products/uptime-checker/) product page.

---

## Running the Uptime Checker

You can run Uptime Checker directly with a Python virtual environment, or with Docker

### Running with Python Virtual Environment

The best way would be to create a new Python virtual environment. Any Python with version 3.8 should work.
The only dependency would be an active Redis 4.0+ installation.

Pull the source code of Uptime Checker:
```
git clone https://github.com/pulsely/uptimechecker
```

Changed to the directory of the Uptime Checker:
```
cd uptimechecker
```

Create a new python virtual environment and install the packages from requirements.txt:
```
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
(Your Python 3 runtime could be named differently, such as 'python3', so change to ```python3 -m venv venv``` if this is the case.)

Then run the uptime checker:
```
python manage.py runserver
```
The manage.py will check if a .env file is create and create one for you automatically if missing. The db.sqlite3 file will also be created for you 4 seconds after the installation is fired up the first time.

You can run your Uptime Checker installation with the shell script ```./run_django_dev.sh``` from now on, or activate the venv virtual environment created previously with these commands:
```
source ./venv/bin/activate
python manage.py runserver
```


### Running with Docker

The Uptime Checker has a default DockerFile which will run with Docker or Podman.

The Docker setup will run the Uptime Checker with Django, Redis and Celery, and run the first run setup automatically.

```
docker-compose up
```

---

###  Celery

Celery is used for scheduling the periodic uptime checks.

A sample shell script will trigger the celery for recurring checks with minutes specified in DEFAULT_PERIODIC_MINUTES at the .env configuration:  
```./run_celery_dev.sh``` 

---

### Django settings that can be overwritten

You should overwrite the default Django settings at ```uptimechecker/settings_customized.py``` which should be created on first run.

| **Varaiable** | **Description** | **Defaults**                                                                                                           |
| ------------- | ------------- |------------------------------------------------------------------------------------------------------------------------|
| ``SECRET_KEY`` |  | ``Random key generated automatically``                                                                                 |
| ``DEBUG``          | | ``true``                                                                                                               |
| ``ALLOWED_HOSTS``   |  | ``*``                                                                                                                  |
| ``DEFAULT_USER_AGENT`` | | ``Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15`` |
| ``DEFAULT_PERIODIC_MINUTES`` | | ``5``                                                                                                                  |
| ``EMAIL_BACKEND`` | | ``django_ses.SESBackend``                                                                                                                  |
| ``AWS_SES_REGION_NAME`` | | ``us-west-2``                                                                                                                  |
| ``AWS_SES_REGION_ENDPOINT`` | | ``email.us-west-2.amazonaws.com``                                                                                                                  |
| ``SERVER_EMAIL`` | | ````                                                                                                                  |


---

## Django Management Commands



Type ```python manage.py``` to check for the default Django management commands available:

```
migrate
createsuperuser
changepassword
```

```python manage.py migrate``` will create database schema on your database settings. It should automatically run by manage.py the first time though.

```python manage.py createsuperuser``` allows you to create superuser at the command line.

```python manage.py changepassword``` let you change password for any user in the system.

These Uptime Checker commands are available for testing and house cleaning.
```
checksites
remove_expired_uptimes
test_ses_email
reset
```

```python manage.py checksites``` will trigger website checks. You can run a cronjob to trigger the checks with Crontab, instead of running the Celery.

```python manage.py remove_expired_uptimes``` will remove expired check results.

```python manage.py test_ses_email``` can be used for sending test e-mail(s) to check your notification configurations.

```python manage.py reset``` will remove the .env, db.sqlite3 and uptimechecker/settings_customized.py configuration files to reset your installation.   
**(Only available for DEBUG mode on.)**

---

## Running databases other than SQLite?

You can use any databases supported by Django. Create the database settings at the uptimechecker/settings.py file following the Django documentations, and you should be good to go.

---

# Credits & Acknowledgements

### Python packages

__Django__  
Copyright (c) Django Software Foundation and individual contributors.   
All rights reserved.   
https://www.djangoproject.com/

__Django Rest Framework__  
Copyright © 2011-present, Encode OSS Ltd. All rights reserved.  
https://www.django-rest-framework.org/

__Celery__  
BSD 3-Clause "New" or "Revised" License   
https://github.com/celery/celery

__Font Awesome__  
CC BY 4.0 License
https://github.com/FortAwesome/Font-Awesome

__python-decouple__
MIT license
https://github.com/HBNetwork/python-decouple

### Graphics

Admin panel template is provided by CoreUI  
Copyright 2022 creativeLabs Łukasz Holeczek. Code released under the MIT License   
https://github.com/coreui/coreui


---

# Copyright and license

The Uptime Checker is written by Pulsely https://www.pulsely.com/

Copyright 2023 Pulsely