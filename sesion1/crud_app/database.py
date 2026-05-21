import sqlite3

DB_NAME = "estudiantes.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            carrera TEXT NOT NULL,
            semestre INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()
