"""
Funções com retorno

numeros = [1, 2, 3]
ret = numeros.pop()
print(f'retorno do pop: {ret}')
ret_pr = print(numeros)
print(f'retorno de print {ret_pr}')

OBS: Em python, quando uma função não retorna nenhum valor, o retorno é None.
OBS: Funções pyhton que retornam valores, devem retornar estes valores com a palavra reservada return
OBS: Não precisamos necessariamente criar uma variavel pra receber o retorno de uma função, podemos passar
     a execução da função para outras funções.



#  Exemplo função

#  Vamos refatorar essa função para que ela retorne o valor (refatorar = reescrever, redefinir)


def quadrado_de_7():
    return 7*7

#  Criação de uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'retorno {ret}')
print(f'retorno {quadrado_de_7()}')

#  Refatorando a primeira função

#  Primeiro tipo, se retorna algo, vc precisa imprimir a função depois pra mostrar
def diz_oi():
    return 'oi, '

#  print(diz_oi())

print()

#  Segundo tipo, se você printa dentro da função e não retorna nada, você pode só chamar ela depois, fora de um print:

def diz_oi():
    print('oi, ')  # isso nn retorna nada

diz_oi()
alguem = 'Pedro'
print(alguem)


print(diz_oi())
alguem = 'Pedro'
print(alguem)
# print(diz_oi() + alguem)  # se usasse a função que nao retorna nada, você nao poderia fazer isso porque vc nao pode
                          #  somar None + String

OBS: Sobre a palavra reservada return
1- ela finaliza a função, ou seja, ela sai da execução da função
2- podemos ter em uma função, diferentes returns;
3- podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores


#  Exemplo 1: 1- ela finaliza a função, ou seja, ela sai da execução da função
def diz_oi():
    print('Estou sendo executado antes do retorno! :D')
    return 'Oi! '
    print('Estou sendo executado após o retorno')  # não será executada pois, depois do return, a função acaba

print(diz_oi())


#  Exemplo 2: 2- podemos ter em uma função, diferentes returns;
def nova_funcao():
    variavel = True  # ou None, ou False
    if variavel:  # "if variavel" assume que é verdadeira
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())


#  Exemplo 3 3- podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(num1)
print(outra_funcao())  # imprime no formato de tupla pq o return tá em tupla (separada por ",")
print(type(outra_funcao()))


#  Vamos criar uma função para jogar a moeda

from random import random
def joga_moeda():
    #  Gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'  # nao precisa colocar else

print(joga_moeda())


#  Erros comuns na utilização do retorno, mas que na verdade nem é erro, mas sim codificação desnecessária
def eh_impar():
    numero = 6
    if numero % 2 != 0:  # DIFERENTE DE 0, ou seja NÃO é par
        return True
    return False  # boas praticas de programação

print(eh_impar())


"""
