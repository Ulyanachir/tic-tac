from colorama import init
init()
from colorama import Back
def draw_board(board):
    print("Игровое поле на данный момент: \n")
    for line in range(3):
        for row in range(3):
            if board[line][row] == "x":
                print(Back.RED + board[line][row] + Back.RESET, end=" | " if row != 2 else " ")
            elif board[line][row] == "0":
                print(Back.BLUE + board[line][row] + Back.RESET, end=" | " if row != 2 else " ")
            else:
                print(Back.WHITE + " " + Back.RESET, end=" | " if row != 2 else " ")
        if line!=2:
            print("\n---------")
        else:
            print("\n")

def ask_player():
    player = input("Введите игрока 'х или 0': ")
    if player == "х":
        player = "x"
    return player

def ask_and_make_move(player, board):
        while True:
            line, row = ask_move(player,board)
            if make_move(player,board, line, row):
                break

def ask_move(player, board):
    while True:
        try:
            line, row = input("Введите координаты хода через пробел: ").strip().split()
            line, row = int(line)-1, int(row) - 1
            if (0 <= int(line) <= 2) and (0 <= int(row) <= 2):
                return line, row
            else:
                print("Координаты должны быть от 1 до 3!")
        except(ValueError):
            print("Неверный формат координат!")

def make_move(player,board, line,row):
    if board[line][row] == " ":
        board[line][row] = player
        return True
    else:
        print("Это место уже занято. Повторите попытку:")
        return False

def check_win(player, board):
    for count in range(0,3):
        if board[count][0] == player and board[count][1] == player and board[count][2] == player:
            return True
        if board[0][count] == player and board[1][count]==player and board[2][count] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1]==player and board[2][0] == player:
        return True
    return False
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = ask_player()
    winner = False
    for count in range(9):
        ask_and_make_move(player,board)
        draw_board(board)
        if check_win(player, board):
            print(f'Победитель: {player}')
            winner = True
            break;
        else:
            player = "x" if player == "0" else "0"
    if not winner:
        print("Ничья")
def ask():
    answer = input("Хотите сыграть? да/нет\n").lower()
    if answer == "да":
        return True
    else:
        return False

while ask():
    tic_tac_toe()

#координаты:
#  11 | 12 | 13
#  ------------
#  21 | 22 | 23
#  -------------
#  31 | 32 | 33
#а еще я пытаюсь заново овладеть Gitом?