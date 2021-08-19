from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=70, blank=False, default='')
    fname = models.CharField(max_length=25, blank=False, default='')
    lname = models.CharField(max_length=15, blank=False, default='')
    pwd = models.CharField(max_length=100, blank=True, default='')
