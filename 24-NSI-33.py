def renverse(chr):
    return chr[::-1]

assert renverse("") == ""
assert renverse("abc") == "cba"
assert renverse("informatique") == "euqitamrofni"

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = i * 2
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]


