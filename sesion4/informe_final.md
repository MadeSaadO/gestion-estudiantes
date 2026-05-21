# Informe Final – Práctica 1
## Introducción a la Gestión de la Configuración del Software

**Asignatura:** Gestión de la Configuración de Software  
**Carrera:** Software – Facultad de Ciencias e Ingenierías  
**Universidad:** Universidad Estatal de Milagro (UNEMI)  
**Fecha:** 2026-05-20  

---

## 1. Resumen Ejecutivo

Esta práctica implementó un flujo completo de Gestión de la Configuración del Software 
sobre un sistema CRUD de gestión de estudiantes desarrollado en Python. A través de 4 
sesiones de trabajo, se aplicaron conceptos de administración del cambio, gestión de 
versiones con Git/GitHub, integración continua con GitHub Actions y entrega simulada 
del producto con GitHub Releases.

---

## 2. Análisis del Control de Cambios y Versiones

### 2.1 Herramienta utilizada
**Git** como sistema de control de versiones distribuido, con **GitHub** como repositorio remoto.

### 2.2 Estrategia de ramas (Branching)

```
main
 └── develop
      ├── feature/busqueda-avanzada
      ├── fix/validacion-email
      └── release/v1.0.0
```

### 2.3 Política de commits aplicada
Se utilizó la convención **Conventional Commits** con tipos: `feat`, `fix`, `docs`, `test`, `ci`.

### 2.4 Historial de cambios relevantes

| Versión | Cambio | Tipo | Rama |
|---------|--------|------|------|
| 0.1.0 | Creación del CRUD base | feat | main |
| 0.2.0 | Actualizar y eliminar estudiantes | feat | feature/update-delete |
| 0.2.0 | Corregir búsqueda de ID inexistente | fix | fix/busqueda-id |
| 1.0.0 | Pipeline CI completo con GitHub Actions | ci | develop → main |
| 1.0.0 | Pruebas automatizadas con pytest | test | develop → main |

---

## 3. Evidencia de CI/CD

### 3.1 Pipeline implementado
Archivo: `.github/workflows/ci.yml`  
Plataforma: **GitHub Actions**

### 3.2 Pasos del pipeline

1. Clonar repositorio (`actions/checkout@v4`)
2. Configurar Python 3.11 (`actions/setup-python@v5`)
3. Instalar dependencias (`pip install -r requirements.txt`)
4. Verificar sintaxis (`python -m py_compile`)
5. Ejecutar pruebas (`pytest -v`)
6. Generar reporte XML (`--junit-xml`)
7. Subir artefacto (`actions/upload-artifact@v4`)

### 3.3 Resultado del pipeline
- **Estado:** SUCCESS
- **Pruebas:** 6/6 PASSED
- **Tiempo total:** ~22 segundos
- **Triggers:** push y pull_request a `main` y `develop`

---

## 4. Evidencia de Entregables

### 4.1 Release v1.0.0
- **Tag:** `v1.0.0`
- **Artefacto:** `gestion-estudiantes-v1.0.0.zip`
- **Reporte:** `reporte_pruebas.xml`
- **Changelog:** `CHANGELOG.md`
- **Plataforma:** GitHub Releases

### 4.2 Estructura final del repositorio

```
practica/
├── sesion1/
│   ├── crud_app/
│   │   ├── database.py       # Conexión SQLite
│   │   ├── models.py         # Lógica CRUD
│   │   ├── main.py           # Interfaz de consola
│   │   ├── test_models.py    # Pruebas pytest
│   │   └── requirements.txt  # Dependencias
│   └── hallazgos.md          # Tabla de análisis conceptual
├── sesion2/
│   ├── git_commands.md       # Comandos Git documentados
│   └── politicas_commits.md  # Convención de commits
├── sesion3/
│   ├── .github/workflows/
│   │   └── ci.yml            # Pipeline GitHub Actions
│   └── diagrama_ci.md        # Diagrama del flujo CI
└── sesion4/
    ├── CHANGELOG.md          # Historial de versiones
    ├── release_notes.md      # Notas del release v1.0.0
    └── informe_final.md      # Este documento
```

---

## 5. Lecciones Aprendidas

### 5.1 Colaboración en equipos de desarrollo
- El uso de **ramas por funcionalidad** evita conflictos entre los miembros del equipo.
- Los **Pull Requests** promueven la revisión de código y mejoran la calidad del producto.
- Una **política de commits** clara facilita entender el historial sin leer el código.

### 5.2 Integración continua
- Automatizar las pruebas elimina el error humano de olvidar ejecutarlas antes de un merge.
- GitHub Actions permite detectar errores de sintaxis y fallos de pruebas en segundos.
- Los reportes en formato JUnit XML son compatibles con herramientas de análisis externas.

### 5.3 Gestión de entregas
- El **versionado semántico** (MAJOR.MINOR.PATCH) comunica claramente el impacto de cada cambio.
- El **CHANGELOG** es fundamental para que los usuarios y el equipo comprendan qué cambió y por qué.
- GitHub Releases centraliza los artefactos entregables y los vincula directamente al código fuente.

---

## 6. Conclusiones

La práctica demostró que la Gestión de la Configuración del Software no es opcional en 
proyectos reales: es la diferencia entre un desarrollo caótico y uno controlado. 
Herramientas como Git, GitHub Actions y las convenciones de commits son accesibles, 
gratuitas y ampliamente adoptadas en la industria. Su aplicación desde etapas tempranas 
del desarrollo reduce significativamente los costos de mantenimiento y mejora la 
colaboración del equipo.

---

## 7. Referencias Bibliográficas

1. Pressman, R. S. (2010). *Ingeniería del Software: Un enfoque práctico* (7.ª ed.). McGraw-Hill.
2. Sommerville, I. (2011). *Ingeniería de Software* (9.ª ed.). Pearson Educación.
