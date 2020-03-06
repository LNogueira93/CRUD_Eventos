from infra.eventos_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.evento import Eventos

def listar():
    return [evento.__dict__() for evento in dao_listar()]

def localizar(id_evento):
    evento = dao_consultar(id_evento)
    if evento == None:
        return None
    return evento.__dict__()

def criar(evento_data):
    if localizar(evento_data["id_evento"]) == None:
        evento = Eventos.criar(evento_data)
        return dao_cadastrar(evento)
    return None

def remover(id_evento):
    dados_evento = localizar(id_evento)
    if dados_evento == None:
        return 0
    dao_remover(Eventos.criar(dados_evento))
    return 1

def atualizar(id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima):
    evento = Eventos.criar({"id_evento": id_evento, "nome_evento": nome_evento, "descricao": descricao, "data_criacao": data_criacao, "data_atualizacao": data_atualizacao, "local_evento": local_evento, "qntd_ingresso": qntd_ingresso, "preco_ingresso": preco_ingresso, "ingresso_vendido": ingresso_vendido, "idade_minima": idade_minima})
    dao_alterar(evento)
    return localizar(id_evento)
    
def resetar():
    eventos = listar()
    for evento in eventos:
        remover(evento["id_evento"])