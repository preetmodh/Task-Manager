# Generated by Django 2.2 on 2020-09-08 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
