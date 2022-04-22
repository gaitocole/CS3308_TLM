from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/")
def landingPage():
    return render_template("LandingPage.html")

@app.route("/new")
def newUserPage():
    return render_template("NewUser.html")

@app.route("/tasks")
def taskPage():
    return render_template("taskPage.html")