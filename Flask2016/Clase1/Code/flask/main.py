from flask import Flask
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
    for r in range(0,255,10):
        for g in range(0,255,10):
            for b in range(0,255,10):
                returnData += "<div style='width:10px;display:inline-block;height10px;background-color:rgb("+str(r)+","+str(g)+","+str(b)+")'>&nbsp;</div>"
                returnData += "</body></html>"
    return returnData



if __name__ == "__main__":
    app.run()