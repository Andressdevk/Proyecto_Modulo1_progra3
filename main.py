from api.consulta_datos import obtener_datos, seleccionar_columnas
from ui.interactuar_usuario import saludo, entrada, mostrar_resultados

saludo()
departamento, num_casos = entrada()
resultados = obtener_datos(departamento, num_casos)
tabla = seleccionar_columnas(resultados)
mostrar_resultados(tabla)