import sqlite3
import pandas as pd
import logging

def ejecutar_consulta(consulta, pregunta_usuario, selected_columns, conn, selected_table, few_shot_queries, descriptions_short, reasoning):
    try:
        cursor = conn.cursor()
        logging.info(f"Ejecutando la consulta SQL: {consulta}")
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        if resultados:
            resultados_df = pd.DataFrame(resultados, columns=[desc[0] for desc in cursor.description])
            respuesta_db = resultados_df.to_markdown()
            respuesta_generada = f"Consulta del usuario: {pregunta_usuario}\nConsulta generada para SQL: {consulta}\nResultados:\n{respuesta_db}"
        else:
            respuesta_generada = f"No se encontraron resultados para la consulta: {pregunta_usuario}"
        cursor.close()
        return respuesta_generada
    except Exception as e:
        logging.error(f"Error al ejecutar la consulta: {e}")
        return f"Error ejecutando la consulta: {str(e)}"