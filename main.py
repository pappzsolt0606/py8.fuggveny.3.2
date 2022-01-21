'''
3.2 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!

Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! 
Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!
'''
def harommal_oszthatok():
    lista = []
    while True:
        be = int(input('adj egy szamot:'))
        if be < 0:
            break
        elif be % 3 == 0:
            lista.append(be)
    return f'a 3-al oszthato szamok osszege: {sum(lista)}, {len(lista)}'

print(harommal_oszthatok())