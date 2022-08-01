from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = python3auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet.html'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)


config = {

  "apiKey": "AIzaSyD01MX_zkp69Jf4qdqqRR83holC3xLDrB4",

  "authDomain": "fir-6a332.firebaseapp.com",

  "projectId": "fir-6a332",
  
  "storageBucket": "fir-6a332.appspot.com",

  "messagingSenderId": "703491393980",

  "appId": "1:703491393980:web:94f1e8259742d77d6043b9",

  "measurementId": "G-6N0XJQ0C9T",

  "databaseURL": ""
} 