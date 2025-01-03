import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Token del bot (cambia esto por tu propio token del BotFather)
TOKEN = "7699790718:AAFFtZ1LFiRdE3JnVK01DpFK7U6WM625j2o"

# Diccionario de comandos y respuestas
COMANDOS = {
    "listadelibros": {
        "func": "lista_de_libros",
        "descripcion": "Ver lista de libros recomendados"
    },
    "contacto": {
        "func": "informacion_contacto",
        "descripcion": "Obtener información de contacto para compra de libros"
    },
    "ayuda": {
        "func": "ayuda",
        "descripcion": "Ver esta ayuda"
    }
}

# Comando de bienvenida (para nuevos miembros)
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            await update.message.reply_text(
                f"👋 ¡Hola {new_member.first_name}! Bienvenido al grupo. Escribe /ayuda para ver los comandos disponibles."
            )

# Comando /listadelibros
async def lista_de_libros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = (
        "📚 Aquí tienes nuestra lista de libros recomendados:\n"
        "1. El Principito\n"
        "2. Cien años de soledad\n"
        "3. Rayuela\n"
        "Escribe /ayuda para más información."
    )
    await update.message.reply_text(respuesta)

# Comando /contacto
async def informacion_contacto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = (
        "📞 Si deseas comprar libros, contáctame directamente a través de Telegram @usuario\n"
        "¡Estaré encantado de ayudarte!"
    )
    await update.message.reply_text(respuesta)

# Comando /ayuda
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = "🤖 Comandos disponibles:\n"
    for comando, info in COMANDOS.items():
        respuesta += f"/{comando} - {info['descripcion']}\n"
    await update.message.reply_text(respuesta)

# Manejador para mensajes no reconocidos
async def mensaje_no_reconocido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚠️ Lo siento, no entiendo ese comando. Escribe /ayuda para ver los comandos disponibles."
    )

# Función para agregar nuevos comandos
def agregar_comando(application, comando, funcion):
    """Agrega un nuevo comando al bot."""
    application.add_handler(CommandHandler(comando, funcion))

# Inicialización del bot
def main():
    # Crear la aplicación
    application = ApplicationBuilder().token(TOKEN).build()

    # Agregar los comandos desde el diccionario
    for comando, info in COMANDOS.items():
        func = globals()[info["func"]]  # Obtener la función asociada al comando
        agregar_comando(application, comando, func)

    # Agregar manejadores adicionales
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))  # Nuevos miembros
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_no_reconocido))  # Mensajes no válidos

    # Ejecutar el bot
    print("🤖 Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling()

if __name__ == "__main__":
    main()