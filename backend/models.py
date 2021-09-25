from django.db import models

# Create your models here.

class Tgbot(models.Model):
    user_id = models.CharField(max_length=100,unique=True)
    fat = models.IntegerField(default=1)
    dumb = models.IntegerField(default=1)
    stupid = models.IntegerField(default=1)


class Command(models.Model):
    fat = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)
    stupid = models.IntegerField(default=0)

