"""
TIPO STRING
"""
print("olá")
print('olá?')
print("""oiii""")
print('''OI''')
nome1 = 'Raquel'
nome2 = "Priscila"
print(nome1, nome2)
print(type(nome1)) #type só pega 1 ou 3 argumentos, não 2
print(type(nome2))
nome3 = "Angelina \nJolie"
print(nome3)
nome4 = ("""Luiz 
José""") #Pra essa pulada de linhas, tem que usar aspas duplas ou aspas simples triplas, pq senao nao funciona
print(nome4)
nome5 = '''Rafael
Mirel'''
print(nome5)
nome = "raquel MeLo"
#print(nome.upper())  coloca todas maiusculas
#print(nome.lower())  coloca todas minusculas
print(nome.title()) #deixa as primeiras letras de cada palavra maiusculas
#print(nome.split()) #transforma em lista

outroNome = ["Raquel", "Melo", "de", "Queiroz"]
print(outroNome[0:3]) #vai do 0 até o numero anterior colocado
#print(outroNome.split()[1]) não prestou?
print(outroNome[::-1]) #começa do primeiro elemento : vai até o último : e inverte -1
