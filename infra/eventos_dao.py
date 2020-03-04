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
        for (id, nome, categoria, local, organizador, email) in rows:
            registros.append(Eventos.criar({"id": id, "nome": nome, "categoria": categoria, "local": local, "organizador": organizador, "email": email}))
        return registros

def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE id = ?", (str(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Eventos.criar({"id": row[0], "nome": row[1], "categoria": row[2], "local": row[3], "organizador": row[4], "email": row[5]})

def cadastrar(evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (id, nome, categoria, local, organizador, email) VALUES (?, ?, ?, ?, ?, ?)"
        result = cursor.execute(sql, (evento.id, evento.nome, evento.categoria, evento.local, evento.organizador, evento.email))
        connection.commit()
        if cursor.lastrowid:
            return evento.__dict__()
        else:
            return None

def alterar(evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome = ?, categoria = ?, local = ?, organizador = ?, email = ? WHERE id = ?"
        cursor.execute(sql, (evento.nome, evento.categoria, evento.local, evento.organizador, evento.email, evento.id))
        connection.commit()

def remover(evento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE id = ?"
        cursor.execute(sql, f"{evento.id}")
        connection.commit()