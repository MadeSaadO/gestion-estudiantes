# Release Notes – v1.0.0

**Nombre del release:** `v1.0.0`  
**Fecha:** 2026-05-20  
**Repositorio:** https://github.com/TU_USUARIO/gestion-estudiantes  
**Tag Git:** `v1.0.0`  

---

## Descripción

Primera versión estable del **Sistema de Gestión de Estudiantes**, una aplicación CRUD 
de consola desarrollada en Python con almacenamiento en SQLite. Esta versión incluye 
todas las operaciones básicas sobre registros de estudiantes y un pipeline de integración 
continua completamente funcional.

---

## Contenido del Release

| Archivo | Descripción |
|---------|-------------|
| `gestion-estudiantes-v1.0.0.zip` | Código fuente empaquetado |
| `reporte_pruebas.xml` | Reporte JUnit de las pruebas automatizadas |
| `CHANGELOG.md` | Historial completo de cambios |

---

## Cómo usar esta versión

### Requisitos
- Python 3.10 o superior
- pip (incluido con Python)

### Instalación

```bash
# 1. Descomprimir el archivo
unzip gestion-estudiantes-v1.0.0.zip
cd gestion-estudiantes-v1.0.0

# 2. Instalar dependencias
pip install -r sesion1/crud_app/requirements.txt

# 3. Ejecutar la aplicación
cd sesion1/crud_app
python main.py

# 4. (Opcional) Ejecutar las pruebas
pytest test_models.py -v
```

---

## Cómo crear el release en GitHub

```bash
# 1. Asegurarse de estar en main con todo commiteado
git checkout main
git pull origin main

# 2. Crear el tag de versión
git tag -a v1.0.0 -m "Release v1.0.0 - Sistema CRUD de Estudiantes completo"

# 3. Subir el tag a GitHub
git push origin v1.0.0

# 4. Comprimir el código fuente
Compress-Archive -Path .\sesion1\crud_app\* -DestinationPath gestion-estudiantes-v1.0.0.zip

# 5. Crear el release con GitHub CLI
gh release create v1.0.0 \
  --title "v1.0.0 - Sistema CRUD Estudiantes" \
  --notes-file sesion4/release_notes.md \
  gestion-estudiantes-v1.0.0.zip \
  sesion3/reporte_pruebas.xml
```

---

## Estado de pruebas

| Test | Estado |
|------|--------|
| test_crear_estudiante | PASSED |
| test_listar_estudiantes_vacio | PASSED |
| test_buscar_estudiante_existente | PASSED |
| test_buscar_estudiante_inexistente | PASSED |
| test_actualizar_estudiante | PASSED |
| test_eliminar_estudiante | PASSED |
| **Total** | **6/6 PASSED** |
