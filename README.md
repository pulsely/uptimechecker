
# Uptime Checker by Pulsely

Uptime Checker is a Django powered app developed by [Pulsely](https://www.pulsely.com/).
Uptime Checker monitors your websites for any downtime, as well as SSL expiration dates.

Any down times can be notified by:
- E-mail
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

---

###

# Celery

Celery is used for scheduling the periodic uptime checks.



---

# Credits & Acknowledgements

### Python packages

Django  
https://www.djangoproject.com/

Django Rest Framework  
https://www.django-rest-framework.org/

Celery  
https://github.com/celery/celery

### Graphics

Admin panel template is provided by CoreUI  
https://github.com/coreui/coreui


