a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

def taille(arbre, lettre):
    if not lettre:
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

assert(taille(a, 'F') == 9)
assert(taille(a, 'B') == 5)
assert(taille(a, 'I') == 2)


def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N-1): 
        imin = k
        for i in range(k, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin)
        
tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
assert(tab == [6, 12, 18, 21, 25, 41, 55])


