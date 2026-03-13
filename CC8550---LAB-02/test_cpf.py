import pytest
from cpf import validar_cpf, formatar_cpf


@pytest.mark.parametrize("cpf", [
    "313.402.809-30",
    "111.444.777-35",
    "12345678909",
], ids=["valido_formatado", "valido_zeros", "valido_sem_formatar"])
def test_cpf_valido(cpf):
    # Arrange
    # Act
    resultado = validar_cpf(cpf)
    # Assert
    assert resultado is True


@pytest.mark.parametrize("cpf", [
    "111.222.333-44",
    "123.456.789-00",
    "111.111.111-11",
    "1234567890",
    "123456789012",
    "1234567890a",
], ids=["digitos_verificadores_errados", "invalido", "todos_iguais", "menos_11", "mais_11", "com_letras"])
def test_cpf_invalido(cpf):
    # Arrange
    # Act
    resultado = validar_cpf(cpf)
    # Assert
    assert resultado is False


def test_cpf_none():
    # Arrange
    # Act
    resultado = validar_cpf(None)
    # Assert
    assert resultado is False


def test_cpf_string_vazia():
    # Arrange
    # Act
    resultado = validar_cpf("")
    # Assert
    assert resultado is False


def test_formatar_cpf_valido():
    # Arrange
    cpf = "12345678909"
    # Act
    resultado = formatar_cpf(cpf)
    # Assert
    assert resultado == "123.456.789-09"


def test_formatar_cpf_invalido_levanta_excecao():
    # Arrange
    cpf = "123.456.789-00"
    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        formatar_cpf(cpf)
    assert "CPF inválido" in str(exc_info.value)


def test_formatar_cpf_none_levanta_excecao():
    # Arrange
    # Act & Assert
    with pytest.raises(ValueError):
        formatar_cpf(None)


def test_formatar_cpf_vazio_levanta_excecao():
    # Arrange
    # Act & Assert
    with pytest.raises(ValueError):
        formatar_cpf("")


def test_formatar_cpf_tamanho_errado_levanta_excecao():
    # Arrange
    # Act & Assert (menos de 11 digitos)
    with pytest.raises(ValueError):
        formatar_cpf("12345")


def test_todos_cpfs_validos_retornam_true(cpfs_validos):
    # Arrange
    # Act & Assert
    for cpf in cpfs_validos:
        assert validar_cpf(cpf) is True


def test_todos_cpfs_invalidos_retornam_false(cpfs_invalidos):
    # Arrange
    # Act & Assert
    for cpf in cpfs_invalidos:
        assert validar_cpf(cpf) is False
