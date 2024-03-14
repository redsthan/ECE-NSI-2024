def max_dico(dico):
    return max(dico.items(), key=lambda x: x[1])

assert max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 })==('Ada', 201)
assert max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 })==('Alan', 222)

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab: 
        if element != '+' and element != '*': 
            p.empiler(element) 
        else:
            if element == '+': 
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat) 
    return p.depiler()

assert eval_expression([2, 3, '+', 5, '*'])==25
assert eval_expression([1, 2, '+', 3, '*'])==9
assert eval_expression([1, 2, 3, '+', '*'])==5
