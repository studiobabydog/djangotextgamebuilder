from django.db import models
from django.urls import reverse

# Create your models here.
class Story(models.Model):
	story_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='story id')
	story_name = models.CharField(max_length=35, verbose_name='story name', default='default story name')
	story_isactive = models.BooleanField(default=True, verbose_name='story is active')
	story_slug = models.SlugField(null=False, default='default-story-slug', verbose_name='story slug (URL-friendly nickname)', unique=True)

	def __str__(self):
		return str(f'{self.story_name}')
	
	def get_absolute_url(self):
		return reverse('play-story', kwargs={'storyslug': self.story_slug})
	
class StoryBlock(models.Model):
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	block_id = models.PositiveIntegerField(default=1)
	block_slug = models.SlugField(null=False, default='block-slug', verbose_name='storyblock slug (URL-friendly nickname)', unique=True)
	block_image = models.URLField(default='https://via.placeholder.com/150')
	block_image_alt = models.TextField(default='image', max_length=255, verbose_name='storyblock image alt text (screenreader-friendly description)')
	block_text = models.TextField(verbose_name='storyblock text')
	prev_block_sub = models.PositiveIntegerField(default=1)
	prev_block_txt = models.CharField(max_length=32, default='return')
	next_block1_add = models.PositiveIntegerField(default=1)
	next_block1_txt = models.CharField(max_length=32, default='block 1')
	next_block2_add = models.PositiveIntegerField(default=1)
	next_block2_txt = models.CharField(max_length=32, default='block 2')
	is_checkpoint = models.BooleanField(default=False)
	class Meta:
		unique_together = ['story_id', 'block_id']
	
	def __str__(self):
			return str(f'adv-{self.story_id}-block-{self.block_id}')