# Generated by Django 5.0.1 on 2024-02-01 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyblock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storychoice',
            name='choice_slug',
            field=models.SlugField(default='choice-slug', unique=True, verbose_name='choice_slug'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_slug',
            field=models.SlugField(default='story-slug', unique=True, verbose_name='story_slug'),
        ),
    ]