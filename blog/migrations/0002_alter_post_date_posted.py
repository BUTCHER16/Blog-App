# Generated by Django 5.0.7 on 2024-08-15 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2024, 8, 15, 4, 4, 9, 566676, tzinfo=datetime.timezone.utc)),
        ),
    ]
