import matplotlib.pyplot as plt
from datetime import datetime, time
import os


# ==========================================================
#             CALCULAR ESTADO (A tiempo / Retardo)
# ==========================================================

# Horarios esperados por turno
HORARIOS = {
    "Turno 1": time(6, 0),
    "Turno 2": time(14, 0),
    "Turno 3": time(22, 0)
}

def calcular_estado(turno, fecha):
    if turno not in HORARIOS:
        return "Desconocido"

    hora_entrada = HORARIOS[turno]
    hora_real = fecha.time()

    if hora_real <= hora_entrada:
        return "A tiempo"
    else:
        return "Retardo"


# ==========================================================
#                LECTURA CORRECTA DE REGISTROS
# ==========================================================

def leer_registros(archivo="entradas.txt"):
    if not os.path.exists(archivo):
        print("No existe el archivo de entradas.")
        return []

    registros = []

    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                partes = linea.strip().split(" - ")

                id_registro = partes[0]
                empleado = partes[1]
                turno = partes[2]              # Turno 1, Turno 2, Turno 3
                fecha_hora_str = partes[3]     # 2025-10-30 02:56:00
                visibilidad = partes[4].split(":")[1].strip()  # V o F

                if visibilidad != "V":
                    continue  # Solo graficar visibles

                fecha = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")

                # Calcular estado automáticamente
                estado = calcular_estado(turno, fecha)

                registros.append({
                    "empleado": empleado,
                    "fecha": fecha,
                    "mes": fecha.strftime("%Y-%m"),
                    "estado": estado,
                })

            except Exception as e:
                print("Error en línea:", linea, e)

    return registros



# ==========================================================
#               GRÁFICA POR EMPLEADO
# ==========================================================

def generar_grafica_por_empleado(registros, empleado):
    datos = [r for r in registros if r["empleado"] == empleado]

    if not datos:
        print(f"No hay registros (V) para {empleado}")
        return

    meses = {}
    for r in datos:
        mes = r["mes"]
        if mes not in meses:
            meses[mes] = {"A tiempo": 0, "Retardo": 0}

        meses[mes][r["estado"]] += 1

    etiquetas = list(meses.keys())
    a_tiempo = [meses[m]["A tiempo"] for m in etiquetas]
    retardos = [meses[m]["Retardo"] for m in etiquetas]

    plt.figure(figsize=(10, 6))
    x = range(len(etiquetas))

    plt.bar(x, a_tiempo, label="A tiempo")
    plt.bar(x, retardos, bottom=a_tiempo, label="Retardo")

    plt.xticks(x, etiquetas)
    plt.ylabel("Cantidad")
    plt.title(f"Asistencia mensual de {empleado} (solo V)")
    plt.legend()
    plt.show()



# ==========================================================
#               GRÁFICA GRUPAL
# ==========================================================

def generar_grafica_grupal(registros):
    if not registros:
        print("No hay registros (V) para graficar.")
        return

    empleados = {}
    for r in registros:
        emp = r["empleado"]
        if emp not in empleados:
            empleados[emp] = {"A tiempo": 0, "Retardo": 0}

        empleados[emp][r["estado"]] += 1

    nombres = list(empleados.keys())
    a_tiempo = [empleados[e]["A tiempo"] for e in nombres]
    retardos = [empleados[e]["Retardo"] for e in nombres]

    plt.figure(figsize=(12, 6))
    x = range(len(nombres))

    plt.bar(x, a_tiempo, label="A tiempo")
    plt.bar(x, retardos, bottom=a_tiempo, label="Retardo")

    plt.xticks(x, nombres, rotation=45)
    plt.ylabel("Cantidad")
    plt.title("Comparación de asistencia (solo V)")
    plt.legend()
    plt.show()



# ==========================================================
#                       MENÚ
# ==========================================================

def menu_graficas():
    registros = leer_registros()

    while True:
        print("\n--- MENÚ DE GRÁFICAS ---")
        print("1. Ver gráfica individual por empleado")
        print("2. Ver gráfica grupal")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            empleado = input("Nombre del empleado: ").strip()
            generar_grafica_por_empleado(registros, empleado)

        elif opcion == "2":
            generar_grafica_grupal(registros)

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")



if __name__ == "__main__":
    menu_graficas()