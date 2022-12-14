## Template code for a login Flask project.
## Two ##s is an explanation or label, and one # is pseudocode that should be replaced

## Imports

## Flask libraries (main library, display template pages, request data, redirect to a new page, and store session data)
from flask import Flask, render_template, request, redirect, session
## SQLlchemy library
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## Start SQL Alchemy things

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' ## Where we store the database
app.secret_key = "Super Secret" ## Secret key for sessions

db = SQLAlchemy(app)

## Create the User table in the database
class User(db.Model):
    ## Column 1: user ID, as a number
    id = db.Column(db.Integer, primary_key=True)
    ## Column 2: username, as a string
    username = db.Column(db.String(80), unique=True, nullable=False)
    ## Column 3: password, as a string
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.usernames

## End SQL Alchemy things

## Main Page

@app.route("/")
def index():
    pass
    # If user is logged in, render the homepage
    # Otherwise, render the login page

## Logout Page

@app.route("/logout")
def logout():
    pass
    # Log the user out

## Login Page

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # When we press the login button, get the username and password data

        user = User.query.filter_by(username=username).first() ## Find the username and password in the database
        
        # Determine if the username and password are in the database
            # If so, log them in!
            # If not, display an error
    else:
        return render_template('login.html')

## Signup Page

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # When we press the signup button, get the username and password data
        # (Don't forget the confirm password field!)

        # If the passwords don't match, return an error
        
        user = User.query.filter_by(username=username).first() ## Find the username and password in the database

        # If the username already exists, return an error
        # Otherwise, add the new user to the database and return to the homepage.
    else:
        return render_template('signup.html')

## Setup

if __name__ == "__main__":
  db.create_all()
  app.run(host='0.0.0.0', port=8080)