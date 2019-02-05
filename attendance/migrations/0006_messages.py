# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-01 18:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20170920_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('m_from', models.IntegerField()),
                ('m_to', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
    ]
