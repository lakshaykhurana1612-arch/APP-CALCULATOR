from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = "secret123"

login_manager = LoginManager()
login_manager.init_app(app)

# dummy user
class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {"bro": {"password": "123"}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def home():
    return "<h1>Home Page</h1><a href='/login'>Login</a>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            user = User(username)
            login_user(user)
            return redirect("/dashboard")

    return render_template("login.html")
@app.route("/calculator")
@login_required
def calculator():
    return render_template("calculator.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("home.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)