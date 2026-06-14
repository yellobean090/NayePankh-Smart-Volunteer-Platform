from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h1>About Page Coming Soon</h1>"


@app.route("/volunteer")
def volunteer():
    return "<h1>Volunteer Page Coming Soon</h1>"


@app.route("/events")
def events():
    return "<h1>Events Page Coming Soon</h1>"


@app.route("/contact")
def contact():
    return "<h1>Contact Page Coming Soon</h1>"


@app.route("/dashboard")
def dashboard():
    return "<h1>Dashboard Coming Soon</h1>"


if __name__ == "__main__":
    print("Starting NayePankh Smart Volunteer Platform...")
    app.run(debug=True)