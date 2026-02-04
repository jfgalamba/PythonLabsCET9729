"""

LABORATÓRIO 2 - Elementos Básicos da Linguagem

Exemplo com MATCH

"""

def main():
    print("1/P  - Pesquisar ocorrência")
    print("2/N  - Adicionar ocorrência")
    print("3/A  - Actualizar BD de ocorrências")
    print("0/T  - Terminar")

    opcao = input("Opção: ");

    match opcao:
        case '1':
            print("Introduza os dados para pesquisa...")
        case '2':
            print("Introduza os dados do novo registo...")
        case '3':
            print("Vamos agora actualizar a BD...")
        case '0':
            print("Programa vai terminar")
        case _:
            print("ERRO: Opção {opcao} inválida")

    if opcao == '1':
        print("Introduza os dados para pesquisa...")
    elif opcao == '2':
        print("Introduza os dados do novo registo...")
    elif opcao == '3':
        print("Vamos agora actualizar a BD...")
    elif opcao == '0':
        print("Programa vai terminar")
    else:
        print("ERRO: Opção {opcao} inválida")

if __name__ == '__main__':
    main()
