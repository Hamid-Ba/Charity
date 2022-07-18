from django.db import models

from accounts.models import User


class Benefactor(models.Model):
    user = models.OneToOneField(User)
    experience = models.SmallIntegerField(choices=(0,1,2),default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    GENDER = (
        ('M','male'),
        ('F','female'),
    )

    STATE = (
        ('P','Pending'),
        ('W','Waiting'),
        ('A','Assigned'),
        ('D','Done'),
    )

    assigned_benefactor = models.ForeignKey(Benefactor, nullable=True,on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity)
    age_limit_from = models.IntegerField()
    age_limit_to = models.IntegerField()
    date = models.DateField()
    description = models.TextField()
    gender_limit = models.CharField(choices=GENDER,max_length=1)
    state = models.CharField(choices=STATE,default='P',max_length=1)
    title = models.CharField(max_length=60)
