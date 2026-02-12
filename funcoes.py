##########################################
#
#       FUNÇÕES
#
##########################################

# Aspectos gerais sobre funções...

#####################################################
# 
#       FUNÇÕES DE PRIMEIRA ORDEM
#       Funções parametrizadas com outras funções
#
#####################################################

from typing import Iterable

nums = [100, -2, -1, 59, 44, 46, 77]
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

def filtra_positivos(itens: Iterable) -> list:
    filtrados = []
    for item in itens:
        if item > 0:
            filtrados.append(item)
    return filtrados
#:

def filtra_pares(itens: Iterable) -> list:
    filtrados = []
    for item in itens:
        if item % 2 == 0:
            filtrados.append(item)
    return filtrados
#:

def filtra_maiores_50(itens: Iterable) -> list:
    filtrados = []
    for item in itens:
        if item > 50:
            filtrados.append(item)
    return filtrados
#:

def filtra_comecados_por_a(itens: Iterable) -> list:
    filtrados = []
    for item in itens:
        if len(item) > 0 and item[0] in ('a', 'A'):
            filtrados.append(item)
    return filtrados
#:

def filtra(itens: Iterable, criterio) -> list:
    filtrados = []
    for item in itens:
        if criterio(item):
            filtrados.append(item)
    return filtrados
#:

# filtra_positivos(nums)   # [100, 59, 44, 46, 77]
# filtra_pares(nums)       # [100, -2, 44, 46]
# filtra_maiores_50(nums)  # [100, 59, 77]
# filtra_comecados_por_a(nomes)       # ['alberto', 'armando', 'albertina']

def e_positivo(num: int | float) -> bool:
    return num > 0
#:

def e_par(num: int | float) -> bool:
    return num % 2 == 0
#:

def e_maior_que_50(num: int | float) -> bool:
    return num > 50
#:

def comeca_por_a(txt: str) -> bool:
    return len(txt) > 0 and txt[0] in ('a', 'A')
#:

filtra(nums, lambda num: num > 0)        # [100, 59, 44, 46, 77]
filtra(nums, lambda num: num % 2 == 0)   # [100, -2, 44, 46]
filtra(nums, lambda num: num > 50)       # [100, 59, 77]
filtra(nomes, lambda txt: len(txt) > 0 and txt[0] in ('a', 'A'))   # ['alberto', 'armando', 'albertina']

# MAPEIA

def mapeia(itens: Iterable, transforma) -> list:
    transformados = []
    for item in itens:
        transformados.append(transforma(item))
    return transformados
#:

def dobro(num: int | float) -> float:
    return 2.0 * num
#:

mapeia(nums, dobro)
mapeia(nums, lambda num: 2.0 * num)
mapeia(nomes, lambda nome: nome[0])
mapeia(nomes, lambda nome: nome[-1])
mapeia(nomes, len)
sum(mapeia(nomes, len))

# TPC:
# Utilizando lambdas, escrever expressões para 
# 1. Filtrar números entre 1 e 20
# 2. Filtrar números começados por 1
# 3. Filtrar números terminados em 0
# 4. Transformar nomes, em nomes maiúsculas

# FUNÇÕES BUILT-IN FILTER, MAP, SORTED

nums = [100, -2, -1, 59, 44, 46, 77]
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

list(filter(lambda num: num > 0, nums))
tuple(map(lambda num: 2.0 * num, nums))

# Três 1as 3 letras dos nomes com 6 ou mais caracteres (MAP e/ou FILTER)
map(lambda nome: nome[:3], filter(lambda nome: len(nome) >= 6, nomes))

# SORTED (TimSort , Tim Peters)

nums = [100, -2, -1, 59, 44, 46, 77, 1_000_000, 10, 440, -7003] 
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

# Ordenação ascendente usando o operador <
sorted(nums)

# Ordenação descendente 
sorted(nums, reverse = True)

# Ordenação ascendente pelo comprimento dos nomes
sorted(nomes, key = len)
# sorted(nomes, key = lambda nome: len(nome))

# Ordenação descendente pelo comprimento dos nomes
sorted(nomes, key = len, reverse = True)

# Ordenação ascendente pelo primeiro algarismo
sorted(nums, key = lambda num: str(abs(num))[0])

##############################################################
# 
#       EXPRESSÃO LISTA (e outras)  /  LIST COMPREHENSION
#       Alternativa mais idiomática a MAP e FILTER
#
##############################################################

list(map(lambda x: 2 * x, nums))
list(filter(lambda x: x > 0, nums))
list(map(lambda x: 2 * x, filter(lambda x: x > 0, nums)))

[2 * num for num in nums]               # SELECT 2 * num FROM nums
[num for num in nums if num > 0]        # SELECT num FROM nums WHERE num > 0
[2 * num for num in nums if num > 0]    # SELECT 2 * num FROM nums WHERE num > 0

