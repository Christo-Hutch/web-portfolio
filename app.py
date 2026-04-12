from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/projects')
def projects_page():
    return render_template("projects.html")

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(
        directory="files", 
        path=filename, 
        as_attachment=True
    )

if __name__ == '__main__':
    app.run()
