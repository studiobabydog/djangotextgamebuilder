"""
URL configuration for textgamebuilder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from playstory.views import *
from editstory.views import *

urlpatterns = [
    path('admin/', admin.site.urls)
    ,path('', home_view, name='home')

    ,path('start-story/<slug:storyslug>', start_story_view, name='start-story')
    ,path('play-story/<slug:storyblockslug>', play_story_view, name='play-story')
    
    # Function-Based Views - Edit Stories and Storyblocks
    ,path('all-stories', all_stories_view, name='all-stories')
    ,path('create-story', create_story_view, name='create-story')
    ,path('edit-story-properties/<int:storyid>', edit_story_properties_view, name='edit-story-properties')
    ,path('delete-story/<slug:storyslug>', delete_story_view, name='delete-story')
    ,path('edit-story/<slug:storyslug>', edit_story_view, name='edit-story')
    ,path('all-storyblocks', all_storyblocks_view, name='all-storyblocks')
    ,path('create-storyblock/<slug:storyslug>', create_storyblock_view, name='create-storyblock')
    ,path('delete-storyblock/<slug:storyblockslug>', delete_storyblock_view, name='delete-storyblock')
    ,path('edit-storyblock/<slug:blockslug>', edit_storyblock_view, name='edit-storyblock')

    # Class-Based Views - Edit Stories and Storyblocks
    ,path('cb-all-stories', cb_all_stories_view.as_view(), name='cb-all-stories')
    ,path('cb-create-story', cb_create_story_view.as_view(), name='cb-create-story')
    ,path('cb-edit-story-properties/<pk>', cb_edit_story_properties_view.as_view(), name='cb-edit-story-properties')
    ,path('cb-delete-story/<pk>', cb_delete_story_view.as_view(), name='cb-delete-story')
    ,path('cb-all-storyblocks', cb_all_storyblocks_view.as_view(), name='cb-all-storyblocks')
    ,path('cb-delete-storyblock/<pk>', cb_delete_storyblock_view.as_view(), name='cb-delete-storyblock')
    ,path('edit-story/cb-edit-block/<pk>', cb_edit_storyblock_view.as_view(), name='cb-edit-storyblock')
    ,path('edit-story/cb-edit-unlinked-block/<pk>', cb_edit_first_storyblock_view.as_view(), name='cb-edit-unlinked-storyblock')

]
