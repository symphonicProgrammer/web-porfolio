from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def my_portfolio():
    return render_template("index.html")

@app.route("/about.html")
def my_home_page():
    return render_template("about.html")

@app.route("/components.html")
def my_components():
    return render_template("components.html")

@app.route("/contact.html")
def my_contact():
    return render_template("contact.html")

@app.route("/thankyou.html")
def my_thanks():
    return render_template("thankyou.html")

@app.route("/work.html")
def my_work():
    return render_template("work.html")

@app.route("/works.html")
def my_works():
    return render_template("works.html")