
import os
import google.generativeai as genai
from main import text_to_speech
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.5,
  "top_p": 0.5,
  "top_k": 50,
  "max_output_tokens": 1000,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="Pablo é um mecânico de 45 anos com 25 anos de experiência, especialista em manuais de veículos e diagnóstico de problemas comuns. Ele combina profundo conhecimento técnico com uma comunicação simples e acessível, explicando claramente qualquer questão mecânica e sempre sugerindo soluções práticas. Simpático e paciente, Pablo gosta de orientar os donos de carros sobre boas práticas de manutenção preventiva, reforçando a importância de cuidar do veículo para evitar problemas futuros. Sempre pronto para ajudar, ele também recomenda verificar o manual do carro para orientações específicas e garantir uma manutenção correta.",
)



chat_session = model.start_chat(
    history=[]
)

print("Bot: Olá, como posso ajudar hoje?")
print()
text_to_speech(" Olá, como posso ajudar hoje")

while True:
    user_input = input("You: ")
    print()

    if user_input.lower() in ['sair', 'exit', 'quit']:
        break

    response = chat_session.send_message(user_input)
    model_response = response.text

    print(f'Bot: {model_response}')
    print()

    # Atualiza o histórico da sessão de chat
    chat_session.history.extend([
        {"role": "user", "parts": [user_input]},
        {"role": "model", "parts": [model_response]}
    ])