# Generated by Django 5.0.1 on 2024-02-01 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storyblock', '0005_rename_story_oldstory_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='oldstoryblock',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='oldstoryblock',
            name='story_id',
        ),
    ]
