from django.shortcuts import render
from storyblock.models import Story, StoryChoice

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "home.html", context)

def all_stories_view(request, *args, **kwargs):
    stories = Story.objects.filter(story_isactive=True)
    context = {
        'stories': stories,
    }
    return render(request, "choose_story.html", context)

def story_view(request, storyslug, *args, **kwargs):
    story = Story.objects.get(story_slug=storyslug)
    story_choice = StoryChoice.objects.filter(story_id=story.story_id, choice_id=1).first()
    context = {
        'story_choice': story_choice,
        }
    return render(request, "play_story.html", context)

def validate_story_choice(request, story_choice, *args, **kwargs):
    if request.POST.get('choice') == 'next1':
        story_do = story_choice.choice_id + story_choice.next_choice1_add
    elif request.POST.get('choice') == 'next2':
        story_do = story_choice.choice_id + story_choice.next_choice2_add
    elif request.POST.get('choice') == 'back':
        story_do = story_choice.choice_id - story_choice.prev_choice_sub
    elif request.POST.get('choice') == 'continue':
        story_do = StoryChoice.objects.filter(story_id = story_choice.story_id, choice_id=request.POST.get('continue_choice')).first().choice_id
    return story_do

def do_choice(request, *args, **kwargs):
    if request.method == "POST":
        # Log story
        story = story.objects.filter(story_name=request.POST.get('story_id')).first()
        story_choice = StoryChoice.objects.filter(story_id=story.story_id, choice_id=request.POST.get('choice_id')).first()
        return_story = validate_story_choice(request, story_choice)
        continue_story_choice = StoryChoice.objects.filter(story_id=story.story_id, choice_id=return_story).first()
        final_story_choice = StoryChoice.objects.all().order_by('-choice_id').first()   
        context = {
            'final_story_choice': final_story_choice,
            'story_choice': continue_story_choice
            }

        return render(request, "do_choice.html", context)
    elif request.method == "GET":
        return render(request, "home.html")