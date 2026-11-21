# Gestor de Tareas CLI
# Autor: Marlon Madril

tareas = []


def agregar_tarea():
    titulo = input("Titulo de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas, start=1):
        estado = "[X]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['titulo']}")


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()
