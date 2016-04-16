from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/second")
def hello2():
    return "<html><body style='background-color:red'>Hello World!</body></html>"


@app.route("/third")
def hello3():
    returnData = "<html><body width=600px;>"
    for r in range(0, 255, 10):
        for g in range(0, 255, 10):
            for b in range(0, 255, 10):
                returnData += "<div style='width:10px;display:inline-block;height10px;background-color:rgb(" + str(
                    r) + "," + str(g) + "," + str(b) + ")'>&nbsp;</div>"
                returnData += "</body></html>"
    return returnData


@app.route("/hello")
@app.route("/hello/<nombre>")
def hello4(nombre="World"):
    return render_template("hello.html", nombre=nombre)

@app.route("/listanombre")

def lista():
    return render_template("loop.html", users={"Jose","Maria","Felipe","Pepe"})



@app.route('/carros/<tipo>')
def carros(tipo):
    if tipo == "lambo":
        return render_template("carro.html", photo="http://i.imgur.com/kgCcPbM.jpg")
    elif tipo == "puntoocho":
        return render_template("carro.html",
                               photo="http://carphotos.cardomain.com/ride_images/3/2278/1101/30693050001_large.jpg")
    return "Ese no lo tengo"


@app.route('/carros/<int:tipo>')
def carros2(tipo):
    if tipo == 1:
        return render_template("carro.html", photo="http://i.imgur.com/kgCcPbM.jpg")
    elif tipo == 2:
        return render_template("carro.html",
                               photo="http://carphotos.cardomain.com/ride_images/3/2278/1101/30693050001_large.jpg")
    return "Ese no lo tengo"


@app.route('/carropost', methods=['POST'])
def carros3():
    if request.method == 'POST':
        tipo = request.form['carro']
        if tipo == "lambo":
            return render_template("carro.html", photo="http://i.imgur.com/kgCcPbM.jpg")
        elif tipo == "puntoocho":
            return render_template("carro.html",
                                   photo="http://carphotos.cardomain.com/ride_images/3/2278/1101/30693050001_large.jpg")
    return "Ese no lo tengo"


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        url = request.form['nextpage']
    if user == "nombre" and password == "pass":
        return redirect(url)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)