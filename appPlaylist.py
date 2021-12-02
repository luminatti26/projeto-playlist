from flask import Flask, render_template, request, redirect
from repositorio import get_token, criar_playlist, criar_lista_artista, criar_lista_musica, finalizar_playlist

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run()
