# Generated by Django 4.2.1 on 2023-05-07 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_show_date_alter_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='time',
            field=models.TimeField(choices=[(datetime.time(9, 0), '9:00 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(15, 0), '3:00 PM'), (datetime.time(18, 0), '6:00 PM'), (datetime.time(21, 0), '9:00 PM')]),
        ),
    ]
