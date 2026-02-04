"""
Faça um programa que produza na saída padrão uma carta formatada semelhante à 
indicada no exemplo que se segue. Deverá solicitar a introdução da informação
em sublinhado, e dos restantes dados que achar necessários. A primeira linha e
as últimas duas A primeira linha e as últimas duas ("Caro Alberto/Armanda", 
"O seu," e "Arnaldo Antunes") deverão ser indentadas com 10 caracteres. A 
primeira linha de cada parágrafo deverá estar afastada 4 caracteres da margem
esquerda. A linha a tracejado deverá conter 20 traços e estar indentada com 7 
caracteres. Deverá dar as linhas de espaço indicadas no exemplo:
"""

INDENT_PARAGRAFO = 4
INDENT_SAUDACAO = 10
INDENT_DESPEDIDA = INDENT_SAUDACAO
INDENT_NOME = INDENT_SAUDACAO
INDENT_SEPARADOR = 7
CARACTER_SEPARACAO = '-'
DIM_SEPARADOR = 20

nome = input("Nome do convidado/da: ")
convite = f"""
{INDENT_SAUDACAO * ' '}Caro {nome}
{INDENT_PARAGRAFO * ' '}Venho por este meio convidá-lo/la para a cerimónia a realizar pelas 16h00 do dia
31/05/2036. Caro Alberto/Armanda, o código de vestimento é formal, o que significa que
deverá usar um fato com gravata/vestido e saltos altos.
{INDENT_PARAGRAFO * ' '}O dia 31/05/2036 é uma data muito especial para mim e contamos com a sua presença. O
convite é extensível à sua companheira/companheiro.

{INDENT_PARAGRAFO * ' '}Aguardamos a sua confirmação

{INDENT_DESPEDIDA * ' '}O seu, 

{INDENT_SEPARADOR * ' '}{CARACTER_SEPARACAO * DIM_SEPARADOR}
{INDENT_NOME * ' '}Arnaldo Antunes
"""
print(convite)

