import random


# display the game board
def display_board(board):
    for index, symbol in enumerate(board):
        if index % 3 == 0 and index != 0:
            # decide when to start a new line
            print('\n-----------------------------')
        # print whitespace if the symbol is '$'
        # otherwise print out the corresponding symbols
        if symbol == '$':
            print(' '*4, end="")
        else:
            print(f'{symbol:4}', end="")
        # display the corresponding index
        print(f'({index})', end="")
        # add a border to different indexes
        if(index + 1) % 3 != 0:
            print('|  ', end="")
    print()


# let user choose the symbol X or O
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Please choose your symbol (X or O) : ').upper()
        print(f'marker is: {marker}')
    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# place the symbol on board to the given index
def place_marker(board, index, symbol):
    board[index] = symbol


# check the board winning condition
def win_check(board, symbol):
    return ((board[0] == symbol and board[1] == symbol and board[2] == symbol) or # first row
    (board[3] == symbol and board[4] == symbol and board[5] == symbol) or # second row
    (board[6] == symbol and board[7] == symbol and board[8] == symbol) or # third row
    (board[0] == symbol and board[3] == symbol and board[6] == symbol) or # first col
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or # second col
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or # third col
    (board[0] == symbol and board[4] == symbol and board[8] == symbol) or # left diagonal
    (board[2] == symbol and board[4] == symbol and board[6] == symbol))   # right diagonal


# use random to decide which player go first
def choose_first():
    turn = random.randrange(2)
    if turn == 0:
        return 'player1'
    return 'player2'


# check if the given index is empty
def space_check(board, index):
    return board[index] == '$'


# check if the board is full
def full_board_check(board):
    return not ('$' in board)


# ask for user's next move
# will loop continuously if received invalid input
def player_choice(board):
    position = int(input('Please choose your next move: '))
    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, position):
        position = int(input('Please choose your next move: '))
    return position


# ask if user want to replay the game
def replay():
    return input('Restart? Yes or No ').lower().startswith('y')


while True:
    print("********Tic Tac Toe Game********")
    board = list('$'*9)
    player1, player2 = player_input()
    turn = choose_first()  # decide which player goes first
    print(f'{turn} goes first')
    game = True
    while game:
        display_board(board) # display board info at the beginning of every turn

        # Player 1's turn
        if turn == 'player1':
            place_marker(board, player_choice(board), player1)

            # Check the game condition
            if win_check(board, player1):
                game = False
                display_board(board)
                print(f'{turn} wins')

            elif full_board_check(board):
                game = False
                display_board(board)
                print('Its a draw')
            turn = 'player2'

        # Player 2's turn
        else:
            place_marker(board, player_choice(board), player2)
            if win_check(board, player2):
                game = False
                display_board(board)
                print(f'{turn} wins')

            elif full_board_check(board):
                game = False
                display_board(board)
                print('Its a draw')
            turn = 'player1'

    # End program if do not replay
    if not replay():
        break
