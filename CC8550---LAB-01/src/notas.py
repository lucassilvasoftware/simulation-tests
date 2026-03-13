def validar_nota(nota):
    """
    Verifica se a nota está entre 0 e 10.
    
    Args:
        nota: Valor numérico a ser validado
        
    Returns:
        bool: True se válida, False caso contrário
    """
    nota_float = float(nota)
    return 0 <= nota_float <= 10


def calcular_media(notas):
    """
    Calcula a média das notas, ignorando as inválidas.
    
    Args:
        notas: Lista de notas
        
    Returns:
        float: Média das notas válidas ou 0 se nenhuma válida
    """
    notas_validas = [n for n in notas if validar_nota(n)]
    
    if not notas_validas:
        return 0
    
    return sum(notas_validas) / len(notas_validas)


def obter_situacao(media):
    """
    Retorna a situação do aluno baseado na média.
    
    Args:
        media: Valor da média (0-10)
        
    Returns:
        str: "Aprovado", "Recuperação" ou "Reprovado"
    """
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def calcular_estatisticas(notas):
    """
    Calcula estatísticas das notas válidas.
    
    Args:
        notas: Lista de notas
        
    Returns:
        dict: Dicionário com: maior, menor, media, quantidade
    """
    notas_validas = [n for n in notas if validar_nota(n)]
    
    if not notas_validas:
        return {
            "maior": None,
            "menor": None,
            "media": 0,
            "quantidade": 0
        }
    
    return {
        "maior": max(notas_validas),
        "menor": min(notas_validas),
        "media": sum(notas_validas) / len(notas_validas),
        "quantidade": len(notas_validas)
    }


def normalizar_notas(notas, max_valor):
    """
    Converte notas de uma escala 0-max_valor para escala 0-10.
    
    Args:
        notas: Lista de notas na escala original
        max_valor: Valor máximo da escala original
        
    Returns:
        list: Lista de notas normalizadas para escala 0-10
    """
    if max_valor <= 0:
        return []
    
    return [(nota * 10) / max_valor for nota in notas]