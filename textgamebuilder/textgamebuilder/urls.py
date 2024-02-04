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
    
    ,path('all-stories', all_stories_view, name='all-stories')
    ,path('create-story', create_story_view, name='create-story')
    ,path('edit-story/<slug:storyslug>', edit_story_view, name='edit-story')
    ,path('delete-story/<slug:storyslug>', delete_story_view, name='delete-story')

    ,path('play-story/<slug:storyslug>', play_story_view, name='play-story')
    #path('do-block', do_block, name='do-choice')
    
    ,path('all-storyblocks', all_storyblocks_view, name='all-storyblocks')
    ,path('create-storyblock/<slug:storyslug>', create_storyblock_view, name='create-storyblock')
    ,path('edit-storyblock/<slug:storyblockslug>', edit_storyblock_view, name='edit-storyblock')
    ,path('delete-storyblock/<slug:storyblockslug>', delete_storyblock_view, name='delete-storyblock')
    #,path('edit-story/edit/<pk>', classbased_edit_storyblock_view.as_view(), name='storyblock-edit')
]
