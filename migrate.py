import json
import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS auditorios (
    nome TEXT PRIMARY KEY,
    lugares INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    auditorio TEXT,
    data TEXT,
    FOREIGN KEY(auditorio) REFERENCES auditorios(nome)
)
''')

# Ler dados do arquivo JSON
with open('database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Inserir dados na tabela auditorios
for auditorio, lugares in data['auditórios'].items():
    cursor.execute('INSERT INTO auditorios (nome, lugares) VALUES (?, ?)', (auditorio, int(lugares.split()[0])))

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()