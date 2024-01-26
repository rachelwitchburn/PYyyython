"""
TUPLAS (TUPLES)

tuplas sãp bastante parecidas com listas.
Existem basicamente duas diferenças básicas.

1- tuplas são representadas por parênteses ()
2- tuplas são imutáveis - isso significa que ao criar uma tupla ela não muda.
   Toda operação em um tupla gera um nova tupla.

"""

"""
#  CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#  CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4)  # isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # isso é uma tupla!  // também pode ir sem o (), mas tem que colocar a vírgula
print(tupla4)
print(type(tupla4))

#  CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula, e não pelo uso dos parênteses

#  Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)

#  Desempacotamento de tupla

tupla = ('Raquel Melo', 'Esposa do Luiz')
nome, conjuge = tupla
print(nome)


print(conjuge)#  OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

#  Métodos para adição e remoção de elementos nas tuplas não existem dado o fato das tuplas serem imutáveis

#  Soma*, Valor Máximo, Valor Mínimo* e Tamanho
#  *se os valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))  # o único que funcionaria se tivesse outro tipo de dado dentro da tupla

#  Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

#  Pra que ela sejam alteradas tem que sobrescrever o valor delas

#  Verificar se determinado elemento está contido na tupla
tupla = 1, 2, 3

print(3 in tupla)
print(33 in tupla)

#   Iterando sobre uma tupla

tupla = 1, 2, 3

for n in tupla:
    print(n)

#  Com o índice:
for indice, valor in enumerate(tupla):
    print(indice, valor)

#  Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(f"Tem {tupla.count('a')} a")
print(f"Tem {tupla.count('b')} b")
print(f"Tem {tupla.count('c')} c")

nome = tuple('Raquel Melo')
print(nome)

print(nome.count('e'))

#  O acesso de elementos de uma tupla também é semelhante a de uma lista

#  Dicas na utilização de tuplas

#  Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

#  Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

print(meses[5])

#  Iterar com o while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

#  Verificamos em qual indice um elemento está na tupla

print(meses.index('Junho'))

#  OBS: caso o elemento não exista, será gerado erro ValueError

#  Slicing

#  tupla[inicio:fim:passo]

print(meses[5:9])

#  Por que utilizar as tuplas?
#  |-> Tuplas são mais rápidas do que listas.
#  |-> Tuplas deixam seu código mais seguro
#    |-> isso porque trabalhar com elementos imutáveis traz segurança para o código

"""

#  Copiando uma tupla para a outra
tupla = 1, 2, 3
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = 4, 5, 6

nova = nova + outra
print(nova)
print(outra)
print(tupla)  # ela se mantém a mesma coisa

#  Na tupla não temos o problema se Shallow Copy
