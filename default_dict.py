"""
Módulo Collections - Default Dict

#  Recap dicionários:
dicionario = {'Curso': 'programação em python essencial'}
print(dicionario)
print(dicionario['Curso'])
print(dicionario['outro'])  # KeyError

Default Dict -> ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver um valor
definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será
atribuído

OBS: lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores

from collections import defaultdict
dicionario = defaultdict(lambda: 0)
dicionario['Curso'] = 'programação em pyhton essencial'
print(dicionario)
print(dicionario['outro'])  # KeyError no dicionario comum
print(dicionario)
"""
