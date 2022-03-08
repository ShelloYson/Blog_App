# This is a blog app that allows users to register and post blogs
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5e4c4a1ab3d094fa267709999c1a2fd2'

# Lists of post dictionaries

posts = [
    
    {
        'author': 'Shello Yson',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 14, 2022',
    },
    
    {
        'author': 'Jake Lee',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 16, 2022',
    },
    
    {
        'author': 'Taehyung Kim',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'February 18, 2022',
    }
    
]

# Routes

# Route for homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# Route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Route for registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# Route for login page
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# Allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)