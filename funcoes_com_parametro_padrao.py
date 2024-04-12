"""
Funções com parâmetros padrão

funções onde a passagem de parâmetros seja opcional

#Exemplo de função que o parametro é opcional
print('raquel e luiz')
print()

def quadrado(numero):
    return nummero **2
print(quadrado()) # typeerror erro - obrigatorio passar parametro
print(quadrado(4))


def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3))
#print(exponencial(4))  # isso da erro
print(exponencial(2, 5))

# se o usuario definir a potencia como 2, ele pode fazer isso:
def exponencial2(numero, potencia=2):
    return numero ** potencia

print(exponencial2(2, 3))
print(exponencial2(4))  # por padrao, se nao especificar ele vai elevar ao que foi definido antes
print(exponencial2(2, 5))


#  OBS: em funções python, se os primeiros valores default (padrao) DEVEM sempre estar ao final da declaracao

def testeexponecial(potencia, num=2):
    return num**potencia

print(testeexponecial(3))

#  Outros exemplos
def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
#print(soma(4))  # typeerror  Se colocoar valores padrao la na função, isso funcionaria
#print(soma())  # typeerror

#  Exemplo mais complexo
def mostra_informacao(nome='raquel', casada=True):
    if nome == 'raquel' and casada:
        return 'Bem vinda, raquel casada com o luiz'
    elif nome == 'raquel':
        return 'Você é outra raquel'
    return f'ola {nome}'

nome = str(input('qual seu nome?'))

if nome == 'raquel':
    casad = input('é casada?')
    if casad == 's':
        casad = True
    elif casad == 'n':
        casad = False
    else:
        print('an?')
    print(mostra_informacao(nome, casad))
else:
    print(mostra_informacao(nome, False))


#  Por que utilizar parametros com valor default?
#  nos permite ser mais flexiveis nas funções
#  evita erros com parametros incorretos
#  nos permite trabalhar com exemplos mais legiveis de codigo

#  Quais tipos de dados podemos utilizar como valores default para parametros?
#  qualquer tipo de dado

def diz_oi():
    print('oi')

diz_oi()
oi = diz_oi()


def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def multiplicacao(num1, num2):
    return num1*num2

def divisao(num1, num2):
    return num1/num2

print(int(divisao(2, 2)))

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(2, 3))
print(mat(2, 2, divisao))


#  Escopo - evitar problemas e confusões
#  variáveis globais
#  variáveis locais

instrutor = 'raquel'  # variavel global
def printt(instrutor):
    return instrutor

print(printt(instrutor))
print(printt('n'))

def diz_oi():
    eu = 'raquel'
    return f'olá {eu}'

print(diz_oi())
#print(diz_oi(eu)) # nameerror, pq a variavel é local, so existe dentro da funcao


#  ATENÇÃO com variaveis globais (Se puder evitar, evite!)

# CORRETO:
total = 0
def incrementa(total):
    total = total +1
    return total

print(incrementa(total))


#OU correto

total = 0
def incrementa():
    global total
    total = total + 1
    return total

print(incrementa())


#  ERRADO:
total = 0
def incrementa():

    total = total +1
    return total

print(incrementa())



"""

#  Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável
def fora():
    contador = 0

    def dentro():
        nonlocal contador  # para se referir a variavel declarada na função de cima
        contador = contador+1
        return contador
    return dentro()

print(fora())
print(fora())