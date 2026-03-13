import pytest
from frete import calcular_frete
from hypothesis import given, strategies as st

# =====================================================
# 1. Classes de Equivalência (5 casos)
# =====================================================

@pytest.mark.parametrize("peso, destino, valor, esperado", [
    (0.5, "mesma_regiao", 100, 10.0),        # CE1
    (3, "outra_regiao", 100, 22.5),         # CE2
    (10, "internacional", 100, 50.0),       # CE3
    (2, "mesma_regiao", 250, 0.0),          # CE11 (frete grátis)
    (1, "mesma_regiao", 100, 10.0),         # fronteira incluída
])
def test_classes_equivalencia(peso, destino, valor, esperado):
    assert calcular_frete(peso, destino, valor) == esperado


# =====================================================
# 2. Valores Limite (9 casos)
# =====================================================

@pytest.mark.parametrize("peso, esperado", [
    (0.99, 10.0),
    (1.00, 10.0),
    (1.01, 15.0),
])
def test_limite_1kg(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == esperado


@pytest.mark.parametrize("peso, esperado", [
    (4.99, 15.0),
    (5.00, 15.0),
    (5.01, 25.0),
])
def test_limite_5kg(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == esperado


@pytest.mark.parametrize("peso, esperado", [
    (19.99, 25.0),
    (20.00, 25.0),
])
def test_limite_20kg_valido(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == esperado


def test_limite_20kg_invalido():
    with pytest.raises(ValueError):
        calcular_frete(20.01, "mesma_regiao", 100)


# =====================================================
# 3. Tabela de Decisão (6 regras mínimas)
# =====================================================

@pytest.mark.parametrize("peso, destino, valor, esperado", [
    (0.5, "mesma_regiao", 100, 10.0),        # R1
    (0.5, "outra_regiao", 100, 15.0),       # R2
    (3, "internacional", 100, 30.0),        # R3
    (10, "mesma_regiao", 100, 25.0),        # R4
    (10, "outra_regiao", 100, 37.5),        # R5
    (10, "internacional", 100, 50.0),       # R6
])
def test_tabela_decisao(peso, destino, valor, esperado):
    assert calcular_frete(peso, destino, valor) == esperado


# =====================================================
# 4. Entradas Inválidas (2 casos)
# =====================================================

def test_peso_invalido():
    with pytest.raises(ValueError):
        calcular_frete(0, "mesma_regiao", 100)


def test_destino_invalido():
    with pytest.raises(ValueError):
        calcular_frete(5, "abc", 100)


# =====================================================
# 5. Property-Based Testing (3 propriedades)
# =====================================================

@given(st.floats(min_value=0.01, max_value=20),
       st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]),
       st.floats(min_value=0, max_value=200))
def test_frete_nunca_negativo(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) >= 0


@given(st.floats(min_value=0.01, max_value=20),
       st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]))
def test_frete_gratis_property(peso, destino):
    assert calcular_frete(peso, destino, 250) == 0.0


@given(st.floats(min_value=0.01, max_value=20),
       st.floats(min_value=0, max_value=200))
def test_outra_regiao_maior_igual(peso, valor):
    f1 = calcular_frete(peso, "mesma_regiao", valor)
    f2 = calcular_frete(peso, "outra_regiao", valor)
    assert f2 >= f1