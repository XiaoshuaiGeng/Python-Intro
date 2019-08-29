def boardinit():
    '''
    Initialize a board
    INPUT: NONE
    OUTPUT: return a list contains 9 '$' elements
    '''
    return list('$'*9)

def printboard():
    pass

def isGameEnd():


print("********Tic Tac Toe Game********")
marker = input('Please choose your symbol (X or O) : ')
while marker != 'X' or marker != 'O':
    marker = input('Please choose your symbol (X or O) : ')

player1 = marker
if player1 == 'X':
    player1first = True
    player2 = 'O'
else:
    player2 = 'X'

while