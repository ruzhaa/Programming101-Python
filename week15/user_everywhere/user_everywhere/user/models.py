from django.db import models


class User(models.Model):
    email = models.CharField(max_length=140, primary_key=True)
    password = models.CharField(max_length=140)

    @classmethod
    def exists(cls, email):
        try:
            u = cls.objects.get(email=email)
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def login_user(cls, email, password):
        try:
            u = cls.objects.get(email=email, password=password)
            return u
        except cls.DoesNotExist:
            return None

    def __str__(self):
        return self.email
