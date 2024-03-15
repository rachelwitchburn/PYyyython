"""
Definindo funções

-Funções são pequenas partes de código que realizam tarefas específicas;
-Pode ou não receber entradas de dados e retornar uma saída de dados;
-Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
     é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções;
-print()
-len()
-max()
-min()
-count()
etc;
"""

#  Exemplo de utilização de funções:
#  cores = ['verde', 'amarelo', 'branco']

#  Utilizando a função integrada (Built-in) do Python. (Built-in são aquelas funções que já vêm integradas do python
#  print(cores)
#  cores.append('roxo')
#  print(cores)


#  Tentei adicionar um ponto ao final da string
#  curso = 'Programação em Python Essencial'
#  print(curso)

#  s = curso.split()  # converte a string em uma lista guardada em s
#  curso = ' '.join(s)  # isso aqui é altamente opcional e nesse caso tem até uma inutilidade, é bom para adicionar espaços entre eles
#  print(f'{curso}.')
#  Mas é um jeito de fazer com que seja adicionado algo, mas isso sem um built-in do pyhton para strings

#  cores.clear()  # função que não recebe nenhum dado, depende de alguem para chamar: CORES.clear()
#  print(cores)

#  print(help(print))
#  DRY - Don't Repeat Yoursel - não repita vc mesmo, ou nn repita seu código

#  Mas então, como definir funções?

"""
Em pyhton, a forma geral de definifir uma função é:
def nome_da_funcao(paramentros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao sempre com letras minusculas, e se for nome composto, separado por _ (Snake Case);
paramentros_de_entrada -> opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não; (QUAIS DADOS A FUNÇÃO RECEBE PARA TRABALHAR?)
bloco_da_funao -> ou corpo_da_funcao ou implementacao é onde o processamento da função acaontece,
                  neste bloco pode ter ou não retorno da função.

OBS: Veja que para definir um função utilizamos 'def' que em pyhton significa que
     estamos definindo uma função, e dps abrimos o bloco de código como ":" que define blocos (em pyhton)
     

"""

#  Definindo a primeira função

def diz_oi():
    print('oi')

"""
OBS: 
1- Veja que dentro das nossas funções podemos utilizar outras funções;
2- Veja que nossa função só executa 1 uma tarefa, ou seja, só printa oi;
3- Veja que esta função não recebe nenhum paramêtro de entrada;
4- Veja que esta função não retorna nada
"""

#  Utilizando funções:

# Chamada de execução:
diz_oi()

"""
ATENÇÃO

Nunca esqueça de utilizar os () ao executar uma função
"""

#  Exemplo 2

def cantar_parabens():
    print('Parabéns pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('VIVAviva o aniversariante')

#for i in range(5):
#    cantar_parabens()

canta = cantar_parabens
canta()