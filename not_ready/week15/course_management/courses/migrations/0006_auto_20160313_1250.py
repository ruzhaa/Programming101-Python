# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20160313_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='approximate',
            field=models.CharField(max_length=100),
        ),
    ]
