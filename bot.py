import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters

# Import from handlers
from handlers import BotHandlers, WAITING_FOR_INPUT, WAITING_FOR_FRACTION, WAITING_FOR_PERCENTAGE, WAITING_FOR_DISCOUNT, WAITING_FOR_AGE, WAITING_FOR_DATE, WAITING_FOR_LENGTH, WAITING_FOR_WEIGHT, WAITING_FOR_TEMPERATURE, WAITING_FOR_AVERAGE

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot"""
    token = os.getenv('BOT_TOKEN')
    if not token:
        logger.error("No BOT_TOKEN found in .env file!")
        return
    
    # Create application
    application = Application.builder().token(token).build()
    
    # Initialize handlers
    bot_handlers = BotHandlers()
    
    # Add all conversation handlers
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('calc', bot_handlers.calc_start)],
            states={WAITING_FOR_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.calc_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('percentage', bot_handlers.percentage_start)],
            states={WAITING_FOR_PERCENTAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.percentage_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('fraction', bot_handlers.fraction_start)],
            states={WAITING_FOR_FRACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.fraction_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('average', bot_handlers.average_start)],
            states={WAITING_FOR_AVERAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.average_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('discount', bot_handlers.discount_start)],
            states={WAITING_FOR_DISCOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.discount_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('age', bot_handlers.age_start)],
            states={WAITING_FOR_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.age_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('date', bot_handlers.date_start)],
            states={WAITING_FOR_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.date_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('length', bot_handlers.length_start)],
            states={WAITING_FOR_LENGTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.length_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('weight', bot_handlers.weight_start)],
            states={WAITING_FOR_WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.weight_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('temp', bot_handlers.temp_start)],
            states={WAITING_FOR_TEMPERATURE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.temp_input)]},
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        )
    )
    
    # Add basic command handlers
    application.add_handler(CommandHandler('start', bot_handlers.start))
    application.add_handler(CommandHandler('help', bot_handlers.help_command))
    
    # Add error handler
    application.add_error_handler(bot_handlers.error_handler)
    
    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=[])
    
if __name__ == '__main__':
    main()
