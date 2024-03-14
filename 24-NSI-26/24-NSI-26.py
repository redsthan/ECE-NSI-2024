from random import randint

def ajoute_dictionnaires(d1, d2):
    '''Ajoute deux dictionnaires d1 et d2 et renvoie le résultat.'''
    resultat = {}
    for cle in d1:
        resultat[cle] = d1[cle]
    for cle in d2:
        if cle in resultat:
            resultat[cle] += d2[cle]
        else:
            resultat[cle] = d2[cle]
    return resultat

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}


def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0
    while nombre_cases_vues < 12: 
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if not cases_vues[case_en_cours]: 
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues + 1
        n = n + 1
    return n
