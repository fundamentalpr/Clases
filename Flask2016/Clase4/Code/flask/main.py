from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from pymongo import MongoClient
import datetime
import hashlib


app = Flask(__name__)
app.secret_key = 'A0cr98j/3yX R~XHH!jmN]LWX/,?RT'
client = MongoClient('mongodb://user:pass@ds051788.mlab.com:51788/class')


@app.route("/")
def index():
    return render_template( "index.html")

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
        return "Cuenta creada"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)