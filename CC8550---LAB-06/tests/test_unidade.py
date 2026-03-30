"""Parte 1 — Testes de unidade da Calculadora com stub (MagicMock)."""
import sys
import unittest
from unittest.mock import MagicMock

from src.calculadora import Calculadora


class TestEntradaSaida(unittest.TestCase):
    """§2.1 — Entrada e saída (retornos e último resultado)."""

    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_soma_retorna_valor_correto(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_subtrair_retorna_valor_correto(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_subtrair_negativo(self):
        self.assertEqual(self.calc.subtrair(3, 10), -7)

    def test_multiplicar_basico(self):
        self.assertEqual(self.calc.multiplicar(6, 7), 42)

    def test_multiplicar_por_zero(self):
        self.assertEqual(self.calc.multiplicar(99, 0), 0)

    def test_dividir_inteiros(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_dividir_decimais(self):
        self.assertAlmostEqual(self.calc.dividir(1, 4), 0.25)

    def test_potencia_quadrado(self):
        self.assertEqual(self.calc.potencia(5, 2), 25)

    def test_potencia_zero(self):
        self.assertEqual(self.calc.potencia(10, 0), 1)

    def test_extra_soma_decimais(self):
        """Teste extra §5.2 — soma com floats."""
        self.assertAlmostEqual(self.calc.somar(0.1, 0.2), 0.30000000000000004)


class TestTipagem(unittest.TestCase):
    """§2.2 — Tipagem inválida e caso bool."""

    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_tipagem_string_rejeitada_somar(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_tipagem_none_rejeitado_dividir(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

    def test_tipagem_segundo_argumento_invalido_subtrair(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(1, "x")

    def test_tipagem_primeiro_invalido_multiplicar(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar([], 2)

    def test_tipagem_potencia_base_invalida(self):
        with self.assertRaises(TypeError):
            self.calc.potencia(None, 2)

    def test_tipagem_potencia_expoente_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.potencia(2, "3")

    def test_bool_eh_aceito_por_isinstance_int(self):
        """bool é subclasse de int: o código atual aceita bool como número."""
        r = self.calc.somar(True, False)
        self.assertEqual(r, 1)
        self.repo.salvar.assert_called()


class TestLimite(unittest.TestCase):
    """§2.3 — Limites inferior/superior e extras (divisor pequeno, potência)."""

    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        self.assertFalse(resultado == float("inf"))

    def test_dividir_divisor_muito_pequeno(self):
        r = self.calc.dividir(1, 1e-300)
        self.assertGreater(r, 1e299)

    def test_potencia_expoente_negativo(self):
        self.assertAlmostEqual(self.calc.potencia(2, -1), 0.5)

    def test_potencia_expoente_fracionario(self):
        self.assertAlmostEqual(self.calc.potencia(9, 0.5), 3.0)

    def test_extra_limite_multiplicacao_grandes(self):
        """Teste extra §5.2 — multiplicação sem infinito (evita overflow)."""
        x = 1e100
        self.assertFalse(self.calc.multiplicar(x, x) == float("inf"))


class TestForaDoIntervalo(unittest.TestCase):
    """§2.4 — Valores fora do domínio (divisão por zero)."""

    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_extra_divisao_zero_nao_salva(self):
        """Teste extra — repositório não deve receber salvar se exceção."""
        with self.assertRaises(ValueError):
            self.calc.dividir(1, 0)
        self.repo.salvar.assert_not_called()


class TestMensagensErro(unittest.TestCase):
    """§2.5 — Mensagens de erro com assertRaisesRegex."""

    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)

    def test_extra_mensagem_tipo_multiplicar(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.multiplicar(1, object())


class TestFluxosControle(unittest.TestCase):
    """§2.6 — Caminhos de cada condição em calculadora.py."""

    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_caminho_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_caminho_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_somar_tipo_a_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.somar("a", 1)

    def test_somar_tipo_b_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.somar(1, "b")

    def test_subtrair_tipo_a_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair((), 1)

    def test_subtrair_tipo_b_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(0, {})

    def test_multiplicar_tipo_a_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar(set(), 1)

    def test_multiplicar_tipo_b_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar(1, [])

    def test_dividir_tipo_a_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.dividir("1", 1)

    def test_dividir_tipo_b_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(1, "1")

    def test_potencia_base_invalida(self):
        with self.assertRaises(TypeError):
            self.calc.potencia("2", 3)

    def test_potencia_expoente_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.potencia(2, (3,))

    def test_obter_ultimo_resultado_inicial_zero(self):
        self.assertEqual(self.calc.obter_ultimo_resultado(), 0)


if __name__ == "__main__":
    unittest.main()
