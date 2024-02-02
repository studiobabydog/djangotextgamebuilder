# Django Imports
from django.shortcuts import render, redirect

# Custom Imports
from .models import Story, StoryBlock
from .forms import CreateStoryForm, CreateStoryBlockForm

# Create your views here.
def all_stories_view(request, *args, **kwargs):
    stories = Story.objects.filter(story_isactive=True)
    context = {
        'stories': stories,
    }
    return render(request, 'all_stories.html', context)

def create_story_view(request, *args, **kwargs):
    if request.method == 'POST':
        create_story_form = CreateStoryForm(request.POST)
        if create_story_form.is_valid():
            story = create_story_form.save(commit=False)
            # Do other validations if necessary
            story.save()
            return redirect('all-stories')
    else:
        create_story_form = CreateStoryForm()
    context = {'form': create_story_form}
    return render(request, 'create_story.html', context)

def edit_story_view(request, storyslug, *args, **kwargs):
    story = Story.objects.get(story_slug=storyslug)
    story_blocks = StoryBlock.objects.filter(story_id=story.story_id)
    context = {
        'story': story,
        'story_blocks': story_blocks,
        }
    return render(request, 'edit_story.html', context)

def all_storyblocks_view(request, *args, **kwargs):
    all_stories = Story.objects.all()
    context = {'all_stories': all_stories}
    return render(request, 'all_storyblocks.html', context)

def create_storyblock_view(request, storyslug, *args, **kwargs):
    story = Story.objects.get(story_slug=storyslug)
    context = {
        'story': story
    }
    return render(request, 'create_storyblock.html', context)

def edit_storyblock_view(request, blockslug, *args, **kwargs):
    block = StoryBlock.objects.get(block_slug=blockslug)
    context = {
        'storyblock': block
    }
    return render(request, 'edit_storyblock.html', context)