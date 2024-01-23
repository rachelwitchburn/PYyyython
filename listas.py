"""
Listas
|-> funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem DINÂMICOS e também de podermos colocar QUALQUER TIPO DE DADO

- Dinâmico: não possui tamanho fixo: pode-se criar a lista e simplesmente ir adicionando elementos
- Não possuem tipo de dado fixo - ou seja, podemos colocar qualquer tipo de dado

Listas em py são representadas em: []
"""


"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['r', 'a', 'q', 'u', 'e', 'l', ' ', 'm', 'e', 'l', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Raquel Melo')

#  podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#  podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

#  podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
if lista1.count(1) <= 1:
    print(f'tem {lista1.count(1)} número "1" na lista.')
else:
    print(f'tem {lista1.count(1)} números "1" na lista.')

#  podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista5.count('e'))
print(lista2.count('l'))

#  adicionar elementos em listas -- append
#  com append nós só conseguimos adicionar 1 elemento por vez
print(lista1)
lista1.append(42) #  coloca a lista como elemento único
print(lista1)

#  mas da pra adicionar um elemento do tipo lista com o append:
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # coloca cada elemento da lista como valor adicional e único
#  o extend nao aceita só UM valor
print(lista1)
"""


"""
lista6 = []
print(lista6)
lista6.append(2)
print(lista6)
#  lista6.append([1, 6])
#  print(lista6)
lista6.extend([1, 2, 3, 4])  # adicionou os elementos sem nichar eles
print(lista6)
lista6.pop(2)  # remove o elemento da posição que especifica ou o último
print(lista6)
lista6.remove(4)  # remove o 4
print(lista6)
lista6.reverse()  # reverteu a ordem da lista
print(lista6)
lista6.insert(2, 2)  # adiciona os elementos pelo endereço e o valor(tipo)
print(lista6)
lista6.reverse()
print(lista6)
lista6.insert(4, 4)
print(lista6)
lista6.pop(3)
print(lista6)
lista6.pop(2)
print(lista6)
lista6.insert(1, 1)
print(lista6)
lista6.insert(3, 3)
print(lista6)
"""

#  Podemos inserir um novo elemento na lista informando a posição do índice
#  Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['r', 'a', 'q', 'u', 'e', 'l', ' ', 'm', 'e', 'l', 'o']
#  print(lista1)
#  lista1.insert(2, 'Novo valor')
#  print(lista1)

"""
#  Podemos facilmente juntar duas listas
lista3 = lista1 + lista2  # fazem a mesma coisa
print(lista3)
lista1.extend(lista2)  # fazem a mesma coisa
print(lista1)


#  Também pode fazer da seguinte forma (pra nao precisar criar outra lista
lista1 = lista1 + lista2
print(lista1)
"""


"""
#  Inverte a lista:

#  Forma 1:
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#  Forma 2:
print(lista1[::-1])  # faz a mesma função do reverte
print(lista2[::-1])
"""


"""
l1 = list('Do not Panic!')
var = l1[::-1]  # o 3 nao mostra o seu elemento, mas o da posição anterior
print(var)
"""

"""
#  Copiar uma lista
lista6 = lista1.copy()
print(lista6)

#  Saber o tamanho da lista
print(len(lista1))

#  Podemos remover todos os elementos (zerar a lista)
print(lista1)
lista1.clear()
print(lista1)

"""

"""
#  Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova*3
print(nova)
"""

"""
# Podemos facilmente converter uma string para uma lista

#  Exemplo 1:
curso = ('Programação em Python: Essencial')
print(curso)
curso = curso.split()  # Por padrão, o split separa os elementos da lista pelo espaço entre elas.
print(curso)

#  Exemplo 2:
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)
"""


"""
#  Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
#  Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)
"""

"""
curso2 = 'Programação$em$Python:$Essencial'
print(curso2)
curso2 = curso2.split('$')  #  O split vai pegar o '$' como referência de onde deve criar os espaço na formação da lista
print(curso2)
curso2 = ' '.join(curso2)  #  O join vai pegar a lista criada e transformar numa string com espaços (' ')
print(curso2)
"""

"""
lista3 = [1, 2, 3, 4, 5]
print(lista3)
lista3.pop(1)
print(lista3)
lista3.append(2)
print(lista3)
lista3.insert(1, 2)
print(lista3)
lista3.pop()
print(lista3)
lista3.remove(1)
print(lista3)
lista3.insert(0, 1)
print(lista3)
"""

"""
#Podemos realmente colocar qualquer tipo de dado numa lista inclusive misturando esses daddos
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 212312382]
print(lista7)
"""


"""
#  Iterando sobre listas

