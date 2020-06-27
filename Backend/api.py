#--------------------------------------------------
#Imports
#--------------------------------------------------

import json 
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from models import Client, Artist, Gallery, Photos, Posts, Comments, setup_db, db
from auth.auth import AuthError, requires_auth

#-------------------------------------------------
#Instance of a flask app
#-------------------------------------------------

app = Flask(__name__)
moment = Moment(app)
db=SQLAlchemy(app)

#------------------------------------------------------------------
#Routes
#------------------------------------------------------------------

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/profile', methods=['GET'])
def profile_artist():
    return render_template('profile.html')

#Posting new enquiries
@app.route('/new_post', methdos=['POST'])
@requires_auth('post:gig')
def post(f)
    body = request.get_json()
    new_post = Posts(
        title = body.get('title'),
        description = body.get('description'),
        price = body.get('price')
        )

    try: 
        new_post.insert()
    except:
        return 'Error implementing new post'

#Post editing route
# @app.route('/price/<int:id>', methods =['PATCH'])
# @requires_auth('patch:edit')
# def post(id):

#     body = request

