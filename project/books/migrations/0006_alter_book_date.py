# Generated by Django 5.0.6 on 2024-05-23 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 23, 17, 54, 4, 208542), verbose_name='Publishing Date'),
        ),
    ]
