
    Check if foreign key checks are enabled: PRAGMA foreign_keys
    Enable foreign key checks: PRAGMA foreign_keys = 1
    Disable foreign key checks: PRAGMA foreign_keys = 0

How to run the app
pip install -r requirements.txt  to install the requirements
python manage.py runserver to run the django app if there are no sql migrations

Please uncomment the ACCOUNT_SID and AUTH_TOKEN FIELD in the settings.py file when you have cloned your project in your local PC for twilio to work. We have done this because twilio doesn't want us to expose its credentials on public repos

