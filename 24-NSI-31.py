def multiplication(a, b):
    """
    a et b : deux entiers
    La fonction renvoie le produit de a par b
    """
    if b == 0:
        return 0
    if b > 0:
        return a + multiplication(a, b - 1)
    if b < 0:
        return -multiplication(a, -b)

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0    


def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False


assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
assert not dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
