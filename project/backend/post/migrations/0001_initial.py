# Generated by Django 2.2.1 on 2019-05-18 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, null=True, upload_to='')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='homepage.Profile')),
                ('repost', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repost', to='homepage.Profile')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Profile')),
                ('post', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
