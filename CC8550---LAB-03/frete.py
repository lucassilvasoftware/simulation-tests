def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:
    if peso <= 0:
        raise ValueError("Peso invalido")

    if valor_pedido < 0:
        raise ValueError("Valor do pedido invalido")

    if valor_pedido > 200:
        return 0.0

    if peso <= 1:
        frete = 10.0
    elif peso <= 5:
        frete = 15.0
    elif peso <= 20:
        frete = 25.0
    else:
        raise ValueError("Peso acima do permitido")

    if destino == "mesma_regiao":
        return frete
    elif destino == "outra_regiao":
        return frete * 1.5
    elif destino == "internacional":
        return frete * 2.0
    else:
        raise ValueError("Destino invalido")