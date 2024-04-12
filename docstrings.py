"""
Documentando funções com Docstrings

Podemos ainda fazer acesso a documentação com a função help()
"""
def diz_oi():
    """Uma função que retorna string 'oi!'"""
    return 'oi!'

print(diz_oi())
print(diz_oi().__doc__)

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou o 'número' a 'potencia' informada
    :param numero: numero que desejamos gerar o exponencial
    :param potencia: potencia que queremos gerar o exponencial (por padrao definido na funcao foi 2)
    :return:
    """
    return numero ** potencia

