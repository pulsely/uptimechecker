
# Uptime Checker Server by Pulsely

![Uptime Checker Server Screenshot](https://pulsely.github.io/products/uptime-checker/images/screenshot.png)

__Uptime Checker Server__ is a Django powered app developed by [Pulsely](https://www.pulsely.com/). __Uptime Checker__ monitors your websites for any downtime, as well as SSL expiration dates.

Any down times can be notified by:
- E-mails
- Websocket Notifications
- <strike>Slack channel notifications</strike> (Coming soon!)
- <strike>Push Notifications</strike> (Coming soon!)
- <strike>SMS Notifications</strike> (Coming soon!)

For more information, please refer to the [Uptime Checker](https://www.pulsely.com/products/uptime-checker/) product page.

---

## Running the Uptimer

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

### Graphics

Admin panel template is provided by CoreUI  
Copyright 2022 creativeLabs Łukasz Holeczek. Code released under the MIT License   
https://github.com/coreui/coreui


---

# Copyright and license

Copyright 2023 Pulsely