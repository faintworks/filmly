# Filmly

Filmly is a platform for movie reviews. 
The basic features will include:

* Account creation and login 
* Posting, editing and deleting movie reviews and rating movies 
* Tagging movies by category for example "comedy" or "horror"
* Searching for movies by name or category
* Viewing the reviews for a movie from other users
* Account profile page listing the reviews made by an user
* Commenting on other users reviews 

Current features:
* Account creation/login/logout
* Posting reviews and viewing them on the front page 
* Editing and deleting reviews
* Searching for reviews by keyword in title or review

Testing instructions:
After cloning the repository and changing your terminal working directory there run these commands:

Creating the virtual environment and installing requirements:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On windows the process is a bit different:

```
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

Create the database tables:

```
sqlite3 database.db < schema.sql
.q #quit sqlite3 and return to terminal
```

Start the app with:

```
flask run
```

Then go to http://localhost:5000 in your browser to use the app.

