"""
CC8550 - Aula 04: Funções dos exercícios de cobertura estrutural.
"""


def verificar(n):
    """Exercício 1 - Caminhos independentes."""
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"


def classificar(x):
    """Exercício 2 - Cobertura de comandos e ramos."""
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"


def acesso(idade, membro):
    """Exercício 3 - Cobertura de condição."""
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"


def somar_ate(n):
    """Exercício 4 - Teste de ciclo."""
    soma = 0
    for i in range(n):
        soma += i
    return soma


def percorrer_matriz(m, n):
    """Exercício 5 - Teste de ciclo aninhado."""
    posicoes = []
    for i in range(m):
        for j in range(n):
            posicoes.append((i, j))
    return posicoes


def analisar(numeros):
    """Exercício 6 - Teste completo (integrador)."""
    total = 0
    for n in numeros:
        if n > 0 and n % 2 == 0:
            total += n
        elif n < 0:
            total -= 1
        else:
            continue
    if total > 10:
        return "Acima"
    return "Abaixo"


def desconto(preco, cliente_vip):
    """Exercício 7 - Fluxo de dados (def-uso)."""
    total = preco
    if cliente_vip:
        desconto_valor = preco * 0.2
        total = preco - desconto_valor
    if total < 50:
        total = 50
    return total
