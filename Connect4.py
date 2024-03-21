""" Connect 4 Game """

RED = '\033[91m' # RED
YELLOW = '\033[93m' # YELLOW
BLUE = '\033[94m'  # BLUE
RESET = '\033[0m' # RESET COLOR

def p1_make_move(column):
    row = 5
    while True:
        if current_board[row][column] == (RED + u'\u2B24' + RESET) or current_board[row][column] == (YELLOW + u'\u2B24' + RESET):
            row -= 1
        else:
            current_board[row][column] = RED + u'\u2B24' + RESET
            return False


def p2_make_move(column):
    row = 5
    while True:
        if current_board[row][column] == (RED + u'\u2B24' + RESET) or current_board[row][column] == (YELLOW + u'\u2B24' + RESET):
            row -= 1
        else:
            current_board[row][column] = YELLOW + u'\u2B24' + RESET
            return False


def draw_board(board):
    for row in range(12):
        if row % 2 == 0:
            enter_row = int(row / 2)
            for column in range(1, 16):
                if column % 2 == 0:
                    enter_column = int(column / 2 - 1)
                    if column != 15:
                        print(board[enter_row][enter_column], end='')
                    else:
                        print(board[enter_row][enter_column])
                elif column == 15:
                    try:
                        print(int(BLUE + '|' + RESET))
                    except Exception as e:
                        error = e
                    finally:
                        print(BLUE + '|' + RESET)
                else:
                    print(BLUE + '|' + RESET, end='')
        else:
            print(BLUE + '---------------' + RESET)
    print()


player_turn = 'Player 1\'s Turn'
current_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
draw_board(current_board)
while True:
    print(player_turn)
    move_column = int(input('Please enter the column: '))
    print('')
    if player_turn == 'Player 1\'s Turn':
        p1_make_move(move_column)
        player_turn = 'Player 2\'s Turn'
    else:
        p2_make_move(move_column)
        player_turn = 'Player 1\'s Turn'
    draw_board(current_board)