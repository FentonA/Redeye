#--------------------------------------------------
#Imports
#--------------------------------------------------

import json 
import babel
from flask import FLASK, render_template, request, Response, flash, redirect, url_for
from flask_moment import flask_moment
from flask_SQLAlchemy import flask_SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Formatter
from form import *
from flask_migrate import flask_migrate

#-------------------------------------------------
#Instance of a flask app
#-------------------------------------------------

app = Flask(__name__)

@app.route('/')
def index():

    return 'Redeye Homepage'
