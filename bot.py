import os
from telebot import TeleBot

TOKEN = os.getenv("TOKEN")
bot = TeleBot(TOKEN)

# Saludar a nuevos usuarios
@bot.message_handler(content_types=["new_chat_members"])
def bienvenida(message):
    for new_member in message.new_chat_members:
        bot.send_message(
            message.chat.id,
            f"¡Hola {new_member.first_name}! Bienvenido al grupo. Escribe /ayuda para ver los comandos disponibles."
        )

# Comando personalizado: /listadelibros
@bot.message_handler(commands=["listadelibros"])
def lista_de_libros(message):
    respuesta = "📚 Aquí tienes nuestra lista de libros recomendados:\n1. El Principito\n2. Cien años de soledad\n3. Rayuela"
    bot.reply_to(message, respuesta)

# Comando de ayuda: /ayuda
@bot.message_handler(commands=["ayuda"])
def ayuda(message):
    respuesta = "🤖 Comandos disponibles:\n/listadelibros - Ver lista de libros recomendados\n/ayuda - Ver esta ayuda."
    bot.reply_to(message, respuesta)

# Inicia el bot
bot.polling()
