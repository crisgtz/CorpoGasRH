from Registro_empleados import (
    guardar_entrada,
    cambiar_visibilidad_manual
)
from Consultar_enteradas import consultar_entradas
from Grafica import menu_graficas
from Registro_empleados import menu_configurar_horarios  # menú de turnos


def menu():
    while True:
        print("\n=== SISTEMA DE ENTRADAS DE EMPLEADOS ===")
        print("1. Registrar entrada de empleado")
        print("2. Consultar entradas")
        print("3. Ver gráficas")
        print("4. Configurar horarios de turnos")
        print("5. Cambiar visibilidad V/F de un registro")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        # 1. Registrar entrada
        if opcion == "1":
            empleado = input("Empleado: ")
            print("\nSelecciona el turno:")
            print("1. Turno 1")
            print("2. Turno 2")
            print("3. Turno 3")

            turno = input("Turno (1-3): ")
            fecha_hora = input("Fecha y hora de entrada (AAAA-MM-DD HH:MM:SS): ")

            guardar_entrada(empleado, turno, fecha_hora)

        # 2. Consultar entradas
        elif opcion == "2":
            consultar_entradas()

        # 3. Gráficas
        elif opcion == "3":
            menu_graficas()

        # 4. Configurar horarios
        elif opcion == "4":
            menu_configurar_horarios()

        # 5. Cambiar visibilidad V/F
        elif opcion == "5":
            print("\n--- CAMBIAR VISIBILIDAD DEL REGISTRO ---")
            print("1. Cambiar a V (Visible)")
            print("2. Cambiar a F (Oculto)")

            sub = input("Elige una opción: ")

            if sub not in ["1", "2"]:
                print("Opción inválida.")
                continue

            try:
                reg = int(input("ID del registro a modificar: "))
                nuevo_valor = "V" if sub == "1" else "F"
                cambiar_visibilidad_manual(reg, nuevo_valor)
            except:
                print("ID inválido.")

        # 6. Salir
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
