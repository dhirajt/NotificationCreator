# -*- coding: utf-8 -*-
import humanize
import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from .models import Notification, UserNotification

from .forms import NotificationForm

def home(request):
    notifications = []
    for notification in Notification.objects.all():
        time_format = datetime.datetime.strftime(
            notification.notify_time, '%B %d, %Y at %I:%M %p')
        notifications.append({
            'notification_header':notification.header,
            'notification_content':notification.content,
            'notification_image':notification.image_url,
            'notification_time_formatted': time_format,
            'notification_time_string': humanize.naturaltime(
                notification.notify_time.replace(tzinfo=None)),
        })
    return render(
        request,template_name="home.html",context={'notifications':notifications})


@require_http_methods(["POST"])
def notification_form_handler(request):
    notification_form = NotificationForm(request.POST)
    error_message = ''
    if notification_form.is_valid():
        rows = []
        with connection.cursor() as cursor:
            cursor.execute(notification_form.cleaned_data['query'])
            rows = cursor.fetchall()
        user_ids = [int(i[0]) for i in rows if i]

        notification = Notification.objects.create(
            header=notification_form.cleaned_data['header'],
            content=notification_form.cleaned_data['content'],
            image_url=notification_form.cleaned_data['image_url'],
            notify_time=notification_form.cleaned_data['notification_time']
        )

        for user_id in user_ids:
            UserNotification.objects.create(
                notification=notification,
                notified=False,
                user_id=user_id
            )

        time_format = datetime.datetime.strftime(
            notification.notify_time, '%B %d, %Y at %I:%M %p')
        feed_response_context = {
            'notification_header':notification.header,
            'notification_content':notification.content,
            'notification_image':notification.image_url,
            'notification_time_formatted': time_format,
            'notification_time_string': humanize.naturaltime(
                notification.notify_time.replace(tzinfo=None)),
        }

        feed_response = render_to_string(
            "notification_event.html",feed_response_context)
        return JsonResponse({
            "status":"success",
            "feed_response": feed_response
            })
    else:
        error_message = notification_form.errors.as_ul()
        return JsonResponse({
            "status":"error",
            "message": error_message
            }, status=500)
