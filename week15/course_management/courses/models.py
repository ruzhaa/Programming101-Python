from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    # approximate = models.CharField(max_length=100)
