# Changelog – Sistema de Gestión de Estudiantes

Todos los cambios notables de este proyecto están documentados en este archivo.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).
Versionado basado en [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.0.0] – 2026-05-20

### Agregado
- Sistema CRUD completo para gestión de estudiantes.
- Módulo `database.py`: conexión y creación de base de datos SQLite.
- Módulo `models.py`: operaciones crear, listar, buscar, actualizar y eliminar estudiantes.
- Módulo `main.py`: interfaz de menú en consola para interacción del usuario.
- Pruebas automatizadas con pytest (`test_models.py`) con 6 casos de prueba.
- Pipeline de integración continua con GitHub Actions (`.github/workflows/ci.yml`).
- Documentación de comandos Git y políticas de commits.
- Diagrama del flujo de CI.

### Detalles técnicos
- **Lenguaje:** Python 3.11
- **Base de datos:** SQLite (sin dependencias externas)
- **Framework de pruebas:** pytest 8.3.5
- **CI/CD:** GitHub Actions

---

## [0.2.0] – 2026-05-19

### Agregado
- Funcionalidad de actualizar y eliminar estudiantes.
- Pruebas para actualización y eliminación.
- Rama `feature/update-delete` fusionada a `develop`.

### Corregido
- Validación de ID inexistente al buscar estudiante devuelve `None` en lugar de lanzar excepción.

---

## [0.1.0] – 2026-05-18

### Agregado
- Inicialización del repositorio.
- Funcionalidades básicas: crear y listar estudiantes.
- Configuración de base de datos SQLite.
- Primer pipeline de CI (solo verificación de sintaxis).

---

## Próximas versiones planificadas

### [1.1.0] – Pendiente
- [ ] Exportar listado de estudiantes a CSV.
- [ ] Búsqueda por nombre o carrera.
- [ ] Validación de formato de email con expresiones regulares.

### [2.0.0] – Planificado
- [ ] Interfaz gráfica con Tkinter.
- [ ] Autenticación de usuarios (administrador / consulta).
- [ ] API REST con Flask.
