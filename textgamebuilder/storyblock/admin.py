from django.contrib import admin
from storyblock.models import Story, StoryChoice

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"story_slug": ("story_name",)}
admin.site.register(Story, StoryAdmin)

admin.site.register(StoryChoice)