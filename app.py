from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY

posts = [
    {
        'author' : 'Jared Delora',
        'title' : ' Blog Post Title 1',
        'content' : 'First post content',
        'date_posted' : 'July 4, 2020'
    },
    {
        'author' : 'Jared Delora-Ellefson',
        'title' : ' Blog Post Title 2',
        'content' : 'Second post content',
        'date_posted' : 'July 5, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
