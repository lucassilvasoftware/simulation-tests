import pytest
from src.notas import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas
)


class TestValidarNota:
    """Suite de testes para a função validar_nota."""
    
    def test_nota_valida_minima(self):
        """Testa se nota 0 (limite mínimo) é válida."""
        # ARRANGE
        nota = 0
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is True
    
    def test_nota_valida_maxima(self):
        """Testa se nota 10 (limite máximo) é válida."""
        # ARRANGE
        nota = 10
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is True
    
    def test_nota_valida_decimal(self):
        """Testa se nota decimal válida (7.5) é aceita."""
        # ARRANGE
        nota = 7.5
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is True
    
    def test_nota_invalida_acima_dez(self):
        """Testa se nota acima de 10 (11) é inválida."""
        # ARRANGE
        nota = 11
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is False
    
    def test_nota_invalida_decimal_acima_dez(self):
        """Testa se nota decimal acima de 10 (10.1) é inválida."""
        # ARRANGE
        nota = 10.1
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is False
    
    def test_nota_string_nao_numero(self):
        """Testa se string não-numérica ("abc") é inválida."""
        # ARRANGE
        nota = "abc"
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is False
    
    def test_nota_none(self):
        """Testa se None é inválido."""
        # ARRANGE
        nota = None
        
        # ACT
        resultado = validar_nota(nota)
        
        # ASSERT
        assert resultado is False
    


class TestCalcularMedia:
    """Suite de testes para a função calcular_media."""
    
    def test_media_notas_todas_validas(self):
        """Testa cálculo de média com todas as notas válidas."""
        # ARRANGE
        notas = [4, 6, 8, 10]
        
        # ACT
        resultado = calcular_media(notas)
        
        # ASSERT
        assert resultado == 7.0
    
    def test_media_lista_vazia(self):
        """Testa cálculo com lista vazia retorna 0."""
        # ARRANGE
        notas = []
        
        # ACT
        resultado = calcular_media(notas)
        
        # ASSERT
        assert resultado == 0
    
    def test_media_notas_decimais(self):
        """Testa cálculo de média com notas decimais."""
        # ARRANGE
        notas = [7.5, 8.5, 9.5]
        
        # ACT
        resultado = calcular_media(notas)
        
        # ASSERT
        assert resultado == 8.5


class TestObterSituacao:
    """Suite de testes para a função obter_situacao."""
    
    def test_situacao_aprovado_exato(self):
        """Testa aprovação com média exatamente 7."""
        # ARRANGE
        media = 7
        
        # ACT
        resultado = obter_situacao(media)
        
        # ASSERT
        assert resultado == "Aprovado"
    
    def test_situacao_aprovado_maximo(self):
        """Testa aprovação com nota máxima (10)."""
        # ARRANGE
        media = 10
        
        # ACT
        resultado = obter_situacao(media)
        
        # ASSERT
        assert resultado == "Aprovado"
    
    def test_situacao_recuperacao_exato(self):
        """Testa recuperação com média exatamente 5."""
        # ARRANGE
        media = 5
        
        # ACT
        resultado = obter_situacao(media)
        
        # ASSERT
        assert resultado == "Recuperação"
    
    def test_situacao_recuperacao_meio(self):
        """Testa recuperação com média no meio do intervalo."""
        # ARRANGE
        media = 6
        
        # ACT
        resultado = obter_situacao(media)
        
        # ASSERT
        assert resultado == "Recuperação"
    
    def test_situacao_reprovado_exato(self):
        """Testa reprovação com média exatamente 5 (abaixo)."""
        # ARRANGE
        media = 4.9
        
        # ACT
        resultado = obter_situacao(media)
        
        # ASSERT
        assert resultado == "Reprovado"
    
    def test_situacao_reprovado_minimo(self):
        """Testa reprovação com média mínima (0)."""
        # ARRANGE
        media = 0
        
        # ACT
        resultado = obter_situacao(media)
        
        # ASSERT
        assert resultado == "Reprovado"
    

class TestCalcularEstatisticas:
    """Suite de testes para a função calcular_estatisticas."""
    
    def test_estatisticas_notas_validas(self):
        """Testa cálculo completo de estatísticas com notas válidas."""
        # ARRANGE
        notas = [3, 5, 7, 9]
        
        # ACT
        resultado = calcular_estatisticas(notas)
        
        # ASSERT
        assert resultado["media"] == 6.0
        assert resultado["maior"] == 9
        assert resultado["menor"] == 3
        assert resultado["quantidade"] == 4
    
    def test_estatisticas_lista_vazia(self):
        """Testa estatísticas com lista vazia."""
        # ARRANGE
        notas = []
        
        # ACT
        resultado = calcular_estatisticas(notas)
        
        # ASSERT
        assert resultado["maior"] is None
        assert resultado["menor"] is None
        assert resultado["media"] == 0
        assert resultado["quantidade"] == 0
    
    def test_estatisticas_todas_notas_invalidas(self):
        """Testa estatísticas quando todas as notas são inválidas."""
        # ARRANGE
        notas = [-1, 15, "abc", None]
        
        # ACT
        resultado = calcular_estatisticas(notas)
        
        # ASSERT
        assert resultado["maior"] is None
        assert resultado["menor"] is None
        assert resultado["media"] == 0
        assert resultado["quantidade"] == 0
    
    def test_estatisticas_uma_nota(self):
        """Testa estatísticas com apenas uma nota válida."""
        # ARRANGE
        notas = [8]
        
        # ACT
        resultado = calcular_estatisticas(notas)
        
        # ASSERT
        assert resultado["maior"] == 8
        assert resultado["menor"] == 8
        assert resultado["media"] == 8
        assert resultado["quantidade"] == 1
    
    def test_estatisticas_retorna_dicionario(self):
        """Testa se o retorno é um dicionário com as chaves esperadas."""
        # ARRANGE
        notas = [5, 7, 9]
        
        # ACT
        resultado = calcular_estatisticas(notas)
        
        # ASSERT
        assert isinstance(resultado, dict)
        assert "maior" in resultado
        assert "menor" in resultado
        assert "media" in resultado
        assert "quantidade" in resultado


class TestNormalizarNotas:
    """Suite de testes para a função normalizar_notas."""
    
    def test_normalizar_escala_100_para_10(self):
        """Testa normalização de escala 0-100 para 0-10."""
        # ARRANGE
        notas = [50, 100, 0]
        
        # ACT
        resultado = normalizar_notas(notas, 100)
        
        # ASSERT
        assert resultado == [5.0, 10.0, 0.0]
    

    def test_normalizar_notas_decimais(self):
        """Testa normalização com notas decimais."""
        # ARRANGE
        notas = [75.5]
        
        # ACT
        resultado = normalizar_notas(notas, 100)
        
        # ASSERT
        assert resultado[0] == 7.55
    
    def test_normalizar_lista_vazia(self):
        """Testa normalização de lista vazia."""
        # ARRANGE
        notas = []
        
        # ACT
        resultado = normalizar_notas(notas, 100)
        
        # ASSERT
        assert resultado == []
    
    def test_normalizar_max_zero(self):
        """Testa normalização com max_valor igual a 0."""
        # ARRANGE
        notas = [5, 10]
        
        # ACT
        resultado = normalizar_notas(notas, 0)
        
        # ASSERT
        assert resultado == []


class TestExcecao:
    def test_validar_nota_string(self):
        """Testa se validar_nota lança exceção para string."""
        with pytest.raises(ValueError):
            validar_nota("abc")
    
    def test_validar_nota_none(self):
        """Testa se validar_nota lança exceção para None."""
        with pytest.raises(ValueError):
            validar_nota(None) 