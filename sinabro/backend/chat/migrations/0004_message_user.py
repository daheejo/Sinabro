# Generated by Django 3.2.5 on 2021-08-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_send_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.BooleanField(default=1),
        ),
    ]
