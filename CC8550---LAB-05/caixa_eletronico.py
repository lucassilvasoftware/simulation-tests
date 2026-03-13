from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Conta:
    numero: str
    saldo: float = 0.0
    historico: List[str] = field(default_factory=list)


def _registrar(conta: Conta, mensagem: str) -> None:
    conta.historico.append(mensagem)


def consultar_saldo(conta: Conta) -> float:
    return conta.saldo


def depositar(conta: Conta, valor: float) -> float:
    if valor <= 0:
        raise ValueError("Valor de depósito deve ser positivo.")

    conta.saldo += valor
    _registrar(conta, f"Depósito de {valor:.2f}")
    return conta.saldo


def sacar(conta: Conta, valor: float) -> float:
    if valor <= 0:
        raise ValueError("Valor de saque deve ser positivo.")

    if valor > conta.saldo:
        raise ValueError("Saldo insuficiente para saque.")

    conta.saldo -= valor
    _registrar(conta, f"Saque de {valor:.2f}")
    return conta.saldo


def transferir(conta_origem: Conta, conta_destino: Conta, valor: float) -> Tuple[float, float]:
    if conta_origem is conta_destino:
        raise ValueError("Conta de origem e destino não podem ser a mesma.")

    if valor <= 0:
        raise ValueError("Valor de transferência deve ser positivo.")

    sacar(conta_origem, valor)
    depositar(conta_destino, valor)

    _registrar(
        conta_origem, f"Transferência enviada de {valor:.2f} para conta {conta_destino.numero}"
    )
    _registrar(
        conta_destino, f"Transferência recebida de {valor:.2f} da conta {conta_origem.numero}"
    )

    return conta_origem.saldo, conta_destino.saldo


def extrato(conta: Conta) -> List[str]:
    return list(conta.historico)
