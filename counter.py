"""
Módulo Collections - Counter (contador)

Collections é conhecido por -> High performance container datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.


#  Utilizando o Counter
from collections import Counter

#  Exemplo 1:
#  Podemos utilizar qualquer iterável, aqui usei uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 7, 23, 6, 6, 9, 7, 1, 12, 2]

#  Utilizando o Counter
res = Counter(lista)
print(type(res))  # collections.Counter
print(res)
#  Counter({1: 6, 2: 5, 3: 5, 4: 3, 5: 3, 7: 2, 6: 2, 45: 1, 23: 1, 9: 1, 12: 1})
#  Veja que, para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrências.


#  Exemplo 2:
print(Counter('Raquel Melo e Luiz José Mendonça'))
#  Counter({' ': 5, 'e': 4, 'o': 3, 'a': 2, 'u': 2, 'l': 2, 'M': 2, 'n': 2, 'R': 1, 'q': 1, 'L': 1, 'i': 1, 'z': 1, 'J': 1, 's': 1, 'é': 1, 'd': 1, 'ç': 1})
#  A ordem de precedência é pelos valores que mais possuem ocorrências, então a preferência é para as chaves


#  Exemplo 3:
texto = ' Cras ultricies urna nec ante elementum, in eleifend justo dapibus. Etiam maximus augue magna, ut vestibulum
 sem cursus sit amet. Mauris porta velit nibh, nec vulputate ipsum aliquam vel. In vel sagittis nulla. Ut feugiat
 commodo metus, eget placerat ipsum tincidunt vel. Fusce gravida justo nibh, ac commodo neque auctor et. Vestibulum mi
 odio, tempus eget orci ut, tempus fermentum sapien. Suspendisse non diam enim. Nullam pulvinar mauris ante, in ornare
 libero tristique vel. Aenean malesuada ornare elit, nec posuere ex euismod ac. Aliquam sed justo interdum est viverra
 convallis. Fusce in nisl ac dolor pharetra condimentum nec id risus. Vivamus cursus purus sed nulla sodales luctus.
 Donec suscipit nibh quis arcu sollicitudin, vel rutrum turpis sollicitudin. Etiam diam sem, suscipit vel nisl in,
 placerat venenatis odio. '

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

print(res.most_common(5))  # 5 mais comuns palavras usadas (maior ocorrência)


#  modo de fazer que separa por palavras:

def separa_por_palavras(frase):
    split = frase.split()
    corte = Counter(split)
    #  print(corte)
#  split = frase.split()
#  corte = Counter(split)
    return corte
print(separa_por_palavras(frase))
#  O print vai sair assim:
#  Counter({'Python': 1, 'é': 1, 'uma': 1, 'linguagem': 1, 'muito': 1, 'engraçadinha.': 1, 'Todo': 1, 'mundo': 1,
#   'quer': 1, 'aprender-la': 1, 'para': 1, 'tentar': 1, 'ganhar': 1, 'dinheiro.': 1})

from collections import Counter
import string


#  Exercício:
frase = 'Python é uma linguagem muito engraçadinha. Todo mundo quer aprender-la para tentar ganhar dinheiro.'
def separa_dois(frase):
    palavras = frase.split()
    cortee = Counter(palavras)
    return cortee

#  for palavra, contagem in sorted(separa_dois(frase).items()):
    #  print(f'{palavra}: {contagem}')
print(separa_dois(frase))
#  Counter({'Python': 1, 'é': 1, 'uma': 1, 'linguagem': 1, 'muito': 1, 'engraçadinha.': 1, 'Todo': 1, 'mundo': 1,
#   'quer': 1, 'aprender-la': 1, 'para': 1, 'tentar': 1, 'ganhar': 1, 'dinheiro.': 1})

"""



