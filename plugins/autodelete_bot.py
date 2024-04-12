
import time
from bot import Bot
from config import TG_BOT_TOKEN

# Set your Telegram bot token
bot = Bot.Bot("TG_BOT_TOKEN")

# Define the message deletion function
def delete_messages():
    # Get a list of all private chats
    chats = bot.get_updates(chat_type="private")

    # Iterate over the chats and delete messages sent by the bot
    for chat in chats:
        messages = bot.get_chat_messages(chat.chat.id)
        for message in messages:
            if message.from_user.id == bot.get_me().id:
                bot.delete_message(chat.chat.id, message.message_id)

# Schedule the message deletion task to run
schedule.every(2).minutes.do(delete_messages)

# Start the bot
bot.polling()
