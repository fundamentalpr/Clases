from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from blog import app
from blog import client
import datetime

@app.route("/")
def index():
    tmp = list(client["class"].post.find().sort("date", 1))
    return render_template("index.html", usersWithPost= tmp)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        user =  session['username']
        contenido = request.form['contenido']
    if user != '' and contenido != '':
        post = {"user": user,
                    "contenido": contenido,
                    "date": datetime.datetime.utcnow()
                    }
        client["class"].post.insert_one(post)
        return redirect('\\')
    else:
        abort(401)

