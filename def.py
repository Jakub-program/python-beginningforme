from random import randrange, uniform
def napis_hlasku( nazev, skore):
    """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

    print( nazev, 'skóre je', skore)

    if skore > 900:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')

napis_hlasku('Tvoje', skore = randrange(0, 5000))
napis_hlasku('Protivníkovo', skore = randrange(0, 5000))
