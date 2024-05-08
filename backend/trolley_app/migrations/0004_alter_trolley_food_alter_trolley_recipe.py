# Generated by Django 5.0.3 on 2024-04-22 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
        ('recipe_app', '0001_initial'),
        ('trolley_app', '0003_alter_trolley_food_alter_trolley_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trolley',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trolley', to='food_app.food'),
        ),
        migrations.AlterField(
            model_name='trolley',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trolley', to='recipe_app.recipe'),
        ),
    ]