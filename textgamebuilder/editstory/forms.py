from django import forms
from .models import Story, StoryBlock

class CreateStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['story_name', 'story_slug']

class CreateStoryBlockForm(forms.ModelForm):
    def __init__(self, storyslug, *args, **kwargs):
        story = Story.objects.get(story_slug=storyslug)
        super(CreateStoryBlockForm, self).__init__(*args, **kwargs)
        self.fields['prev_block_slug'] = forms.ModelChoiceField(queryset=StoryBlock.objects.filter(story_id=story.story_id), label='Previous storyblock slug')
        self.fields['next_block1_slug'] = forms.ModelChoiceField(queryset=StoryBlock.objects.filter(story_id=story.story_id), label='Choice 1 storyblock slug')
        self.fields['next_block2_slug'] = forms.ModelChoiceField(queryset=StoryBlock.objects.filter(story_id=story.story_id), label='Choice 2 storyblock slug')

    class Meta:
        model = StoryBlock
        fields = ['story_id'
                  ,'block_slug'
                  ,'block_image' 
                  ,'block_image_alt' 
                  ,'block_text'
                  ,'prev_block_slug'
                  ,'prev_block_txt'
                  ,'next_block1_slug'
                  ,'next_block1_txt'
                  ,'next_block2_slug'
                  ,'next_block2_txt']

class CreateFirstStoryBlockForm(forms.ModelForm):
    class Meta:
        model = StoryBlock
        fields = ['story_id'
                  ,'block_slug'
                  ,'block_image' 
                  ,'block_image_alt' 
                  ,'block_text'
                  ,'next_block1_txt'
                  ,'next_block2_txt'
                  ]

class EditStoryBlockForm(forms.ModelForm):
    def __init__(self, storyslug, *args, **kwargs):
        story = Story.objects.get(story_slug=storyslug)
        super(EditStoryBlockForm, self).__init__(*args, **kwargs)
        self.fields['prev_block_slug'] = forms.ModelChoiceField(queryset=StoryBlock.objects.filter(story_id=story.story_id), label='Previous storyblock slug')
        self.fields['next_block1_slug'] = forms.ModelChoiceField(queryset=StoryBlock.objects.filter(story_id=story.story_id), label='Choice 1 storyblock slug')
        self.fields['next_block2_slug'] = forms.ModelChoiceField(queryset=StoryBlock.objects.filter(story_id=story.story_id), label='Choice 2 storyblock slug')
    class Meta:
        model = StoryBlock
        fields = ['story_id'
                  ,'block_slug'
                  ,'block_image' 
                  ,'block_image_alt' 
                  ,'block_text'
                  ,'prev_block_slug'
                  ,'prev_block_txt'
                  ,'next_block1_slug'
                  ,'next_block1_txt'
                  ,'next_block2_slug'
                  ,'next_block2_txt']
