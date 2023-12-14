"""
recebendo os dados do usuario com input e armazenando
"""
print("Qual seu nome?")
nome = input()
print("Olá,", nome.title())
print("Qual sua idade?")
idade = input()
print("%s tem %s anos" %(nome.title(), idade))
print(idade, "é a idade de", nome.title())

"""
OUTRAS IDEIAS DE PRINT::
"""
print('{0} tem {1} anos.'.format(nome.title(), idade))
"""title para a primeira letra ficar maiuscula"""
print(f'Bem-vindo(a), {nome.title()}')
print(f'{nome.title()} nasceu no ano de {2023 - int(idade)}')
