def print_board(string):
    print('---------')
    print('|', string[0], string[1], string[2], '|')
    print('|', string[3], string[4], string[5], '|')
    print('|', string[6], string[7], string[8], '|')
    print('---------')


def translate_coordinate(coord_x, coord_y):
    """
    Convert user readable coordinates (eg. x = 3, y = 1) to index that our data structure use (in this example x of 3 and y of 1 translate to index of 2)
    """
    return coord_y * 3 + coord_x - 4


def check_game_state(string):
    row_list = [[item for item in game_board[i:i + 3]] for i in range(0, 7, 3)]
    col_list = [[item[i] for item in row_list] for i in range(3)]
    main_diagonal = [[row_list[i][i] for i in range(3)]]
    secondary_diagonal = [[row_list[i][2 - i] for i in range(3)]]
    game_matrix = row_list + col_list + main_diagonal + secondary_diagonal

    X_wins = ['X', 'X', 'X']
    O_wins = ['O', 'O', 'O']
    X_count = game_board.count('X')
    O_count = game_board.count('O')

    if X_wins in game_matrix and O_wins in game_matrix:
        return 'Impossible'
    elif abs(X_count - O_count) > 1:
        return 'Impossible'
    elif X_wins in game_matrix:
        return 'X wins'
    elif O_wins in game_matrix:
        return 'O wins'
    elif '_' not in string:
        return 'Draw'
    else:
        return 'Game not finished'


game_board = '_________'
print_board(game_board)

turn = 'X'
while True:
    coord = input("Enter the coordinates: ")

    if len(coord.split(" ")) != 2:
        print("Coordinate should be two number separated by a space")
        continue

    coord_y, coord_x = coord.split(" ")

    if not coord_x.isnumeric() or not coord_y.isnumeric():
        print("You should enter numbers!")
        continue

    coord_x, coord_y = (int(coord_x), int(coord_y))

    if coord_x < 1 or coord_x > 3 or coord_y < 1 or coord_y > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    coord = translate_coordinate(coord_x, coord_y)

    if game_board[coord] != '_':
        print("This cell is occupied! Choose another one!")
        continue

    game_board = list(game_board)
    game_board[coord] = turn
    game_board = ''.join(game_board)
    print_board(game_board)

    # Check for victory, this code block should be the only code block that break the loop. Don't insert code breaking the loop anywhere else!
    game_state = check_game_state(game_board)
    if game_state == 'X wins':
        print('X wins')
        break
    elif game_state == 'O wins':
        print('O wins')
        break
    elif game_state == 'Draw':
        print('Draw')
        break

    # switch to the next player
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    else:
        print(
            f"Error: Invalid state. Turn should always be either 'X' or 'O' but is {turn} instead")
