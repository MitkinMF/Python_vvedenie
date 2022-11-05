import logger
from simpleeval import simple_eval
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackQueryHandler, Application

value = ""

old_value = ""

help_menu='''Калькулятор для вычисления комплексных и рациональных чисел
Комплексные числа рекомендуется задавать в виде: (1+5j)
Для запуска калькулятора введите команду: /start
Для получения логов используйте команду: /log'''

keyboard = [
        [
            InlineKeyboardButton("C", callback_data="C"),
            InlineKeyboardButton("<=", callback_data="backspace"),            
        ],              
        [
            InlineKeyboardButton("j", callback_data="j"),
            InlineKeyboardButton("(", callback_data="("),
            InlineKeyboardButton(")", callback_data=")"),
            InlineKeyboardButton("/", callback_data=" / "),
        ],        
        [
            InlineKeyboardButton("7", callback_data="7"),
            InlineKeyboardButton("8", callback_data="8"),
            InlineKeyboardButton("9", callback_data="9"),
            InlineKeyboardButton("*", callback_data=" * "),
        ],
        [
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
            InlineKeyboardButton("6", callback_data="6"),
            InlineKeyboardButton("-", callback_data=" - "),
        ],        
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("+", callback_data=" + "),
        ],        
        [
            InlineKeyboardButton(" ", callback_data="no"),
            InlineKeyboardButton("0", callback_data="0"),
            InlineKeyboardButton(",", callback_data="."),
            InlineKeyboardButton("=", callback_data="="),
        ],
    ]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('0', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global value, old_value
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "no":
        pass
    elif data == "backspace":
        value = value[:-1]
    elif data == "C":
        value = ""
    elif data == "j":
        if len(value) == 0:
            value = '1j'
        else:
            value = value + 'j'
    elif data == "=":
        try:
            value = value.replace('+ j', '+ 1j').replace('- j', '- 1j')
            temp = value
            result = str(simple_eval(value))
            logger.log_operation(f'{temp} = {result}')
            value=result
        except:
            value = "Ошибка!"
            logger.log_operation('Ошибка!')
    else:
        value += data

    if value != old_value:
        if value == "":
            await query.edit_message_text(text="0", reply_markup=reply_markup)
        else:
            await query.edit_message_text(text=value, reply_markup=reply_markup)

    old_value = value
    if value == "Ошибка!":
        value = ""

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(help_menu)
   
async def getlog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    file = open('./log/logging.csv', 'rb')
    await update.message.reply_document(file) 
    
def main_loop():
           
    app = Application.builder().token(my_token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command ))
    app.add_handler(CommandHandler('log', getlog ))
    app.add_handler(CallbackQueryHandler(button))
    print('Bot started')
    app.run_polling()
    