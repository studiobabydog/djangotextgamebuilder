from django.shortcuts import render
from editstory.models import Story, StoryBlock

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

def play_story_view(request, storyslug, *args, **kwargs):
    story = Story.objects.get(story_slug=storyslug)
    story_block = StoryBlock.objects.filter(story_id=story.story_id, block_id=1).first()
    context = {
        'story': story,
        'story_block': story_block,
        }
    return render(request, 'play_story.html', context)

def validate_story_block(request, story_block, *args, **kwargs):
    if request.POST.get('block') == 'next1':
        story_do = story_block.block_id + story_block.next_block1_add
    elif request.POST.get('block') == 'next2':
        story_do = story_block.block_id + story_block.next_block2_add
    elif request.POST.get('block') == 'back':
        story_do = story_block.block_id - story_block.prev_block_sub
    elif request.POST.get('block') == 'continue':
        story_do = StoryBlock.objects.filter(story_id = story_block.story_id, block_id=request.POST.get('continue_block')).first().block_id
    return story_do

def do_block(request, *args, **kwargs):
    if request.method == 'POST':
        # Log story
        story = story.objects.filter(story_name=request.POST.get('story_id')).first()
        story_block = StoryBlock.objects.filter(story_id=story.story_id, block_id=request.POST.get('block_id')).first()
        return_story = validate_story_block(request, story_block)
        continue_story_block = StoryBlock.objects.filter(story_id=story.story_id, block_id=return_story).first()
        final_story_block = StoryBlock.objects.all().order_by('-block_id').first()   
        context = {
            'final_story_block': final_story_block,
            'story_block': continue_story_block
            }

        return render(request, 'do_block.html', context)
    elif request.method == 'GET':
        return render(request, 'home.html')