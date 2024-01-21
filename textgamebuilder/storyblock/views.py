from django.shortcuts import render

# Create your views here.
def all_storyblocks_view(request, *args, **kwargs):
    context = {}
    return render(request, "all_storyblocks.html", context)

def create_story_view(request, *args, **kwargs):
    context = {}
    return render(request, "create_story.html", context)

def create_storyblock_view(request, *args, **kwargs):
    context = {}
    return render(request, "create_storyblock.html", context)

def edit_storyblock_view(request, *args, **kwargs):
    context = {}
    return render(request, "edit_storyblock.html", context)