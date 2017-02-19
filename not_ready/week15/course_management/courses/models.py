from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    approximate = models.CharField(max_length=50)


class Lectures(models.Model):
    unique_id = models.AutoField(primary_key=True)
    lecture = models.CharField(max_length=50)
    week = models.IntegerField()
    course = models.ForeignKey(Courses)
    URL = models.URLField(max_length=200)
