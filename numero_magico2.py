"""
Vamos fazer um programa de adivinha. Este programa começa por solicitar um
número ao utilizador e, caso este número seja igual a um número pré-defenido
(o número mágico), o programa felicita o utlizador por ter acertado. Caso
contrário, indica que o utilizador falhou.

Investigue o módulo random e acrescente possibilidade de o número mágico 
ser um número (pseudo) aleatório entre 1 e 20.

Acrescente a possibilidade de repetição ao programa anterior enquanto o 
utilizador não acertar. O programa deve dar pistas ao utilizador. Se este
estiver a três valores de distância, então o programa indica que "está 
próximo", se estiver a um valor, o programa diz que "está muito próximo".

v2: Utilização constantes em Python

"""

from random import randint


LIM_INF_NUM_MAGICO = 1
LIM_SUP_NUM_MAGICO = 30
DIST_MUITO_PROXIMO = 1
DIST_PROXIMO = 3


def main():
    num_magico = randint(LIM_INF_NUM_MAGICO, LIM_SUP_NUM_MAGICO)

    while True:
        palpite = int(input(f"Adivinhe o número mágico ({LIM_INF_NUM_MAGICO} a {LIM_SUP_NUM_MAGICO}): "))
        dist = abs(num_magico - palpite)

        if dist == 0:
            print("Parabéns! Acertou!")
            break
        elif dist <= DIST_MUITO_PROXIMO:
            print("Muito próximo!!!")
        elif dist <= DIST_PROXIMO:
            print("Está próximo!")
        else:
            print("Falhou... Tente novamente.")
#:

if __name__ == '__main__':
    main()
