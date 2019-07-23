from app import app

@app.route('/') # decorator('/) function will "fire" index() when entering this url
def index():
    return "Hello World"

@app.route('/about')
def about():
    return "<h1 style='color:red'> About!</h1>"