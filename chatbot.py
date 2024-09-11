import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a API com a chave
genai.configure(api_key=os.getenv("gemini_api_key"))

# Cria o modelo
generation_config = {
    "temperature": 0.5,
    "top_p": 0.5,
    "top_k": 50,
    "max_output_tokens": 700,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "harm_category_harassment", "threshold": "block_none"},
    {"category": "harm_category_hate_speech", "threshold": "block_medium_and_above"},
    {"category": "harm_category_sexually_explicit", "threshold": "block_medium_and_above"},
    {"category": "harm_category_dangerous_content", "threshold": "block_medium_and_above"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="Pablo é um mecânico com anos de experiência, especialista em manuais de veículos e diagnóstico de problemas comuns. Ele combina profundo conhecimento técnico com uma comunicação direta, simples e acessível, explicando de forma sucinta e clara qualquer questão mecânica. Além disso, ele sugere soluções práticas. Simpático e paciente, Pablo gosta de orientar os donos de carros sobre boas práticas de manutenção preventiva, reforçando a importância de cuidar do veículo para evitar problemas futuros.",
)

# Inicializa a sessão de chat e o histórico
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Configurando o layout da página
st.title("Chatbot com Streamlit e Google Generative AI")

# Exibindo mensagens anteriores
for msg in st.session_state.messages:
    st.text(msg)

# Caixa de entrada para o usuário
user_input = st.text_input("Você: ", "")

# Quando o usuário envia a mensagem
if st.button("Enviar"):
    if user_input:
        # Adiciona a mensagem do usuário à sessão
        st.session_state.messages.append(f"Você: {user_input}")

        # Envia a mensagem do usuário para o chatbot e obtém a resposta
        response = st.session_state.chat_session.send_message(user_input)
        model_response = response.text

        # Adiciona a resposta do chatbot à sessão
        st.session_state.messages.append(f"Chatbot: {model_response}")

        # Limpa o campo de entrada
        st.rerun()  # Atualiza a página para mostrar as novas mensagens