# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-03-21 20:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='fav_num',
            new_name='fav_nums',
        ),
    ]
