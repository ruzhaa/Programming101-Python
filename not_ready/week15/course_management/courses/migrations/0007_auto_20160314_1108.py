# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20160313_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('lecture', models.CharField(max_length=50)),
                ('week', models.IntegerField()),
                ('URL', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='courses',
            name='approximate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='lectures',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses'),
        ),
    ]
