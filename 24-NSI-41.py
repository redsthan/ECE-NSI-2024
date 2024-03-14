class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit
        
a = Noeud(1, Noeud(4, None, None),
             Noeud(0, None,
                      Noeud(7, None, None)))

def taille(a):
    if a is None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a is None:
        return -1
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))

assert hauteur(a) == 2
assert taille(a) == 4
assert hauteur(None) == -1
assert taille(None) == 0
assert hauteur(Noeud(1, None, None)) == 0
assert taille(Noeud(1, None, None)) == 1


def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]
    return tab_ins


assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(0, 4, [7, 8, 9]) == [4, 7, 8, 9]