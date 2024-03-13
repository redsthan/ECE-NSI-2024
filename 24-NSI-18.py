def multiplication(n1, n2):
    '''Renvoie le produit de n1 par n2'''
    result = 0
    if n2 == 0:
        return 0
    if n2 < 0:
        for i in range(-n2):
            result -= n1
        return result
    for i in range(n2):
        result += n1
    return result

assert multiplication(2, 4) == 8
assert multiplication(0, 10) == 0
assert multiplication(5, -3) == -15
assert multiplication(-6, -2) == 12

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m+1, j) 
    elif tab[m] > x:
        return chercher(tab, x, i, m-1) 
    else:
        return m
    
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) is None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) is None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2


