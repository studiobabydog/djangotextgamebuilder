# Django Text Game Builder by Studio Babydog
Build your own browser-based text games using Django!

Please be nice! This is my first time building a standalone Django module, and there is a lot to learn about publishing code to GitHub. I write code for fun, as a hobby -- if you find any glaring holes, feel free to let me know, or branch and patch them yourself. That's the great thing about open-source code!

## Requirements:
Programs:
* Python
* IDE (Visual Studio Code or similar)
* Web Browser

Basic knowledge that will help you get started:
* Python
* Django
* Bash/command prompt/terminal or similar
* Starting and running a local web server
* [What is a "slug" in web code?](https://www.codecademy.com/article/christine_belzie/create-a-url-using-slugs)

## Notes on the module:
1. This module is built on and requires Django, which is a lightweight full-stack web development framework using Python to communicate from a front-end webpage to a back-end database. If you do not know how to use Django yet, I recommend Traversy Media, Corey Schafer, and Programming with Mosh on YouTube to learn the basics!
2. Usually Django will create you a sqlite database as a starter, but you can use many different relational databases (see Django's documentation for more information). This module does not require any particular type of relational database, but we have included a basic .sql file compatible with a sqlite database, which you can use to build you some "test" Stories and Story Blocks to mess around with and get the feel of the module.
3. This module is written for development and playing in a local environment, and is not tested to be cyber-secure. If you are moving any of this code into a production environment, on a remote server, or need any of your data to be secured, please ensure you have followed the Django Deployment Checklist, which can be found at https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

## Optional configurations:
1. If you would rather use the Django Admin panel to manage, create, and delete your Stories and Story Blocks (which you can do in-browser with a running django server), you can uncomment the code in textgamebuilder/edistory/admin.py.
2. If you would like to use the local Static directory to hold images for your Story Blocks, rather than linking them using a URL, use the code block in textgamebuilder/editstory/models.py under the dev note to switch the block_image property.

## How to Use:
1. Download the Files: Clone this repository to the machine where you want to build your stories.
2. Get Started: Open the repository folder in your Integrated Development Envrionment (IDE) of choice (we recommend Visual Studio Code -- it's free, and there is a .vscode folder included here with a launch.json file that will help you get going!)
3. Set up a Virtual Environment: We recommend setting up a virtual environment using the "venv" module (`python -m pip install venv`) to keep the Python programs you need for this repository separate from your other Python programs. If you choose not to use a virtual environment, you can check requirements.txt file to know what you'll need, and install them individually using the appropriate pip commands.
4. Install Requirements: Open a terminal (bash, cmd, etc) and navigate to the repository folder. Run `python -m pip install -r requirements.txt` to install the required programs, or run the appropriate pip install commands.
5. Launch the Server: In your terminal, start your Django server with the textgamebuilder/manage.py file. Your input should look something like this: `python manage.py runserver`. If you are using a virtual environment, it may also look like: `<path to virtual environment>/bin/python <path to textgamebuilder/manage.py> runserver`. If you are using VSCode, you can just use the "Run and Debug" option and use .vscode/launch.json, with the Python: Django interpreter, to launch the server instead. If your server starts up correctly, you should see something like this in your terminal: `Starting development server at http://127.0.0.1:8000/`.
6. Open Running Server: In a browser of your choice (we recommend Firefox), open your server. The default Django location is http://127.0.0.1:8000/ but you can change this with some settings if you need to.
7. Start Building Stories: If you have done all of the above correctly, when you open your web browser and navigate to your running server page, you should see a message that says "Hello! Let's build some great text adventures!" and a simple bullet list navigation menu.
8. Add Sample Stories (Optional): Open your database using a Relational Database Management software (for the standard sqlite db, we recommend DBrowser for SQLite). Run the .sql file in textgamebuilder/sample_stories.sql to insert a new Story and a set of Story Blocks into your database. Refresh your web browser and you should now see these in the "All Stories" and "All Story Blocks" pages.

### Happy adventuring!
____

Find us online at [studiobabydog.com](http://studiobabydog.com)!
