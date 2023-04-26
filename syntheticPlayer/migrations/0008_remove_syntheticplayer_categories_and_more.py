# Generated by Django 4.2 on 2023-04-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntheticPlayer', '0007_alter_categories_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syntheticplayer',
            name='categories',
        ),
        migrations.AddField(
            model_name='syntheticplayer',
            name='categories',
            field=models.ManyToManyField(to='syntheticPlayer.categories'),
        ),
    ]