def motif(m, t):
    '''Renvoie la liste des positions des occurrences
    du motif m dans le texte t'''
    n, p = len(t), len(m)
    occ = []
    for i in range(n-p+1):
        if t[i:i+p] == m:
            occ.append(i)
    return occ

assert motif("ab", "") == []
assert motif("ab", "cdcdcdcd") == []
assert motif("ab", "abracadabra") == [0, 7]
assert motif("ab", "abracadabraab") == [0, 7, 11]


def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc


assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0) == [0, 1, 2, 3]
assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4) == [4, 5]