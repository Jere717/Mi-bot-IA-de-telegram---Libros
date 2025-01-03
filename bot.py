import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Token del bot (cambia esto por tu propio token del BotFather)
TOKEN = "7699790718:AAFFtZ1LFiRdE3JnVK01DpFK7U6WM625j2o"

# Diccionario de comandos y respuestas
COMANDOS = {
    "listadelibros": {
        "func": "lista_de_libros",
        "descripcion": "Ver lista de libros recomendados"
    },
    "comprarlibros": {
        "func": "comprar_libros",
        "descripcion": "Obtener información de contacto para compra de libros"
    },
    "ayuda": {
        "func": "ayuda",
        "descripcion": "Ver esta ayuda"
    }
    # "bienvenida": {
    #     "func": "bienvenida_comando",
    #     "descripcion": "Ver el mensaje de bienvenida"
    # }
}

# Función para generar el mensaje de bienvenida
def generar_mensaje_bienvenida(new_member_name):
    return (
        f"👋 ¡Hola {new_member_name}, como estas? 👋\n"
        "¡Bienvenid@ a nuestro grupo! 📚\n\n"
        "En el grupo encontrarás libros y resúmenes compartidos por todos.\n\n"
        "✅Te invitamos al canal privado, para acceder a libros y resúmenes exclusivos aportados únicamente por el admin, uniéndote con el botón de abajo.\n\n"
        "✅Tambien puedes comprar el libro que no encuentras escribiéndole al admin @jere717"
    )

# Comando de bienvenida (para nuevos miembros)
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            # Crear los botones
            keyboard = [
                [
                    InlineKeyboardButton("Unirme al canal 💬", url="https://t.me/+818Gc88EOOo0NTQx"),  # Reemplaza con tu canal
                    InlineKeyboardButton("Comprar libros 📚", url="https://t.me/jere717")  # Reemplaza con tu nombre de usuario
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            # Generar el mensaje de bienvenida
            mensaje_bienvenida = generar_mensaje_bienvenida(new_member.first_name)
            
            # Enviar mensaje de bienvenida con botones
            await update.message.reply_text(
                mensaje_bienvenida,
                reply_markup=reply_markup
            )

# Comando /bienvenida (para ver el mensaje de bienvenida manualmente)
async def bienvenida_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Crear los botones
    keyboard = [
        [
            InlineKeyboardButton("Únete al canal", url="https://t.me/+818Gc88EOOo0NTQx"),  # Reemplaza con tu canal
            InlineKeyboardButton("Comprar libros", url="https://t.me/jere717")  # Reemplaza con tu nombre de usuario
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Generar el mensaje de bienvenida
    mensaje_bienvenida = generar_mensaje_bienvenida(update.message.from_user.first_name)
    
    # Enviar el mensaje de bienvenida con botones
    await update.message.reply_text(
        mensaje_bienvenida,
        reply_markup=reply_markup
    )

# Comando /listadelibros
async def lista_de_libros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = (
        "📚 Aquí tienes nuestra lista de libros recomendados:\n"
        "1. 48 Leyes del poder\n"
        "2. El hombre en busca de sentido\n"
        "3. El principito\n"
        "Escribe /ayuda para más información."
    )
    await update.message.reply_text(respuesta)

# Comando /contacto
async def comprar_libros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = (
        "📞 Si deseas comprar libros, contáctame directamente a través de Telegram @jere717\n"
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