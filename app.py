# Gestor de Tareas CLI
# Autor: Marlon Madril

tareas = []


def agregar_tarea():
    titulo = input("Titulo de la tarea: ").strip()
    if not titulo:
        print("Error: el titulo de la tarea no puede estar vacio.")
        return
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas, start=1):
        estado = "[X]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['titulo']}")


def pedir_indice():
    if not tareas:
        print("No hay tareas.")
        return None
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea['titulo']}")
    try:
        indice = int(input("Numero de la tarea: ")) - 1
    except ValueError:
        print("Debe ingresar un numero.")
        return None
    if 0 <= indice < len(tareas):
        return indice
    print("Numero fuera de rango.")
    return None


def completar_tarea():
    indice = pedir_indice()
    if indice is not None:
        tareas[indice]["completada"] = True
        print("Tarea completada.")


def eliminar_tarea():
    indice = pedir_indice()
    if indice is not None:
        eliminada = tareas.pop(indice)
        print(f"Tarea eliminada: {eliminada['titulo']}")


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS - Menu principal ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el numero de una opcion: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()
