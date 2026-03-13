"""
CC8550 - Aula 04: Casos de teste para cobertura estrutural (relatório).
"""
import pytest
from exercicios import (
    verificar,
    classificar,
    acesso,
    somar_ate,
    percorrer_matriz,
    analisar,
    desconto,
)


# --- Exercício 1 ---
@pytest.mark.parametrize("n,esperado", [
    (0, "Zero"),
    (2, "Par positivo"),
    (-1, "Negativo"),
    (3, "Impar positivo"),
])
def test_verificar(n, esperado):
    assert verificar(n) == esperado


# --- Exercício 2 ---
@pytest.mark.parametrize("x,esperado", [
    (150, "Alto"),
    (75, "Medio"),
    (25, "Baixo"),
])
def test_classificar(x, esperado):
    assert classificar(x) == esperado


# --- Exercício 3 ---
@pytest.mark.parametrize("idade,membro,esperado", [
    (25, True, "Permitido"),
    (20, False, "Negado"),
    (25, False, "Negado"),
    (17, True, "Negado"),
    (17, False, "Negado"),
])
def test_acesso(idade, membro, esperado):
    assert acesso(idade, membro) == esperado


# --- Exercício 4 ---
@pytest.mark.parametrize("n,esperado", [
    (0, 0),
    (1, 0),
    (2, 1),
    (5, 10),
    (10, 45),
])
def test_somar_ate(n, esperado):
    assert somar_ate(n) == esperado


# --- Exercício 5 ---
@pytest.mark.parametrize("m,n,total_elementos", [
    (0, 0, 0),
    (3, 0, 0),
    (0, 3, 0),
    (1, 3, 3),
    (3, 1, 3),
    (2, 3, 6),
    (4, 5, 20),
])
def test_percorrer_matriz(m, n, total_elementos):
    resultado = percorrer_matriz(m, n)
    assert len(resultado) == total_elementos
    if total_elementos > 0:
        assert resultado[0] == (0, 0)
        assert resultado[-1] == (m - 1, n - 1) if m and n else True


# --- Exercício 6 ---
@pytest.mark.parametrize("numeros,esperado", [
    ([], "Abaixo"),
    ([6], "Abaixo"),
    ([6, 8], "Acima"),
    ([1], "Abaixo"),
    ([-2], "Abaixo"),
    ([4, 3, 8], "Acima"),
    ([6, -2, 8], "Acima"),
    ([2, 4, 1], "Abaixo"),
    ([0, 6, 8], "Acima"),
])
def test_analisar(numeros, esperado):
    assert analisar(numeros) == esperado


# --- Exercício 7 ---
@pytest.mark.parametrize("preco,vip,esperado", [
    (100, False, 100),
    (40, False, 50),
    (100, True, 80.0),
    (40, True, 50),
    (60, False, 60),
    (150, True, 120.0),
])
def test_desconto(preco, vip, esperado):
    assert desconto(preco, vip) == esperado
