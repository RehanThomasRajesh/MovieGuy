# Generated by Django 4.2.1 on 2023-05-07 13:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_show_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 7))]),
        ),
    ]
