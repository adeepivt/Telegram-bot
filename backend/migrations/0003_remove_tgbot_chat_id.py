# Generated by Django 3.2.7 on 2021-09-25 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_tgbot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tgbot',
            name='chat_id',
        ),
    ]
