from app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return '<h2> Admin Dashboard Area</h2>'
@app.route('/admin/profile')
def admin_profile():
    return("<h1 style='color:red'> Er.Manendra Nath Shukla")
