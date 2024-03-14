def verifie(tab):
    return tab == sorted(tab)

assert verifie([0, 5, 8, 8, 9])
assert not verifie([8, 12, 4])
assert verifie([-1, 4])
assert verifie([])
assert verifie([5])



def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : 
            nmax = election[candidat]
    liste_finale = [ nom for nom in election if election[nom] == nmax] 
    return liste_finale


assert depouille([ 'A', 'B', 'A' ]) == {'A': 2, 'B': 1}
assert depouille([]) == {}
election = depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B'])
assert election == {'A': 3, 'B': 4, 'C': 3}
assert vainqueurs(election) == ['B']
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) == ['A', 'B']