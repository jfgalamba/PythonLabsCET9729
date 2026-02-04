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

v4: desaparece opção terminar, pergunta se pretende mais conversões
    (versão com return)
"""

from decimal import Decimal as dec

def main():
    cambio = dec('1.1875')      # preço do euro em dólares, em 27/01/2026
    while True:
        # 1. Exibir opções do menu
        print("Escolha o sentido da conversão")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")

        # 2. Ler opção
        opcao = input("> ")

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

        # 4. Terminar ou continuar
        while True:
            opcao_repetir = input("Pretende efectuar mais conversões (S/N)? ")
            match opcao_repetir.upper():
                case 'N' | 'NAO' | 'NÃO':
                    print("Fim do programa")
                    return
                case 'S' | 'SIM':
                    break
                case _:
                    print("ATENÇÃO: Introduza apenas (S)im ou (N)ão!")
    #: fim do WHILE de fora (ie, do WHILE do menu)
#:

if __name__ == '__main__':
    main()

