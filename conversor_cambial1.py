"""
Conversor cambial EUR<->USD. 
Exibe um menu com as opções em baixo indicadas.

    $ python3 conversor_cambial1.py

    Escolha o sentido da conversão
    1. Euros -> Dólares
    2. Dólares -> Euros
    T. Terminar
    > 2

    Montante em dólares: 2000
    Euros -> 1851.85

    Escolha o sentido da conversao
    1. Euros -> Dolares
    2. Dólares -> Euros
    T. Terminar
    > T

    $

v1: Versão normal, sem while True
"""

from decimal import Decimal as dec

def main():
    cambio = dec('1.1875')      # preço do euro em dólares, em 27/01/2026
    opcao = ''
    while opcao.upper() not in ('T', 'TERMINAR'):
        # 1. Exibir opções do menu
        print("Escolha o sentido da conversão")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")
        print("T. Terminar")

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
            case 'T' | 'TERMINAR' :
                print("Fim do programa")
            case _:
                print(f"Opção <{opcao}> inválida!")
#:

if __name__ == '__main__':
    main()

