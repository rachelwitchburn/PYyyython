"""
LOOP DO FOR
for item in interável:
execução do loop
"""
nome = 'Raquel Melo'
"""
for letra in nome:
    print(letra, end='') #  end = '' (sem espaço entre as aspas pra nao ficar com espaço)
"""
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #  tem que transformar em uma lista

#  for valor in enumerate(nome):
#    print(valor)

#  for indice, letra in enumerate(nome):
#   print(nome[indice])

"""
#  Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#  Exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)

#  Exemplo de for 3 (iterando em um range)
for numero in range(1, 10):  #  lembrar que não pega o 10, vai só até o 9
    print(numero)

"""

#  print(nome[0:7])

"""
qntd = int(input('Quantas vezes o loop deve rodar? '))
soma = 0


for n in range(1, qntd+1):
    print(f'Imprimindo {n}')
"""

"""
for n in range(1, qntd+1):
    num = int(input(f'Digite o valor {n} de {qntd}: '))
    soma = soma + num
print(soma)
"""
#  ORIGINAL: U+1F60D
#  MODIFICADO: U0001F60D (tem que usar esse//substitui o '+' por '000')
#  U+1F600 -> U0001F600
#  U+1F631	-> U0001F631

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F631' * num)
