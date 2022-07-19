from django.db import models
from django.db.models import Q

from accounts.models import User

class TaskManager(models.Manager):
    def related_tasks_to_charity(self,user):
       return Task.objects.filter(charity__user = user)    

    def related_tasks_to_benefactor(self,user):
       return super().get_queryset().filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self,user):
       return super().get_queryset().filter(Q(charity__user=user) | Q(assigned_benefactor__user=user) | Q(state = 'P'))
       

class Benefactor(models.Model):
    EXPERIENCE = (
        (0,'beginner'),
        (1,'intermediate'),
        (2,'advance'),  
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE,default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
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

    assigned_benefactor = models.ForeignKey(Benefactor, null=True,on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity,null=True,on_delete=models.SET_NULL)
    age_limit_from = models.IntegerField(blank=True,null=True)
    age_limit_to = models.IntegerField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    gender_limit = models.CharField(choices=GENDER,max_length=1,blank=True,null=True)
    state = models.CharField(choices=STATE,default='P',max_length=1)
    title = models.CharField(max_length=60)

    objects = TaskManager()