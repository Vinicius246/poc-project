import sqlite3

DB_NAME = 'database.db'

def _conectar_banco():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DB_NAME)

def inicializar_db():
    """Cria a tabela de reservas se não existir."""
    conn = _conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sala TEXT NOT NULL,
            horario TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def listar_reservas_repo():
    """Consulta todas as reservas no banco de dados."""
    conn = _conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservas')
    registros = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'sala': r[1], 'horario': r[2]} for r in registros]

def reservar_sala_repo(sala, horario):
    """Adiciona uma nova reserva ao banco de dados."""
    conn = _conectar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reservas (sala, horario) VALUES (?, ?)', (sala, horario))
    conn.commit()
    conn.close()
