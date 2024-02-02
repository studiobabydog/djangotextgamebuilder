# Generated by Django 5.0.1 on 2024-02-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editstory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storyblock',
            name='next_block1_add',
        ),
        migrations.RemoveField(
            model_name='storyblock',
            name='next_block2_add',
        ),
        migrations.RemoveField(
            model_name='storyblock',
            name='prev_block_sub',
        ),
        migrations.AddField(
            model_name='storyblock',
            name='next_block1_slug',
            field=models.SlugField(default='block-slug', verbose_name='choice 1 storyblock slug'),
        ),
        migrations.AddField(
            model_name='storyblock',
            name='next_block2_slug',
            field=models.SlugField(default='block-slug', verbose_name='choice 2 storyblock slug'),
        ),
        migrations.AddField(
            model_name='storyblock',
            name='prev_block_slug',
            field=models.SlugField(default='block-slug', verbose_name='previous storyblock slug'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='block_image',
            field=models.URLField(default='https://via.placeholder.com/150', verbose_name='storyblock image URL'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='block_text',
            field=models.TextField(default='text', verbose_name='storyblock text'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='next_block1_txt',
            field=models.CharField(default='go left', max_length=32, verbose_name='choice 1 button text'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='next_block2_txt',
            field=models.CharField(default='go right', max_length=32, verbose_name='choice 2 button text'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='prev_block_txt',
            field=models.CharField(default='return', max_length=32, verbose_name='return to previous block button text'),
        ),
    ]