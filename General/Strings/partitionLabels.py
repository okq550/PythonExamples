def partitionLabels(S: str):
    lastIndecies = {c: i for i, c in enumerate(S)}
    # {'a': 8, 'b': 5, 'c': 7,       'd': 14, 'e': 15, 'f': 11, 'g': 13,     'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
    # print(lastIndecies)

    partitions = []
    i = 0
    j = anchor = 0
    
    for i, c in enumerate(S):
        j = max(j, lastIndecies[c])
        if i == j:
            partitions.append(i - anchor + 1)
            anchor = i + 1

    return partitions

string = 'ababcbacadefegdehijhklij'
#output = "ababcbaca", "defegde", "hijhklij"

output = partitionLabels(string)
print(output)
