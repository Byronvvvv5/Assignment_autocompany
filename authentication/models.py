from django.db import models
from django.contrib.auth.models import User


class client(models.Model):

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    # Relation
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class merchant(models.Model):

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    # Relation
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class adminUser(models.Model):

    name = models.CharField(max_length=255)

    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)