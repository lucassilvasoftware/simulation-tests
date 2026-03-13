"""
Simulação e Teste de Software (CC8550)
Aula 04 - Técnicas caixa-branca: critérios de cobertura estrutural
Prof. Luciano Rossi
Ciência da Computação
Centro Universitário FEI

Aluno: Lucas Rebouças Silva
R.A: 22.122.048-6
2º Semestre de 2025
"""


# ============================================================================
# EXERCÍCIO 1 - Caminhos Independentes
# ============================================================================
def verificar(n):
    """
    Verifica se um número é par positivo, impar positivo, negativo ou zero.
    
    Args:
        n: Um número inteiro
    
    Returns:
        str: Classificação do número
    """
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"


# ============================================================================
# EXERCÍCIO 2 - Cobertura de Comandos e Ramos
# ============================================================================
def classificar(x):
    """
    Classifica um valor em Alto, Médio ou Baixo baseado em limiares.
    
    Args:
        x: Um número
    
    Returns:
        str: Classificação do valor
    """
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"


# ============================================================================
# EXERCÍCIO 3 - Cobertura de Condição
# ============================================================================
def acesso(idade, membro):
    """
    Verifica se acesso é permitido baseado em idade e status de membro.
    
    Args:
        idade: Idade do usuário (inteiro)
        membro: Booleano indicando se é membro
    
    Returns:
        str: "Permitido" ou "Negado"
    """
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"


# ============================================================================
# EXERCÍCIO 4 - Teste de Ciclo
# ============================================================================
def somar_ate(n):
    """
    Calcula a soma de inteiros de 0 a n-1.
    
    Args:
        n: Limite superior (exclusivo)
    
    Returns:
        int: Soma dos números no intervalo
    """
    soma = 0
    for i in range(n):
        soma += i
    return soma


# ============================================================================
# EXERCÍCIO 5 - Teste de Ciclo Aninhado
# ============================================================================
def percorrer_matriz(m, n):
    """
    Simula a navegação em uma matriz m x n.
    
    Args:
        m: Número de linhas
        n: Número de colunas
    
    Returns:
        list: Lista de posições visitadas
    """
    posicoes = []
    for i in range(m):
        for j in range(n):
            posicoes.append((i, j))
    return posicoes


# ============================================================================
# EXERCÍCIO 6 - Teste Completo (Integrador)
# ============================================================================
def analisar(numeros):
    """
    Analisa uma lista de números, somando os pares positivos e 
    decrementando para negativos.
    
    Args:
        numeros: Lista de inteiros
    
    Returns:
        str: "Acima" se total > 10, "Abaixo" caso contrário
    """
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


# ============================================================================
# EXERCÍCIO 7 - Fluxo de Dados
# ============================================================================
def desconto(preco, cliente_vip):
    """
    Calcula o preço final com desconto para clientes VIP.
    
    Args:
        preco: Preço original (float)
        cliente_vip: Booleano indicando se é cliente VIP
    
    Returns:
        float: Preço final após aplicação de descontos
    """
    total = preco  # def(total) - linha 2
    if cliente_vip:
        desconto_valor = preco * 0.2  # def(desconto_valor) - linha 4
        total = preco - desconto_valor  # def(total) - linha 5, uso(preco, desconto_valor)
    if total < 50:  # uso(total) - linha 6
        total = 50  # def(total) - linha 7
    return total  # uso(total) - linha 8
