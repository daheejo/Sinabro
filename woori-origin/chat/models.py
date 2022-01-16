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

    def was_published_recently(self):
        return self.pub_data >= timezone.now()

datetime.timedelta(days=1)