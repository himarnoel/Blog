# Generated by Django 5.0.1 on 2024-01-29 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApi', '0005_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
