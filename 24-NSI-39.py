def recherche(elt, tab):
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == elt:
            return i
        
assert recherche(1, [2, 3, 4]) is None
assert recherche(1, [10, 12, 1, 56])==2
assert recherche(1, [1, 0, 42, 7])==0
assert recherche(1, [1, 50, 1])==2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8])==5


class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = ['192.168.0.0', '192.168.0.255'] 
        return self.adresse in reservees

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()
        if octets[-1] == 254: 
            return None
        octet_nouveau = octets[-1] + 1
        return AdresseIP('192.168.0.' + str(octet_nouveau)) 
    
adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')

assert adresse1.liste_octets() == [192, 168, 0, 1]
assert not adresse1.est_reservee()
assert adresse3.est_reservee()
assert adresse2.adresse_suivante().adresse == '192.168.0.3'

