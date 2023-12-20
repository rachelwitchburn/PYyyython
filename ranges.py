"""
RANGES - gerar sequencias numericas nao de forma aleatoria, mas sim de maneira especificada
range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

#FORMA 1:
for num in range(11):
    print(num)

#FORMA 2:
range(valor_de_inicio, valor_de_parada) #  valor_de_inicio especificado

#FORMA 3:
range(valor_de_inicio, valor_de_parada, passo)

#FORMA 4 (inversa):
range(valor_de_parada, valor_de_inicio, passo)

"""

"""
for num in range(1, 4):  # essa é a forma 2
    print(num)
print('')
for valor in range(2):  # essa é a forma 1
    print(valor)
print('')
for numero in range(1, 10, 2):  # 3  esse passo é de 2 em 2
    print(numero)
"""


"""
#  PEDINDO O PASSO AO USUARIO (exem3)
num_inicial = int(input('Qual o número inicial? '))
num_final = int(input('Qual o número final? '))
passo = int(input('De quanto em quanto? '))
if num_inicial >= num_final:
    print('Não funciona. O número incial deve ser menor que o final.')
else:
    for i in range(num_inicial, num_final, passo):
        print(i)
"""


#  PEDINDO O PASSO AO USUARIO: (exem4, regressivo):
rst_num = int(input('Começa de que número? '))
st_num= int(input('Termina em que número? '))
step = int(input('-1? REGRESSÃO '))
for t in range(rst_num, st_num, -1):
    print(t)
