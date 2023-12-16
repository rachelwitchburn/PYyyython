"""
Estruturas Lógicas - and, or, not, is

is fica mais ou menos: if blabla is True;; mas nao acho muito útil ou bonito
mas é bom para verificação de algo
nome = 'raquel'
nome.istitle()
False
verificação se o nome está em title
"""
ativo = False
logado = False

if ativo and logado:  # assume-se que é True só em dizer 'ativo' ou 'logado
    print('Usuário ativo no sistema.')
elif logado:
    print('Você precisa ativar sua conta, cheque seu e-mail.')
elif ativo:
    print('Ativo! Confirme seu e-mail.')
else:
    print('Usuário não é logado no sistema.')

desempregado = False
procurandoEmprego = True
estudante = True

if desempregado:
    print("Desclassificado.")
elif desempregado and procurandoEmprego:
    print("Desclassificado.")
elif procurandoEmprego and estudante:
    print("Em análise.")
elif estudante:
    print("Aceito!")
elif estudante and desempregado:
    print("Estudante. Não desempregado. ")
else:
    print("Por favor, tente se inscrever novamente depois.")

rico = True  # aqui só vai prestar o not se o rico for True
pobre = True  # aqui tbm

if not rico and not pobre:
    print('Pode se inscrever no programa de bolsas.')
elif not rico:
    print('Pode se inscrever no programa de bolsas.')
elif not pobre:
    print('Não pode se inscrever no programa de bolsas.')
elif not rico and not pobre:
    print('Faça o teste.')
else:
    print('Faça o teste.')

professora = False
coordenadora = False
diretora = False

if professora and not coordenadora and not diretora:
    print('Não pode entrar.')
elif professora and coordenadora or diretora:
    print('Pode entrar.')
elif coordenadora or diretora:
    print('Pode entrar.')
else:
    print('Intruso!')
