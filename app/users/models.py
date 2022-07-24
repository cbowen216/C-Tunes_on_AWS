from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=50, blank=False, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    first_name = models.CharField(max_length=100, blank=False, default='')
    last_name = models.CharField(max_length=100, blank=False, default='')


