from django.db import models
from django.urls import reverse

# Create your models here.
class Story(models.Model):
	story_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name="story_id")
	story_name = models.CharField(max_length=35, verbose_name="story_name")
	story_isactive = models.BooleanField(default=True, verbose_name="story_is_active")
	story_slug = models.SlugField(null=False, verbose_name="story_slug", unique=True)

	def __str__(self):
		return str(f'{self.story_name}')
	
	def get_absolute_url(self):
		return reverse("play-story", kwargs={"storyslug": self.story_slug})
	
class StoryChoice(models.Model):
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	choice_id = models.PositiveIntegerField(default=1)
	choice_image = models.URLField(default='https://via.placeholder.com/150')
	choice_image_alt = models.TextField(default='image', max_length=255, verbose_name="choice_image_alt_text")
	choice_text = models.TextField()
	prev_choice_sub = models.PositiveIntegerField(default=1)
	prev_choice_txt = models.CharField(max_length=32, default='return')
	next_choice1_add = models.PositiveIntegerField(default=1)
	next_choice1_txt = models.CharField(max_length=32, default='choice 1')
	next_choice2_add = models.PositiveIntegerField(default=1)
	next_choice2_txt = models.CharField(max_length=32, default='choice 2')
	is_checkpoint = models.BooleanField(default=False)
	class Meta:
		unique_together = ["story_id", "choice_id"]
	
	def __str__(self):
			return str(f'adv-{self.story_id}-choice-{self.choice_id}')