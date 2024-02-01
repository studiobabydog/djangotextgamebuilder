# Django Imports
from django.shortcuts import render, redirect

# Custom Imports
from .models import Story, StoryBlock
from .forms import CreateStoryForm, CreateStoryBlockForm

# Create your views here.
def all_storyblocks_view(request, *args, **kwargs):
    context = {}
    return render(request, "all_storyblocks.html", context)

def create_story_view(request, *args, **kwargs):
    if request.method == "POST":
        create_story_form = CreateStoryForm(request.POST)
        if create_story_form.is_valid():
            story = create_story_form.save(commit=False)
            # Do other validations if necessary
            story.save()
            return redirect('all-stories')
    else:
        create_story_form = CreateStoryForm()
    context = {'form': create_story_form}
    return render(request, "create_story.html", context)

def create_storyblock_view(request, *args, **kwargs):
    context = {}
    return render(request, "create_storyblock.html", context)

def edit_storyblock_view(request, *args, **kwargs):
    context = {}
    return render(request, "edit_storyblock.html", context)