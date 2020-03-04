import sqlite3

db_name = "eventos.db"
table_name = "evento"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY AUTOINCREMENT, nome TEXT null, categoria TEXT null, local TEXT null, organizador TEXT null, email TEXT null);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, id, nome, categoria, local, organizador, email):
    sql = f"INSERT INTO {table_name} (id, nome, categoria, local, organizador, email) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (id, nome, categoria, local, organizador, email))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, 1, "Lucas Nogueira", "Gospel", "Avenida Paulista", "Deus é amor", "ln@email.com")
        popularDb(cursor, 2, "Sidney Santos", "Rock", "Rua do Rock", "Rokcker", "ss@email.com")
        popularDb(cursor, 3, "Matheus Leal", "Balada", "Rua Augusta", "DrinkOu", "ml@email.com")
        popularDb(cursor, 4, "Pedro Barata", "Fumaceira", "Avenida Paulista", "Gnomos verdes", "pb@email.com")
        popularDb(cursor, 5, "Paulo Guedes", "Rocketseat", "Rua do DEV", "Codar até morrer", "pg@email.com")
        popularDb(cursor, 6, "Roberto Carlos", "Clássico", "Sala São Paulo", "Orq. sinfônica", "rc@email.com")
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()
    
init()