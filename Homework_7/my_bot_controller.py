import telephone_book as tb
import view
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler

main_menu = '''/print - вывести телефонный справочник 
/export - экспорт файла в формате .csv
/new - создать новую запись 
/save - сохранить базу '''
t_book=view.read_file('1') 
PERSON_CREATE = range(1)  

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
async def bot_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global main_menu
    await update.message.reply_text(main_menu)


async def tbook_out(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(view.out_to_bot(t_book))
    
async def save_t_book(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global t_book
    view.out_file(t_book,'1') 
    await update.message.reply_text( 'База сохранена')
    
async def t_book_export(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('tel_book.csv', 'rb')
    await update.message.reply_document(file)   
    
    
async def bot_person_create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text( 'Введите запись в формате: Фамилия Имя Телефон')
    return PERSON_CREATE  


async def user_person_create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global t_book
    global main_menu
    n_p = update.message.text
    new_pers=tuple(n_p.rstrip('\n').split())
    tb.person_create(t_book, new_pers)
    print (t_book)
    await update.message.reply_text('Запись добавлена')
    await update.message.reply_text(main_menu)
    return ConversationHandler.END
     

def main_loop():
   
    app = ApplicationBuilder().token(my_token).build()
    
    person_create_conv_handler = ConversationHandler(
            entry_points=[CommandHandler("new", bot_person_create)],
            states={
                PERSON_CREATE: [
                    MessageHandler(filters.TEXT, user_person_create)],
            },
            fallbacks="",
        )

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("print", tbook_out))
    app.add_handler(CommandHandler("start", bot_menu))
    app.add_handler(CommandHandler("save", save_t_book))
    app.add_handler(CommandHandler("export", t_book_export))
    app.add_handler(person_create_conv_handler)
    app.run_polling()
