from flask import Flask, jsonify, request, render_template, Blueprint
from rotas.eventos_api import eventos_app
import requests as Req
import infra.eventos_db as eventos_db

app = Flask(__name__)
app.register_blueprint(eventos_app)

@app.route('/')
def all():
    return render_template("index.html")

eventos_db.init()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
