import os

#Get terminal width and height
(width, height) = os.popen('stty size', 'r').read().split()

def drawSquare(numOfRow, numOfCol):
    #Convert screen dimension values to int for comparisons
    if numOfRow > int(width) or numOfCol > int(height):
        return False

    #Draw the board
    for row in range(numOfRow):
        if row % 2 == 0:
            for x in range(numOfCol):
                print(' ', end='')
                print('| ', end='')
        else:
            print('-' * numOfRow * 3, end='')
        print('')
    return True

drawSquare(10, 10)