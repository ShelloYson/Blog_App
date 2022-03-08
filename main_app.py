from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)