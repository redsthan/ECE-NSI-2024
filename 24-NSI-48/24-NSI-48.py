def voisins_entrants(adj, sommet):
    '''Renvoie la liste des sommets voisins de sommet dans le graphe orienté adj'''
    return [s for s, a in enumerate(adj) if sommet in a]

assert voisins_entrants([[1, 2], [2], [0], [0]], 0)==[2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1)==[0]

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + str(chiffre) 
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + str(chiffre) 
    resultat += lecture_chiffre
    return resultat

assert nombre_suivant('1211')=='111221'
assert nombre_suivant('311')=='1321'


