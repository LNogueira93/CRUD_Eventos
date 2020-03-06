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
        novo_evento["id_evento"] = request.form.get("id_evento")
        novo_evento["nome_evento"] = request.form.get("nome_evento")
        novo_evento["descricao"] = request.form.get("descricao")
        novo_evento["data_criacao"] = request.form.get("data_criacao")
        novo_evento["data_atualizacao"] = request.form.get("data_atualizacao")
        novo_evento["local_evento"] = request.form.get("local_evento")
        novo_evento["qntd_ingresso"] = request.form.get("qntd_ingresso")
        novo_evento["preco_ingresso"] = request.form.get("preco_ingresso")
        novo_evento["ingresso_vendido"] = request.form.get("ingresso_vendido")
        novo_evento["idade_minima"] = request.form.get("idade_minima")
        # novo_evento["id"] = request.form.get("id")
        # novo_evento["nome"] = request.form.get("nome")
        # novo_evento["categoria"] = request.form.get("categoria")
        # novo_evento["local"] = request.form.get("local")
        # novo_evento["organizador"] = request.form.get("organizador")
        # novo_evento["email"] = request.form.get("email")
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

@eventos_app.route('/atualizar/<int:id_evento>', methods=['GET', 'POST'])
def alterar_evento(id_evento):
    if request.is_json:
        evento_data = request.get_json()
        print("ATUALIZAR VIA APII_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(evento_data)
        if request.method == "POST":
            if ("nome_evento" not in evento_data):
                return jsonify({"erro": "evento sem nome"}), 400
            elif ("descricao" not in evento_data):
                return jsonify({"erro": "evento sem descricao"}), 400
            elif ("data_criacao" not in evento_data):
                return jsonify({"erro": "evento sem data de criacao"}), 400
            elif ("data_atualizacao" not in evento_data):
                return jsonify({"erro": "evento sem data de atualizacao"}), 400
            elif ("local_evento" not in evento_data):
                return jsonify({"erro": "evento sem local do evento"}), 400
            elif ("qntd_ingresso" not in evento_data):
                return jsonify({"erro": "evento sem quantidade de ingresso"}), 400
            elif ("preco_ingresso" not in evento_data):
                return jsonify({"erro": "evento sem preco do ingresso"}), 400
            elif ("ingresso_vendido" not in evento_data):
                return jsonify({"erro": "evento sem quantidade de ingresso vendido"}), 400
            elif ("idade_minima" not in evento_data):
                return jsonify({"erro": "evento sem idade minima"}), 400
            atualizado = service_atualiza(id_evento, evento_data["nome_evento"], evento_data["descricao"], evento_data["data_criacao"], evento_data["data_atualizacao"], evento_data["local_evento"], evento_data["qntd_ingresso"], evento_data["preco_ingresso"], evento_data["ingresso_vendido"], evento_data["idade_minima"])
            if atualizado != None:
                return jsonify(atualizado), 200
            return jsonify({"erro": "evento nao encontrado"}), 400
        return render_template("atualizar.html", evento_data=evento_data)
    else:
        evento = service_localiza(id_evento)
        print("LOCALIZOU EVENTOO_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(evento)
        if evento != None:
            print("ATUALIZAR VIA FORM_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print(evento)
            if request.method == "POST":
                evento = {}
                evento["id_evento"] = request.form.get("id_evento")
                evento["nome_evento"] = request.form.get("nome_evento")
                evento["descricao"] = request.form.get("descricao")
                evento["data_criacao"] = request.form.get("data_criacao")
                evento["data_atualizacao"] = request.form.get("data_atualizacao")
                evento["local_evento"] = request.form.get("local_evento")
                evento["qntd_ingresso"] = request.form.get("qntd_ingresso")
                evento["preco_ingresso"] = request.form.get("preco_ingresso")
                evento["ingresso_vendido"] = request.form.get("ingresso_vendido")
                evento["idade_minima"] = request.form.get("idade_minima")
                if ("nome_evento" not in evento):
                    return jsonify({"erro": "evento sem nome"}), 400
                elif ("descricao" not in evento):
                    return jsonify({"erro": "evento sem descricao"}), 400
                elif ("data_criacao" not in evento):
                    return jsonify({"erro": "evento sem data de criacao"}), 400
                elif ("data_atualizacao" not in evento):
                    return jsonify({"erro": "evento sem data de atualizacao"}), 400
                elif ("local_evento" not in evento):
                    return jsonify({"erro": "evento sem local do evento"}), 400
                elif ("qntd_ingresso" not in evento):
                    return jsonify({"erro": "evento sem quantidade de ingresso"}), 400
                elif ("preco_ingresso" not in evento):
                    return jsonify({"erro": "evento sem preco do ingresso"}), 400
                elif ("ingresso_vendido" not in evento):
                    return jsonify({"erro": "evento sem quantidade de ingresso vendido"}), 400
                elif ("idade_minima" not in evento):
                    return jsonify({"erro": "evento sem idade minima"}), 400
                atualizado = service_atualiza(id_evento, evento["nome_evento"], evento["descricao"], evento["data_criacao"], evento["data_atualizacao"], evento["local_evento"], evento["qntd_ingresso"], evento["preco_ingresso"], evento["ingresso_vendido"], evento["idade_minima"])
                print("ATUALIZOU O EVENTOO_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                print(atualizado)
                if atualizado != None:
                    eventos = service_listar()
                    return render_template("lista.html", eventos=eventos)#, jsonify(atualizado), 200
                return jsonify({"erro": "evento nao encontrado"}), 400
            return render_template("atualizar.html", evento=evento)
        return jsonify({"erro": "evento nao encontrado"}), 400

@eventos_app.route('/buscar/<int:id_evento>', methods=['GET'])
def localizar_evento(id):
    evento = service_localiza(id)
    if evento != None:
        return jsonify(evento)
    return jsonify({'erro': 'evento nao encontrado'}), 400

@eventos_app.route('/excluir/<int:id_evento>', methods=['GET', 'DELETE'])
def remover_evento(id_evento):
    removido = service_remover(id_evento)
    if removido == 1:
        eventos = service_listar()
        return render_template("lista.html", eventos=eventos)#return jsonify(removido), 202
    return jsonify({'erro': 'evento nao encontrado'}), 400

@eventos_app.route('/eventos/resetar', methods=['DELETE'])
def resetar():
    service_resetar()
    return jsonify("Base de eventos reiniciada"), 202
