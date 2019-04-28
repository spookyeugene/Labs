#from __init__ import db
#from datetime import datetime
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#def slugify(s):
    #pattern = r'[^\w+]'
    #return re.sub(pattern, '-',s)

#class Post(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String(140))
    #slug = db.Column(db.String(140), unique=True)
    #body = db.Column(db.Text)
    #created = db.Column(db.DateTime, default=datetime.now())


  #  def __init__(self, *args, **kwargs):
        #super(Post, self), __init__(*args, **kwargs)
        #self.generate_slug()

    #def generate_slug(self):
        #if self.title:
            #self.slug = slugify(self.title)


    #def __repr__(self):
        #return '<Post id: [], title: ()>',format(self.id, self.title)