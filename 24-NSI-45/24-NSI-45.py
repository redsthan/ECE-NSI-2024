pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def compte_occurrences(x, tab):
    nb_occurrences = 0
    for elem in tab:
        if elem == x:
            nb_occurrences = nb_occurrences + 1
    return nb_occurrences

assert compte_occurrences(5, [])==0
assert compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4])==1
assert compte_occurrences('a', ['a','b','c','a','d','e','a'])==3

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i]) 
        a_rendre = a_rendre - pieces[i] 
    return rendu

assert rendu_monnaie(700, 700)==[]
assert rendu_monnaie(102, 500)==[200, 100, 50, 20, 20, 5, 2, 1]


