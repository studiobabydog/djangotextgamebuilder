# Django Text Game Builder by Studio Babydog
Build your own browser-based text games using Django!

Please be nice! This is my first time building a standalone Django module, and there is a lot to learn about publishing code to GitHub. I write code for fun, as a hobby -- if you find any glaring holes, feel free to let me know, or patch them yourself. That's the great thing about open-source code!

## Notes on Django:
1. This module is built on and requires Django, which is a lightweight full-stack web development framework using Python to communicate from a front-end webpage to a back-end database. If you do not know how to use Django yet, I recommend Traversy Media, Corey Schafer, and Programming with Mosh on YouTube to learn the basics!
2. Usually Django will create you a sqlite database as a starter, but you can use many different relational databases (see Django's documentation for more information). This module does not require any particular type of relational database, but we have included a basic .sql file compatible with a sqlite database, which you can use to build you some "test" Stories and Story Blocks to mess around with and get the feel of the module.
3. This module is written for development and playing in a local environment, and is not tested to be cyber-secure. If you are moving any of this code into a production environment, on a remote server, or need any of your data to be secured, please ensure you have followed the Django Deployment Checklist, which can be found at https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

## Optional Configurations:
1. If you would rather use the Django Admin panel to manage, create, and delete your Stories and Story Blocks (which you can do in-browser with a running django server), you can uncomment the code in textgamebuilder/edistory/admin.py.
2. If you would like to use the local Static directory to hold images for your Story Blocks, rather than linking them using a URL, use the code block in textgamebuilder/editstory/models.py under the dev note to switch the block_image property.

## How to Use:
1. Clone this repository to the machine where you want to build your stories.
2. Open the repository in your text editor of choice (we use Visual Studio Code, it's free!)
3. 
