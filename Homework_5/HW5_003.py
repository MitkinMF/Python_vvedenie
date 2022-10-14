# Создайте программу для игры в ""Крестики-нолики"".

def field(moves):
    
    y1 = f"    {moves[1]}  |  {moves[2]}  | {moves[3]}  "
    y1_1 = "  --1--+--2--+--3--"
    y2 = f"    {moves[4]}  |  {moves[5]}  | {moves[6]}  "
    y1_2 = "  --4--+--5--+--6--"
    y3 = f"    {moves[7]}  |  {moves[8]}  | {moves[9]}  "
    y0 =  "  --7--+--8--+--9--"
    print(y1)
    print(y1_1)
    print(y2)
    print(y1_2)
    print(y3)
    print(y0)

def wins(moves):
    if ((moves[1] == moves[2] == moves[3]
        or moves[4] == moves[5] == moves[6]
        or moves[7] == moves[8] == moves[9])
        and moves[1] != ' ' and moves[5] != ' ' and moves[9] != ' '):
        return moves[1]
    elif ((moves[1] == moves[4] == moves[7]
           or moves[2] == moves[5] == moves[8]
           or moves[3] == moves[6] == moves[9])
          and moves[1] != ' ' and moves[5] != ' ' and moves[9] != ' '):
        return moves[5]
    elif ((moves[1] == moves[5] == moves[9]
           or moves[7] == moves[5] == moves[3])
          and moves[9] != ' ' and moves[7] != ' '):
        return moves[9]
    return False


def move(symbol, moves, player):
    #print(player[1], player[-1])
    if player == '1':
        moves[1] = symbol
    elif player == '2':
        moves[2] = symbol
    elif player == '3':
        moves[3] = symbol
    elif player == '4':
        moves[4] = symbol 
    elif player == '5':
        moves[5] = symbol  
    elif player == '6':
        moves[6] = symbol 
    elif player == '7':
        moves[7] = symbol 
    elif player == '8':
        moves[8] = symbol  
    elif player == '9':
        moves[9] = symbol 
    return moves

moves_out = ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
field(moves_out)

count_move = 0
win = False
while not win:
    count_move += 1
    player_out = input('Введите номер ячейки: ')
    if count_move % 2:
        symbol_out = 'X'
    else:
        symbol_out = 'O'
    moves_out = move(symbol_out, moves_out, player_out)
    field(moves_out)
    win = wins(moves_out)
print(f'На {count_move} ходу победили {win}')