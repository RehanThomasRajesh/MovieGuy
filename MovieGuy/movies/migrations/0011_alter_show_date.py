# Generated by Django 4.2.1 on 2023-05-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_alter_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateField(),
        ),
    ]
