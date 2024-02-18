"""
DICIONÁRIOS
OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))


#  Separação da CHAVE pro VALOR é de ':'  ('chave:valor')
#   depois separa por ,
#  Tanto chave quanto valor podem ser de qualquer tipo de dado
#  Podemos misturar tipos de dados


#  Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type((paises)))

#  Forma 2 (menos comum)

paises = dict(br='brasil', eua='estados unidos', py='paraguai')
print(paises)
print(type((paises)))

#  Acessando elementos

#  Forma 1: acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
#  print(paises['ru']  #error KeyError

#  Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

#  Forma 2: acessando via get - recomendado
print(paises.get('br'))
print(paises.get('ru'))

#  Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

if pais:
    print(f'Encontrei o país {pais}.')
else:
    print(f'Não encontrei o país.')

#  Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}.')

#  Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)  # aqui dá falso, pq a verificação é por chave, e não por valor

if 'ru' in paises:
    russia = paises['ru']
print(paises)

#  Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionario, como chaves
#  de dicionários


#Tuplas por exemplo são muito interessantes de serem usadas como chave de dicionários, pois elas são imutáveis
localidades = {
    (35.6895, 39.6917) : 'Escritório em Tókio',
    (40.7120, 74.0060) : 'Escritório em Nova York',
    (37.7749, 122.4194) : 'Escritório em São Paulo',
}
#  essas chaves acima são tuplas
print(localidades)
print(type(localidades))


#  Adicionar elementos em um dicionário
receita = {
    'jan' : 100, 'fev' : 120, 'mar' : 300
}
print(receita)
print(type(receita))

#  Forma 1 - mais comum
receita['abr'] = 350
print(receita)

#  Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

#  Forma 3
receita.update({'jun': 500})
print(receita)

#  Atualizando dados em um dicionário

#  Forma 1
receita['mai'] = 550
print(receita)

#  Forma 2
receita.update({'mai': 600})
print(receita)

#  CONCLUSÃO 1: A forma de adiciconar novos elementos e atualizar dados em um dicionário é a mesma
#  CONCLUSÃO 2: Em dicionários NÃO podemos ter chaves repetida

itens = {}
print(type(itens))
print('LISTA DE COMPRAS')
produto1 = input('Qual o nome do produto?\n')
preco1 = float(input('Qual o valor?\n'))
produto2 = input('Qual o nome do produto?\n')
preco2 = float(input('Qual o valor?\n'))
print(f'Produto 1: {produto1}\nPreço: R${preco1}')
itens.update({produto1: preco1})
print('')
print(f'Produto 2: {produto2}\nPreço: R${preco2}')
itens.update({produto2: preco2})
print(f'Produtos: {itens}')

print('MÉDIA')
notas = {}
media = {}
nota1 = float(input('Qual a 1° nota? \n'))
nota2 = float(input('Qual a 2° nota? \n'))
nota3 = float(input('Qual a 3° nota? \n'))
nota4 = float(input('Qual a 4° nota? \n'))
notas.update({'Nota 1': nota1, 'Nota 2': nota2, 'Nota 3': nota3, 'Nota 4': nota4})
print(f'Notas: {notas}')
media.update({'Média': (nota1 + nota2 + nota3 + nota4)/4})
print(f'Média: {media}')


#  Remover dados de um dicionário
receita = {
    'jan' : 100, 'fev' : 120, 'mar' : 300
}
print(receita)

#  Forma 1 - Mais comum - você pode recuperar o valor removido
ret = receita.pop('mar')
print(ret)

print(receita)
#  OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
#  OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado

#  Forma 2:
del receita['fev']
print(receita)

#  Se a chave não existir, será gerado um KeyError
#  OBS: Neste caso o valor removido não é retornado

#  Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        -nome;
        -quantidade;
        -preço;
    Produto 2:
        -nome;
        -quantidade;
        -preço;

# 1 -  Poderiamos utilizar uma lista para isso? Sim
carrinho = []
produto1 = ['Playstation 4', 1, 2300]
produto2 = ['God of War', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#  Teríamos que saber qual é o índice de cada informação no produto.

#  2 - Poderíamos utilizar uma tupla para isso? Sim
produto1 = ('PlayStation 4', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

#  Poderíamos utilizar um dicionário para isso? Sim
carrinho = []
produto1 = {'nome': 'PlayStation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#  Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a
#  certeza sobre cada informação


#  Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#  Limpar o dicionário (zerar dados) -> .clear()

d.clear()
print(d)

#  Copiando um dicionário para outro
#  Forma 1
novo = d.copy()  # Deep Copy
print(novo)
novo['d'] = 4

print(d)  # continua com os mesmos dados
print(novo)

#  Forma 2  # Shallow Copy
novo = d  # altera valor
print(novo)
novo['d'] = 4
print(d)
print(novo)


"""

#  Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')  # não funciona se eu coloco
#  outra chave pra distribuir, pois vão ser printadas todas as 'chaves' em todos os itens
print(usuario)

#  O método fromkeys recebe dois parâmetros: um interável e um valor.
#  Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')  # se não usar o [], ele vai assumir que cada letra dentro da string,
#  é uma iterável particular
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
