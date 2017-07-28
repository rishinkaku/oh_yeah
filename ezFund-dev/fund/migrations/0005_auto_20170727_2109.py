# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0004_auto_20170726_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='activity_date',
            field=models.DateField(default=datetime.datetime(2017, 7, 27, 13, 9, 55, 937118, tzinfo=utc), verbose_name='活动日期'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='apply_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 27, 13, 9, 55, 937118, tzinfo=utc), verbose_name='申请日期'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='plan_file',
            field=models.FileField(upload_to='%y/%m/%d/plan_file'),
        ),
    ]