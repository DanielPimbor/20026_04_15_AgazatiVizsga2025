"""Vendégenként 3 tojás, 10% al tobbet vesznek mindig (torottek mniatt),"""

#MATH:CEIL A KEREKITESES CUCC
import math


vendegek_szama = input('Add meg a vendégek számát!')
raktarban_tojasok_szama = input('Add meg a raktárban lévő tojások számát!')
szukseges_tojasok_szama = math.ceil(((int(vendegek_szama) * 3) * 1.1))
vasarolni_szukseges_tojasok_szama = int(szukseges_tojasok_szama) - int(raktarban_tojasok_szama)

print(f'Vendégek száma:{vendegek_szama}')
print(f'Raktáron lévő tojások: {raktarban_tojasok_szama}')
print(f'Ennyi vendéghez {round(szukseges_tojasok_szama)} tojásra van szükség.')
if int(raktarban_tojasok_szama) >= int(szukseges_tojasok_szama):
    print(f'Nem kell több tojást vásárolni.')
else:
    print(f'Kell még {vasarolni_szukseges_tojasok_szama} tojást vásárolni.')
