import telebot
from config import TOKEN_TG

bot = telebot.TeleBot(TOKEN_TG)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"To add a link, use /add <link> , to view latest link use /latest")


@bot.message_handler(commands=['add'])
def send_welcome(message: telebot.types.Message):
    link = message.text.split()[1]
    bot.send_message(message.chat.id, f"Adding link {link}")

    with open("latest_link.txt", "w") as f:
        f.write(link)

    bot.send_message(message.chat.id, f"Added link {link}")


@bot.message_handler(commands=['latest'])
def send_welcome(message):

    bot.send_message(message.chat.id, "Getting latest link")

    with open("latest_link.txt", "r") as f:
        bot.send_message(message.chat.id, f"Current link is {f.read()}")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Oops, wrong command, try using /start to view all commands!")


bot.infinity_polling()