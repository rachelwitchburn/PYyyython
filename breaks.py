"""
SAINDO DE LOOPS COM BREAK
"""

"""
#  EXEMPLO 1:
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saiu do loop')
"""

"""
#  USANDO O EXEMPLO ACIMA PARA PEDIR A PARADA AO USUARIO:
parada = int(input('Qual deve ser a parada? '))
total= int(input('Qual o total de números?'))
inicio = int(input('Qual deve ser o número inicial? '))
if inicio >= total:
    print('Não funciona. O número incial não pode ser menor ou igual o número total.')
else:
    for numero in range(inicio, total):
        if numero == parada+1:
            break
        else:
            print(numero)
"""

#  EXEMPLO 2 (FORÇANDO LOOP INFINITO):
while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        print('Entendido!')
        break
