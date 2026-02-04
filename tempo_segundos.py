"""
Calcula tempo em segundos após introdução de horas, minutos e
segundos.

DADOS DE ENTRADA:
    horas    : h, string -> int
    minutos  : m, string -> int
    segundos : s, string -> int

DADOS DE SAÍDA:
    segundos : total_segs, int
    total_segs = h*3600 + m*60 + s
"""

def main():
    h = int(input("Horas    : "))
    m = int(input("Minutos  : "))
    s = int(input("Segundos : "))

    print()
    print("Total segundos: ", h*3600 + m*60 + s)
#:

if __name__ == '__main__':
    main()
#: