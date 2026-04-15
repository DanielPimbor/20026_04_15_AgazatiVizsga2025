urhajosok = []
with open('Python/3_feladat/urhajos.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        urhajos = {'nev': adatok[0], 'orszag': adatok[1], 'nem': adatok[2], 'szulev': adatok[3], 'urido': adatok[4]}
        urhajosok.append(urhajos)

print(f'{urhajosok=}')

