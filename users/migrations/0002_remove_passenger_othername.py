# Generated by Django 4.0 on 2022-01-01 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='otherName',
        ),
    ]
