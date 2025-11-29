from datetime import datetime

def consultar_entradas():
    #Menú para mostrar registros según su estado V/F.

    while True:
        print("\n=== CONSULTAR ENTRADAS ===")
        print("1. Mostrar solo registros VERDADEROS (V)")
        print("2. Mostrar solo registros FALSOS (F)")
        print("3. Mostrar TODOS los registros")
        print("4. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_registros(filtro="V")

        elif opcion == "2":
            mostrar_registros(filtro="F")

        elif opcion == "3":
            mostrar_registros(filtro="TODOS")

        elif opcion == "4":
            break

        else:
            print("Opción no válida, intenta de nuevo.")


def mostrar_registros(filtro="TODOS"):
    #Lee el archivo y muestra registros filtrados por V/F y ordenados por fecha.

    try:
        with open("entradas.txt", "r", encoding="utf-8") as f:
            entradas = [linea.strip() for linea in f if linea.strip()]

        if not entradas:
            print("No hay entradas registradas aún.")
            return

        # Obtener fecha correcta de cada registro
        def obtener_fecha(entrada):
            try:
                partes = entrada.split(" - ")
                fecha_hora_str = partes[3].split(" V/F ")[0].strip()
                return datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
            except:
                return datetime.min

        # Ordenar por fecha
        entradas_ordenadas = sorted(entradas, key=obtener_fecha)

        print("\n=== RESULTADOS ===\n")

        for entrada in entradas_ordenadas:
            estado = entrada.split("V/F")[-1].strip()

            if filtro == "V" and estado != "V":
                continue

            if filtro == "F" and estado != "F":
                continue

            print(entrada)

    except FileNotFoundError:
        print("El archivo 'entradas.txt' no existe aún.")