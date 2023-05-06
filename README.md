
# Uptime Checker Server by Pulsely

![Uptime Checker Server Screenshot](https://pulsely.github.io/products/uptime-checker/images/screenshot.png)

__Uptime Checker Server__ is a Django powered app developed by [Pulsely](https://www.pulsely.com/). __Uptime Checker__ monitors your websites for any downtime, as well as SSL expiration dates.

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

Create a new python virtual environment with:
```
python -m venv venv
source ./venv/bin/activate
```

Then run the uptime checker:
```
python manage.py runserver
```

You can also run your Uptime Checker installation with the shell script ```./run_django_dev.sh```


### Running with Docker

The Uptime Checker has a default DockerFile which will run with Docker or Podman.

The setup will run the Uptime Checker with Django, Redis and Celery automatically.

---

###  Celery

Celery is used for scheduling the periodic uptime checks.

A sample shell script will trigger the celery for recurring checks with minutes specified in DEFAULT_PERIODIC_MINUTES at the .env configuration:  
```./run_celery_dev.sh``` 

---

## Django Management Commands



Type ```python manage.py``` to check these Django commands are available for testing and house cleaning.
```
checksites
remove_expired_uptimes
test_ses_email
```

```python manage.py checksites``` will trigger website checks. You can run a cronjob to trigger the checks with Crontab, instead of running the Celery.

```python manage.py remove_expired_uptimes``` will remove expired check results.

```python manage.py test_ses_email``` can be used for sending test e-mail(s) to check your notification configurations.


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