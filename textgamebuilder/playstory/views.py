from django.shortcuts import render
from editstory.models import Story, StoryBlock

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

def play_story_view(request, storyslug, *args, **kwargs):
    # Find the story we have requested and the first block belonging to that story.
    story = Story.objects.get(story_slug=storyslug)
    storyblock = StoryBlock.objects.filter(story_id=story.story_id, block_id=1).first()
    context = {
        'story': story,
        'storyblock': storyblock,
        }
    return render(request, 'play_story.html', context)

# def do_block(request, *args, **kwargs):
    # if request.method == 'POST':
    #     # Log story
    #     story = story.objects.filter(story_name=request.POST.get('story_id')).first()
    #     story_block = StoryBlock.objects.filter(story_id=story.story_id, block_id=request.POST.get('block_id')).first()
    #     continue_story_block = StoryBlock.objects.filter(story_id=story.story_id, block_id=return_story).first()
    #     final_story_block = StoryBlock.objects.all().order_by('-block_id').first()   
    #     context = {
    #         'final_story_block': final_story_block,
    #         'story_block': continue_story_block
    #         }

    #     return render(request, 'do_block.html', context)
    # elif request.method == 'GET':
    #     return render(request, 'home.html')