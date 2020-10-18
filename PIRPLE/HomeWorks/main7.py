"""
Below you can find song/album attibutes:
"""
songDictionary = {
    'SingerFirstName':'Fadel',
    'SingerLastName':'Shaker',
    'SongTitle':'Law 3ala albi',
    'AlbumTitle':'AlbumTitle',
    'ReleaseYear':'2002',
    'SongType':'Classic',
    'AlbumPrice':'12.4'
}

def guessSongAttribute(key, value):
    #Get all dicionary keys as a list
    # keysList = list(songDictionary)
    # if key in keysList:
    if value == songDictionary[key]:
        return True
    return False

print('Current Song Attributes Are: ')
for key in songDictionary:
    # print(key, ': ', songDictionary[key])
    print(key)
print()

guessedAttributeKey = input('Please choose one of the above attibutes for song guess game: ')
guessedAttributeValue = input('Please enter the value of the song attibute guess game: ')

#Get all dicionary keys as a list
keysList = list(songDictionary)

if guessedAttributeKey in keysList:
    didHeGetitRight = guessSongAttribute(guessedAttributeKey, guessedAttributeValue)
    if didHeGetitRight:
        print('Success, You\'re right, Congrats!')
    else:
        print('Error, Get better and come back!')
else:
    print('Error, You entered invalid attribute name.')