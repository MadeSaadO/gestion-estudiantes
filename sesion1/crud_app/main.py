from database import inicializar_db
from models import (
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante,
)


def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
    print("1. Agregar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")
    print("=============================================")


def main():
    inicializar_db()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
            semestre = int(input("Semestre: "))
            email = input("Email: ")
            crear_estudiante(nombre, carrera, semestre, email)

        elif opcion == "2":
            estudiantes = listar_estudiantes()
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print(f"\n{'ID':<5} {'Nombre':<25} {'Carrera':<20} {'Sem':<5} {'Email'}")
                print("-" * 75)
                for e in estudiantes:
                    print(f"{e[0]:<5} {e[1]:<25} {e[2]:<20} {e[3]:<5} {e[4]}")

        elif opcion == "3":
            id_est = int(input("ID del estudiante: "))
            est = buscar_estudiante(id_est)
            if est:
                print(f"\nID: {est[0]} | Nombre: {est[1]} | Carrera: {est[2]} | Semestre: {est[3]} | Email: {est[4]}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            id_est = int(input("ID del estudiante a actualizar: "))
            nombre = input("Nuevo nombre: ")
            carrera = input("Nueva carrera: ")
            semestre = int(input("Nuevo semestre: "))
            email = input("Nuevo email: ")
            actualizar_estudiante(id_est, nombre, carrera, semestre, email)

        elif opcion == "5":
            id_est = int(input("ID del estudiante a eliminar: "))
            eliminar_estudiante(id_est)

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
