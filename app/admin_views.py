from app import app

@app.route('/admin/dashboard') # decorator('/) function will "fire" index() when entering this url
def admin_dashboard():
    return "Admin dashboard"

@app.route('/admin/profile')
def admin_profile():
    return "Admin profile"