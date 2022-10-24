def suma(lst):
    res = 0
    for i in range(len(lst)):
        res += lst[i]

    return res

def resta(lst):
    res = lst[0]
    for i in range(1, len(lst)):
        res -= lst[i]

    return res

def multiplicacion(lst):
    res = 1
    for i in range(len(lst)):
        res *= lst[i]

    return res

def division(lst):
    res = lst[0]
    for i in range(1, len(lst)):
        res /= lst[i]

    return res

def promedio(lst):
    res = 0
    for i in range(len(lst)):
        res += lst[i]

    return res / len(lst)



     