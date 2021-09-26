from django.db import models

# Create your models here.

class Tgbot(models.Model):
    user_id = models.CharField(max_length=100,unique=True)
    username = models.CharField(max_length=200)
    fat = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)
    stupid = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Command(models.Model):
    command_name = models.CharField(max_length=50, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.command_name
