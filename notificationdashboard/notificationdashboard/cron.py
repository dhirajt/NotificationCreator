# -*- coding: utf-8 -*-
import os
import sys
import kronos
import random
import logging
import datetime
import django

if not os.environ['DJANGO_SETTINGS_MODULE']:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'notification.dashboard.prod'
django.setup()

from dashboard.models import Notification, UserNotification

from logging.handlers import RotatingFileHandler

def setup_logging():
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(os.path.join(PROJECT_PATH,'logs')):
        os.mkdir(os.path.join(PROJECT_PATH,'logs'))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    ch = RotatingFileHandler(
        filename=os.path.join(PROJECT_PATH,'logs','cron.log'),
        maxBytes=100000,
        backupCount=1)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger

@kronos.register('* * * * *')
def send_notifications():
    logger = setup_logging()
    user_notifications = UserNotification.objects.select_related(
        'user','notification').filter(notified=False, notification__notify_time__lte=datetime.datetime.now())
    logger.info("Started send notification job ...")
    for user_notification in user_notifications:
        payload = {
            'header': user_notification.notification.header,
            'content': user_notification.notification.content,
            'image_url': user_notification.notification.image_url,
        }
        send_notification(user_notification.user_id, payload)
        UserNotification.objects.filter(id=user_notification.id).update(notified=True)

        logger.info("Notified user notification id: " + str(user_notification.id))
    logger.info("Completed send notification job ...")


def send_notification(user_id, notification_payload):
    return True
