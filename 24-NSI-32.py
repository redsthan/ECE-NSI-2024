def ou_exclusif(tab1, tab2):
    '''tab1 et tab2 sont des listes de même longueur'''
    assert len(tab1) == len(tab2), "Les deux listes doivent être de même longueur"
    res = []
    for i in range(len(tab1)):
        res.append(tab1[i] ^ tab2[i])
    return res

assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]

class Carre:
    def __init__(self, liste, n): 
        self.ordre = n        
        self.tableau = [[liste[i + j * n] for i in range(n)] 
                        for j in range(n)] 
                                   
    def affiche(self):        
        '''Affiche un carré''' 
        for i in range(self.ordre): 
            print(self.tableau[i]) 
                                   
    def somme_ligne(self, i): 
        '''Calcule la somme des valeurs de la ligne i''' 
        somme = 0             
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0) 
        #test de la somme de chaque ligne 
        for i in range(1, self.ordre): 
            if self.somme_ligne(i) != s: 
                return False
                                   
        #test de la somme de chaque colonne 
        for j in range(self.ordre): 
            if self.somme_col(j) != s: 
                return False
                                   
        return True
    
lst_c2 = [1, 7, 7, 1]
c2 = Carre(lst_c2, 2)
lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)
lst_c3bis = [2, 9, 4, 7, 0, 3, 6, 1, 8]
c3bis = Carre(lst_c3bis, 3)
assert c2.est_semimagique()
assert c3.est_semimagique()
assert not c3bis.est_semimagique()


