from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025


def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = [] 

    for i in range(len(notes)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)


assert eleves_du_mois(['a','b','c','d','e','f','g','h','i','j'], [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]) == (80, ['c', 'f', 'h'])
assert eleves_du_mois([], []) == (0, [])