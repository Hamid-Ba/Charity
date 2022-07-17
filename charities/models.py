from django.db import models


class Benefactor(models.Model):
    pass


class Charity(models.Model):
    pass


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
