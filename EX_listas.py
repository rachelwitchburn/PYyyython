"""
Exercícios para praticar listas
"""

#  Mostre as seguintes listas derivadas de:
#  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#  Intervalo de 1 a 9
print(list(range(1, 10)))
#  Intervalo de 8 a 13
print(list(range(8, 14)))
#  Números pares
print('Números pares: ', end='')
for i in lista:
    if i % 2 == 0:
        print(i, end=' ')
print(' ')
#  Números ímpares
print('Números ímpares: ', end='')
for i in lista:
    if i % 2 != 0:
        print(i, end=' ')
print('')
#  Múltiplos de 2 (números pares)
print('Números múltiplos de 2: ', end='')
for i in lista:
    if i % 2 == 0:
        print(i, end=' ')
print('')
#  Múltiplos de 3
print('Números múltiplos de 3: ', end='')
for i in lista:
    if i % 3 == 0:
        print(i, end=' ')
print('')
#  Múltiplos de 4
print('Números múltiplos de 4: ', end='')
for i in lista:
    if i % 4 == 0:
        print(i, end=' ')
print('')
#  lista.reverse()
#  print(lista)
#  ou:
print(lista[::-1])
print('')
#  razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9
soma1 = 0
soma2 = 0
for i in list(range(10, 16)):  #  75
    soma1 += i
print(soma1)
for j in list(range(3, 10)):  #  42
    soma2 += j
print(soma2)
razao = soma1 / soma2
print(float(razao))

