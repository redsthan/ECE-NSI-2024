def ecriture_binaire_entier_positif(n):
    '''Renvoie l'écriture binaire de l'entier positif n.'''
    if n == 0:
        return '0'
    else:
        resultat = ''
        while n > 0:
            resultat = str(n % 2) + resultat
            n = n // 2
        return resultat

def test_ecriture_binaire_entier_positif():
    assert ecriture_binaire_entier_positif(0) == '0'
    assert ecriture_binaire_entier_positif(2) == '10'
    assert ecriture_binaire_entier_positif(105) == '1101001'

test_ecriture_binaire_entier_positif()

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n-1, 0, -1): 
        for j in range(i): 
            if tab[j] > tab[j+1]: 
                echange(tab, j, j+1) 
                


tab = []
tri_bulles(tab)
assert tab == []

tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
assert tab2 == [1, 2, 3, 3, 6, 7, 9]

tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
assert tab3 == [3, 4, 7, 9]
