# -*- coding: utf-8 -*-
from django import forms
from django.db import connection

from django.utils import timezone

UNSAFE_COMMANDS = [
    'create', 'alter', 'drop', 'truncate', 'comment', 'rename', 'insert',
    'delete', 'update', 'merge', 'call', 'grant', 'revoke', 'commit',
    'rollback', 'savepoint', 'set']

class NotificationForm(forms.Form):
    header = forms.CharField(label="Header", min_length=20, max_length=150)
    content = forms.CharField(label="Content", min_length=20,max_length=300)
    image_url = forms.URLField(label="URL")
    notification_time = forms.DateTimeField(['%B %d, %Y %I:%M %p'])
    query = forms.CharField(label="Query")

    def clean_notification_time(self):
        notification_time = self.cleaned_data['notification_time']
        if notification_time < timezone.now():
            raise forms.ValidationError(
                "Notification cannot be scheduled before current time.")
        return notification_time

    def clean_query(self):
        query = self.cleaned_data['query']
        contains_unsafe_commands = [True for i in UNSAFE_COMMANDS if i in query.lower()]
        if not query or any(contains_unsafe_commands):
            raise forms.ValidationError(
                "Query contains unsafe commands. Use a valid SELECT statement.")

        # use first query if there are more than one query
        query = query.split(';')[0]
        if 'select' not in query.lower():
            raise forms.ValidationError(
                "Query doesn't contain a valid SELECT statement.")

        rows = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        try:
            user_ids = [int(i[0]) for i in rows if i]
        except ValueError:
            raise forms.ValidationError(
                "Query doesn't return valid user ids.")
        return query
