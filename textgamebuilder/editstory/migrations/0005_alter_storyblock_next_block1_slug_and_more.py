# Generated by Django 5.0.1 on 2024-02-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editstory', '0004_alter_storyblock_next_block1_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyblock',
            name='next_block1_slug',
            field=models.SlugField(blank=True, default='block-slug', null=True, verbose_name='choice 1 storyblock slug'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='next_block1_txt',
            field=models.CharField(blank=True, default='go left', max_length=32, null=True, verbose_name='choice 1 button text'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='next_block2_slug',
            field=models.SlugField(blank=True, default='block-slug', null=True, verbose_name='choice 2 storyblock slug'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='next_block2_txt',
            field=models.CharField(blank=True, default='go right', max_length=32, null=True, verbose_name='choice 2 button text'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='prev_block_slug',
            field=models.SlugField(blank=True, default='block-slug', null=True, verbose_name='previous storyblock slug'),
        ),
        migrations.AlterField(
            model_name='storyblock',
            name='prev_block_txt',
            field=models.CharField(blank=True, default='return', max_length=32, null=True, verbose_name='previous storyblock button text'),
        ),
    ]