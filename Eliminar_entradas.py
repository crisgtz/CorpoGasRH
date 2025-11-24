def eliminar_entrada(id_registro):
    """Elimina una entrada del archivo 'entradas.txt' usando el número de registro (ID)."""
    try:
        with open("entradas.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        # Filtrar las líneas que no comienzan con el ID especificado
        nuevo_contenido = [l for l in lineas if not l.strip().startswith(f"{id_registro} ")]

        # Si no se eliminó ninguna línea, el ID no existe
        if len(lineas) == len(nuevo_contenido):
            print(f"No se encontró ninguna entrada con el ID {id_registro}.")
            return

        # Reescribir el archivo sin la entrada eliminada
        with open("entradas.txt", "w", encoding="utf-8") as f:
            f.writelines(nuevo_contenido)

        print(f"Entrada con ID {id_registro} eliminada correctamente.")

    except FileNotFoundError:
        print("No hay entradas guardadas aún.")


if __name__ == "__main__":
    try:
        id_registro = int(input("Ingrese el número (ID) del registro a eliminar: ").strip())
        eliminar_entrada(id_registro)
    except ValueError:
        print("Debes ingresar un número válido para el ID.")