# SESIÓN 1 – Diagnóstico y Conceptualización
## Proyecto: Sistema de Gestión de Estudiantes (CRUD)

---

## Descripción del Proyecto

Sistema CRUD desarrollado en Python con SQLite que permite gestionar registros de estudiantes 
(crear, listar, buscar, actualizar y eliminar). Sirve como base para aplicar prácticas de 
Gestión de la Configuración del Software a lo largo de las 4 sesiones.

**Tecnologías usadas:**
- Lenguaje: Python 3.x
- Base de datos: SQLite (sqlite3 integrado)
- Pruebas: pytest

---

## Actividad 2 – Tabla de Hallazgos

| Área | Hallazgo | Concepto Teórico Asociado |
|------|----------|--------------------------|
| Administración del cambio | El proyecto no contaba con ningún proceso formal para registrar cambios. Cada modificación se realizaba directamente sobre el código sin registro. | La **administración del cambio** implica identificar factores de cambio (nuevos requerimientos, corrección de errores), evaluar su costo-beneficio y aplicar un procedimiento controlado antes de implementar cualquier modificación (Sommerville, 2011). |
| Gestión de versiones | No existía historial de versiones ni etiquetas de release. Los archivos se copiaban con nombres como "proyecto_final_v2". | La **gestión de versiones** permite mantener múltiples variantes de un sistema, registrar el historial de cambios y recuperar versiones anteriores mediante herramientas como Git (Pressman, 2010). |
| Construcción del sistema | La ejecución del sistema se realizaba manualmente desde la línea de comandos sin automatización ni validación previa. | La **construcción del sistema** incluye el uso de herramientas que automatizan la compilación, ejecución de pruebas y generación de artefactos. La integración continua (CI) garantiza que cada cambio sea validado automáticamente (Sommerville, 2011). |
| Gestión de entregas | No existía ningún proceso de empaquetado ni versionado semántico de entregas. | La **gestión de entregas** define cómo se distribuye el software a los usuarios finales, incluyendo la numeración de versiones, el changelog y el repositorio de artefactos (Pressman, 2010). |

---

## Conceptos Teóricos

### 1. Administración del Cambio
- **Factores para el cambio:** errores detectados, nuevos requerimientos del cliente, cambios tecnológicos o de entorno.
- **Beneficios:** mayor calidad, trazabilidad y control sobre las modificaciones.
- **Costos:** tiempo de análisis, pruebas de regresión y documentación adicional.

### 2. Gestión de Versiones
- **Características:** identificación única de versiones, ramas de desarrollo paralelas, fusión de cambios.
- **Gestión de almacenamiento:** repositorios centralizados (GitHub) o distribuidos.
- **Historial de cambios:** registro cronológico de quién cambió qué y por qué.

### 3. Construcción del Sistema
- **Plataformas:** GitHub Actions, Jenkins, GitLab CI/CD.
- **Características:** automatización del build, ejecución de tests, generación de reportes.
- **Pasos de integración continua:** push → trigger → build → test → reporte.

### 4. Gestión de Entregas
- **Factores técnicos:** compatibilidad, dependencias, plataforma destino.
- **Factores organizacionales:** plazos, acuerdos de servicio, equipos de QA.
- **Repositorio de artefactos:** GitHub Releases, donde se almacenan los paquetes entregables.

---

## Referencias
- Pressman, R. (2010). *Ingeniería del Software*. McGraw-Hill.
- Sommerville, I. (2011). *Ingeniería de Software*. Pearson.
