import streamlit as st
import sqlite3
import pandas as pd
from dotenv import load_dotenv
import os
import requests
import json
import logging
import base64
from catálogo.catalogo import catalogo
from tools.sqltool import ejecutar_consulta

# Configuración de la página debe ir primero
st.set_page_config(page_title="Asistente de consultas SQL", page_icon="🤖", layout="wide")

# Cargar las variables del entorno
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai_chat_deployment_name = os.getenv('OPENAI_CHAT_DEPLOYMENT_NAME')
openai_api_version = os.getenv('OPENAI_API_VERSION')
openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

# Conexión a la base de datos
def crear_conexion(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info("Conexión a la base de datos establecida.")
    except sqlite3.Error as e:
        logging.error(f"Error al conectar con la base de datos: {e}")
    return conn

conn = crear_conexion('modified_finanzas.db')

# Función para generar respuesta con Azure OpenAI
def generar_respuesta_natural_azure(resultado_sql, user_query):
    prompt = f"El usuario preguntó: \"{user_query}\". Aquí está el resultado de la consulta SQL: {resultado_sql}. Por favor, genera una respuesta clara, concisa y en lenguaje natural, utilizando terminología relevante del sector automotriz de Volkswagen. Resume los resultados de manera profesional, destacando los puntos más importantes que puedan ser de interés para el usuario. Si los datos no están disponibles o se produjo un error en la consulta, ofrece una explicación cortés y guía al usuario con recomendaciones o próximos pasos. No incluyas la consulta SQL en la respuesta; únicamente muestra el resultado en negrita. Agrega el contexto adicional en un párrafo separado al final de la respuesta. No incluyas contexto negativo a tu respuesta, como por ejemplo: 'Lamentablemente, los resultados proporcionados solo incluyen la información de diciembre, y no disponemos de los datos de facturación para los otros meses del año. Esto podría deberse a un error en la base de datos o a una limitación en la consulta realizada.'"

    headers = {
        'Content-Type': 'application/json',
        'api-key': openai_api_key
    }

    body = {
        "messages": [
            {"role": "system", "content": "Eres un asistente experto en el sector automotriz de Volkswagen que transforma resultados de consultas SQL en respuestas en lenguaje natural. Proporciona explicaciones claras y resumidas, utilizando terminología específica del sector, y ofrece ayuda adicional si es necesario."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150
    }

    response = requests.post(openai_endpoint, headers=headers, json=body)

    if response.status_code == 200:
        response_json = response.json()
        return response_json['choices'][0]['message']['content'].strip()
    else:
        return f"Error al conectar con la API de Azure OpenAI: {response.status_code} - {response.text}"

# Función para obtener la respuesta del agente SQL
def get_response(user_query, chat_history, conn):
    for consulta_key, consulta_value in catalogo.items():
        if consulta_value["question"].lower() in user_query.lower():
            consulta_sql = consulta_value["query"]
            selected_columns = consulta_value["selected_columns"]
            selected_table = consulta_value["selected_tables"]
            reasoning = consulta_value["reasoning"]
            resultado_sql = ejecutar_consulta(consulta_sql, user_query, selected_columns, conn, selected_table, None, None, reasoning)
            
            # Generar una respuesta en lenguaje natural usando Azure OpenAI API
            respuesta_natural = generar_respuesta_natural_azure(resultado_sql, user_query)
            return respuesta_natural
    
    return "Lo siento, no tengo una respuesta para esa pregunta en mi catálogo."

# Función para convertir imagen a base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Inicializar la variable de página en st.session_state si no existe
if 'page' not in st.session_state:
    st.session_state.page = 'landing'  # Establecer página por defecto

# Obtener la imagen en formato base64
img_base64 = get_base64_image("background.png")

if st.session_state.page == 'landing':
    st.markdown(f"""
        <style>
        .landing-page {{
            background-image: url('data:image/png;base64,{img_base64}');
            background-size: cover;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
        }}
        .landing-page h1 {{
            font-size: 4em;
            margin-bottom: 0.5em;
            color: #FFFFFF; /* Color blanco para mejor contraste */
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7); /* Sombra para mayor legibilidad */
        }}
        .landing-page p {{
            font-size: 1.5em;
            margin-bottom: 2em;
            color: #1A237E; /* Color azul oscuro para el subtítulo */
            text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5); /* Sombra para mejorar legibilidad */
        }}
        .landing-page .button-container {{
            display: flex;
            justify-content: center;
            margin-top: 2em;
        }}
        .landing-page button {{
            background-color: #007BFF;
            border: none;
            color: white;
            padding: 15px 30px;
            font-size: 1.5em;
            border-radius: 10px;
            cursor: pointer;
        }}
        .landing-page button:hover {{
            background-color: #0056b3;
        }}
        </style>

        <div class="landing-page">
            <h1>Simplifica tus consultas SQL con IA Generativa</h1>
            <p>Haz clic en '<strong>Iniciar</strong>' y accede a respuestas instantáneas para tus consultas SQL</p>
            <div class="button-container">
                <button>Iniciar</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    
    if st.button("Iniciar", key="start_button"):
        st.session_state.page = 'chat'  # Cambiar de página al chatbot

# Página del chatbot
elif st.session_state.page == 'chat':
    st.title("SQL Agent")
    st.write("Conversaciones con tu base de datos al alcance de la mano")

    # Historial de la sesión
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "¡Hola! Estoy aquí para ayudarte a consultar tu base de datos de forma rápida y sencilla. ¿Qué consulta te gustaría hacer hoy?"}
        ]

    # Interfaz de chat
    st.subheader("💬 Habla con tu Asistente SQL")
    chat_container = st.container()

    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "assistant":
                st.info(message["content"])
            elif message["role"] == "user":
                st.success(message["content"])

    # Formulario para ingresar la consulta
    with st.form("chat_form"):
        user_query = st.text_input("💡 Ingresa tu consulta aquí...", key="user_input")
        submit_button = st.form_submit_button("Enviar")

    if submit_button and user_query:
        # Guardar la consulta del usuario en el historial (solo la última)
        st.session_state.chat_history = [{"role": "user", "content": user_query}]
        
        # Obtener la respuesta del agente SQL
        response = get_response(user_query, st.session_state.chat_history, conn)
        
        # Guardar la respuesta del agente en el historial (solo la última)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Mostrar solo la última consulta y respuesta
        st.success(st.session_state.chat_history[0]["content"])  # Mostrar la consulta del usuario
        st.info(st.session_state.chat_history[1]["content"])  # Mostrar la respuesta del asistente

