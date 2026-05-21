# SESIÓN 3 – Construcción e Integración del Sistema

## Herramienta utilizada: GitHub Actions

GitHub Actions es la plataforma de CI/CD integrada en GitHub. Permite automatizar flujos de 
trabajo (workflows) mediante archivos YAML que se ejecutan en respuesta a eventos del repositorio 
(push, pull request, etc.).

---

## Diagrama del Flujo de Integración Continua

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLUJO DE INTEGRACIÓN CONTINUA                │
└─────────────────────────────────────────────────────────────────┘

  Developer                GitHub                 GitHub Actions
     │                       │                         │
     │── git push ──────────>│                         │
     │                       │── trigger workflow ────>│
     │                       │                         │
     │                       │              ┌──────────┴──────────┐
     │                       │              │  JOB: build-and-test │
     │                       │              │                      │
     │                       │              │ [1] Checkout repo    │
     │                       │              │        ↓             │
     │                       │              │ [2] Setup Python 3.11│
     │                       │              │        ↓             │
     │                       │              │ [3] pip install      │
     │                       │              │        ↓             │
     │                       │              │ [4] Lint / sintaxis  │
     │                       │              │        ↓             │
     │                       │              │ [5] pytest tests     │
     │                       │              │        ↓             │
     │                       │              │ [6] Generar reporte  │
     │                       │              │        ↓             │
     │                       │              │ [7] Upload artifact  │
     │                       │              └──────────┬──────────┘
     │                       │                         │
     │                       │<── resultado (✓/✗) ─────│
     │<── notificación ──────│                         │
     │                       │                         │
```

---

## Explicación de cada paso del Pipeline

| Paso | Nombre | Descripción |
|------|--------|-------------|
| 1 | Clonar repositorio | Descarga el código del repositorio al runner de GitHub Actions usando `actions/checkout@v4` |
| 2 | Configurar Python | Instala Python 3.11 en el entorno de ejecución usando `actions/setup-python@v5` |
| 3 | Instalar dependencias | Ejecuta `pip install -r requirements.txt` para instalar pytest y demás librerías |
| 4 | Verificar sintaxis | Compila cada módulo Python con `py_compile` para detectar errores de sintaxis sin ejecutar |
| 5 | Ejecutar pruebas | Corre `pytest` contra `test_models.py` con salida detallada (`-v`) y reporte corto de fallos |
| 6 | Generar reporte XML | Exporta los resultados en formato JUnit XML para integración con herramientas de reporte |
| 7 | Publicar artefacto | Sube el reporte XML como artefacto descargable desde la interfaz de GitHub Actions |

---

## Triggers del Pipeline

```yaml
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
```

El pipeline se activa automáticamente cuando:
- Se hace **push** a `main` o `develop`
- Se abre o actualiza un **Pull Request** hacia `main` o `develop`

---

## Resultado esperado en GitHub Actions

```
✓ 1. Clonar repositorio          (2s)
✓ 2. Configurar Python 3.11      (8s)
✓ 3. Instalar dependencias       (5s)
✓ 4. Verificar sintaxis          (1s)
✓ 5. Ejecutar pruebas            (3s)
  - test_crear_estudiante        PASSED
  - test_listar_estudiantes_vacio PASSED
  - test_buscar_estudiante_existente PASSED
  - test_buscar_estudiante_inexistente PASSED
  - test_actualizar_estudiante   PASSED
  - test_eliminar_estudiante     PASSED
  6 passed in 0.42s
✓ 6. Generar reporte             (1s)
✓ 7. Publicar artefacto          (2s)

Total: 22s  |  Estado: SUCCESS ✓
```
