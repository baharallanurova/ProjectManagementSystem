# Generated by Django 5.0.1 on 2024-01-18 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_developer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='user',
        ),
    ]
