from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {

  "apiKey": "AIzaSyD01MX_zkp69Jf4qdqqRR83holC3xLDrB4",

  "authDomain": "fir-6a332.firebaseapp.com",

  "projectId": "fir-6a332",
  
  "storageBucket": "fir-6a332.appspot.com",

  "messagingSenderId": "703491393980",

  "appId": "1:703491393980:web:94f1e8259742d77d6043b9",

  "measurementId": "G-6N0XJQ0C9T",

  "databaseURL": "https://console.firebase.google.com/project/fir-6a332/database/fir-6a332-default-rtdb/data/~2F"
} 

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = python3auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        Full name = request.form['full name']
        Name = request.form['name']
        Bio = request.form['bio']
        try:
            login_session{'user'} = python3auth.create_user_with_email_and_password(email, password)
            user = {"name": Name, "bio": Bio, "full name": Full name}
            db.child("usera").child(login_session['user']['localId']).set(user)
            return redirect(ur_for("add_tweet"))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == "POST":
        try:
            tweet = {"Full name":request.form['full name'], "Name" :request.form['name'], "Bio": request.form['bio'], uid: ["localId"]}
            db.child("Tweets").push(tweet)
        except:
           print("Couldn't add tweet, try again")
    return render_template("add_tweet.html")

@app.route('/all_tweets', methods=['GET', 'POST'])
def all_tweets():
    display = db.child("Display").get().val()
    return render_template("tweets.html")

if __name__ == '__main__':
    app.run(debug=True)
