from django.shortcuts import render
from editstory.models import Story, StoryBlock

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

def play_story_view(request, storyblockslug, *args, **kwargs):
    # Find the requested storyblock and present it.
    storyblock = StoryBlock.objects.get(block_slug=storyblockslug)
    story = Story.objects.get(story_id=storyblock.story_id.story_id)
    context = {
        'story': story,
        'storyblock': storyblock,
    }
    return render(request, 'play_story.html', context)