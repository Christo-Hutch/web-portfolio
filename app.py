from flask import Flask, render_template
import os

from data_to_web import get_details, get_projects

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/projects')
def projects_page():
    return render_template("projects.html", projects=get_projects())

@app.route('/journey')
def journey_page():
    return render_template("journey.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html", details=get_details())

if __name__ == '__main__':
    app.run()