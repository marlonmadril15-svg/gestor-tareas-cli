# Gestor de Tareas CLI
# Autor: Marlon Madril

tareas = []


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()

