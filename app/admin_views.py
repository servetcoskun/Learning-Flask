from app import app

from flask import render_template

@app.route('/admin/dashboard') # decorator('/) function will "fire" index() when entering this url
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route('/admin/profile')
def admin_profile():
    return render_template("admin/profile.html")