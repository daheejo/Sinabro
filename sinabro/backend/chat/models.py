import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    send_text = models.CharField(max_length=200)
    check_read = models.BooleanField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.BooleanField(default=1)
    # TODO adding time, auth  

    def __str__(self):
        return self.send_text

class SuvMessage(models.Model):
    send_text = models.CharField(max_length=200)
    check_read = models.BooleanField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.BooleanField(default=1)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.send_text

    def get_score(self):
        return self.score

# https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models
class TmpUser(models.Model):
    name = models.CharField(max_length=10)
    nature_activities = models.TextField(null=True)
    city_activities = models.TextField(null=True)
    person_activities = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
