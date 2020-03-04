from infra.eventos_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.evento import Eventos

def listar():
    # for evento in dao_listar():
    #     return Eventos.__call__(self=evento)
    # lista = []
    # eventos = Eventos.__dict__()
    # daoListar = dao_listar()
    # for evento in daoListar:
    #     lista.push(eventos)
    #lista = [Eventos.__dict__() for evento in dao_listar()]
    # return [Eventos.__dict__() for evento in dao_listar()]
    # return [Eventos.__call__(self=evento) for evento in dao_listar()]
    return [evento.__dict__() for evento in dao_listar()]

def localizar(id):
    evento = dao_consultar(id)
    if evento == None:
        return None
    return evento.__call__()

def criar(evento_data):
    # if localizar(evento_data["id"]) == None:
    if localizar(evento_data) == None:
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