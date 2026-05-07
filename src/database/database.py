import sqlite3

conexao = sqlite3.connect("cinema.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    duracao INTEGER NOT NULL,
    genero TEXT NOT NULL,
    classificacao TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")

