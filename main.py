# ****************************************************** #
#  Project Title:    TIC TAC TOE                         #
#  App Version:      Alpha 0.01                          #
#  Coder:            Jim "Kodegero" Arriesgado           #
#  Project Started:  November 9, 2020                    #
#  Update Finished:  November 9, 2020                    #
# ****************************************************** #

# ========================================>>>>>>>>
# == INITIALIZE VARIABLES & FUNCTIONS ====>>>>>>>>
# ========================================>>>>>>>>

player_odd = ''
player_even = ''
board_piece = {'1': '-', '2': '-', '3': '-', '4': '-', '5': '-', '6': '-', '7': '-', '8': '-', '9': '-'}
game_over = False

# Choose player piece
player1_piece = input("Pick piece for player 1 (O or X): ")
if player1_piece.upper() == 'O':
    piece_assign = {'player1_piece': 'O', 'player2_piece': 'X'}
    player_odd = "Player 1"
    player_even = "Player 2"
elif player1_piece.upper() == 'X':
    piece_assign = {'player1_piece': 'X', 'player2_piece': 'O'}
    player_even = "Player 1"
    player_odd = "Player 2"

# ========================================>>>>>>>>
# == GAME LOOP ===========================>>>>>>>>
# ========================================>>>>>>>>

for turn in range(1, 10):
    print(f'''
        =================
        || {board_piece['1']} || {board_piece['2']} || {board_piece['3']} ||
        =================
        || {board_piece['4']} || {board_piece['5']} || {board_piece['6']} ||
        =================
        || {board_piece['7']} || {board_piece['8']} || {board_piece['9']} ||
        =================
        ''')
    active_piece = ''
    piece_position = ''
    correct_position = False

    while not correct_position:
        if turn % 2 != 0:
            active_piece = 'O'
            piece_position = input(f"{player_odd} please choose a position in the board: ")
        elif turn % 2 == 0:
            active_piece = 'X'
            piece_position = input(f"{player_even} please choose a position in the board: ")
        if board_piece[piece_position] == '-':
            board_piece[piece_position] = active_piece
            correct_position = True
        else:
            print("That position is already taken")

print(f'''
        =================
        || {board_piece['1']} || {board_piece['2']} || {board_piece['3']} ||
        =================
        || {board_piece['4']} || {board_piece['5']} || {board_piece['6']} ||
        =================
        || {board_piece['7']} || {board_piece['8']} || {board_piece['9']} ||
        =================
''')
