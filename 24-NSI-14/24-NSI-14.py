def min_et_max(tab):
    """ Renvoie le minimum et le maximum d'un tableau de nombres. """
    min = tab[0]
    max = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < min:
            min = tab[i]
        if tab[i] > max:
            max = tab[i]
    return {'min': min, 'max': max}

def test_min_et_max():
    """ Fonction de test pour la fonction min_et_max. """
    assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
    assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
    assert min_et_max([3]) == {'min': 3, 'max': 3}
    assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}
    assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}

test_min_et_max()

class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        self.contenu = []
        for couleur in range(1, 5):
            for valeur in range(1, 14):
                self.contenu.append(Carte(couleur, valeur))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        assert 0 <= pos < 52, "Position invalide"
        return self.contenu[pos]

def test_Paquet_de_cartes():
    jeu = Paquet_de_cartes()
    carte1 = jeu.recuperer_carte(20)
    assert carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur() == "8 de coeur"
    carte2 = jeu.recuperer_carte(0)
    assert carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur() == "As de pique"
    try:
        carte3 = jeu.recuperer_carte(52)
        assert False, "AssertionError: paramètre pos invalide"
    except AssertionError as e:
        assert str(e) == "Position invalide"

test_Paquet_de_cartes()
