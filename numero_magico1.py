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
"""

from random import randint

def main():
    num_magico = randint(1, 20)

    while True:
        palpite = int(input("Adivinhe o número mágico (1 a 20): "))
        dist = abs(num_magico - palpite)

        if dist == 0:
            print("Parabéns! Acertou!")
            break
        elif dist <= 1:
            print("Muito próximo!!!")
        elif dist <= 3:
            print("Está próximo!")
        else:
            print("Falhou... Tente novamente.")
#:

if __name__ == '__main__':
    main()