{num: 2 * num for num in nums}

# def main():
#     linha = input("Introduza uma linha de texto: ")

#     conta_vogais = 0
#     conta_digitos = 0

#     for ch in linha:
#         if ch in '0123456789':
#             conta_digitos += 1
#         elif ch in 'aeiou':
#             conta_vogais += 1

#     print(f"Vogais minúsculas : {conta_vogais}")
#     print(f"Dígitos           : {conta_digitos}")
# #:

# def main2():
#     linha = input("Introduza uma linha de texto: ")
#     print(f"Vogais minúsculas : {sum(ch in 'aeiou' for ch in linha)}")
#     print(f"Dígitos           : {sum(ch in '0123456789' for ch in linha)}")
# #:

#####################################################
# 
#       RECURSIVIDADE
#       FUNÇÕES INTERNAS / ANINHADAS / NESTED
#
#####################################################

#
# FACTORIAL
# ()

# N! = N x (N-1) x (N-2) x ... x 1
# N! = N x (N-1)!
# 1! = 1
# 0! = 1
# 5! = 5 x 4 x 3 x 2 x 1 = 120

def factorialI(n: int) -> int:
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return  res
#:

def factorialR(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorialR(n - 1)
#:

# factorialR(5) = 5 * 24 = 120 
# factorialR(4) = 4 * 6 = 24
# factorialR(3) = 3 * 2 = 6
# factorialR(2) = 2 * 1 = 2
# factorialR(1) = 1

def fibI(n: int) -> int:
    if n in (0, 1):
        return n
    x, y = 0, 1    # x -> fib(n-2)    y -> fib(n-1)
    for _ in range(2, n + 1):
        y, x = y + x, y
    return y
#:

def fibI(n: int) -> int:
    if n in (0, 1):
        return n
    f2, f1 = 0, 1
    for _ in range(2, n + 1):
        fN = f1 + f2
        f2 = f1
        f1 = fN
    return fN
#:

def fibR(n: int) -> int:
    if n in (0, 1):
        return n
    return fibR(n - 1) + fibR(n - 2)
#:

# Fib(N) = Fib(N-1) + Fib(N-2)
# Fib(1) = 1
# Fib(0) = 0

def acelera_com_cache(fun):   # memoize
    cache = {}
    def outra_fun(*args):
        if args in cache:
            return cache[args]
        x = fun(*args)
        cache[args] = x
        return x
    return outra_fun
#:

fibR = acelera_com_cache(fibR)

from functools import cache

@cache
def fibR(n: int) -> int:
    if n in (0, 1):
        return n
    return fibR(n - 1) + fibR(n - 2)
#:

#####################################################
# 
#       FUNÇÕES INTERNAS: CLOSURES
#
#       CLOSURE: Função interna que guarda o estado 
#       (ie, variáveis locais) a função externa
#
#####################################################

# def verde(Z):
#     X = ...    # definir X
#     def vermelha(...):
#         Y = ...
#         # tem acesso a X e a Y e a Z
#         ...
#     ...
#     # tem acesso apenas X 
#     return vermelha 
#
#         ┌─────────────────────────────────┐
#         │              ┌───────────────┐  │
#         │              │               │  │
#         │  VERMELHA    │     VERDE     │  │
#         │              │               │  │
#         │              └───────────────┘  │
#         └─────────────────────────────────┘

def somador(x: int):
    def soma(y: int):
        return x + y
    return soma
#:

def somador(x: int):
    return lambda y: x + y
#:

def contador(inicio = 0):
    i = inicio - 1
    def conta():
        nonlocal i
        i += 1
        return i
    return conta
#:

##################

# 1a Versão: variável global

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def month_name(month_num: int) -> str:
    return months[month_num - 1]
#:

# 2a Versão: variável local

def month_name(month_num: int) -> str:
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return months[month_num - 1]
#:

# 3a Versão: variável local com closure

def _make_month_name():
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return lambda month_num: months[month_num - 1]
#:

month_name = _make_month_name()























# def handle_fetch(request, response):
#     # operacao 1
#     # operacao 2
# #:

# fetch('https://www.bla.com/get_elements', handle_fetch)

# fetch('https://www.bla.com/get_elements').next(function(request, response) {
#     // operacao 1
#     // operacao 2
# });


# fetch('https://www.bla.com/get_elements').next(function(request, response) {
#     // operacao 1
#     // operacao 2
# });

"""
def comeca_por(letra: str):
    def comeca_por_aux(txt: str) -> bool:
        return len(txt) > 0 and txt[0] in (letra.lower(), letra.upper())
    #:
    return comeca_por_aux
#
"""