from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f77dbe78c1bec4a526d35172e6b6c944'


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(F'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '789456123':
            flash(F'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
   app.run(debug=True) 