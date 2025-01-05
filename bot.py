import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
)

# Configuración del logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Token del bot
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
}

# Generador de mensajes de bienvenida
def generar_mensaje_bienvenida(nombre_usuario):
    return (
        f"👋 ¡Hola {nombre_usuario}, como estas? 👋\n"
        "¡Bienvenid@ a nuestro grupo! 📚\n\n"
        "En el grupo encontrarás libros y resúmenes compartidos por todos.\n\n"
        "✅ Te invitamos al canal privado para acceder a libros y resúmenes exclusivos aportados únicamente por el admin, uniéndote con el botón de abajo.\n\n"
        "✅ También puedes comprar el libro que no encuentras escribiéndole al admin @gaspar_111"
    )

# Comandos
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            keyboard = [
                [
                    InlineKeyboardButton("Unirme al canal 💬", url="https://t.me/+818Gc88EOOo0NTQx"),
                    InlineKeyboardButton("Comprar libros 📚", url="https://t.me/gaspar_111")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            mensaje_bienvenida = generar_mensaje_bienvenida(new_member.first_name)
            await update.message.reply_text(mensaje_bienvenida, reply_markup=reply_markup)

async def lista_de_libros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = (
        "📚 Aquí tienes nuestra lista de libros recomendados:\n"
        "1. 48 Leyes del poder\n"
        "2. El hombre en busca de sentido\n"
        "3. El principito\n"
        "Escribe /ayuda para más información."
    )
    await update.message.reply_text(respuesta)

async def comprar_libros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = (
        "📞 Si deseas comprar libros, contáctame directamente a través de Telegram @gaspar_111\n"
        "¡Estaré encantado de ayudarte!"
    )
    await update.message.reply_text(respuesta)

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = "🤖 Comandos disponibles:\n"
    for comando, info in COMANDOS.items():
        respuesta += f"/{comando} - {info['descripcion']}\n"
    await update.message.reply_text(respuesta)

# Manejador para mensajes no reconocidos
async def mensaje_no_reconocido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message

    # Comprobar si el mensaje es un comando no reconocido
    if mensaje.text and mensaje.text.startswith("/"):
        await mensaje.reply_text(
            "⚠️ Lo siento, no entiendo ese comando. Escribe /ayuda para ver los comandos disponibles."
        )

# Inicialización del bot
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Agregar comandos
    for comando, info in COMANDOS.items():
        func = globals()[info["func"]]
        application.add_handler(CommandHandler(comando, func))

    # Manejadores adicionales
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_no_reconocido))

    # Ejecutar el bot
    print("🤖 Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling()

if __name__ == "__main__":
    main()