from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Abas El-aaad',
        'title': 'Post Blog 1',
        'content': 'Content 1',
        'date': 'Mar, 20, 2024',
    },
    {
        'author': 'Taha Hussin',
        'title': 'Post Blog 2',
        'content': 'Content 2',
        'date': 'Mar, 21, 2024',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
   app.run(debug=True) 