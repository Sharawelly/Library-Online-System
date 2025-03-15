# Generated by Django 5.0.6 on 2024-05-22 12:33

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Title')),
                ('author', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.datetime(2024, 5, 22, 15, 33, 33, 234327), verbose_name='Publishing Date')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Cover')),
                ('availability', models.BooleanField(default=True)),
                ('Borrow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.category')),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]
