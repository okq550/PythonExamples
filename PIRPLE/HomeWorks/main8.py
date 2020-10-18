import os

def readFile(fileName):
    #Print the content of the passed file
    print('** Operation Read For File', fileName , '**')
    myFileHandler = open(fileName, 'r')
    print(myFileHandler.read())
    myFileHandler.close()
    return True
    
def appendToFile(fileName):
    #Append content to the passed file
    print('** Operation Append To File', fileName , '**')
    content = input('Please enter the content to be appended to file ' + fileName + ': ')
    myFileHandler = open(fileName, 'a')
    myFileHandler.write(content + '\n')
    myFileHandler.close()
    return True

def replaceFile(fileName):
    #Empty the file to start over again
    print('** Operation Replace File', fileName, 'file content has been dumped, You can start over again! **')
    myFileHandler = open(fileName, 'w')
    myFileHandler.write('')
    myFileHandler.close()
    return True

def replaceSingleLineInFile(fileName):
    print('** Operation Replace Single Line In File', fileName , '**')
    lineNumber = 1
    filesLinesAsList = []
    with open(fileName, 'r') as currentFile:
        for line in currentFile:
            print(lineNumber, end=' ')
            print(line)
            filesLinesAsList.append(line.strip())
            lineNumber += 1
    
    #Ask the user for line number and the content then replace it in the passed file
    editlineNumber = int(input('Please enter the line number you want to edit: '))
    if editlineNumber > len(filesLinesAsList) or editlineNumber <= 0:
        print('Error, Invalid line number.')
        
    newContent = input('Please enter the content for line number ' + str(editlineNumber) + ':')
    filesLinesAsList[editlineNumber-1] = newContent
    
    myFileHandler = open(fileName, 'w')
    myFileHandler.write('\n'.join(filesLinesAsList))
    myFileHandler.close()
    
    return True

userFileName = input('Please enter file name: ')

if not os.path.isfile(userFileName):
    fileContent = input('Please enter file content: ')
    myFileHandler = open(userFileName, 'w')
    myFileHandler.write(fileContent)
    myFileHandler.close()
else:
    print('File ', userFileName, ' already exists.')
    operationMode = input('Please enter the operation you want to make on the file (read = 1, append = 2, replace = 3, edit single line = 4): ')
    
    if operationMode == '1':
        readFile(userFileName)
    elif operationMode == '2':
        appendToFile(userFileName)
    elif operationMode == '3':
        replaceFile(userFileName)
    elif operationMode == '4':
        replaceSingleLineInFile(userFileName)
    else:
        print("Error, operation mode is not supported.")