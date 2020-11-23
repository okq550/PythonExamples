def flatten_dictionary(dictionary):
    flattenDictionary = {}
    flattenDictionaryHelper("", dictionary, flattenDictionary)
    return flattenDictionary


def flattenDictionaryHelper(initialKey, dictionary, flatDict):
    for key, value in dictionary.items():
        if type(value) == dict:
            if initialKey != '':
                flattenDictionaryHelper(initialKey + '.' + key, value, flatDict)
            else:
                flattenDictionaryHelper(key, value, flatDict)
        else:
            if initialKey != '':
                flatDict[initialKey + '.' + key] = value
            else:
                flatDict[key] = value
    
    return flatDict

myDic = {
    "Key1": "1", 
    "Key2": 
        {
            "a": "2", 
            "b": "3", 
            "c": 
                {
                    "d": "3", 
                    "e": "1"
                }
        }
}

output = flatten_dictionary(myDic)

print('output', output)
