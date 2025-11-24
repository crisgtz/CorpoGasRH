import matplotlib.pyplot as plt 
from datetime import datetime
import os


# LEE ARCHIVO DE ENTRADAS — SOLO REGISTROS VÁLIDOS (V)
def leer_registros(archivo="entradas.txt"):
    if not os.path.exists(archivo):
        print("No existe el archivo de entradas.")
        return []

    registros = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                partes = linea.strip().split(" - ")
                empleado = partes[1]

                # Fecha y hora (antes del símbolo "|")
                fecha_hora_str = partes[3].split("|")[0].strip()
                fecha = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")

                # ESTADO FINAL (V o F)
                estado_final = linea.strip().split("|")[-1].strip()

                #  FILTRO: SOLO REGISTROS VERDADEROS
                if estado_final != "V":
                    continue

                # Estado descriptivo ("A tiempo", "Retardo", etc.)
                estado = partes[4].replace("Estado:", "").split("|")[0].strip()

                registros.append({
                    "empleado": empleado,
                    "fecha": fecha,
                    "mes": fecha.strftime("%Y-%m"),
                    "estado": estado  
                })

            except Exception as e:
                print("Error procesando línea:", linea, e)

    return registros



# GRÁFICA INDIVIDUAL
def generar_grafica_por_empleado(registros, empleado):
    datos = [r for r in registros if r["empleado"] == empleado]

    if not datos:
        print(f"No hay registros válidos (V) para {empleado}")
        return

    meses = {}
    for r in datos:
        mes = r["mes"]
        if mes not in meses:
            meses[mes] = {"A tiempo": 0, "Retardo": 0, "Falta": 0}

        if "Retardo" in r["estado"]:
            meses[mes]["Retardo"] += 1
        elif "A tiempo" in r["estado"]:
            meses[mes]["A tiempo"] += 1
        elif "Falta" in r["estado"]:
            meses[mes]["Falta"] += 1

    etiquetas = list(meses.keys())
    a_tiempo = [meses[m]["A tiempo"] for m in etiquetas]
    retardos = [meses[m]["Retardo"] for m in etiquetas]
    faltas = [meses[m]["Falta"] for m in etiquetas]

    plt.figure(figsize=(10, 6))

    x = range(len(etiquetas))
    plt.bar(x, a_tiempo, label="A tiempo")
    plt.bar(x, retardos, bottom=a_tiempo, label="Retardos")
    bottom_sum = [a_tiempo[i] + retardos[i] for i in range(len(a_tiempo))]
    plt.bar(x, faltas, bottom=bottom_sum, label="Faltas")

    plt.xticks(x, etiquetas)
    plt.ylabel("Cantidad")
    plt.title(f"Asistencia mensual de {empleado} (solo registros V)")
    plt.legend()
    plt.tight_layout()
    plt.show()



# GRÁFICA GRUPAL
def generar_grafica_grupal(registros):
    if not registros:
        print("No hay registros verdaderos (V) para graficar.")
        return

    empleados = {}
    for r in registros:
        emp = r["empleado"]
        if emp not in empleados:
            empleados[emp] = {"A tiempo": 0, "Retardo": 0, "Falta": 0}

        if "Retardo" in r["estado"]:
            empleados[emp]["Retardo"] += 1
        elif "A tiempo" in r["estado"]:
            empleados[emp]["A tiempo"] += 1
        elif "Falta" in r["estado"]:
            empleados[emp]["Falta"] += 1

    nombres = list(empleados.keys())
    a_tiempo = [empleados[e]["A tiempo"] for e in nombres]
    retardos = [empleados[e]["Retardo"] for e in nombres]
    faltas = [empleados[e]["Falta"] for e in nombres]

    plt.figure(figsize=(12, 6))

    x = range(len(nombres))
    plt.bar(x, a_tiempo, label="A tiempo")
    plt.bar(x, retardos, bottom=a_tiempo, label="Retardos")
    bottom_sum = [a_tiempo[i] + retardos[i] for i in range(len(a_tiempo))]
    plt.bar(x, faltas, bottom=bottom_sum, label="Faltas")

    plt.xticks(x, nombres, rotation=45)
    plt.ylabel("Cantidad")
    plt.title("Comparación de asistencia (solo registros V)")
    plt.legend()
    plt.tight_layout()
    plt.show()



# MENÚ PRINCIPAL DE GRÁFICAS
def menu_graficas():
    registros = leer_registros()

    while True:
        print("\n--- MENÚ DE GRÁFICAS ---")
        print("1. Ver gráfica individual por empleado (solo V)")
        print("2. Ver gráfica grupal (solo V)")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            empleado = input("Nombre del empleado: ").strip()
            generar_grafica_por_empleado(registros, empleado)

        elif opcion == "2":
            generar_grafica_grupal(registros)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

# Ejecutar si se usa directamente
if __name__ == "__main__":
    menu_graficas()