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

#-------------------------------------------------
#Instance of a flask app
#-------------------------------------------------

app = Flask(__name__)
moment = Moment(app)
db=SQLAlchemy(app)

@app.route('/')
def index():

    return 'Redeye Homepage'
