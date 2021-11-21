def print_board(string):
    print('---------')
    print('|', string[0], string[1], string[2], '|')
    print('|', string[3], string[4], string[5], '|')
    print('|', string[6], string[7], string[8], '|')
    print('---------')


user_input = input('Enter: ')
print_board(user_input)

row_list = [[item for item in user_input[i:i + 3]] for i in range(0, 7, 3)]
col_list = [[item[i] for item in row_list] for i in range(3)]
main_diagonal = [[row_list[i][i] for i in range(3)]]
secondary_diagonal = [[row_list[i][2 - i] for i in range(3)]]
print(secondary_diagonal)

X_wins = ['X', 'X', 'X']
O_wins = ['O', 'O', 'O']
X_count = user_input.count('X')
O_count = user_input.count('O')

# if X_wins in game_matrix and O_wins in game_matrix:
#     print('Impossible')
# elif abs(X_count - O_count) > 1:
#     print('Impossible')
# elif X_wins in game_matrix:
#     print('X wins')
# elif O_wins in game_matrix:
#     print('O wins')
# elif '_' not in user_input:
#     print('Draw')
# else:
#     print('Game not finished')

# row_list = [[item for item in user_input[i:i + 3]] for i in range(0, 7, 3)]
# col_list = [[item[i] for item in row_list] for i in range(3)]
# main_diagonal = [[row_list[i][i] for i in range(3)]]
# secondary_diagonal = [[row_list[i][2 - i] for i in range(3)]]
# game_matrix = row_list + col_list + main_diagonal + secondary_diagonal
