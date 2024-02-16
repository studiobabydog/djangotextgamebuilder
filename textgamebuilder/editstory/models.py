from django.db import models
from django.db.models import UniqueConstraint, Q
from django.urls import reverse

# Create your models here.
class Story(models.Model):
	story_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='story id')
	story_name = models.CharField(max_length=35, verbose_name='story name', default='default story name', unique=True)
	story_isactive = models.BooleanField(default=True, verbose_name='story is active')
	story_slug = models.SlugField(null=False, default='default-story-slug', verbose_name='story slug (URL-friendly nickname)', unique=True)
	class Meta:
		verbose_name_plural = 'stories'

	def __str__(self):
		return str(f'{self.story_name}')
	
	def get_start_url(self):
		return reverse('start-story', kwargs={'storyslug': self.story_slug})
	
	def get_edit_story_properties_url(self):
		return reverse('edit-story-properties', kwargs={'storyid': self.story_id})
	
	def get_edit_story_url(self):
		return reverse('edit-story', kwargs={'storyslug': self.story_slug})
	
	def get_edit_storyblocks_url(self):
		return reverse('edit-storyblocks', kwargs={'storyslug': self.story_slug})
	
	def get_create_storyblock_url(self):
		return reverse('create-storyblock', kwargs={'storyslug': self.story_slug})
	
	def get_delete_story_url(self):
		return reverse('delete-story', kwargs={'storyslug': self.story_slug})
	
class StoryBlock(models.Model):
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	block_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='storyblock id')
	block_slug = models.SlugField(null=False, default='block-slug', verbose_name='new storyblock slug (URL-friendly nickname)', unique=True)
	block_image = models.URLField(default='https://via.placeholder.com/150', verbose_name='new storyblock image URL')
	block_image_alt = models.TextField(default='image', max_length=255, verbose_name='new storyblock image alt text (screenreader-friendly description)')
	block_text = models.TextField(verbose_name='new storyblock text', default='text')
	prev_block_slug = models.SlugField(null=True, blank=True, default='block-slug', verbose_name='previous storyblock slug')
	prev_block_txt = models.CharField(null=True, blank=True, max_length=32, default='return', verbose_name='previous storyblock button text')
	next_block1_slug = models.SlugField(null=True, blank=True, default='block-slug', verbose_name='choice 1 storyblock slug')
	next_block1_txt = models.CharField(null=True, blank=True, max_length=32, default='go left', verbose_name='choice 1 button text')
	next_block2_slug = models.SlugField(null=True, blank=True, default='block-slug', verbose_name='choice 2 storyblock slug')
	next_block2_txt = models.CharField(null=True, blank=True, max_length=32, default='go right', verbose_name='choice 2 button text')
	is_checkpoint = models.BooleanField(default=False)
	is_starting_block = models.BooleanField(default=False)
	class Meta:
		unique_together = ['story_id', 'block_id']
		verbose_name_plural = 'story blocks'
		constraints = [
			UniqueConstraint(fields=('story_id',), condition=Q(is_starting_block=True), name='one_starting_block_per_story')
			]
	
	def __str__(self):
			return str(f'{self.block_slug}')
	
	def get_edit_storyblock_url(self):
		return reverse('edit-storyblock', kwargs={'storyblockslug': self.block_slug})
	
	def get_delete_storyblock_url(self):
		return reverse('delete-storyblock', kwargs={'storyblockslug': self.block_slug})
	
	def get_prev_block_url(self):
		return reverse('play-story', kwargs={'storyblockslug': self.prev_block_slug})
	
	def get_next_block1_url(self):
		return reverse('play-story', kwargs={'storyblockslug': self.next_block1_slug})
	
	def get_next_block2_url(self):
		return reverse('play-story', kwargs={'storyblockslug': self.next_block2_slug})