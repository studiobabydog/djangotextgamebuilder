from django.shortcuts import render
from editstory.models import Story, StoryBlock

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

def start_story_view(request, storyslug, *args, **kwargs):
    # Find the story we have requested and the first block belonging to that story.
    story = Story.objects.get(story_slug=storyslug)
    storyblocks = StoryBlock.objects.filter(story_id=story.story_id)
    starting_storyblock = StoryBlock.objects.get(story_id=story.story_id, is_starting_block=True)
    context = {
        'story': story,
        'storyblocks': storyblocks,
        'starting_storyblock': starting_storyblock,
        }
    return render(request, 'start_story.html', context)

def play_story_view(request, *args, **kwargs):
    # Find the requested storyblock and present it.
    print(request.GET)
    storyblock = StoryBlock.objects.get(block_slug='default-block-slug')
    story = Story.objects.get(story_id = storyblock.story_id)
    context = {
        'story': story,
        'storyblock': storyblock
    }
    return render(request, 'play_story.html', context)