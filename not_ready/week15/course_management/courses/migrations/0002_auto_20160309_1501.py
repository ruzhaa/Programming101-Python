# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
