from django.contrib import admin
from editstory.models import Story, StoryBlock

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"story_slug": ("story_name",)}
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryBlock)