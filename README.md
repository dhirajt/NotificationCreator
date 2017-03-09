# Notification Management Dashboard

Notification Management Dashboard


Tools used
==================================
Favicon : Icon made by [http://www.flaticon.com/authors/dimitry-miroliubov] from www.flaticon.com 

UI Framework used: http://semantic-ui.com/

Datepicker Used: https://github.com/mdehoog/Semantic-UI-Calendar/


Setting Up the project
==================================
1. Create a MySQL database:
   CREATE DATABASE notification_dashboard DEFAULT CHARACTER SET utf8 DEFAULT CHARACTER SET utf8;

2. Install and setup virtualenv[https://virtualenv.pypa.io/] and virtualenvwrapper[https://virtualenvwrapper.readthedocs.io/].

3. Create a virutalenv and install project dependencies:
   - mkvirtualenv notifdash
   - workon notifdash
   - cd notificationdashboard
   - pip install -r requirements/dev.txt

4. Setup configuration:
   Edit config.sh with all the details as shown in config.sh.example.

5. Setup database by running `python manage.py migrate`.

6. django-kronos[https://github.com/jgorset/django-kronos] is being used to periodically lookup and send notifications.
   To setup django-kronos run `python manage.py installtasks`.
   P.S. : Unix crontab edit access is required by this command. If crontab access is denied this step will fail.

7. Run `python manage.py runserver` to run the project.

8. Add notifications via form provided at http://127.0.0.1:8000

9. Look into logs folder for user notification logs.
