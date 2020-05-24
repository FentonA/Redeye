#-----------------------------------
#imports
#-----------------------------------
import os
from sqlalchemy import Column, String, Integer, create_engine
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
        payment_history = db.Column(db.string(128), index=True)
        
        
    class Artist(db.model):
        __tablename__ = 'artists'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        #Authkey
        received_invoices = db.Column(db.String(128), index=True)
        Gallery = db.relationship('Gallery', backref='artists', lazy=True)

    class Gallery(db.model):

        id = Column(Integer, primary_key=True)
        Title = Column(db.Varchar(120))
        Description = Column(db.Varchar(255))
        photo = db.relationship('Photos', backref='Gallery', lazy=True)
    
    class Photos(db.model):
        __tablename__ = 'photos'
        id = Column(Integer, primary_key = True)
        Title = Column(db.Vachar(120))
        Description = Column(db.Varchar(128))
        Image = Column(db.Varchar(50))