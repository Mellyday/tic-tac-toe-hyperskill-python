def print_board(board):
    print("---------")
    for row in board:
        print("|", row[0], row[1], row[2], "|")
    print("---------")


def game_is_impossible(board):
    # It's impossible that the difference between the number of Xs and Os on the board is more than one.
    X_count, O_count = (0, 0)
    for row in board:
        for cell in row:
            if cell == "X":
                X_count += 1
            if cell == "O":
                O_count += 1
    if abs(X_count - O_count) > 1:
        return True

    # It's impossible that there are two winners on the board.
    if X_win(board) and O_win(board):
        return True

    return False


def game_is_unfinished(board):
    if X_win(board) or O_win(board):
        return False

    if game_is_impossible(board):
        return False

    for row in board:
        if '_' in row:
            return True

    return False


def game_is_drawn(board):
    if X_win(board) or O_win(board):
        return False

    if game_is_impossible(board):
        return False

    if game_is_unfinished(board):
        return False

    return True


def X_win(board):
    if all_X_row_exist(board):
        return True
    if all_X_column_exist(board):
        return True
    if all_X_diagonal_exist(board):
        return True

    return False


def O_win(board):
    if all_O_row_exist(board):
        return True
    if all_O_column_exist(board):
        return True
    if all_O_diagonal_exist(board):
        return True

    return False


def all_X_row_exist(board):
    for row in board:
        result = set(row)
        if len(result) == 1 and "X" in result:
            return True
    return False


def all_X_column_exist(board):
    # we loop three times because the board is 3x3
    for y in range(3):
        temp = []
        for x in range(3):
            temp.append(board[x][y])
        result = set(temp)
        if len(result) == 1 and "X" in result:
            return True
    return False


def all_X_diagonal_exist(board):
    first_diagonal = set()
    first_diagonal.update(board[0][0], board[1][1], board[2][2])
    second_diagonal = set()
    second_diagonal.update(board[0][2], board[1][1], board[2][0])
    if len(first_diagonal) == 1 and "X" in first_diagonal:
        return True
    if len(second_diagonal) == 1 and "X" in second_diagonal:
        return True
    return False


def all_O_row_exist(board):
    for row in board:
        result = set(row)
        if len(result) == 1 and "O" in result:
            return True
    return False


def all_O_column_exist(board):
    # we loop three times because the board is 3x3
    for y in range(3):
        temp = []
        for x in range(3):
            temp.append(board[x][y])
        result = set(temp)
        if len(result) == 1 and "O" in result:
            return True
    return False


def all_O_diagonal_exist(board):
    first_diagonal = set()
    first_diagonal.update(board[0][0], board[1][1], board[2][2])
    second_diagonal = set()
    second_diagonal.update(board[0][2], board[1][1], board[2][0])
    if len(first_diagonal) == 1 and "O" in first_diagonal:
        return True
    if len(second_diagonal) == 1 and "O" in second_diagonal:
        return True
    return False


print("Enter cells: ")
symbols = input()
row_one = ['_', '_', '_']
row_two = ['_', '_', '_']
row_three = ['_', '_', '_']
symbols = list(symbols)
row_one = symbols[0:3]
row_two = symbols[3:6]
row_three = symbols[6:9]
game_board = [row_one, row_two, row_three]
print_board(game_board)

if X_win(game_board):
    print("X wins")
if O_win(game_board):
    print("O wins")
if game_is_impossible(game_board):
    print("Impossible")
if game_is_unfinished(game_board):
    print("Game not finished")
if game_is_drawn(game_board):
    print("Draw")
