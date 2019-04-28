from app import app
from flask import render_template

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/signup')
def reg():
    return render_template('signup.html')

@app.route('/login')
def log():
    return render_template('login.html')

