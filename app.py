import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuración de la API de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interfaz de Streamlit
st.title("📝 Asistente Simplificado")
st.write("¡Hazme una pregunta!")

# Entrada del usuario
user_input = st.text_input("¿En qué puedo ayudarte hoy?", "")

# Lógica del asistente
if st.button("Enviar"):
    if user_input:
        # Generar respuesta con OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cambia a "gpt-3.5-turbo" si prefieres un modelo más económico
            messages=[{"role": "system", "content": "Eres un asistente útil."},
                    {"role": "user", "content": user_input}]
        )

        respuesta_texto = response.choices[0].message.content
        st.write(respuesta_texto)