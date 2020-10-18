#initializing the array id.
id = [x for x in range(10)]
sz = [0 for x in range(10)]

def getRoot(i):
    while i != id[i]:
        i = id[i]
    return i

def isConnected(p, q):
    if getRoot(id[p]) == getRoot(id[q]):
        return True
    return False

def connectNodes(p, q):
    i = getRoot(p)
    j = getRoot(q)
    if i == j:
        return
    
    if sz[i] < sz[j]:
        id[i] = j
        sz[j] += sz[i]
    else:
        id[j] = i
        sz[i] += sz[j]
    print(id)
    
p = int(input('Enter P:'))
q = int(input('Enter q:'))

while(p >= 0 and q >= 0):
    connectNodes(p, q)
    p = int(input('Enter P:'))
    q = int(input('Enter q:'))
