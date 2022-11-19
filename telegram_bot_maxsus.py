from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, BotCommand

TOKEN = '5840402232:AAE2c9XvEEVzgC8BMI9sepdu-rNridDH21o'


def start(update, context):

    buttons = [
        [InlineKeyboardButton(text="Haridor", callback_data="client")],
        [InlineKeyboardButton(text="Sotuvchi", callback_data="sotuvchi")],
    ]
    update.message.reply_text(text=f"Salom hurmatli {update.message.from_user.first_name}, bo'limni tanlang:",
                              reply_markup=InlineKeyboardMarkup(buttons))

def inline_messages(update, context):
    query = update.callback_query
    if query.data == "client":
        buttons = [
            [InlineKeyboardButton(text="Iltimos ro'yxatdan o'ting", callback_data="m1")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
        query.message.reply_text(text=f"Iltimos so'ralgan malumotlarni kiriting:",
                                  reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == "sotuvchi":
        buttons = [
            [InlineKeyboardButton(text="Iltimos ro'yxatdan o'ting", callback_data="m1")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
        query.message.reply_text(text=f"Iltimos so'ralgan malumotlarni kiriting:",
                                  reply_markup=InlineKeyboardMarkup(buttons))
        update.message

        reply_markup = InlineKeyboardMarkup(buttons)

        update.message.reply_text("Please choose:", reply_markup=reply_markup)
    elif query.data == 'm1':
        buttons = [
                    [InlineKeyboardButton(text="Ism", callback_data="p1")],
                    [InlineKeyboardButton(text="Familiya", callback_data="p2")],
                    [InlineKeyboardButton(text="Manzil", callback_data="p3")],
                    [InlineKeyboardButton(text="Kontakt", callback_data="p4")],
                ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))



updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(inline_messages))

updater.start_polling()
updater.idle()

