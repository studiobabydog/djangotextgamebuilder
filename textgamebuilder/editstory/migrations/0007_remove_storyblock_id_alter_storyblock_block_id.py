# Generated by Django 5.0.1 on 2024-02-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editstory', '0006_alter_story_options_alter_storyblock_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storyblock',
            name='id',
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='block_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='storyblock id'),
        ),
    ]