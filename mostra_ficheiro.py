"""
Mostra ficheiro de texto, linha a linha, com numeração de linhas
"""

import sys

def main():
    if len(sys.argv) != 2:
        print(f"Utilização: {sys.argv[0]} FICHEIRO")
        sys.exit(3)

    with open(sys.argv[1], 'rt') as file_in:
        for i, line in enumerate(file_in, 1):
            print(f'{i:03} | {line}', end = '')
#:

if __name__ == '__main__':
    main()