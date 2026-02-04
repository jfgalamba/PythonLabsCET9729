"""
Um grupo de pessoas participou num jantar em que todos encomendaram o 
menu turístico e pretende fazer um programa para calcular a conta. Para
tal, o programa deve começar por ler o número de pessoas envolvidas no
jantar e, de seguida, calcular o valor da conta. O menu custa 
15,00 € + IVA por pessoa. Assuma que o IVA é 23% e a gorjeta para o
empregado é de 10% sobre o montante total com IVA. O programa deve 
exibir a despesa total sem IVA e sem gorjeta, o montante de IVA, o valor
da gorjeta e a despesa total final.

Exemplo:

$ python jantar1.py
Número de comensais: 10

Despesa s/ IVA  : 150€
Montante IVA    : 34.5€
Despesa c/ IVA  : 184.5€
Gorjeta (10%)   : 18.45€

Despesa TOTAL   : 202.95€
"""

from decimal import Decimal as dec

PRECO_MENU = dec('15.0')   # em €
TAXA_IVA   = dec('23.0')   # em %
GORJETA    = dec('10.0')   # em %

num_pessoas = int(input("Número de comensais: "))

despesa_s_iva = num_pessoas * PRECO_MENU
montante_iva = despesa_s_iva * (TAXA_IVA / 100)
despesa_c_iva = despesa_s_iva + montante_iva
montante_gorjeta = despesa_c_iva * (GORJETA / 100)
despesa_total = despesa_c_iva + montante_gorjeta

print("Despesa s/ IVA  :", despesa_s_iva, "€")
print("Montante IVA    :", montante_iva, "€")
print("Despesa c/ IVA  :", despesa_c_iva, "€")
print("Gorjeta (10%)   :", montante_gorjeta, "€")
print()
print("Despesa TOTAL   :", despesa_total, "€")
