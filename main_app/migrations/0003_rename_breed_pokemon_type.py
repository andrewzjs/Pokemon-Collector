# Generated by Django 4.1.7 on 2023-03-20 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pokemon_breed_pokemon_description_pokemon_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='breed',
            new_name='type',
        ),
    ]
