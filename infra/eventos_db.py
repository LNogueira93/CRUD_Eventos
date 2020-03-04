import sqlite3

db_name = "eventos.db"
table_name = "eventos"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (ident integer PRIMARY KEY AUTOINCREMENT not null, nome TEXT null, categoria TEXT null, local TEXT null, organizador TEXT null, email TEXT null);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, ident, nome, categoria, local, organizador, email):
    sql = f"INSERT INTO {table_name} (ident, nome, categoria, local, organizador, email) VALUES (?, ?, ?, ?, ?, ?);"
    cursor.execute(sql, (ident, nome, categoria, local, organizador, email))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, "Thomas Alexandre", "Gospel", "Avenida Paulista", "Deus é amor", "thomas@email.com")
        popularDb(cursor, "Lucio Mendes", "Rock", "Rua do Rock", "Rokcker", "rocker@email.com")
        popularDb(cursor, "Vinicius Williams", "Clássico", "Sala São Paulo", "Vinicius", "vinicius@email.com")
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()
    
init()