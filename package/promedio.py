def calcular(lst):
    res = 0
    for i in range(len(lst)):
        res += lst[i]

    return res / len(lst)