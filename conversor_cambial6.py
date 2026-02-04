"""
Conversor cambial EUR<->USD. 
Exibe um menu com as opções em baixo indicadas.

    $ python3 conversor_cambial3.py

    Escolha o sentido da conversão
    1. Euros -> Dólares
    2. Dólares -> Euros
    > 2

    Montante em dólares: 2000
    Euros -> 1851.85

    Escolha o sentido da conversao
    1. Euros -> Dolares
    2. Dólares -> Euros
    T. Terminar
    > T

No final de uma conversão, o programa questiona o utilizador se pretende
realizar nova conversão:

    Pretende efectuar mais conversões (S/N)? n
    Fim do programa

Como respostas válidas a esta pergunta, apenas devem ser aceites os
seguintes valores: s, n, sim, nao e não, com qualquer combinação de 
"capitalização"/"case" (ou seja, deve aceitar, s, S, sim, SIM,
Sim, etc.). Qualquer outro valor deve levar a uma mensagem de erro 
e a nova pergunta

v6: melhorar output do main, funções extra
"""

from decimal import Decimal as dec
import os
import subprocess

def main():
    cambio = dec('1.1875')      # preço do euro em dólares, em 27/01/2026
    while True:
        # 1. Exibir opções do menu
        clear_screen()
        print("Escolha o sentido da conversão")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")

        # 2. Ler opção
        opcao = input("> ")
        print()
        
        # 3. Analisar e executar a opção
        match opcao.upper():
            case '1':
                euros = dec(input("Montante em euros: "))
                dolares = euros * cambio
                print(f"Dólares -> {dolares:.2f}")
            case '2':
                dolares = dec(input("Montante em dólares: "))
                euros = dolares / cambio
                print(f"Euros -> {euros:.2f}")
            case _:
                print(f"Opção <{opcao}> inválida!")
                pause()
                continue

        print()

        # 4. Terminar ou continuar
        if not confirma("Pretende efectuar mais conversões (S/N)? "):
            print("Fim do programa")
            break
#:

def confirma(pergunta: str) -> bool:
    while True:
        opcao_repetir = input(pergunta)
        match opcao_repetir.upper():
            case 'N' | 'NAO' | 'NÃO':
                return False
            case 'S' | 'SIM':
                return True
            case _:
                print("ATENÇÃO: Introduza apenas (S)im ou (N)ão!")
#:

def clear_screen():
    if os.name == 'posix':
        subprocess.run(['clear'])
    elif os.name == 'nt':
        subprocess.run(['cls'], shell = True)
#:

def pause():
    input("Pressione ENTER para prosseguir...")
#:

if __name__ == '__main__':
    main()

"""
def soma_ints(a: int, b: int) -> int:
    return a + b
#:

def calculo_especial(a: int, b: str) -> float:
    c = int(b)
    return a + c * 2.5
#:
"""