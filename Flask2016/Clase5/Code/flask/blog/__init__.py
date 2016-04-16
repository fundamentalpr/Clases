__author__ = 'alfredo'
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'A0cr98j/3yX R~XHH!jmN]LWX/,?RT'
client = MongoClient('mongodb://user:pass@ds051788.mlab.com:51788/class')

import blog.views
import blog.account