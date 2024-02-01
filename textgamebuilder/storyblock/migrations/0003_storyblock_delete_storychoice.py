# Generated by Django 5.0.1 on 2024-02-01 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyblock', '0002_storychoice_choice_slug_alter_story_story_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id', models.PositiveIntegerField(default=1)),
                ('block_slug', models.SlugField(default='block-slug', unique=True, verbose_name='block_slug')),
                ('block_image', models.URLField(default='https://via.placeholder.com/150')),
                ('block_image_alt', models.TextField(default='image', max_length=255, verbose_name='block_image_alt_text')),
                ('block_text', models.TextField()),
                ('prev_block_sub', models.PositiveIntegerField(default=1)),
                ('prev_block_txt', models.CharField(default='return', max_length=32)),
                ('next_block1_add', models.PositiveIntegerField(default=1)),
                ('next_block1_txt', models.CharField(default='block 1', max_length=32)),
                ('next_block2_add', models.PositiveIntegerField(default=1)),
                ('next_block2_txt', models.CharField(default='block 2', max_length=32)),
                ('is_checkpoint', models.BooleanField(default=False)),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storyblock.story')),
            ],
            options={
                'unique_together': {('story_id', 'block_id')},
            },
        ),
        migrations.DeleteModel(
            name='StoryChoice',
        ),
    ]