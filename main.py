from telegram.ext import Updater, MessageHandler, Filters

# Функция-обработчик для эхо-бота
def echo(update, context):
    # Получаем текст сообщения от пользователя
    message_text = update.message.text

    # Отправляем пользователю ответное сообщение с тем же текстом
    update.message.reply_text(message_text)

def main():
    # Создаем объект Updater и передаем ему токен вашего бота
    updater = Updater('YOUR_BOT_TOKEN', use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик для текстовых сообщений от пользователя
    echo_handler = MessageHandler(Filters.text &amp; (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
