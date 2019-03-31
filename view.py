from app import app
from flask import render_template

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/index')
def index():
    return render_template('posts/index.html')

@app.route('/registration')
def reg():
    return render_template('registration.html')

@app.route('/login')
def log():
    return render_template('authorization.html')

#@app.route('/admin')
#def admin():
 #   return render_template('AdminPage.html')

@app.route('/test')
def test():
    POST_USERNAME="python"
    POST_PASSWORD="python"

    Session = sessionmaker(bind=engine)
    s=Session()
    query=s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result=query.first()
    if result:
        return "Object found"
    else:
        return "Object not found" + POST_USERNAME + " " + POST_PASSWORD