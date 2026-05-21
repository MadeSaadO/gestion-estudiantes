# SESIÓN 2 – Gestión de Versiones y Control de Cambios

## Actividad 1 – Configuración del Repositorio en GitHub

### Paso 1: Inicializar el repositorio local

```bash
# Inicializar git en la carpeta del proyecto
git init

# Verificar el estado del repositorio
git status
```
**Explicación:** `git init` crea un repositorio Git vacío en el directorio actual. Genera la carpeta `.git` que almacena todo el historial de versiones.

---

### Paso 2: Primer commit (commit inicial)

```bash
# Agregar todos los archivos al área de staging
git add .

# Crear el primer commit
git commit -m "feat: commit inicial - sistema CRUD de estudiantes"

# Verificar el historial
git log --oneline
```
**Explicación:** `git add .` mueve todos los archivos al área de preparación. `git commit` guarda una instantánea permanente del estado actual del proyecto.

---

### Paso 3: Conectar con GitHub

```bash
# Agregar el repositorio remoto en GitHub
git remote add origin https://github.com/TU_USUARIO/gestion-estudiantes.git

# Subir la rama principal
git push -u origin main
```
**Explicación:** `git remote add origin` vincula el repositorio local con el remoto en GitHub. `-u` establece el tracking para futuros `push` y `pull`.

---

### Paso 4: Crear ramas por funcionalidad

```bash
# Crear y cambiar a rama para nueva funcionalidad
git checkout -b feature/busqueda-avanzada

# Crear rama para corrección de errores
git checkout -b fix/validacion-email

# Crear rama de desarrollo
git checkout -b develop

# Listar todas las ramas
git branch -a
```
**Explicación:** Las ramas permiten trabajar en funcionalidades o correcciones de forma aislada sin afectar la rama principal (`main`).

---

### Paso 5: Realizar cambios y commits en la rama

```bash
# (Hacer cambios en los archivos del proyecto)

# Ver qué archivos cambiaron
git diff

# Agregar archivos modificados
git add models.py

# Commit con mensaje descriptivo
git commit -m "fix: agregar validacion de formato de email"

# Subir la rama al repositorio remoto
git push origin fix/validacion-email
```

---

### Paso 6: Pull Request y merge

```bash
# (El Pull Request se crea desde la interfaz de GitHub)

# Después de aprobar el PR, traer los cambios a main
git checkout main
git pull origin main

# Eliminar la rama ya fusionada
git branch -d fix/validacion-email
git push origin --delete fix/validacion-email
```
**Explicación:** El Pull Request es el mecanismo de revisión de código. Permite que otros miembros del equipo revisen los cambios antes de fusionarlos a `main`.

---

### Paso 7: Simular corrección de error

```bash
# Cambiar a la rama de fix
git checkout -b fix/error-eliminacion

# (Corregir el error en models.py)

git add models.py
git commit -m "fix: corregir eliminacion de estudiante con ID inexistente"
git push origin fix/error-eliminacion
```

---

### Paso 8: Ver historial completo

```bash
# Historial detallado con ramas
git log --oneline --graph --all

# Ver detalles de un commit específico
git show <hash_del_commit>

# Ver quién modificó cada línea
git blame models.py
```

---

## Resumen de Comandos Utilizados

| Comando | Descripción |
|---------|-------------|
| `git init` | Inicializa un repositorio Git local |
| `git status` | Muestra el estado de los archivos (modificados, staged, sin seguimiento) |
| `git add .` | Agrega todos los cambios al área de staging |
| `git commit -m "msg"` | Guarda los cambios con un mensaje descriptivo |
| `git push origin rama` | Sube los cambios al repositorio remoto |
| `git pull origin rama` | Descarga e integra cambios del remoto |
| `git checkout -b rama` | Crea y cambia a una nueva rama |
| `git merge rama` | Fusiona una rama en la rama actual |
| `git branch -d rama` | Elimina una rama local |
| `git log --oneline --graph` | Muestra historial visual de commits |
| `git diff` | Muestra diferencias entre archivos modificados |
| `git blame archivo` | Muestra quién editó cada línea de un archivo |
| `git show <hash>` | Muestra detalles de un commit específico |
| `git remote add origin URL` | Conecta el repo local con GitHub |
| `git tag v1.0.0` | Crea una etiqueta de versión |
