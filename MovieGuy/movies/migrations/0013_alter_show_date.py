# Generated by Django 4.2.1 on 2023-05-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_show_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateField(),
        ),
    ]
