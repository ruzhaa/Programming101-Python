# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160309_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='end_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courses',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]
