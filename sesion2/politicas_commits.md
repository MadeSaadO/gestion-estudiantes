# Políticas de Commits – Proyecto CRUD Estudiantes

## Convención: Conventional Commits

Todos los mensajes de commit siguen la especificación **Conventional Commits**:

```
<tipo>(<alcance opcional>): <descripción corta>

[cuerpo opcional]

[pie opcional]
```

---

## Tipos de Commit Permitidos

| Tipo | Uso | Ejemplo |
|------|-----|---------|
| `feat` | Nueva funcionalidad | `feat: agregar búsqueda por carrera` |
| `fix` | Corrección de error | `fix: corregir validación de email duplicado` |
| `docs` | Solo documentación | `docs: actualizar README con instrucciones` |
| `test` | Agregar o corregir pruebas | `test: agregar tests para eliminación` |
| `refactor` | Reestructuración sin cambio funcional | `refactor: extraer lógica de conexión a módulo` |
| `chore` | Tareas de mantenimiento | `chore: actualizar dependencias` |
| `ci` | Cambios en CI/CD | `ci: agregar workflow de GitHub Actions` |

---

## Política de Ramas

| Rama | Propósito |
|------|-----------|
| `main` | Código estable listo para producción. Solo se modifica por PR. |
| `develop` | Integración de funcionalidades en desarrollo. |
| `feature/<nombre>` | Nueva funcionalidad específica. Ej: `feature/busqueda-avanzada` |
| `fix/<nombre>` | Corrección de errores. Ej: `fix/validacion-email` |
| `release/<version>` | Preparación de una entrega. Ej: `release/v1.0.0` |

---

## Reglas de Commits

1. El mensaje debe estar en **español o inglés**, pero ser consistente en el proyecto.
2. La descripción corta **no supera 72 caracteres**.
3. Usar **verbos en infinitivo** (agregar, corregir, actualizar).
4. Un commit = un cambio lógico (no mezclar múltiples funcionalidades).
5. **No hacer commit de archivos generados** (.db, __pycache__, .pyc).

---

## Ejemplo de Historial de Commits

```
a1b2c3d (HEAD -> main) chore: agregar .gitignore
f4e5d6c feat: implementar eliminacion de estudiantes
b7a8c9d feat: implementar actualizacion de estudiantes
1e2f3a4 feat: implementar busqueda por ID
9d8c7b6 feat: implementar listado de estudiantes
5a4b3c2 feat: implementar creacion de estudiantes
2f1e0d9 feat: commit inicial - sistema CRUD de estudiantes
```

---

## Archivo .gitignore Recomendado

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Base de datos SQLite
*.db
*.sqlite3

# Entorno virtual
venv/
env/
.env

# Editor
.vscode/
.idea/

# Pytest
.pytest_cache/
```
