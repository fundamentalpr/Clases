__author__ = 'alfredo'

from flask import session
from flask import request
from flask import redirect
from flask import abort
from blog import app
from blog import client
import datetime
import hashlib



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        url = request.form['nextpage']
        coleccion = client["class"].usuarios
        doc = coleccion.find_one({"_id":user})
        if user == doc["_id"] and hashlib.sha224(password.encode('utf-8')).hexdigest() == doc["pass"]:
            session['username'] = user
            session['logged_in'] = True
            return redirect(url)
        else:
            abort(401)




@app.route('/logout')
def logout():
     session['username'] = ''
     session['logged_in'] = False
     return redirect('\\')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
    if user != '' and password != '':
        usuario = {"_id": user,
                    "pass": hashlib.sha224(password.encode('utf-8')).hexdigest(),
                    "date": datetime.datetime.utcnow()
                    }
        client["class"].usuarios.insert_one(usuario)
        session['username'] = user
        session['logged_in'] = True
        return redirect('\\')
    else:
        abort(401)