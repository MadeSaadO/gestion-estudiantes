import os
import sys
import pytest

# Usar base de datos temporal para pruebas
import database
database.DB_NAME = "test_estudiantes.db"

from database import inicializar_db
from models import (
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante,
)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    inicializar_db()
    yield
    if os.path.exists(database.DB_NAME):
        os.remove(database.DB_NAME)


def test_crear_estudiante():
    crear_estudiante("Ana Lopez", "Software", 3, "ana@test.com")
    resultados = listar_estudiantes()
    assert len(resultados) == 1
    assert resultados[0][1] == "Ana Lopez"


def test_listar_estudiantes_vacio():
    resultados = listar_estudiantes()
    assert resultados == []


def test_buscar_estudiante_existente():
    crear_estudiante("Carlos Ruiz", "Sistemas", 5, "carlos@test.com")
    estudiante = buscar_estudiante(1)
    assert estudiante is not None
    assert estudiante[1] == "Carlos Ruiz"


def test_buscar_estudiante_inexistente():
    resultado = buscar_estudiante(999)
    assert resultado is None


def test_actualizar_estudiante():
    crear_estudiante("Maria Gil", "Software", 2, "maria@test.com")
    actualizar_estudiante(1, "Maria Gil Actualizada", "Software", 4, "maria_v2@test.com")
    estudiante = buscar_estudiante(1)
    assert estudiante[1] == "Maria Gil Actualizada"
    assert estudiante[3] == 4


def test_eliminar_estudiante():
    crear_estudiante("Pedro Mora", "Civil", 6, "pedro@test.com")
    eliminar_estudiante(1)
    resultado = buscar_estudiante(1)
    assert resultado is None
