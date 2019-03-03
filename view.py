from app import app
from flask import render_template

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration')
def reg():
    return render_template('registration.html')

@app.route('/login')
def log():
    return render_template('authorization.html')

#@app.route('/admin')
#def admin():
 #   return render_template('AdminPage.html')
