from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from utils import calc_utils, unit_converter

# Conversation states
WAITING_FOR_INPUT = 1
WAITING_FOR_FRACTION = 2
WAITING_FOR_PERCENTAGE = 3
WAITING_FOR_DISCOUNT = 4
WAITING_FOR_AGE = 5
WAITING_FOR_DATE = 6
WAITING_FOR_LENGTH = 7
WAITING_FOR_WEIGHT = 8
WAITING_FOR_TEMPERATURE = 9
WAITING_FOR_AVERAGE = 10

class BotHandlers:
    
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message"""
        welcome_text = """
🎯 *Welcome to DondreeBot!* 🎯

I'm your all-in-one calculation and conversion assistant!

*Available Commands:*
📊 `/calc` - Basic calculator
💯 `/percentage` - Percentage calculator
🧮 `/fraction` - Fraction calculator
📈 `/average` - Average calculator
🏷️ `/discount` - Discount calculator
🎂 `/age` - Age calculator
📅 `/date` - Date calculator
📏 `/length` - Length converter
⚖️ `/weight` - Weight converter
🌡️ `/temp` - Temperature converter
❓ `/help` - Show this message

*How to use:*
Simply click on a command and follow the instructions!
"""
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
    
    @staticmethod
    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message"""
        help_text = """
📚 *Detailed Help Guide*

*Calculator Functions:*
1. `/calc` - Enter expression (e.g., 25+30*2, 100/4)
2. `/percentage` - Enter: number percentage (e.g., 200 15)
3. `/fraction` - Enter: operation num1/den1 num2/den2
4. `/average` - Enter numbers separated by spaces
5. `/discount` - Enter: price discount%
6. `/age` - Enter birth date (YYYY-MM-DD)
7. `/date` - Enter two dates (YYYY-MM-DD YYYY-MM-DD)

*Converter Functions:*
8. `/length` - Enter: value from_unit to_unit
9. `/weight` - Enter: value from_unit to_unit
10. `/temp` - Enter: value from_unit to_unit

*Examples:*
`/calc 25+30*2`
`/percentage 200 15`
`/length 10 m ft`
`/weight 5 kg lb`
`/temp 32 C F`

*Units Available:*
📏 Length: mm, cm, m, km, in, ft, yd, mi
⚖️ Weight: mg, g, kg, ton, oz, lb
🌡️ Temperature: C, F, K
"""
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    @staticmethod
    async def calc_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🔢 *Basic Calculator*\n\n"
            "Enter your expression (use +, -, ×, ÷, *, /, (, )):\n"
            "Example: `25 + 30 * 2`\n\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_INPUT
    
    @staticmethod
    async def calc_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        expression = update.message.text
        result = calc_utils.basic_calc(expression)
        await update.message.reply_text(result)
        return ConversationHandler.END
    
    @staticmethod
    async def percentage_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "💯 *Percentage Calculator*\n\n"
            "Enter: `number percentage`\n"
            "Example: `200 15` (calculates 15% of 200)\n\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_PERCENTAGE
    
    @staticmethod
    async def percentage_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 2:
                await update.message.reply_text("❌ Please enter exactly two numbers!")
                return WAITING_FOR_PERCENTAGE
            
            number = float(parts[0])
            percentage = float(parts[1])
            result = calc_utils.percentage_calc(number, percentage)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Please enter valid numbers!")
            return WAITING_FOR_PERCENTAGE
        return ConversationHandler.END
    
    @staticmethod
    async def fraction_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🧮 *Fraction Calculator*\n\n"
            "Enter: `operation num1/den1 num2/den2`\n"
            "Example: `+ 1/2 3/4`\n\n"
            "Operations: +, -, *, /\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_FRACTION
    
    @staticmethod
    async def fraction_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 3:
                await update.message.reply_text("❌ Invalid format! Use: operation num1/den1 num2/den2")
                return WAITING_FOR_FRACTION
            
            operation = parts[0]
            frac1 = parts[1].split('/')
            frac2 = parts[2].split('/')
            
            if len(frac1) != 2 or len(frac2) != 2:
                await update.message.reply_text("❌ Invalid fraction format! Use numerator/denominator")
                return WAITING_FOR_FRACTION
            
            num1, den1 = int(frac1[0]), int(frac1[1])
            num2, den2 = int(frac2[0]), int(frac2[1])
            
            result = calc_utils.fraction_calc(operation, num1, den1, num2, den2)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Please enter valid numbers!")
            return WAITING_FOR_FRACTION
        return ConversationHandler.END
    
    @staticmethod
    async def average_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "📈 *Average Calculator*\n\n"
            "Enter numbers separated by spaces:\n"
            "Example: `10 20 30 40 50`\n\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_AVERAGE
    
    @staticmethod
    async def average_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            numbers = [float(x) for x in update.message.text.split()]
            if not numbers:
                await update.message.reply_text("❌ Please enter at least one number!")
                return WAITING_FOR_AVERAGE
            result = calc_utils.average_calc(numbers)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Please enter valid numbers!")
            return WAITING_FOR_AVERAGE
        return ConversationHandler.END
    
    @staticmethod
    async def discount_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🏷️ *Discount Calculator*\n\n"
            "Enter: `price discount%`\n"
            "Example: `100 25` (25% off $100)\n\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_DISCOUNT
    
    @staticmethod
    async def discount_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 2:
                await update.message.reply_text("❌ Please enter exactly two numbers!")
                return WAITING_FOR_DISCOUNT
            
            price = float(parts[0])
            discount = float(parts[1])
            result = calc_utils.discount_calc(price, discount)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Please enter valid numbers!")
            return WAITING_FOR_DISCOUNT
        return ConversationHandler.END
    
    @staticmethod
    async def age_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🎂 *Age Calculator*\n\n"
            "Enter your birth date (YYYY-MM-DD):\n"
            "Example: `1990-05-15`\n\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_AGE
    
    @staticmethod
    async def age_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        birth_date = update.message.text
        result = calc_utils.age_calc(birth_date)
        await update.message.reply_text(result)
        return ConversationHandler.END
    
    @staticmethod
    async def date_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "📅 *Date Calculator*\n\n"
            "Enter two dates (YYYY-MM-DD YYYY-MM-DD):\n"
            "Example: `2023-01-01 2024-01-01`\n\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_DATE
    
    @staticmethod
    async def date_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 2:
                await update.message.reply_text("❌ Please enter exactly two dates!")
                return WAITING_FOR_DATE
            
            result = calc_utils.date_calc(parts[0], parts[1])
            await update.message.reply_text(result)
        except Exception:
            await update.message.reply_text("❌ Invalid input! Please use YYYY-MM-DD format.")
            return WAITING_FOR_DATE
        return ConversationHandler.END
    
    @staticmethod
    async def length_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "📏 *Length Converter*\n\n"
            "Enter: `value from_unit to_unit`\n"
            "Example: `10 m ft` (converts 10 meters to feet)\n\n"
            "Units: mm, cm, m, km, in, ft, yd, mi\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_LENGTH
    
    @staticmethod
    async def length_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 3:
                await update.message.reply_text("❌ Please enter: value from_unit to_unit")
                return WAITING_FOR_LENGTH
            
            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[2]
            
            result = unit_converter.length_convert(value, from_unit, to_unit)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Invalid value! Please enter a number.")
            return WAITING_FOR_LENGTH
        return ConversationHandler.END
    
    @staticmethod
    async def weight_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "⚖️ *Weight Converter*\n\n"
            "Enter: `value from_unit to_unit`\n"
            "Example: `5 kg lb` (converts 5 kg to pounds)\n\n"
            "Units: mg, g, kg, ton, oz, lb\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_WEIGHT
    
    @staticmethod
    async def weight_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 3:
                await update.message.reply_text("❌ Please enter: value from_unit to_unit")
                return WAITING_FOR_WEIGHT
            
            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[2]
            
            result = unit_converter.weight_convert(value, from_unit, to_unit)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Invalid value! Please enter a number.")
            return WAITING_FOR_WEIGHT
        return ConversationHandler.END
    
    @staticmethod
    async def temp_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🌡️ *Temperature Converter*\n\n"
            "Enter: `value from_unit to_unit`\n"
            "Example: `32 C F` (converts 32°C to Fahrenheit)\n\n"
            "Units: C, F, K\n"
            "Type `/cancel` to cancel.",
            parse_mode='Markdown'
        )
        return WAITING_FOR_TEMPERATURE
    
    @staticmethod
    async def temp_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            parts = update.message.text.split()
            if len(parts) != 3:
                await update.message.reply_text("❌ Please enter: value from_unit to_unit")
                return WAITING_FOR_TEMPERATURE
            
            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[2]
            
            result = unit_converter.temperature_convert(value, from_unit, to_unit)
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text("❌ Invalid value! Please enter a number.")
            return WAITING_FOR_TEMPERATURE
        return ConversationHandler.END
    
    @staticmethod
    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("❌ Operation cancelled. Type /start to see commands.")
        return ConversationHandler.END
    
    @staticmethod
    async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"Update {update} caused error {context.error}")
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ An error occurred! Please try again or contact support."
            )
