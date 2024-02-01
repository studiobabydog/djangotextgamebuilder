from django import forms
from .models import Story, StoryBlock

class CreateStoryForm(forms.ModelForm):
    # story_name = forms.CharField(label='Story Name', max_length=45)
    # story_slug = forms.SlugField(label='Story Slug (Nickname)')
    class Meta:
        model = Story
        fields = ['story_name', 'story_slug']

class CreateStoryBlockForm(forms.ModelForm):
    class Meta:
        model = StoryBlock
        fields = ['story_id'
                  ,'block_slug'
                  ,'block_image' 
                  ,'block_image_alt' 
                  ,'block_text'
                  ,'prev_block_txt'
                  ,'next_block1_txt'
                  ,'next_block2_txt']