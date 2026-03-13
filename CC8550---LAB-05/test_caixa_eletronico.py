import pytest

from caixa_eletronico import (
    Conta,
    consultar_saldo,
    depositar,
    sacar,
    transferir,
    extrato,
)


def criar_conta(numero: str, saldo_inicial: float = 0.0) -> Conta:
    conta = Conta(numero=numero, saldo=saldo_inicial)
    return conta


def test_saldo_inicial_zero():
    conta = criar_conta("001")
    assert consultar_saldo(conta) == 0.0


def test_deposito_aumenta_saldo():
    conta = criar_conta("001")
    novo_saldo = depositar(conta, 100.0)
    assert novo_saldo == 100.0
    assert consultar_saldo(conta) == 100.0


def test_nao_permite_deposito_negativo_ou_zero():
    conta = criar_conta("001")
    with pytest.raises(ValueError):
        depositar(conta, 0.0)
    with pytest.raises(ValueError):
        depositar(conta, -10.0)


def test_saque_diminui_saldo():
    conta = criar_conta("001", saldo_inicial=200.0)
    novo_saldo = sacar(conta, 50.0)
    assert novo_saldo == 150.0
    assert consultar_saldo(conta) == 150.0


def test_nao_permite_saque_maior_que_saldo():
    conta = criar_conta("001", saldo_inicial=50.0)
    with pytest.raises(ValueError):
        sacar(conta, 60.0)


def test_pode_sacar_todo_saldo():
    conta = criar_conta("001", saldo_inicial=80.0)
    novo_saldo = sacar(conta, 80.0)
    assert novo_saldo == 0.0
    assert consultar_saldo(conta) == 0.0


def test_transferencia_move_saldo_correto():
    origem = criar_conta("001", saldo_inicial=300.0)
    destino = criar_conta("002", saldo_inicial=50.0)

    saldo_origem, saldo_destino = transferir(origem, destino, 100.0)

    assert saldo_origem == 200.0
    assert saldo_destino == 150.0
    assert consultar_saldo(origem) == 200.0
    assert consultar_saldo(destino) == 150.0


def test_nao_permite_transferencia_para_mesma_conta():
    conta = criar_conta("001", saldo_inicial=100.0)
    with pytest.raises(ValueError):
        transferir(conta, conta, 10.0)


def test_extrato_registra_operacoes_na_ordem():
    conta = criar_conta("001")
    depositar(conta, 100.0)
    sacar(conta, 40.0)

    historico = extrato(conta)
    assert len(historico) == 2
    assert "Depósito de 100.00" in historico[0]
    assert "Saque de 40.00" in historico[1]


def test_contas_tem_historicos_independentes():
    conta1 = criar_conta("001")
    conta2 = criar_conta("002")

    depositar(conta1, 50.0)
    depositar(conta2, 80.0)

    historico1 = extrato(conta1)
    historico2 = extrato(conta2)

    assert len(historico1) == 1
    assert len(historico2) == 1
    assert "50.00" in historico1[0]
    assert "80.00" in historico2[0]
