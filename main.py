# main.py
import os
from dotenv import load_dotenv
from telegram.ext import Application, MessageHandler, filters
from handlers import manejar_mensaje
from menu import BOT_INICIADO


load_dotenv()
TOKEN = os.getenv("TOKEN")

def main():
    # paso 2: crea la conexion con Telegram
    app = Application.builder().token(TOKEN).build()
    
    # paso 3: registra el handler — cualquier mensaje de texto
    # va a la funcion manejar_mensaje de handlers.py
    app.add_handler(MessageHandler(filters.TEXT, manejar_mensaje))

    print(BOT_INICIADO)
    
    # paso 4: arranca el polling (loop infinito)
    app.run_polling()

if __name__ == "__main__":
    main()