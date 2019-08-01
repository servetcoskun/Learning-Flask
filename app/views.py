from app import app

from flask import render_template, request, redirect, jsonify, make_response

from datetime import datetime


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")


# decorator('/) function will "fire" index() when entering this url
@app.route('/')
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


@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form

        username = req["username"]
        email = req.get("email")
        password = request.form["password"]  # pull straight from form

        print(username, email, password)

        return redirect(request.url)

    return render_template('public/sign_up.html')


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creator of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):
    user = None
    if username in users:
        user = users[username]

    return render_template("public/profile.html", username=username, user=user)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {bar} bar is {baz} baz is {foo}"

@app.route("/json", methods=["POST"])
def json():

    if request.is_json:
        
        req = request.get_json()

        response = {
            "message": "JSON received",
            "name": req.get("name")
        }
        # jsonify convert python string, list, and dicts to JSON
        res = make_response(jsonify(response), 200)

        return res
    
    else:

        res = make_response(jsonify({"message":"No JSON received"}), 400)

        return res


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    res = make_response(jsonify(req), 200)

    return res