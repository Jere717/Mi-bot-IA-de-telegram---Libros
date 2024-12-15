import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Asignar el token directamente
TOKEN = "8049075999:AAGEwH7eoD11W0ruIL5hKfsDxUjd9M4BSZo"

# Comando de bienvenida
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_member in update.message.new_chat_members:
        await update.message.reply_text(
            f"¡Hola {new_member.first_name}! Bienvenido al grupo. Escribe /ayuda para ver los comandos disponibles."
        )

# Comando /listadelibros
async def lista_de_libros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = "📚 Aquí tienes nuestra lista de libros recomendados:\n1. El Principito\n2. Cien años de soledad\n3. Rayuela"
    await update.message.reply_text(respuesta)

# Comando de ayuda: /ayuda
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = "🤖 Comandos disponibles:\n/listadelibros - Ver lista de libros recomendados\n/ayuda - Ver esta ayuda."
    await update.message.reply_text(respuesta)

# Inicialización del bot
async def main():
    # Crea la aplicación con el token directamente
    application = ApplicationBuilder().token(TOKEN).build()

    # Manejadores para los comandos
    application.add_handler(CommandHandler("new_chat_members", bienvenida))  # Para nuevos miembros
    application.add_handler(CommandHandler("listadelibros", lista_de_libros))  # Para la lista de libros
    application.add_handler(CommandHandler("ayuda", ayuda))  # Para el comando de ayuda

    # Ejecuta el bot
    await application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    # Aquí no es necesario usar asyncio.run()
    # Se usa directamente application.run_polling() que maneja el ciclo de eventos
    main()