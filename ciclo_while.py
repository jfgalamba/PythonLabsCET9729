"""
Ciclo WHILE

while CONDIÇÃO:
    INST1
    INST2
    ...
    INST_N
"""

# 1o EXEMPLO: Ciclo de contagem (gama de valores)
print("1o EXEMPLO: Ciclo de contagem (gama de valores)")

soma = 0
i = 1
while i <= 5000:      # mudar para 5 e fazer debugging
    soma += i
    i += 1

print(f"Soma: {soma:}")
print(f"Último valor de i: {i}")

# 2o EXEMPLO: Percorrer os elementos de uma estrutura de dados (string)
print("2o EXEMPLO: Percorrer os elementos de uma estrutura de dados (string)")
nome = 'ALBERTINA'

i = 0
while i < len(nome):
    print(nome[i])
    i += 1

print('-----------')

i = 0
while i < len(nome):
    print(f"{i} -> {nome[i]}")
    i += 1

print('-----------')

i = len(nome) - 1     # ou usar indíces negativos (-1, -2, etc.)
while i > -1:         # ou i >= 0 
    print(nome[i])
    i -= 1

"""
A
N
I
T
R
E
B
L
A
"""

# 3o EXEMPLO: Percorrer os elementos de uma estrutura de dados (lista)
print("3o EXEMPLO: Percorrer os elementos de uma estrutura de dados (lista)")
vals = [10, -50, 40, -29]

soma = 0
i = 0
while i < len(vals):
    soma += vals[i]
    i += 1

print(f"Soma dos valores: {soma}")

# 4o EXEMPLO: Ciclo de validação
print("4o EXEMPLO: Ciclo de validação")

idade_str = input("Qual a sua idade? ")
while not idade_str.isdigit():
    print("Idade inválida")
    idade_str = input("Qual a sua idade? ")

idade = int(idade_str)
print(f"Dobro da sua idade: {2 * idade}")

print("--------------------------")

while True:
    idade_str = input("Qual a sua idade? ")
    if idade_str.isdigit():
        break
    print("Idade inválida")

idade = int(idade_str)
print(f"Dobro da sua idade: {2 * idade}")

# 5o EXEMPLO: Menu de opções
print("5o EXEMPLO: Menu de opções")

opcao = ''
while opcao != 'T':
    # 1. Exibir o menu de opções
    print("1 - LEVANTAR")
    print("2 - DEPOSITAR")
    print("3 - CONSULTAR")
    print("T - TERMINAR")

    # 2. Ler a opção introduzida
    opcao = input("Opção: ")
    print()

    # 3. Analisar e executar a opção introduzida
    match opcao:
        case '1':
            print("Opção LEVANTAR escolhida")
        case '2':
            print("Opção DEPOSITAR escolhida")
        case '3':
            print("Opção CONSULTAR escolhida")
        case 'T':
            print("Fim do programa")
        case _:
            print(f"Opção <{opcao}> inválida!")

    # if opcao == '1':
    #     print("Opção LEVANTAR escolhida")
    # elif opcao == '2':
    #     print("Opção DEPOSITAR escolhida")
    # elif opcao == '3':
    #     print("Opção CONSULTAR escolhida")
    # elif opcao == 'T':
    #     print("Fim do programa")
    # else:
    #     print(f"Opção <{opcao}> inválida")

    print()

"""
while C:
    BLOCO_INSTS

while True:
    if not C:
        break
    BLOCO_INSTS

i = ???
while i != 0:
    print(i)
    x = 3 * i
    # etc...
    i = ???

i = ???
while True:
    if i == 0:
        break
    print(i)
    x = 3 * i
    # etc...
    i = ???
"""
