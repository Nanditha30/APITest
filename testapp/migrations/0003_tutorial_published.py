# Generated by Django 4.0.5 on 2022-06-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_remove_tutorial_published_tutorial_is_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]