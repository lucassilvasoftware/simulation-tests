"""Parte 3 — Stubs e mocks (test doubles)."""
import unittest
from unittest.mock import MagicMock

from src.calculadora import Calculadora


class TestComStub(unittest.TestCase):
    """§4.1 — Stub: repositório substituído, foco na lógica da calculadora."""

    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)


class TestComMock(unittest.TestCase):
    """§4.2 — Mock: verificação de chamadas a salvar()."""

    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_subtrair_argumento_correto(self):
        self.calc.subtrair(9, 4)
        self.mock_repo.salvar.assert_called_once_with("9 - 4 = 5")

    def test_mock_multiplicar_argumento_correto(self):
        self.calc.multiplicar(3, 7)
        self.mock_repo.salvar.assert_called_once_with("3 * 7 = 21")

    def test_mock_dividir_argumento_correto(self):
        self.calc.dividir(8, 2)
        self.mock_repo.salvar.assert_called_once_with("8 / 2 = 4.0")

    def test_mock_potencia_argumento_correto_apos_correcao_do_bug(self):
        """Bug original registrava '*' em vez de '**'; após correção espera-se **."""
        self.calc.potencia(2, 8)
        self.mock_repo.salvar.assert_called_once_with("2 ** 8 = 256")

    def test_mock_dividir_nao_salva_em_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(1, 0)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_tipo_invalido_nao_chama_salvar_potencia(self):
        with self.assertRaises(TypeError):
            self.calc.potencia("2", 3)
        self.mock_repo.salvar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
