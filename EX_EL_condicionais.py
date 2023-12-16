"""
Exercícios de estruturas lógicas e condicionais
"""
import math


#  1- Faça um programa que receba dois números e mostre qual deles é maior.
"""
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print('Números iguais')
"""

#  2- Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
num = float(input('Digite um número: '))
if num >= 0:
    raiz = math.sqrt(num)
    print(raiz)
else:
    print('Número inválido.')
"""

#  3- Leia um número real. Se o número for positivo, imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.
"""
num = float(input('Digite um número: '))
if num >= 0:
    raiz = math.sqrt(num)
    print(raiz)
else:
    quadrado = num*num
    print(quadrado)
"""
