import os
import logging
import time
import sqlite3
from langchain.llms import OpenAI
from langchain.agents import AgentExecutor, tool
from langchain.schema import AIMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from tools.sqltool import ejecutar_consulta
from catálogo.catalogo import catalogo

# Cargar variables de entorno
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Configurar el modelo de lenguaje
llm = OpenAI(temperature=0.3, openai_api_key=openai_api_key)

# Definir la herramienta para obtener respuestas SQL
@tool("get_LLMSQL_response", return_direct=True)
def get_LLMSQL_response(pregunta_usuario: str) -> str:
    """Transforma una pregunta en una consulta SQL, obtiene el resultado y devuelve una respuesta en lenguaje natural."""
    logging.info('INICIA TOOL SQL')
    # Conectar a la base de datos
    conn = sqlite3.connect('modified_finanzas.db')
    try:
        # Verificar si la pregunta está en el catálogo
        for consulta_key, consulta_value in catalogo.items():
            if consulta_value["question"].lower() in pregunta_usuario.lower():
                consulta_sql = consulta_value["query"]
                selected_columns = consulta_value["selected_columns"]
                selected_table = consulta_value["selected_tables"]
                reasoning = consulta_value["reasoning"]
                resultado = ejecutar_consulta(consulta_sql, pregunta_usuario, selected_columns, conn, selected_table, None, None, reasoning)
                return resultado
        return "Lo siento, no tengo una respuesta para esa pregunta en mi catálogo."
    except Exception as e:
        logging.error(f"Error al procesar la consulta: {e}")
        return f"Error al procesar la consulta: {str(e)}"
    finally:
        conn.close()

# Definir el agente conversacional
class IAAssistant:
    def __init__(self):
        # Definir la memoria de la conversación
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        # Definir el agente ejecutor con la herramienta
        self.agent_executor = AgentExecutor.from_agent_and_tools(
            agent=llm,
            tools=[get_LLMSQL_response],
            verbose=True,
            memory=self.memory
        )

    def process_message(self, input_msg):
        """Procesa el mensaje de entrada y devuelve la respuesta del agente."""
        try:
            response = self.agent_executor.run(input_msg)
            return response
        except Exception as e:
            logging.error(f"Error al procesar el mensaje: {e}")
            return "Lo siento, hubo un error al procesar tu solicitud."