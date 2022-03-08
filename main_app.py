from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5e4c4a1ab3d094fa267709999c1a2fd2'

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)