# Generated by Django 5.0.1 on 2024-01-29 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApi', '0003_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
