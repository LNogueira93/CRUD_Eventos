from infra.eventos_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.evento import Eventos

def listar():
    return [evento.__dict__() for evento in dao_listar()]

def localizar(id):
    evento = dao_consultar(id)
    if evento == None:
        return None
    return evento.__dict__()

def criar(evento_data):
    if localizar(evento_data["id"]) == None:
        evento = Eventos.criar(evento_data)
        return dao_cadastrar(evento)
    return None

def remover(id):
    dados_evento = localizar(id)
    if dados_evento == None:
        return 0
    dao_remover(Eventos.criar(dados_evento))
    return 1

def atualizar(id, nome, categoria, local, organizador, email):
    evento = Eventos.criar({"id": id, "nome": nome, "categoria": categoria, "local": local, "organizador": organizador, "email": email})
    dao_alterar(evento)
    return localizar(id)
    
def resetar():
    eventos = listar()
    for evento in eventos:
        remover(evento["id"])