
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

1. Open the file.
2. Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Update the title to match the name of your website.

### Running with Docker

Docker instructions pending.

###  Celery

Celery is used for scheduling the periodic uptime checks.

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

Copyright 2023 Pulsely