# Generated by Django 4.1.7 on 2023-03-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntheticPlayer', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='syntheticplayer',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
