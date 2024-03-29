
# Uptime Checker by Pulsely

![Uptime Checker Screenshot](https://pulsely.github.io/products/uptime-checker/images/screenshot.png)

__Uptime Checker__ is a Django powered app developed by [Pulsely](https://www.pulsely.com/). __Uptime Checker__ monitors your websites for any downtime, as well as SSL expiration dates.

Any down times can be notified by:
- E-mails
- Slack channel notifications
- <strike>Websocket Notifications</strike> (Coming soon!)
- <strike>Push Notifications</strike> (Coming soon!)
- <strike>SMS Notifications</strike> (Coming soon!)

For more information, please refer to the [Uptime Checker](https://www.pulsely.com/products/uptime/checker/) product page.

---

## Running the Uptime Checker

You can run Uptime Checker directly with a Python virtual environment, or with Docker.

### Running with Python Virtual Environment

The best way would be to create a new Python virtual environment. Any Python with version 3.8 should work.
The only dependency would be an active Redis 4.0+ installation.

* Pull the source code of Uptime Checker:
  ```sh
  git clone https://github.com/pulsely/uptimechecker
  ```

* Changed to the directory of the Uptime Checker:
  ```sh
  cd uptimechecker
  ```

* Create a new python virtual environment and install the packages from requirements.txt:
  ```sh
  python -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
  ```
(Your Python 3 runtime could be named differently, such as 'python3', so change to ```python3 -m venv venv``` if this is the case.)

* Then run the uptime checker:
  ```sh
  python manage.py runserver
  ```
  The manage.py will check if a .env file is create and create one for you automatically if missing. The db.sqlite3 file will also be created for you 4 seconds after the installation is fired up the first time.

* You can run your Uptime Checker installation in development mode with the Make command ```make dev``` from now on, or activate the venv virtual environment created previously with these commands:
  ```sh
  source ./venv/bin/activate
  python manage.py runserver
  ```


### Running with Docker

The Uptime Checker has a default DockerFile which will run with Docker or Podman in development mode.

* The Docker setup will run the Uptime Checker with Django, Redis and Celery, and run the first run setup automatically.

  ```sh
  docker-compose up
  ```

* To run the Docker setup in daemon mode:

  ```sh
  docker-compose up -d
  ```

---

###  Celery

Celery is used for scheduling the periodic uptime checks.

A sample Make command will trigger the celery for recurring checks with minutes specified in ``DEFAULT_PERIODIC_MINUTES`` with the .env configuration:  
```make celery``` 

---

### Django settings that can be configured and overwritten

These settings are stored at the ``.env`` file and can be overwriten at the default Django settings at ```uptimechecker/settings_customized.py``` which should be created on first run.

| **Varaiable** | **Description**                                                             | **Defaults**                                                                                                           |
| ------------- |-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ``SECRET_KEY`` | The secret key for Django user authentication                               | ``Random key generated automatically``                                                                                 |
| ``DEBUG``          | Django DEBUG mode for development. Set to false for deployment              | ``true``                                                                                                               |
| ``ALLOWED_HOSTS``   | Host/domain names that this Django site can serve.                          | ``*``                                                                                                                  |
| ``DEFAULT_USER_AGENT`` | Default user agent for sending the HTTP request for uptime check            | ``Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15`` |
| ``DEFAULT_PERIODIC_MINUTES`` | Number of minutes to refresh all websites checks                            | ``15``                                                                                                                 |
| ``DEFAULT_ADD_RANDOMNESS`` | Add some random delay of 1 to 30 seconds for each HTTP requests. Disable by default. | ``false``                                                                                                              |
| ``EMAIL_BACKEND`` | The default E-mail backend, set to django-ses for AWS deployment            | ``django_ses.SESBackend``                                                                                              |
| ``AWS_SES_REGION_NAME`` | Default AWS SES region Name                                                 | ``us-west-2``                                                                                                          |
| ``AWS_SES_REGION_ENDPOINT`` | Default AWS SES region endpoint                                             | ``email.us-west-2.amazonaws.com``                                                                                      |
| ``SERVER_EMAIL`` | E-mail for sending the notification emails                                  |                                                                                                                   |
| ``SLACK_TOKEN`` | Slack Team Token                                                            |                                                                                      |
| ``SLACK_ROOM`` | Room to show the error Slack message.                                       | ``#general``                                                                                                           |


---
## Special notes on deployment

If you deploy to production such as Nginx with Supervisord, you will need to overwrite the default ``CSRF_TRUSTED_ORIGINS`` variable at the file ``uptimechecker/settings_customized.py``.

Configuration details of the ``CSRF_TRUSTED_ORIGINS`` is available at [Django website](https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-trusted-origins)

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
mail_test
reset
```

```python manage.py checksites``` will trigger website checks. You can run a cronjob to trigger the checks with Crontab, instead of running the Celery.

```python manage.py remove_expired_uptimes``` will remove expired check results.

```python manage.py mail_test``` can be used for sending test e-mail(s) to check your notification configurations.

```python manage.py reset``` will remove the .env, db.sqlite3, celerybeat-schedule and uptimechecker/settings_customized.py configuration files to reset your installation.   
**(Only available for DEBUG mode on.)**

---

## Running databases other than SQLite?

You can use any databases supported by Django. Create the database settings at the uptimechecker/settings.py file following the Django documentations, and you should be good to go.

---

# Credits & Acknowledgements

This project utilizes the following components:

### Python packages

* __Celery__  
  Copyright (c) 2015-2016 Ask Solem & contributors.  All rights reserved.
  Copyright (c) 2012-2014 GoPivotal, Inc.  All rights reserved.
  Copyright (c) 2009, 2010, 2011, 2012 Ask Solem, and individual contributors.  All rights reserved.
  BSD 3-Clause "New" or "Revised" License  
  https://github.com/celery/celery

* __Django__  
  Copyright (c) Django Software Foundation and individual contributors.   
  All rights reserved.   
  https://www.djangoproject.com/

* __Django Rest Framework__  
  Copyright © 2011-present, Encode OSS Ltd. All rights reserved.  
  https://www.django-rest-framework.org/

* __Django SES__  
  Copyright (c) 2011 Harry Marr  
  MIT license  
  https://github.com/django-ses/django-ses

* __Font Awesome__  
  CC BY 4.0 License  
  https://github.com/FortAwesome/Font-Awesome

* __python-decouple__  
  Copyright (c) 2013 Henrique Bastos, MIT license  
  https://github.com/HBNetwork/python-decouple

### JavaScript Frameworks

* __Vue.js__  
  MIT license  
  https://github.com/vuejs

* __Axios__  
  MIT license  
  https://github.com/axios/axios

### Graphics

* __Admin panel template is provided by CoreUI__  
  Copyright 2022 creativeLabs Łukasz Holeczek. Code released under the MIT License   
  https://github.com/coreui/coreui


---

# Copyright and license

The Uptime Checker is written by Pulsely https://www.pulsely.com/

Copyright 2023 Pulsely

This program is free software: you can redistribute it and/or modify it under the terms of the Server Side Public License, version 1, as published by MongoDB, Inc.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Server Side Public License for more details.

You should have received a copy of the Server Side Public License along with this program. If not, see

http://www.mongodb.com/licensing/server-side-public-license

As a special exception, the copyright holders give permission to link the code of portions of this program with the OpenSSL library under certain conditions as described in each individual source file and distribute linked combinations including the program with the OpenSSL library. You must comply with the Server Side Public License in all respects for all of the code used other than as permitted herein. If you modify file(s) with this exception, you may extend this exception to your version of the file(s), but you are not obligated to do so. If you do not wish to do so, delete this exception statement from your version. If you delete this exception statement from all source files in the program, then also delete it in the license file.

