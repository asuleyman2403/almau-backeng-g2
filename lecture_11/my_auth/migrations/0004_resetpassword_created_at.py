# Generated by Django 4.1.6 on 2023-03-17 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0003_remove_resetpassword_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetpassword',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
