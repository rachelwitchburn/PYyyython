"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da matemática

-Aqui no python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos nos preocupar com chaves,
valores ou itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos(Set) e mapas(dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.


#  Definindo um conjunto:

#  Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)
print(type(s))

#  OBS: ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
#       será ignorado sem gerar erros e não fará parte do conjunto

#  Forma 2 - Mais comum:
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

#  Verificar se um elemento está contido no conjunto:
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


#  Importante lembrar que além de não termos valores duplicados, não temos ordem

#  (Listas e tuplas aceitam valores duplicados)
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

#  (Dicionários não aceitam a mesma chave (chaves iguais) e conjuntos também não repetem elementos)
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

#  Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))
for i in s:
    print(i)

#  Usos interessantes com sets
#  Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visistantes
#  informam manualmente a cidade de onde vieram.
#  Nós adicionamos cada cidade em uma pista Python, já que em uma lista podemos adicionar novos elementos e ter
#  repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

#  Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
#  O que você faria? Faria um loop na lista...?
#  Podemos utilizar o set para isso:
print(len(set(cidades)))

#  Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)
s.add(4)  # Mutáveis
s.add(4)  # Não dá erro, mas também não printa outro 4 (pq nao repete os valores)
print(s)

#  Remover elementos
s = {1, 2, 3}
print(s)

#  Forma 1
s.remove(3)  # Não é índice (endereço), é o valor que será removido
print(s)

#  OBS: Caso o valor não seja encontrado, será gerado erro KeyError

#  Forma 2
s.discard(2)  # O DISCARD NÃO GERA ERROR SE O VALOR DADO NÃO EXISTIR, ELE NÃO VAI TIRAR NADA!
print(s)


s = {1, 2, 3}
print(s)
#  Copiando um conjunto para outro...
print()
#  Forma 1 (DEEP COPY):
novoconjunto = s.copy()
print(novoconjunto)
print()
novoconjunto.add(4)
print(novoconjunto)
print(s)

#  Forma 2 (Shallow Copy):
novo = s
novo.add(4)
print(novo)
print(s)


#  Podemos remover todos os itens de um conjunto
s.clear()
print(s)

#  Precisamos gerar um conjunto com nomes de estudantes únicos

#  Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)  # printa todos os estudantes unidos
print(unicos1)

#  Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

#  Veja que alguns alunos que estudam python também estudam JAVA.

#  Gerar um conjunto de estudantes que estão ambos os cursos
#  Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#  Forma 2 - Utilizando o &

ambos2 = estudantes_java & estudantes_python
print(ambos2)






#  Métodos matemáticos de CONJUNTOS
#  Imagine que temos dois conjuntos, um tenho estudantes do curso Python e
#  um contendo estudantes do curso de JAVA

estudantes_python = {'Marcos', 'Patrícia', 'Hellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}

#  Gerar um conjunto de estudantes que não estão estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(f'Lista de quem só estuda Python: {so_python}')
so_java = estudantes_java.difference(estudantes_python)
print(f'Lista de quem só estuda JAVA: {so_java}')
"""


