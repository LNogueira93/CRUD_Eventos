import sqlite3
from model.evento import Eventos
from contextlib import closing

db_name = "eventos.db"
model_name = "evento"

def con():
    return sqlite3.connect(db_name)

def listar():
    registros = []
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name}")
        rows = cursor.fetchall()
        for (id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima) in rows:
            registros.append(Eventos.criar({"id_evento": id_evento, "nome_evento": nome_evento, "descricao": descricao, "data_criacao": data_criacao, "data_atualizacao": data_atualizacao, "local_evento": local_evento, "qntd_ingresso": qntd_ingresso, "preco_ingresso": preco_ingresso, "ingresso_vendido": ingresso_vendido, "idade_minima": idade_minima}))
        return registros

def consultar(id_evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE id_evento = ?", (str(id_evento),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Eventos.criar({"id_evento": row[0], "nome_evento": row[1], "descricao": row[2], "data_criacao": row[3], "data_atualizacao": row[4], "local_evento": row[5], "qntd_ingresso": row[6], "preco_ingresso": row[7], "ingresso_vendido": row[8], "idade_minima": row[9] })

def cadastrar(evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        result = cursor.execute(sql, (evento.id_evento, evento.nome_evento, evento.descricao, evento.data_criacao, evento.data_atualizacao, evento.local_evento, evento.qntd_ingresso, evento.preco_ingresso, evento.ingresso_vendido, evento.idade_minima))
        connection.commit()
        if cursor.lastrowid:
            return evento.__dict__()
        else:
            return None

def alterar(evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome_evento = ?, descricao = ?, data_criacao = ?, data_atualizacao = ?, local_evento = ?, qntd_ingresso = ?, preco_ingresso = ?, ingresso_vendido = ?, idade_minima = ? WHERE id_evento = ?"
        cursor.execute(sql, ( evento.nome_evento, evento.descricao, evento.data_criacao, evento.data_atualizacao, evento.local_evento, evento.qntd_ingresso, evento.preco_ingresso, evento.ingresso_vendido, evento.idade_minima, evento.id_evento))
        connection.commit()

def remover(evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE id_evento = ?"
        cursor.execute(sql, [evento.id_evento])
        connection.commit()