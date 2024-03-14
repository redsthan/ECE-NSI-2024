from random import randint
from collections import Counter

def lancer(n):
    return [randint(1, 6) for _ in range(n)]

def paire_6(tab):
    return tab.count(6) >= 2

lancer1 = [5, 6, 6, 2, 2]
lancer2 = [6,5,1,6,6]
lancer3 = [2, 2, 6]
assert paire_6(lancer2)
assert not paire_6(lancer3)
lancer4 = lancer(0)
assert lancer4 == []
assert not paire_6(lancer4)

def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j]
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil: 
                nouvelle_image[i][j] = 0
            else:
                nouvelle_image[i][j] = 1 
    return nouvelle_image

img=[[20, 34, 254, 145, 6], 
     [23, 124, 237, 225, 69],
     [197, 174, 207, 25, 87], 
     [255, 0, 24, 197, 189]]
assert nombre_lignes(img) == 4
assert nombre_colonnes(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img, 120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]