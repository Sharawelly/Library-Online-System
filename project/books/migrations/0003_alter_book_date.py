# Generated by Django 5.0.6 on 2024-05-22 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 22, 19, 45, 32, 687346), verbose_name='Publishing Date'),
        ),
    ]
