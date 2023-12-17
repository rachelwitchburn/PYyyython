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

#  4- Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
#  O número digitado ao quadrado
#  A raiz quadrada do número digitado
"""
num = float(input('Digite um número: '))
if num >= 0:
    raiz = math.sqrt(num)
    print(f'Esse número ao quadrado é: {num*num}')
    print(f'A raíz quadrada do número é: {raiz}')
else:
    print('Número negativo.')
"""

#  5- Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} dividido por 2 é igual a: {num/2}. É par.')
else:
    print(f'{num} dividido por 2 é igual a: {num/2}. É ímpar.')
"""

#  6- Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
    print(f'A diferença deles é de: {num1 - num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
    print(f'A diferença deles é de: {num2 - num1}')
else:
    print('Números igauis.')
"""
#  8- Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma notá válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
nota1 = int(input('Digite a nota: '))
nota2 = int(input('Digite a nota: '))
if (nota1 and nota2) >= 0.0 and (nota1 and nota2) <= 10.0:
    media = (nota1 + nota2)/2
    print('A média das notas é de: ', media)
else:
    print('Notas inválidas.')
"""
#  9- Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""
salario = float(input('SALÁRIO: '))
prestacao = float(input('PRESTAÇÃO: '))
porcentagem = salario * (20 / 100)
if prestacao > porcentagem:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')
"""
#  10- Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
#      Homens: (72.7 * h) - 58
#      Mulheres: (62,1 * h) - 44,7
"""
altura = float(input('ALTURA: '))
sexo = bool(input('Escreva: "False" caso homem. Escreva "True" caso mulher.'))
if sexo:
    calculo = (62.1 * altura) - 44.7
    print(f'RESULTADO: {calculo}')
else:
    calculo = (72.7 * altura) - 58
    print(f'RESULTADO: {calculo}')
"""

