# Generated by Django 4.0.5 on 2022-06-10 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='is_status',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
    ]