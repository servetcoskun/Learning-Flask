from app import app

from flask import render_template

from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route('/') # decorator('/) function will "fire" index() when entering this url
def index():
    return render_template("public/index.html")

@app.route('/jinja')
def jinja():

    my_name = "Servet"

    age = 27

    langs = ["Python", "C++", "Bash", "C", "MATLAB"]

    friends = {
        "Hank": 44,
        "Tony": 56,
        "Melissa": 30,
        "John": 28
    }

    colours = ('Red', 'Green', 'Blue')

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        
        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name="Flask Jinja",
        description="Template design tutorial",
        url="https://github.com/servetcoskun/jinja.git"
    )

    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h2> This is some HTML</h2>"

    suspicious = "<script>alert('You got hacked!')</script>"

    return render_template('public/jinja.html', my_name=my_name, age=age,
    langs=langs, friends=friends, colours=colours,
    cool=cool, GitRemote=GitRemote, repeat=repeat,
    my_remote=my_remote, date=date, my_html=my_html,
    suspicious=suspicious)

@app.route('/about')
def about():
    return render_template("public/about.html")