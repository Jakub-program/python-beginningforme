x = 0

def nastav_x(hodnota):
    x = hodnota  # Přiřazení do lokální proměnné!
    print('Ve funkci nastav_x: x =', x)

nastav_x(40)
print('Venku: x =', x)