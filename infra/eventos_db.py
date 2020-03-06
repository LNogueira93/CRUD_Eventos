import sqlite3

db_name = "eventos.db"
table_name = "evento"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id_evento INTEGER PRIMARY KEY AUTOINCREMENT not null, nome_evento TEXT VARCHAR (20) not null, descricao TEXT VARCHAR (50) null, data_criacao NUMERIC DATETIME null, data_atualizacao NUMERIC DATETIME null, local_evento TEXT VARCHAR (50) not null, qntd_ingresso INTEGER not null, preco_ingresso REAL not null, ingresso_vendido INTEGER null, idade_minima INTEGER not null);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima):
    sql = f"INSERT INTO {table_name} (id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, 1, "Deus é amor", "Gospel", "02/10/2019", "02/05/2020", "Rua Santa", 150, 51.5, 70, 12)
        popularDb(cursor, 2, "Rockers", "Rock", "02/10/2017", "02/08/2019", "Rua do Rock", 160, 65.5, 80, 18)
        popularDb(cursor, 3, "Baladeiros", "Balada", "02/03/2020", "06/03/2020", "Rua Augusta", 300, 75.9, 180, 18)
        popularDb(cursor, 4, "Fumaceiçou", "Fumaceira", "15/12/2018", "02/01/2020", "Rua dos Gnomos Verdes", 90, 33.7, 60, 16)
        popularDb(cursor, 5, "Rocketseat", "DEV Master", "28/02/2020", "05/03/2020", "Rua do Object", 550, 125.8, 441, 15)
        popularDb(cursor, 6, "Orq. sinfônica", "Clássico", "27/08/2013", "20/01/2020", "Rua do Maestro", 1500, 154.9, 750, 12)
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()
    
init()