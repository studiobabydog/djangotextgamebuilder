# Django Imports
from django.shortcuts import render, redirect
from django.urls import reverse

# Custom Imports
from .models import Story, StoryBlock
from .forms import CreateStoryForm, CreateStoryBlockForm, CreateFirstStoryBlockForm

# Create your views here.
def all_stories_view(request, *args, **kwargs):
    # Show me ALL active stories (until you deactive a story, it will be active.)
    stories = Story.objects.filter(story_isactive=True)
    context = {
        'stories': stories,
    }
    return render(request, 'all_stories.html', context)

def create_story_view(request, *args, **kwargs):
    # If we are currently creating a new story, use the POST data and validate it.
    if request.method == 'POST':
        create_story_form = CreateStoryForm(request.POST)
        if create_story_form.is_valid():
            story = create_story_form.save(commit=False)
            # Do other validations if necessary
            story.save()
            return redirect('all-stories')
    # Else if we are just looking at the page, set up a blank form to enter data into.
    else:
        create_story_form = CreateStoryForm()
    context = {'form': create_story_form}
    return render(request, 'create_story.html', context)

def edit_story_view(request, storyslug, *args, **kwargs):
    # Find the story we're going to edit, and the blocks that belong to it.
    story = Story.objects.get(story_slug=storyslug)
    storyblocks = StoryBlock.objects.filter(story_id=story.story_id)
    if storyblocks.count() == 0:
        storyblocks = None
    if storyblocks.count() < 3:
        new_story = True
    else:
        new_story = False
    context = {
        'story': story
        ,'storyblocks': storyblocks
        ,'new_story': new_story
        }
    return render(request, 'edit_story.html', context)

def delete_story_view(request, storyslug, *args, **kwargs):
    # Find the story we're going to delete, and the blocks that belong to it.
    story = Story.objects.get(story_slug=storyslug)
    context = {
        'story': story
    }
    story.delete()
    return render(request, 'delete_story.html', context)

def all_storyblocks_view(request, *args, **kwargs):
    # Show me ALL the storyblocks, no matter which story they belong to.
    all_storyblocks = StoryBlock.objects.all()
    context = {'storyblocks': all_storyblocks}
    return render(request, 'all_storyblocks.html', context)

def create_storyblock_view(request, storyslug, *args, **kwargs):
    # Find the story we are going to create blocks for, and any blocks that belong to it.
    story = Story.objects.get(story_slug=storyslug)
    storyblocks = StoryBlock.objects.filter(story_id=story.story_id)
    # If it is a new story without other blocks, this will change which form we use.
    if storyblocks.count() <= 3:
        new_story = True
    else:
        new_story = False
    if request.method == 'POST':
        # If we are currently creating a storyblock, use the POST data and validate it.
        if new_story == False:
            create_storyblock_form = CreateStoryBlockForm(storyslug, request.POST)
        elif new_story == True:
            create_storyblock_form = CreateFirstStoryBlockForm(request.POST)
        if create_storyblock_form.is_valid():
            storyblock = create_storyblock_form.save(commit=False)
            # Do other validations if necessary
            storyblock.save()
            return redirect('edit-story', storyslug)
        else:
            context = {
            'story': story
            ,'form': create_storyblock_form
            }
        return render(request, 'create_storyblock.html', context)
    # Else if we are just looking at the page, set up a blank form...
    elif request.method != 'POST':
        # If there are already storyblocks in this story, show me a form with more fields!
        if storyblocks:
            create_storyblock_form = CreateStoryBlockForm(storyslug, initial={'story_id':story.story_id})
        # Else if there are no storyblocks and this is the first one, we need fewer fields.
        elif not storyblocks:
            create_storyblock_form = CreateFirstStoryBlockForm(initial={'story_id':story.story_id, 'prev_block_slug': '', 'next_block1_slug': '', 'next_block2_slug': ''})
        context = {
            'story': story
            ,'form': create_storyblock_form
            }
        return render(request, 'create_storyblock.html', context)

def edit_storyblock_view(request, blockslug, *args, **kwargs):
    # Find the storyblock that we want to edit.
    block = StoryBlock.objects.get(block_slug=blockslug)
    context = {
        'storyblock': block
    }
    return render(request, 'edit_storyblock.html', context)

def delete_storyblock_view(request, storyblockslug, *args, **kwargs):
    # Find the story we're going to delete, and the blocks that belong to it.
    storyblock = StoryBlock.objects.get(block_slug=storyblockslug)
    context = {}
    return render(request, 'delete_storyblock.html', context)