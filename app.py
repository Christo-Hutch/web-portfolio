from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/projects')
def projects_page():
    return render_template("projects.html")

@app.route('/journey')
def journey_page():
    return render_template("journey.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
