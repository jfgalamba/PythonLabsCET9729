"""
if CONDIÇÃO:
    INST1
    ...
    INST_N

if CONDIÇÃO:
    INST1
    ...
    INST_N
else:
    INST1
    ...
    INST_M

if CONDIÇÃO1:
    INST1
    ...
    INST_N
elif CONDIÇÃO2:
    INST1
    ...
    INST_M
elif CONDIÇÃO3:
    INST1
    ...
    INST_P
etc...
else:
    INST1
    ...
    INST_K
"""

x = 10
print("ANTES")
if x > 0:
    print("X positivo")
print("DEPOIS")

"""
Quando x = 10:
ANTES
X positivo
DEPOIS

Quando x = -10:
ANTES
DEPOIS
"""

# -----------

x = 0
print("ANTES")
if x > 5:
    print("X maior que cinco")
elif x >= -5:       # x >= -5 and x <= 5
    print("X entre -5 e 5")
else:
    print("X menor que -5")
print("DEPOIS")

"""
Quando x = 10
ANTES
X maior que cinco
DEPOIS

Quando x = 0
ANTES
X entre -5 e 5
DEPOIS

Quando x = -10
ANTES
X menor que -5 
DEPOIS
"""

# Expressão IF / Expressão Condicional
#
#       CONSEQUÊNCIA if CONDIÇÃO else ALTERNATIVA
#
# Operador Ternário (linguagens derivadas de C):
#
#       CONDIÇÃO ? CONSEQUÊNCIA : ALTERNATIVA

x = 5
if x > 0:
    txt = 'positivo' 
else:
    txt = 'negativo ou zero'

txt = 'positivo' if x > 0 else 'negativo ou zero'

x = 5
if x > 0:
    txt = 'positivo'
elif x == 0:
    txt = 'zero'
else:
    txt = 'negativo'

txt = 'positivo' if x > 0 else ('zero' if x == 0 else 'negativo')
txt = 'positivo' if x > 0 else 'zero' if x == 0 else 'negativo'   # parênteses não são obrigatórios

# C/C++, Java, C#, JavaScript (ainda que o exemplo completo seja para Java)
#   String txt = x > 0 ? "positivo" : (x == 0 ? "zero" : "negativo");

valor1 = 77.90
if valor1 == 80:
    valor2 = 5
else:
    valor2 = -5

valor2 = 5 if valor1 == 80 else -5
