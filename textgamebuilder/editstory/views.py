# Django Imports
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

# Custom Imports
from .models import Story, StoryBlock
from .forms import CreateStoryForm, EditStoryPropertiesForm, CreateStoryBlockForm, CreateFirstStoryBlockForm, EditStoryBlockForm, EditFirstStoryBlockForm


### Dev note: we included both function-based and class-based views; feel free to use
### whichever works best for you! The base deployment site uses both, so check it out.

### !!! Code for Stories starts here -- scroll down for StoryBlocks !!! ###
# Function-based view to see all stories
def all_stories_view(request, *args, **kwargs):
    # Show me ALL active stories (until you deactive a story, it will be active.)
    stories = Story.objects.all()
    context = {
        'stories': stories,
    }
    return render(request, 'all_stories.html', context)

# Class-based view to see all stories
class cb_all_stories_view(ListView):
    model = Story
    template_name = 'all_stories.html'

# Function-based view to create stories:
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

# Class-based view to create stories:
class cb_create_story_view(CreateView):
    model = Story
    form_class = CreateStoryForm
    template_name = 'create_story.html'
    success_url = 'all-stories'

# Function-based view to edit story properties (name/slug):
def edit_story_properties_view(request, storyid, *args, **kwargs):
    # Find the storyblock that we want to edit.
    story = Story.objects.get(story_id=storyid)
    if request.method == 'POST':
        edit_story_properties_form = EditStoryPropertiesForm(storyid)
        is_active = request.POST.get('story_isactive')
        try:
            story.story_name = request.POST.get('story_name')
            story.story_slug = request.POST.get('story_slug')
            if is_active == 'on':
                story.story_isactive = True
            else:
                story.story_isactive = False
            story.full_clean()
            story.save()
        except Exception as e:
            print(e)
        return redirect('all-stories')
    elif request.method != 'POST':
       edit_story_properties_form = EditStoryPropertiesForm(storyid, initial={'story_name':story.story_name, 'story_slug': story.story_slug, 'story_isactive': story.story_isactive})
    context = {
        'story': story
        ,'form': edit_story_properties_form
    }
    return render(request, 'edit_story_properties.html', context)


# Class-based view to edit story properties (name/slug):
class cb_edit_story_properties_view(UpdateView):
    model = Story
    form_class = EditStoryPropertiesForm
    template_name = 'edit_story_properties.html'
    success_url = 'all-stories'

# Function-based view to edit stories:
def edit_story_view(request, storyslug, *args, **kwargs):
    # Find the story we're going to edit, and the blocks that belong to it.
    story = Story.objects.get(story_slug=storyslug)
    storyblocks = StoryBlock.objects.filter(story_id=story.story_id)
    new_story = True
    if storyblocks.count() == 0:
        storyblocks = None
    elif storyblocks.count() >= 3:
        new_story = False
    context = {
        'story': story
        ,'storyblocks': storyblocks
        ,'new_story': new_story
        }
    return render(request, 'edit_story.html', context)

# Class-based view to edit stories:
# Coming soon!

# Function-based view to delete stories:
def delete_story_view(request, storyslug, *args, **kwargs):
    # Find the story we're going to delete, and the blocks that belong to it.
    story = Story.objects.get(story_slug=storyslug)
    context = {
        'story': story
    }
    story.delete()
    return render(request, 'delete_story.html', context)

# Class-based view to delete stories:
class cb_delete_story_view(DeleteView):
    model = Story
    template_name = 'delete_story.html'
    success_url  = 'all-stories'

### !!! Code about StoryBlocks is Below !!! ###
# Function-based view to see all storyblocks:
def all_storyblocks_view(request, *args, **kwargs):
    # Show me ALL the storyblocks, no matter which story they belong to.
    all_storyblocks = StoryBlock.objects.all()
    context = {'object_list': all_storyblocks}
    return render(request, 'all_storyblocks.html', context)

# Class-based view to see all storyblocks:
class cb_all_storyblocks_view(ListView):
    # Show me ALL the storyblocks, no matter which story they belong to.
    model = StoryBlock
    template_name = 'all_storyblocks.html'


# Function-based view to create a new storyblock:
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
            create_storyblock_form = CreateFirstStoryBlockForm(request.POST, initial={'is_starting_block': True})
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

# Class-based view to create a new storyblock:
# Coming soon!

# Function-based view to edit storyblocks
def edit_storyblock_view(request, storyblockslug, *args, **kwargs):
    # Find the storyblock that we want to edit.
    block = StoryBlock.objects.get(block_slug=storyblockslug)
    story = Story.objects.get(story_id=block.story_id.story_id)
    if request.method == 'POST':
      edit_storyblock_form = EditFirstStoryBlockForm(request.POST)
    elif request.method != 'POST':
       edit_storyblock_form = EditFirstStoryBlockForm()
    context = {
        'story': story
        ,'storyblock': block
        ,'form': edit_storyblock_form
    }
    return render(request, 'edit_storyblock.html', context)

# Class-based view to edit LINKED storyblocks (with slugs to other storyblocks)
class cb_edit_storyblock_view(UpdateView):
    model = StoryBlock
    template_name = 'edit_storyblock.html'
    form_class = EditStoryBlockForm
    def get_success_url(self):
        story = Story.objects.get(story_id = self.request.POST.get('story_id'))
        story_slug = str(story.story_slug)
        return reverse('edit-story', kwargs={'storyslug':story_slug})

# Class-based view to edit UNLINKED storyblocks (no links to other storyblocks yet)
class cb_edit_first_storyblock_view(UpdateView):
    model = StoryBlock
    template_name = 'edit_storyblock.html'
    form_class = EditFirstStoryBlockForm
    def get_success_url(self):
        story = Story.objects.get(story_id = self.request.POST.get('story_id'))
        story_slug = str(story.story_slug)
        return reverse('edit-story', kwargs={'storyslug':story_slug})

# Function-based view to delete storyblocks:
def delete_storyblock_view(request, storyblockslug, *args, **kwargs):
    # Find the story we're going to delete, and the blocks that belong to it.
    storyblock = StoryBlock.objects.get(block_slug=storyblockslug)
    context = {
        'storyblock': storyblock
    }
    return render(request, 'delete_storyblock.html', context)

# Class-based view to delete storyblocks:
class cb_delete_storyblock_view(DeleteView):
    model = StoryBlock
    template_name = 'delete_storyblock.html'
    def get_success_url(self):
        story = Story.objects.get(story_id = self.request.POST.get('story_id'))
        story_slug = str(story.story_slug)
        return reverse('edit-story', kwargs={'storyslug':story_slug})