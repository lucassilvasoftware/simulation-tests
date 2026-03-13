def _so_digitos(cpf: str) -> str:
    return "".join(c for c in cpf if c.isdigit())


def _calcular_digito(digitos: str, peso_inicial: int) -> int:
    soma = sum(int(d) * (peso_inicial - i) for i, d in enumerate(digitos))
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto


def validar_cpf(cpf: str) -> bool:
    if cpf is None:
        return False
    nums = _so_digitos(cpf)
    if len(nums) != 11:
        return False
    if not nums.isdigit():
        return False
    if len(set(nums)) == 1:
        return False
    d9 = _calcular_digito(nums[:9], 10)
    if int(nums[9]) != d9:
        return False
    d10 = _calcular_digito(nums[:10], 11)
    if int(nums[10]) != d10:
        return False
    return True


def formatar_cpf(cpf: str) -> str:
    if cpf is None or (isinstance(cpf, str) and cpf.strip() == ""):
        raise ValueError("CPF inválido")
    nums = _so_digitos(cpf)
    if len(nums) != 11 or not nums.isdigit():
        raise ValueError("CPF inválido")
    if not validar_cpf(nums):
        raise ValueError("CPF inválido")
    return f"{nums[:3]}.{nums[3:6]}.{nums[6:9]}-{nums[9:]}"
