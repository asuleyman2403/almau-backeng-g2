# Generated by Django 4.1.6 on 2023-03-17 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0002_resetpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resetpassword',
            name='created_at',
        ),
    ]
