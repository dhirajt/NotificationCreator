# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    header = models.CharField("header", max_length=150)
    content = models.CharField("content", max_length=300)
    image_url = models.URLField()
    notify_time = models.DateTimeField(db_index=True)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __unicode__(self):
        return u"<%s - %s>" % (self.id, self.header)


class UserNotification(models.Model):
    notification = models.ForeignKey(
        Notification, on_delete=models.CASCADE)
    notified = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')

    class Meta:
        verbose_name = "UserNotification"
        verbose_name_plural = "UserNotifications"

    def __unicode__(self):
        return u"<%s - %s>" % (self.notification.id, self.user.id)

