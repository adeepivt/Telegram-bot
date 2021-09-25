# Generated by Django 3.2.7 on 2021-09-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210925_1229'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Command',
        ),
        migrations.RemoveField(
            model_name='tgbot',
            name='command',
        ),
        migrations.AlterField(
            model_name='tgbot',
            name='dumb',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tgbot',
            name='fat',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tgbot',
            name='stupid',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tgbot',
            name='user_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
