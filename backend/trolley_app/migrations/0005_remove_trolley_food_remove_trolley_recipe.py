# Generated by Django 5.0.3 on 2024-04-22 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trolley_app', '0004_alter_trolley_food_alter_trolley_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trolley',
            name='food',
        ),
        migrations.RemoveField(
            model_name='trolley',
            name='recipe',
        ),
    ]
