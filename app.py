from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## start SQL Alchemy things
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = "Super Secret"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
## end SQL Alchemy things

@app.route("/")
def index():
    # if this user is logged in, take to home
    # if not logged in, take to login
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form["confirm-password"]

        if password != confirm_password:
            return render_template('signup.html', error = "Passwords do not match!")
        
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('signup.html', error = "Username already exists.")
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/")
    else:
        return render_template('signup.html')

if __name__ == "__main__":
  db.create_all()
  app.run(host='0.0.0.0', port=8080)