#  |-> exemplo 1 - Utilizando FOR
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

soma2 = 0
for elemento in lista1:
    print(elemento)
    soma2 = soma2 + elemento
print(soma2)
"""

"""
#  |-> exemplo 2 - Utilizando While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
"""

"""
#  Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
"""

"""
#  Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

#  Fazer acesso aos elementos de forma indexada inversa
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
#  print(cores[-5])  -> erro, pois não existe
"""

"""
cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

print('')

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
"""

cores = ['verde', 'amarelo', 'azul', 'branco']

"""
#  Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
"""

"""
#  Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
"""

"""
#  Outros métodos não tão importantes mas também úteis

#  Encontrar o índice de um elemento em lista

numeros = [5, 6, 7, 8, 9, 10]
"""

"""
valor = int(input('Qual valor você quer saber o endereço? '))
print(f'O valor do endereço do {valor} é: {numeros.index(valor)}')

print('')

#  Em qual índice está o valor 6?
print(numeros.index(6))

#  Em qual índice está o valor 9?
print(numeros.index(9))

#  OBS: Caso não tenha esse elemento na lista, será apresentado erro

#  OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))
"""

"""
#  Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 0))  # buscando a partir do índice 1 // erro, porque não tem nenhum número 5 depois do índice 0

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 1, 6))  # buscar o índice do valor 8 entre os índices 6 a 8
"""


"""
#  Revisão do slice
#  lista[inicio:fim:passo]
#  range(inicio:fim:passo)

#  Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]  #  [1, 2, 3, 4, 1, 2, 3, 4]
print(lista[:1:-1])
print(lista[:2:-1])  # vai dar o 4, porque é de lá pra cá e o número do meio é de onde termina da ordem normal
print(lista[2:1:-1])
print('')
#  Revisando com o paramentro 'fim'

print(lista[:2])  # começa em 0, pega até o índice 2 - 1
print(lista[:4])  # começa em 0, pega até o índice 4 - 1
print(lista[1:3])  # começa em 0, pega até o índice 3 - 1
print(lista[:])  # também printa tudo

#  Invertendo valores em uma lista

nomes = ['Raquel', 'Melo']
#  nomes = nomes[1], nomes[0]  # uma forma de inverter
#  print(nomes)
nomes.reverse()  # essa função precisa ser estabelecida fora de um print, depois é só printar a lista
print(nomes)
"""

"""
#  Soma*, valor maximo*, valor minimo*, tamanho
#  * se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(f'A soma da lista é de {sum(lista)}')  # soma
print(f'O valor máximo da lista é de {max(lista)}.')  # maximo valor // somente inteiros ou reais
print(f'O valor mínimo da lista é de {min(lista)}.')  # minimo valor // somente inteiros ou reais
print(f'O tamanho da lista é de {len(lista)}.')  # tamanho da lista // Qualquer tipo de dado

print('')

lista2 = [23, 324, 23, 12, 76, 4534, 75, 464, 7797, 2123, 895, 1124, 6780, 0, 9, 8, 7, 6, 4, 757, 234, 2, 34, 4352, 12, 543, 778, 99, 664, 423, 1, 1, 1, 1, 1, 1, 12, 123, 43, 54, 75, 863, 9842, 97, 9, 3, 8, 234]
print(f'A soma da lista é de {sum(lista2)}')  # soma
print(f'O valor máximo da lista é de {max(lista2)}.')  # maximo valor // somente inteiros ou reais
print(f'O valor mínimo da lista é de {min(lista2)}.')  # minimo valor // somente inteiros ou reais
print(f'O tamanho da lista é de {len(lista2)}.')  # tamanho da lista // Qualquer tipo de dado
"""

"""
#  Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))
"""

"""
#  Desempacotamento de listas

lista = [1, 2, 3]
#  num1, num2 = lista  // precisa de todos os valores pra poder desempacotar
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
"""

"""
#  Copiando uma lista para outra (Shallow Copy e Deep Copy)

#  Forma 1 - DEEP COPY
lista = [1, 2, 3]
print(lista)

noval = lista.copy()  # com esse copy, qualquer modificação que voce tiver na lista nova, não afeta a antiga
print(noval)
noval.append(4)  # não afeta a outra lista
print(lista)
print(noval)
#  Em PYTHON, isso é chamado de DEEP COPY
print('')
#  forma 2 - SHALLOW COPY
lista2 = [1, 2, 3]
print(lista2)
nova = lista2  # nova recebe lista, se isso acontecer, a lista também é alterada
print(nova)
nova.append(4)
print(nova)
print(lista2)
#  Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista,
#  mas após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas,
#  isso em PYTHON é chamado de Shallow Copy
"""
