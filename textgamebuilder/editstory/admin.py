from django.contrib import admin
from editstory.models import Story, StoryBlock

# Register your models here.

# Dev note: if you would rather use the built-in Django Admin panel in your site 
# to manage your stories and story blocks, you can uncomment the below code.
# This will require a "superuser" or "user" to be created to access the /admin area of your site.
# View documentation here: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/


# class StoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"story_slug": ("story_name",)}
# admin.site.register(Story, StoryAdmin)
# admin.site.register(StoryBlock)