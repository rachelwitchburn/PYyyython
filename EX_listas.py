"""
Exercícios para praticar listas
"""

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
"""

#  Ler uma lista de 5 números inteiros e mostre cada número juntamente com sua posição na lista
l = [7, 4, 8, 5, 1]
for i in l:
    print(f'Número: {i}','posicção: ',l.index(i))

#  Ler uma lista de 10 números reais e mostre-os na ordem inversa
l2 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
print(l2[::-1])
print('')

#  Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média
notas = []
notas.extend([10, 8, 9.5, 10])
soma = 0
print(notas)
for i in notas:
    soma = soma + i
print(soma)
media = soma / 4
print(f'A média é de: {media}')
print(notas)
#  duas formas de fazer :)
"""
notas.append(10)
notas.append(9.5)
notas.append(8.5)
notas.append(9.2)
soma = 0
print(notas)
for i in notas:
    soma = soma + i
print(soma)
media = soma / 4
print(f'A média é de: {media}')
"""
print('')

#  Ler um vetor com 20 idades e exibir a maior e menor.
idades = [9, 13, 87, 14, 6, 74, 33, 25, 80, 7, 9, 67, 42, 10, 54, 23, 20, 45, 22, 40]
idades.sort()
print(idades)
print(f'A menor idade é: {idades[0]}')
print(f'A maior idade é: {idades[19]}')
