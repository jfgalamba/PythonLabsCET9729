"""
- Exercício: script (calculos1.py) que pede número (float) ao utilizador e 
  que exibe:
    . dobro
    . triplo
    . quadrado
    . cubo
    . resultado de 2.5 * x + 10, onde x é o número pedido ao utilizador

v2: docstring e testar c/ 10.3 incorporar decimal
"""

from decimal import Decimal as dec

num = dec(input("Introduza um número: "))

print("Dobro     :", 2 * num)
print("Triplo    :", 3 * num)
print("Quadrado  :", num ** 2)
print("Cubo      :", num ** 3)
print("2.5x + 10 :", dec('2.5') * num + 10)
