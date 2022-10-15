# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"

from random import choice, randint


def user_input(s):
    num = input(s)
    while not (num[0] != '0' and num.isdigit()):  # проверка на число
        num = input(s)
    return int(num)


def bot_answer(db):
    print(f"Бот взял {db[2]} конфет. Теперь твоя очередь")
    db[0] = db[0] - db[2]
    db[1] = 1
    db[2] = 0
    db[3] += 1
    db[4]= 0
    return


def user_answer(s,db):
    db[2] = user_input((f"{s}, введите количество конфет, которое хотите взять (от 1 до {db[5]}): "))
    while not (0 < db[2] <= db[5]):
        db[2] = user_input((f"{s}, введите количество конфет, которое хотите взять (от 1 до {db[5]}): "))
    db[0] = db[0] - db[2]
    db[4] += db[2]
    db[2] = 0
    return

game_db = [0,       0,      0,        0,         0 ,           0]
       # [sweets, player, step, count_steps, previos_step, max_sweets]

game_db[0] = user_input("Введите количество конфет: ")
game_db[5] = user_input("Введите максимальное количество конфет, которое можно взять за один ход: ")
select_game = int(input("Введите тип игры (1 - игрок против бота, 2 - игорок против игрока): "))
if select_game == 1:
    # выбор, кто ходит первым  0 -  бот , 1 - игрок1,  2 - игрок2
    game_db[1] = choice([0, 1])
else:
    game_db[1] = choice([1, 2])
game_db[3] = 0  # Для отделения первого для бота хода от всех его ходов
game_db[4] = 0
while game_db[0] // game_db[5]:
    if game_db[1] == 1 or  game_db[1] == 2:   
        if game_db[1]==1:
            user_answer('Игрок1',game_db)
            game_db[1] = 0
            if select_game == 2:
                user_answer('Игрок2',game_db)
                game_db[1] = 1
        elif game_db[1] == 2:
            user_answer('Игрок2')
            game_db[1] = 1

    else:      #"интеллект" бота
        if game_db[3] == 0 and game_db[4] != game_db[0] % (game_db[5] + 1):
            game_db[2] = game_db[0]  % (game_db[5] + 1)
            bot_answer(game_db)
        elif game_db[3] != 0:
            game_db[2] = (game_db[5] + 1) - game_db[4]
            bot_answer(game_db)
        else:
            game_db[2] = randint(1, game_db[5])
            bot_answer(game_db)
    print(game_db[0])
if game_db[1]==1:
    print("Победил, игрок1")
else:
    if select_game == 2:
        print("Победил, игрок2")
    print(f"Победил, Бот")
