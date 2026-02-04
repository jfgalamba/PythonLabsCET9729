"""
- Exercício: script (calculos1.py) que pede número (float) ao utilizador e 
  que exibe:
    . dobro
    . triplo
    . quadrado
    . cubo
    . resultado de 2.5 * x + 10, onde x é o número pedido ao utilizador

v3: f-strings (9 espaços + 3 casas decimais)
"""

from decimal import Decimal as dec

num = dec(input("Introduza um número: "))

print(f"Dobro     : {2 * num:9.3f}")
print(f"Triplo    : {3 * num:9.3f}")
print(f"Quadrado  : {num ** 2:9.3f}")
print(f"Cubo      : {num ** 3:9.3f}")
print(f"2.5x + 10 : {dec('2.5') * num + 10:9.3f}")
