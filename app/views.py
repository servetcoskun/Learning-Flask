from app import app

from flask import render_template

@app.route('/') # decorator('/) function will "fire" index() when entering this url
def index():
    return render_template("public/index.html")

@app.route('/about')
def about():
    return render_template("public/about.html")