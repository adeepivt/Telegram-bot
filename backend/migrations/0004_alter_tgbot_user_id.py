# Generated by Django 3.2.7 on 2021-09-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_tgbot_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tgbot',
            name='user_id',
            field=models.TextField(),
        ),
    ]