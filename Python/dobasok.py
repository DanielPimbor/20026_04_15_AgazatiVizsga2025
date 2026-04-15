import random

#HATÁROKAT IS BELEÉRTVE TEHÁT 8 és 4 is

def kozte(a,b,c):
    if a <= b and a >= c or a <= c and a >= b:
        return True
    else:
        return False
    

dobasok = []

for i in range(150):
    dobas = random.randint(1, 12)
    dobasok.append(dobas)

nyolc_es_negy_koze_esett_dobasok_szama = 0

print(dobasok)

for dobas in dobasok:
    if kozte(dobas,4,8) == True:
        nyolc_es_negy_koze_esett_dobasok_szama += 1

print(f'A 150 dobásból {nyolc_es_negy_koze_esett_dobasok_szama} esett 4 és 8 közé.')
print(f'Ez az összes dobás {round(((nyolc_es_negy_koze_esett_dobasok_szama / 150) * 100), 2)}%-a.')
