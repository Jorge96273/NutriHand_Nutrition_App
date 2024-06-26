# Generated by Django 5.0.4 on 2024-04-11 15:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_app', '0001_initial'),
        ('recipe_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trolley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trolley', to='food_app.food')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trolley', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trolley', to='recipe_app.recipe')),
            ],
        ),
    ]
