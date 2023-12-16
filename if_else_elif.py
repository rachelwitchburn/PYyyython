"""
IF, ELSE, ELIF
"""
print("Qual sua idade?")
idade = int(input())


if idade < 18:
    print('Menor de idade')
elif 18 <= idade < 60:  # simplificado AND// antes eu tinha feito: elif idade >= 18 and idade < 60:
    print('Maior de idade')
else:
    print('Idoso')
