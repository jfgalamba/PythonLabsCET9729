"""

for ELEM in COLECÇÃO/ITERÁVEL:
    INST1
    INST2
    ...
    INST_N

ELEM é uma variável

"""

# 1o EXEMPLO: Ciclo de contagem (gama de valores)
print("1o EXEMPLO: Ciclo de contagem (gama de valores)")

soma = 0
for i in range(1, 5001):
    soma += i

print(f"Soma: {soma:}")
print(f"Último valor de i: {i}")

# 2o EXEMPLO: Percorrer os elementos de uma estrutura de dados (string)
print("2o EXEMPLO: Percorrer os elementos de uma estrutura de dados (string)")
nome = 'ALBERTINA'

for letra in nome:
    print(letra)

print('-----------')

for i, letra in enumerate(nome):
    print(f"{i} -> {letra}")

print('-----------')

for letra in reversed(nome):
    print(letra)

# 3o EXEMPLO: Percorrer os elementos de uma estrutura de dados (lista)
print("3o EXEMPLO: Percorrer os elementos de uma estrutura de dados (lista)")
vals = [10, -50, 40, -29]

soma = 0
for val in vals:
    soma += val

print(f"Soma dos valores: {soma}")

# 4o EXEMPLO: Dicionários
print("4o EXEMPLO: Dicionários")
idades = {'alberto': 23, 'ana': 55, 'armando': 19, 'arnaldo': 47}

for nome in idades:
    print(nome)

for nome in idades:
    print(idades[nome])

for idade in idades.values():
    print(idade)

for nome, idade in idades.items():
    print(nome, idade)

# for key, value in my_dict.items():
#     print(key, value)

# x, y, *_ = 'ABCDEF'