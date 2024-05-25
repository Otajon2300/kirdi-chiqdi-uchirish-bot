import logging
import os
from background import keep_alive
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.ext import ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Salom! Men guruhda qo\'shilish va chiqish xabarlarini yashiraman. \nMeni guruhga qo\'shib admin sifatida tayinlang. ')

async def handle_new_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.message.new_chat_members:
        try:
            await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            logger.info(f"{member.full_name} uchun qo'shilish xabarini o'chirdim {update.message.chat.title}")
        except Exception as e:
            logger.error(f"Qo'shilish xabarini o'chirishda xato: {e}")

async def handle_left_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        logger.info(f"Chiqish xabarini o'chirdim {update.message.chat.title}")
    except Exception as e:
        logger.error(f"Chiqish xabarini o'chirishda xato: {e}")

keep_alive()
if __name__ == '__main__':

    # Botingizning API tokenini kiriting
    # token = '6328093327:AAGBnOnAzeVK-5Tkk9DPqYe90Tu_ccL4wZg'
    token = '6328093327:AAGBnOnAzeVK-5Tkk9DPqYe90Tu_ccL4wZg'

    # Handlerlarni ro'yxatga olish
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_chat_members))
    app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, handle_left_chat_member))

# Start the webhook
    app.run_webhook(listen="0.0.0.0", port=8443, url_path=token)
    app.bot.set_webhook(f"https://kirdi-chiqdi-uchirish-bot.onrender.com/{token}")
