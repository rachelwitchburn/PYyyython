"""
OS 5 PRIMEIROS MÚLTIPLOS DE 3 SÃO: 0, 3, 6, 9, 12
"""
#  1- Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.

#  2- Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar uma estrutura de repetição for, a segunda while, e a terceira do while
"""
for i in range(1, 101):
    print(i)
"""

"""
numero = 0
while numero < 101:
    print(numero)
    numero = numero + 1
"""

"""
esse dá errado :p
numero = 0
while True:
    print(numero + 1)
    if not (numero > 100):
        break
"""

#  3- Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após a contagem.

"""
numero = 10
while numero > 0:
    print(numero)
    numero = numero - 1
print("FIM!")
"""

#  4- Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil)
"""
numero = 0
for i in range(numero, 100001, 1000):
    print(i)
"""

#  5- Faça um programa que peça ao usuário para digitar 10 valores e some-os.

"""
for i in range(1, 11):
    numero = int(input("Digite um número: "))
    numero = numero + numero
print(i)
"""

#  6- Faça um programa que leia 10 inteiros e imprima sua média.


