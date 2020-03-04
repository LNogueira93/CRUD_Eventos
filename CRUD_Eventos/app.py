from flask import Flask, jsonify, request, render_template, Blueprint
from rotas.eventos_api import eventos_app
import requests as Req
import infra.eventos_db as eventos_db

app = Flask(__name__)
app.register_blueprint(eventos_app)

@app.route('/')
def all():
    #eventos = Req.get("http://localhost:5000/").json()
    return render_template("index.html")#eventos=eventos

eventos_db.init()

if __name__ == '__main__':
    app.run(port=5000, debug=True)

#######################################################

# ANTIGO

# from flask import Flask, render_template, request, url_for, redirect

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# db = SQLAlchemy(app)


# class Eventos(db.Model):
#     __tablename__ = 'eventos'
#     _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String)
#     categoria = db.Column(db.String)
#     local = db.Column(db.String)
#     organizador = db.Column(db.String)
#     email = db.Column(db.String)

#     def __init__(self, nome, categoria, local, organizador, email):
#         self.nome = nome
#         self.categoria = categoria
#         self.local = local
#         self.organizador = organizador
#         self.email = email

# db.create_all()


# @app.route("/index")
# def index():
#     return render_template("index.html")

# @app.route("/cadastrar")
# def cadastrar():
#     return render_template("cadastro.html")

# @app.route("/cadastro", methods=['GET', 'POST'])
# def cadastro():
#     if request.method == "POST":
#         nome = request.form.get("nome")
#         categoria = request.form.get("categoria")
#         local = request.form.get("local")
#         organizador = request.form.get("organizador")
#         email = request.form.get("email")

#         if nome and categoria and local and organizador and email:
#             event = Eventos(nome, categoria, local, organizador, email)
#             db.session.add(event)
#             db.session.commit()
#     return redirect(url_for("index"))


# @app.route("/lista")
# def lista():
#     eventos = Eventos.query.all()
#     return render_template("lista.html", eventos=eventos)

# @app.route("/excluir/<int:id>")
# def excluir(id):
#     evento = Eventos.query.filter_by(_id=id).first()

#     db.session.delete(evento)
#     db.session.commit()

#     eventos = Eventos.query.all()
#     return render_template("lista.html", eventos=eventos)


# @app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
# def atualizar(id):
#     evento = Eventos.query.filter_by(_id=id).first()

#     if request.method == "POST":
#         nome = request.form.get("nome")
#         categoria = request.form.get("categoria")
#         local = request.form.get("local")
#         organizador = request.form.get("organizador")
#         email = request.form.get("email")

#         if nome and categoria and local and organizador and email:
#             evento.nome = nome
#             evento.categoria = categoria
#             evento.local = local
#             evento.organizador = organizador
#             evento.email = email

#             db.session.commit()

#             return redirect(url_for("lista"))

#     return render_template("atualizar.html", evento=evento)

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)