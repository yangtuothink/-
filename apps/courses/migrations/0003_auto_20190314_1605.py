# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-03-14 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courseresource_lesson_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='students',
        ),
    ]
