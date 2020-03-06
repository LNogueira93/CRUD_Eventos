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

@eventos_app.route('/cadastrar', methods=["POST"])
def cadastrar_evento():
    if request.is_json:
        novo_evento = request.get_json()
        print("NOVO JSON DA APII_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(novo_evento)
        evento = service_criar(novo_evento)
        if evento == None:
            return jsonify({'erro': 'evento ja existe'}), 400
        return jsonify(evento)
    else:
        novo_evento = {}
        novo_evento["id"] = request.form.get("id")
        novo_evento["nome"] = request.form.get("nome")
        novo_evento["categoria"] = request.form.get("categoria")
        novo_evento["local"] = request.form.get("local")
        novo_evento["organizador"] = request.form.get("organizador")
        novo_evento["email"] = request.form.get("email")
        print("NOVO JSON DO FORM_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(novo_evento)
        evento = service_criar(novo_evento)
        if evento == None:
            return jsonify({'erro': 'evento ja existe'}), 400
        # return jsonify(evento)
        eventos = service_listar()
        return render_template("lista.html", eventos=eventos)

@eventos_app.route('/cadastro', methods=['GET', 'POST'])
def pagina_cadastro():
    return render_template("cadastro.html")

@eventos_app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def alterar_evento(id):
    if request.is_json:
        evento_data = request.get_json()
        print("ATUALIZAR VIA APII_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(evento_data)
        if request.method == "POST":
            if ("nome" not in evento_data):
                return jsonify({"erro": "evento sem nome"}), 400
            elif ("categoria" not in evento_data):
                return jsonify({"erro": "evento sem categoria"}), 400
            elif ("local" not in evento_data):
                return jsonify({"erro": "evento sem local"}), 400
            elif ("organizador" not in evento_data):
                return jsonify({"erro": "evento sem oraganizador"}), 400
            elif ("email" not in evento_data):
                return jsonify({"erro": "evento sem email"}), 400
            atualizado = service_atualiza(id, evento_data["nome"], evento_data["categoria"], evento_data["local"], evento_data["organizador"], evento_data["email"])
            if atualizado != None:
                return jsonify(atualizado), 200
            return jsonify({"erro": "evento nao encontrado"}), 400
        return render_template("atualizar.html", evento_data=evento_data)
    else:
        evento = service_localiza(id)
        print("LOCALIZOU EVENTOO_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(evento)
        if evento != None:
            print("ATUALIZAR VIA FORM_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print(evento)
            if request.method == "POST":
                evento["nome"] = request.form.get("nome")
                evento["categoria"] = request.form.get("categoria")
                evento["local"] = request.form.get("local")
                evento["organizador"] = request.form.get("organizador")
                evento["email"] = request.form.get("email")
                if ("nome" not in evento):
                    return jsonify({"erro": "evento sem nome"}), 400
                elif ("categoria" not in evento):
                    return jsonify({"erro": "evento sem categoria"}), 400
                elif ("local" not in evento):
                    return jsonify({"erro": "evento sem local"}), 400
                elif ("organizador" not in evento):
                    return jsonify({"erro": "evento sem oraganizador"}), 400
                elif ("email" not in evento):
                    return jsonify({"erro": "evento sem email"}), 400
                atualizado = service_atualiza(id, evento["nome"], evento["categoria"], evento["local"], evento["organizador"], evento["email"])
                print("ATUALIZOU O EVENTOO_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                print(atualizado)
                if atualizado != None:
                    eventos = service_listar()
                    return render_template("lista.html", eventos=eventos)#, jsonify(atualizado), 200
                return jsonify({"erro": "evento nao encontrado"}), 400
            return render_template("atualizar.html", evento=evento)
        return jsonify({"erro": "evento nao encontrado"}), 400

@eventos_app.route('/buscar/<int:id>', methods=['GET'])
def localizar_evento(id):
    evento = service_localiza(id)
    if evento != None:
        return jsonify(evento)
    return jsonify({'erro': 'evento nao encontrado'}), 400

@eventos_app.route('/excluir/<int:id>', methods=['GET', 'DELETE'])
def remover_evento(id):
    removido = service_remover(id)
    if removido == 1:
        eventos = service_listar()
        return render_template("lista.html", eventos=eventos)
        #return jsonify(removido), 202
    return jsonify({'erro': 'evento nao encontrado'}), 400

@eventos_app.route('/eventos/resetar', methods=['DELETE'])
def resetar():
    service_resetar()
    return jsonify("Base de eventos reiniciada"), 202
