def saludo():
    print("SISTEMA DE CONSULTA FILTRADA POR DEPARTAMENTO DE CASOS DE CONTAGIO DE CORONAVIRUS")


def entrada():
    departamento = input("Ingrese el departamento que desea consultar: ").strip().upper()

    num_casos = input("Ingrese el número de casos (máximo recomendado 1000): ")
    while not num_casos.isdigit() or int(num_casos) <= 0 or int(num_casos) > 1000:
        num_casos = input("Dato inválido. Ingrese un número entero mayor que 0: ")

    return departamento, int(num_casos)


def mostrar_resultados(tabla):
    if tabla.empty:
        print("No se encontraron datos. Verifique el nombre del departamento.")
        return

    formato = "{:<20} {:<20} {:<6} {:<15} {:<12} {:<20}"

    print(formato.format("Ciudad", "Departamento", "Edad", "Tipo", "Estado", "País"))
    print("-" * 95)

    for i, fila in tabla.iterrows():
        print(formato.format(
            fila["ciudad_municipio_nom"],
            fila["departamento_nom"],
            fila["edad"],
            fila["fuente_tipo_contagio"],
            fila["estado"],
            fila["pais_viajo_1_nom"]
        ))