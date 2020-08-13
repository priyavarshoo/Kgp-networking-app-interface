from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, AdminRegistrationForm
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
posts = [
    {
         'author': 'Abc Def',
        'title': 'Foundation Day Celebration',
        'content': 'XXXXX XX XXXXXXXx',
        'date_posted': 'April 28, 2017'
    },
    {
        'author': 'Dr. Ranjita Bhagwan',
        'title': 'Seminar on "Using Data to Build Better Systems and Services" ',
        'content': 'Microsoft Research',
        'date_posted': 'January 16, 2020'
    }
]


@app.route("/signup")
def signup():
    return render_template('signup.html', title='Sign Up')
    
@app.route("/logincom")
def logincom():
    return render_template('logincom.html', title='Log In')
    
@app.route("/")
@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html',title='User Sign Up', form = form)


@app.route("/adregister",methods=['GET','POST'])
def adregister():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
   
    return render_template('adregister.html',title='Admin Sign Up' ,form = form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html', title="Register", form=form)

@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title='Home')

if __name__ == '__main__':
    app.run(debug=True)
