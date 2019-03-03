from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from posts.blueprint import posts

app=Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_pefix='/blog')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  username = db.Column(db.String(80), unique=True, nullable=False)
   # email = db.Column(db.String(120), unique=True, nullable=False)

    #def __repr__(self):
     #   return '<User %r>' % self.username

