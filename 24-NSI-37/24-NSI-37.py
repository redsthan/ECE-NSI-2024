def moyenne(tab):
    '''tab est un tableau d'entiers.
    La fonction renvoie la moyenne des valeurs contenues dans le tableau'''
    somme = 0
    assert len(tab) > 0
    for i in range(len(tab)):
        somme = somme + tab[i]
    return somme / len(tab)

assert moyenne([5, 3, 8]) == 5.333333333333333
assert moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5


def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j = len(tab)-1 # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = i+1 
        else:
            valeur = tab[j] 
            tab[j] = 1 
            tab[i] = valeur
            j = j - 1
    return tab

assert tri([0, 1, 0, 1, 0, 1, 0, 1, 0])== [0, 0, 0, 0, 0, 1, 1, 1, 1]
            



