import telebot
import src.box_package.bot.config as config
import src.box_package.bot.replies as replies
from src.box_package.schedule.ScheduleDef import ScheduleDef


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['help'])
def reply(message):
    bot.reply_to(message, replies.Replies())


@bot.message_handler(commands=['now'])
def reply(message):
    now = ScheduleDef()
    bot.reply_to(message, now.to_string(now.get_week(4)))
