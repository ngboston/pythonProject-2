def meanF(*args):
    s = 0
    k = 0
    for i in args:
        s+=i
        k+=1
    res = round(s/k, 2)
    return res

def printinfo(*clients):
    for i in range(len(clients)