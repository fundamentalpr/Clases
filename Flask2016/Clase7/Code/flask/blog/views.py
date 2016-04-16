from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from blog import app
from blog import client
import datetime
import os
import markdown
from flask import send_file

@app.route("/")
def index():
    tmp = list(client["class"].post.find().sort("date", 1))
    return render_template("index.html", usersWithPost= tmp)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        user =  session['username']
        contenido = markdown.markdown(request.form['contenido'])
        file = request.files['file']
        photo = ''
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo = os.path.join("..\\uploads", filename)
    if user != '' and contenido != '':
        post = {"user": user,
                    "contenido": contenido,
                    "date": datetime.datetime.utcnow(),
                    "photo": photo
                    }
        client["class"].post.insert_one(post)
        return redirect('\\')
    else:
        abort(401)

@app.route('/subirfotos')
def fotos():
    return render_template("subirfotos.html")

@app.route('/subirfotos2', methods=['GET', 'POST'])
def fotospost():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect('\\')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join("..\\uploads", filename))
