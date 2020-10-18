##Files handling order
# myFileHandler = open('countries.txt', 'w')
# myFileHandler.write(str(MyVisitedCountries))
# myFileHandler.read() OR myFileHandler.readLine()
# myFileHandler.close()

MyVisitedCountries = ['SAU', 'ARE', 'JOR', 'EGY']

##Wrtiting to a file
myFileHandler = open('countries.txt', 'w')
# myFileHandler.write(str(MyVisitedCountries))
for county in MyVisitedCountries:
    myFileHandler.write(county + '\n')
myFileHandler.close()

myFileHandler = open('countries.txt', 'a')
myFileHandler.write('SYR')
myFileHandler.close()

# ##Reading from file
# myFileHandler = open('countries.txt', 'r')
# print(myFileHandler.read())
# myFileHandler.close()

##No need to close the file when using the with key word.
with open('countries.txt', 'r') as countriesFile:
    for line in countriesFile:
        print(line)