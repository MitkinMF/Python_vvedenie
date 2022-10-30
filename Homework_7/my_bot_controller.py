import telephone_book as tb
import view
t_book=[]

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')



#  global t_book
#     flag=1
#     while flag:
#         view.main_menu()
#         s=view.cmd_input()
#         if s=='1':
#             view.menu_select_read_file()
#             t_book=view.read_file(view.cmd_input())           
#         elif s=='2':
#             tb.person_create(t_book, view.person_input())             
#         elif s=='3':
#             view.out_to_screen(t_book)
#         elif s=='4':  
#             view.menu_select_out_format()
#             view.out_file(t_book,view.cmd_input())
#         elif s=='0':  
#             flag=0
#             break
#         s=input('Нажмите Enter чтобы продолжить')
#         system("cls")
        

async def bot_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global t_book
    t_book=view.read_file('1') 
    await update.message.reply_text('/print - вывести телефонный справочник \n ' \
'/export - экспорт файла в формате .csv \n /new - создать новую запись')


async def tb_out(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(view.out_to_bot(t_book))
    
async def bot_person_create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global t_book
    n_p=''
    app.add_handler(MessageHandler(filters.TEXT))
    n_p=update.message.text    
    new_pers=tuple(n_p.rstrip('\n').split())
    tb.person_create(t_book ,new_pers)
    #await update.message.reply_text(view.out_to_bot(buff_list))   




# async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global candies
#     msg = update.message.text
#     candies -= int(msg)
#     await update.message.reply_text(f'На столе {candies} конфет')
#     if win_in_game():
#         await update.message.reply_text(f'Выиграл {update.effective_user.first_name}')
#         return
#     await update.message.reply_text(f'Бот взял {bot_candy()} конфет, на столе {candies} конфет')

#     if win_in_game():
#         await update.message.reply_text('Выиграл БОТ')
#         return

# async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global candies
#     msg = update.message.text
#     candies -= int(msg)
#     await update.message.reply_text(f'На столе {candies} конфет')
#     if win_in_game():
#         await update.message.reply_text(f'Выиграл {update.effective_user.first_name}')
#         return
#     await update.message.reply_text(f'Бот взял {bot_candy()} конфет, на столе {candies} конфет')

#     if win_in_game():
#         await update.message.reply_text('Выиграл БОТ')
#         return


# def bot_candy():
#     global candies
#     if candies > 28:
#         candy = candies % 29
#     else:
#         candy = candies
#     candies -= candy
#     return candy


# def win_in_game():
#     global candies
#     return candies < 1

# candies = 100

app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("print", tb_out))
app.add_handler(CommandHandler("start", bot_menu))
app.add_handler(CommandHandler("new", bot_person_create))
app.run_polling()
