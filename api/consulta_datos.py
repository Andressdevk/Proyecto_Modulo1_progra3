import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite_registros):
    client = Socrata("www.datos.gov.co", None)
    resultados = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=departamento)
    return resultados

def seleccionar_columnas(resultados):
    columnas = ["ciudad_municipio_nom", "departamento_nom", "edad",
                "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"]
    resultados_df = pd.DataFrame.from_records(resultados)
    return resultados_df.reindex(columns=columnas)