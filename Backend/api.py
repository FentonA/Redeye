#--------------------------------------------------
#Imports
#--------------------------------------------------

import json 
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from models import Client, Artist, Gallery, Photos, Posts, Comments, setup_db, db
from auth.auth import AuthError, requires_auth
from flask_cors import CORS



#===================================================================
# Pagination
#===================================================================
#ITEMS_PER_PAGE = 15
# def paginate_questions(request, selection):
#     page = request.args.get('page', 1, type=int)
#     start = (page - 1) * QUESTIONS_PER_PAGE
#     end = start + QUESTIONS_PER_PAGE
#     # format is function in model will arrange data like in it
#     questions = [question.format() for question in selection]
#     # select data from page =1 to 10
#     current_questions = questions[start:end]
#     return current_questions

#-------------------------------------------------
#Instance of a flask app and CORS set up

app = Flask(__name__)
moment = Moment(app)
db=SQLAlchemy(app)
CORS(app)
   

#------------------------------------------------------------------
#Cors setup
#------------------------------------------------------------------

@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type, Authorization, true')
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET, PATCH, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Origin', '*')
        
    return response 
#------------------------------------------------------------------
#Routes
#------------------------------------------------------------------

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile_artist():
    return render_template('profile.html')


@app.route('/posts')
@requires_auth('get:post')
def get_post():
    try:
        post = Post.query.order_by(desc(Post.id))
        return jsonify({
            'success': True,
            'post': post
        })
    except:
        return "error"
#Posting new enquiries
@app.route('/new_post', methods=['POST'])
@requires_auth('post:gig')
def post(f):
    body = request.get_json()
    new_post = Posts(
        title = body.get('title'),
        description = body.get('description'),
        price = body.get('price')
        )

    try: 
        new_post.insert()
        return jsonify({
            'success': True, 
            'posts':  Post.query.all()
        })
    except:
        return 'Error implementing new post'

#Post editing route
# @app.route('/price/<int:id>', methods =['PATCH'])
# @requires_auth('patch:edit')
# def post(id):

#     body = request

