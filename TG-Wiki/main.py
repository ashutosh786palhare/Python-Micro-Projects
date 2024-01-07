import logging
import wikipedia
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! I'm a Wikipedia bot. Type /search [query] to search Wikipedia.")

# Function to handle Wikipedia search
def search(update, context):
    query = ' '.join(context.args)
    try:
        result = wikipedia.summary(query)
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    except wikipedia.exceptions.DisambiguationError as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please be more specific or choose from these options:\n" + ', '.join(e.options))
    except wikipedia.exceptions.PageError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, no information found.")

# Function to handle unknown commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I don't understand that command.")

def main():
    # Create an Updater object and pass your bot token
    updater = Updater(token='Token ko idhar Dalneka', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('search', search))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
