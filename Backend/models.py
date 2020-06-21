#-----------------------------------
#imports
#-----------------------------------
import os
from sqlalchemy import Column, String, Integer, VARCHAR, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

db_name = 'redeye'
db_path = "postgresql://postgres:7Pillars@{}/{}".format('localhost:5432', db_name)

db = SQLAlchemy()

'''
Database Set Up 
'''
def setup_db(app, database_path=db_path ):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()

    '''
    Clients
    '''
class Client(db.Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Authkey
    payment_id = db.Column(db.String(128), index=True)
    payment_history = db.Column(db.String(128), index=True)
    comments = db.relationship('Comments', backref = 'cient', lazy= True)
        
        
class Artist(db.Model):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    #Authkey
    received_invoices = db.Column(db.String(128), index=True)
    gallery = db.relationship('Gallery', backref='artists', lazy=True)
    comments = db.relationship('Comments', backref = 'artists', lazy = True)

class Gallery(db.Model):

    id = Column(Integer, primary_key=True)
    title = Column(db.VARCHAR(120))
    description = Column(db.VARCHAR(255))
    photo = db.relationship('Photos', backref='Gallery', lazy=True)
    
class Photos(db.Model):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key = True)
    title = Column(db.VARCHAR(120))
    description = Column(db.VARCHAR(128))
    image = Column(db.VARCHAR(50))

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    price = db.Column(db.VARCHAR(10))
    comments = db.relationship('Comments', backref ='Posts', lazy=True)

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(128), index = True)
    post_id = db.Column(db.Integer, db.ForeignKey('Posts.id'), nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable = False)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable = False)
