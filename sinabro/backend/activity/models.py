from django.db import models
from django.utils import timezone

# Create your models here.
class StartChoise(models.IntegerChoices):
    one = 1, "★"
    two = 2, "★★"
    three = 3, "★★★"
    four = 4, "★★★★"
    five = 5, "★★★★★"

# https://stackoverflow.com/questions/1117564/set-django-integerfield-by-choices-name
class Post(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=30)
    star = models.IntegerField(default=StartChoise.one, choices=StartChoise.choices)
    memo = models.TextField(null=True)

    def __str__(self):
        template = '{}  {}  {}'.format(self.pub_date, self.action, self.memo)
        return template