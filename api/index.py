from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/Inicio")
def Inicio():
    return render_template("Inicio.html")

@app.route("/Sobre")
def Sobre():
    return render_template("Sobre.html")

@app.route("/Contato")
def Contato():
    return render_template("Contato.html")
