from database import conectar


def crear_estudiante(nombre, carrera, semestre, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO estudiantes (nombre, carrera, semestre, email) VALUES (?, ?, ?, ?)",
        (nombre, carrera, semestre, email)
    )
    conn.commit()
    conn.close()
    print(f"Estudiante '{nombre}' creado correctamente.")


def listar_estudiantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    filas = cursor.fetchall()
    conn.close()
    return filas


def buscar_estudiante(id_estudiante):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE id = ?", (id_estudiante,))
    fila = cursor.fetchone()
    conn.close()
    return fila


def actualizar_estudiante(id_estudiante, nombre, carrera, semestre, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE estudiantes SET nombre=?, carrera=?, semestre=?, email=? WHERE id=?",
        (nombre, carrera, semestre, email, id_estudiante)
    )
    conn.commit()
    conn.close()
    print(f"Estudiante ID {id_estudiante} actualizado correctamente.")


def eliminar_estudiante(id_estudiante):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conn.commit()
    conn.close()
    print(f"Estudiante ID {id_estudiante} eliminado correctamente.")
