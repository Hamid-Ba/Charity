from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER = (
        ('M','male'),
        ('F','female'),
    )
    
    address = models.TextField(blank=True)
    age = models.PositiveSmallIntegerField(blank=True)
    date_joined = models.DateTimeField()
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(blank=True)
    last_name = models.CharField(blank=True)
    gender = models.CharField(choices=GENDER,max_length=1,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True)
    password = models.CharField()
    phone = models.CharField(max_length=15,blank=True)
    username = models.CharField()


