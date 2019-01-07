from django.db import models

# Create your models here.
class signup_table(models.Model):
    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

class usernametable(models.Model):
    uname = models.CharField(max_length=50)

class logintable(models.Model):
    uname = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)



