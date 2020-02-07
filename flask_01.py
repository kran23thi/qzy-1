from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'quiz 1': '.....',

    },
    {
        'quiz 2': '.....',

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('homepage.html', posts=posts)


@app.route("/about")
def about():
    return render_template('aboutpage.html', title='About')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registrationpage.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ananya.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('loginpage.html', title='Login', form=form)

@app.route("/Quizpage1", methods =['GET','POST'])
def quiz1():
    return render_template('Quizpage1.html', title='Quiz')

if __name__ == '__main__':
    app.run(debug=True)
