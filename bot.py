import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Token del bot
TOKEN = 'AQUI_VA_TU_TOKEN'

# Creamos el objeto updater y el dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Definimos la función que enviará la respuesta
def responder(update, context):
    # Obtenemos el mensaje recibido
    mensaje = update.message.text
    # Creamos la respuesta
    respuesta = 'Hola {}, ¿cómo estás?'.format(update.message.from_user.first_name)
    # Enviamos la respuesta
    context.bot.send_message(chat_id=update.message.chat_id, text=respuesta)

# Creamos el handler y lo agregamos al dispatcher
handler = MessageHandler(Filters.text & (~Filters.command), responder)
dispatcher.add_handler(handler)

# Iniciamos el bot
updater.start_polling()
updater.idle()
