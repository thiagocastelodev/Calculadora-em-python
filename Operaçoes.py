import re


def Calcular(expressão):
    expressão = expressão.replace('x', '*')
    if '!' in expressão:
        expressão = Verifica(expressão)
    try:
        return str(eval(expressão))
    except SyntaxError:
        return 'Erro de Sintase'


def Fib(n):
    valor = int(n)
    for i in range(valor-1, 0, -1):
        valor *= i
    return str(valor)


def Verifica(expressão):
    resultado = re.findall((r"\d+!"), expressão)
    nova_expressão = expressão
    for v in resultado:
        nova_expressão = nova_expressão.replace(v, Fib(v[0:-1]))
    return nova_expressão