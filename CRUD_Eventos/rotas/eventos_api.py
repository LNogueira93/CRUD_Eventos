from flask import Blueprint, jsonify, request, Flask, render_template
from services.eventos_services import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar

eventos_app = Blueprint('eventos_app', __name__, template_folder='templates')



@eventos_app.route('/index')
def home():
    return render_template("index.html")

@eventos_app.route('/lista')  # '/lista'
def listar_eventos():
    eventos = service_listar()
    return render_template("lista.html", eventos=eventos)
    # return jsonify(lista)


# cadastro , methods=['POST']
@eventos_app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_evento():
    novo_evento = request.get_json()
    evento = service_criar(novo_evento)
    if evento == None:
        return jsonify({'erro': 'evento ja existe'}), 400
    return jsonify(evento)

    # cadastro , methods=['POST']
@eventos_app.route('/cadastro', methods=['GET', 'POST'])
def pagina_cadastro():
    return render_template("cadastro.html")


@eventos_app.route('/atualizar/<int:ident>', methods=['PUT'])  # atualizar
def alterar_evento(ident):
    evento_data = request.get_json()
    if ('nome' not in evento_data):
        return jsonify({'erro': 'evento sem nome'}), 400
    elif ('categoria' not in evento_data):
        return jsonify({'erro': 'evento sem categoria'}), 400
    elif ('local' not in evento_data):
        return jsonify({'erro': 'evento sem local'}), 400
    elif ('organizador' not in evento_data):
        return jsonify({'erro': 'evento sem oraganizador'}), 400
    elif ('email' not in evento_data):
        return jsonify({'erro': 'evento sem email'}), 400
    atualizado = service_atualiza(ident, evento_data['nome'], evento_data['categoria'],
                                  evento_data['local'], evento_data['organizador'], evento_data['email'])
    if atualizado != None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'evento nao encontrado'}), 400


@eventos_app.route('/buscar/<int:ident>', methods=['GET'])  # buscar
def localizar_evento(ident):
    evento = service_localiza(ident)
    if evento != None:
        return jsonify(evento)
    return jsonify({'erro': 'evento nao encontrado'}), 400


@eventos_app.route('/excluir/<int:ident>', methods=['DELETE'])  # excluir
def remover_evento(ident):
    removido = service_remover(ident)
    if removido == 1:
        return jsonify(removido), 202
    return jsonify({'erro': 'evento nao encontrado'}), 400


@eventos_app.route('/eventos/resetar', methods=['DELETE'])
def resetar():
    service_resetar()
    return jsonify("Base de eventos reiniciada"), 202


##########################################################


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
#     evento = Eventos.query.filter_by(ident=id).first()

#     db.session.delete(evento)
#     db.session.commit()

#     eventos = Eventos.query.all()
#     return render_template("lista.html", eventos=eventos)


# @app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
# def atualizar(id):
#     evento = Eventos.query.filter_by(ident=id).first()

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
