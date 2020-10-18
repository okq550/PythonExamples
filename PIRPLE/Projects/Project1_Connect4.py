import sys
from termcolor import colored, cprint

nodesToConnect = 4
rows = 6
columns = 7
player = 1
playerColor = ['blue', 'white']
playingMatrix = [[' ' for i in range(columns)] for j in range(rows)]

def checkIfAnyPlayerWins(rows, columns, playerColor, selectedColumn, availableMaxRow, playingMatrix):
    # print(playingMatrix[availableMaxRow][selectedColumn])
    print(rows, columns, playerColor, selectedColumn, availableMaxRow)
    is4NodesConnected = False
    #Check if player connected 4 nodes upwards:
    if rows - (availableMaxRow + 1) >= 3:
        #There is a possibility to connect 4 nodes updwards
        for i in range(1, 4):
            nextElement = playingMatrix[availableMaxRow + i][selectedColumn]
            if nextElement != playerColor:
                is4NodesConnected = False
                break
            else:
                is4NodesConnected = True
                
    
    # #Check if player connected 4 nodes downwards:
    # if (availableMaxRow + 1) + 3 <= rows:
    #     #There is a possibility to connect 4 nodes downwards
    #     break
    
    return is4NodesConnected

def drawBoard(rows, columns, playerColor, selectedColumn, playingMatrix):
    #Fill the playingMatrix
    availableMaxRow = rows - 1
    while availableMaxRow >= 0:
        if playingMatrix[availableMaxRow][selectedColumn] == ' ':
            playingMatrix[availableMaxRow][selectedColumn] = playerColor
            break
        else:
            availableMaxRow -= 1
    
    #Draw the board
    gameOverFlag = True
    for i in range(rows):
        print(' ', end='')
        print('-' * (columns * 3 + 1))
        for j in range(columns):
            if playingMatrix[i][j] != ' ':
                print(' |', end='')
                cprint(u'\u2B24', playingMatrix[i][j], end='') 
            else:
                gameOverFlag = False
                print(' |' + playingMatrix[i][j], end='')
        print(' |')
    print(' ', end='')
    print('-' * (columns * 3 + 1))
    
    #If the game is not ended, then check if someone won the game!
    if not gameOverFlag:
        return checkIfAnyPlayerWins(rows, columns, playerColor, selectedColumn, availableMaxRow, playingMatrix)
    
    return gameOverFlag

while True:
    print('Its player ' + str(player) + ' turn, Please enter your next move (column). values are from 0 to ' + str(columns - 1))
    currentPlayerColor = playerColor[player % 2]
    selectedColumn = int(input('Player ' + str(player) + ') column (' + currentPlayerColor + '):' ))
    if selectedColumn < 0 or selectedColumn > 6:
        print('Column value must be between 0 and ' + str(columns - 1))
    else:
        gameOverFlag = drawBoard(rows, columns, currentPlayerColor, selectedColumn, playingMatrix)
        if gameOverFlag:
            # print('Player ' + str(player) + ' win the game!')
            break
        else:
            if player % 2 == 0:
                player = 1
            else:
                player = 2

print('Game Over!')