# tic tac toe

def drawBoard(board):

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top=R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
