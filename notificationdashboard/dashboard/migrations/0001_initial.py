# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=150, verbose_name=b'header')),
                ('content', models.CharField(max_length=300, verbose_name=b'content')),
                ('image_url', models.URLField()),
                ('notify_time', models.DateTimeField(db_index=True)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notified', models.BooleanField(default=False)),
                ('notification', models.ForeignKey(to='dashboard.Notification')),
                ('user', models.ForeignKey(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserNotification',
                'verbose_name_plural': 'UserNotifications',
            },
        ),
    ]
