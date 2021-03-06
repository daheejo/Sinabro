# Generated by Django 3.2.5 on 2021-09-18 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_message_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuvMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_text', models.CharField(max_length=200)),
                ('check_read', models.BooleanField(default=0)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.BooleanField(default=1)),
            ],
        ),
    ]
