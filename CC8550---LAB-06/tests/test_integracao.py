"""Parte 2 — Testes de integração com HistoricoRepositorio real."""
import unittest

from src.calculadora import Calculadora
from src.repositorio import HistoricoRepositorio


class TestIntegracao(unittest.TestCase):
    """§3 — Integração calculadora + repositório."""

    def setUp(self):
        self.repo = HistoricoRepositorio()
        self.calc = Calculadora(self.repo)

    def test_operacoes_sequenciais(self):
        # 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        self.calc.somar(2, 3)
        self.calc.multiplicar(self.calc.obter_ultimo_resultado(), 4)
        self.calc.dividir(self.calc.obter_ultimo_resultado(), 2)

        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)
        self.assertEqual(self.repo.total(), 3)

    def test_historico_registra_formato_correto(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        registros = self.repo.listar()
        self.assertIn("2 + 3 = 5", registros)
        self.assertIn("4 * 5 = 20", registros)

    def test_limpar_historico(self):
        self.calc.somar(1, 1)
        self.repo.limpar()
        self.assertEqual(self.repo.total(), 0)

    def test_potencia_no_historico_usa_operador_correto(self):
        self.calc.potencia(2, 3)
        registros = self.repo.listar()
        self.assertIn("2 ** 3 = 8", registros)

    def test_sequencia_com_subtracao_e_total(self):
        self.calc.subtrair(10, 3)
        self.calc.potencia(2, 4)
        self.assertEqual(self.repo.total(), 2)


if __name__ == "__main__":
    unittest.main()
