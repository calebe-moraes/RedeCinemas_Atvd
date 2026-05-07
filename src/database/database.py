import sqlite3

conexao = sqlite3.connect("cinema.db")

cursor = conexao.cursor()

# Tabela filmes
cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    duracao INTEGER NOT NULL,
    genero TEXT NOT NULL,
    classificacao TEXT NOT NULL
)
""")

# Tabela cinemas
cursor.execute("""
CREATE TABLE IF NOT EXISTS cinemas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    capacidade INTEGER NOT NULL
)
""")

# Tabela sessoes
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    horario TEXT NOT NULL,
    publico INTEGER NOT NULL,
    filme_id INTEGER NOT NULL,
    cinema_id INTEGER NOT NULL,

    FOREIGN KEY (filme_id) REFERENCES filmes(id),
    FOREIGN KEY (cinema_id) REFERENCES cinemas(id)
)
""")

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")

