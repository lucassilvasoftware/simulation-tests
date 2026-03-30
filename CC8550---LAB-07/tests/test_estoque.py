"""
test_estoque.py — Atividade LAB 07 (TDD).

Evidencia do ciclo Red / Green / Refactor:
- Cada bloco RED descreve o teste escrito antes do comportamento existir;
- GREEN corresponde à implementação mínima em src/estoque.py;
- REFACTOR aparece na produção (validação unificada, listagem ordenada).
"""
import unittest

from src.estoque import Estoque


# --- Ciclo 1 (RED -> GREEN): adicionar e consultar basico ---
class TestAdicionarEConsultar(unittest.TestCase):
    """RED: especificar adicao e consulta antes da implementacao completa."""

    def test_adicionar_novo_produto_aumenta_estoque(self):
        e = Estoque()
        e.adicionar_produto("caneta", 10)
        self.assertEqual(e.consultar_quantidade("caneta"), 10)

    def test_adicionar_produto_existente_incrementa(self):
        e = Estoque()
        e.adicionar_produto("papel", 5)
        e.adicionar_produto("papel", 3)
        self.assertEqual(e.consultar_quantidade("papel"), 8)

    def test_consultar_inexistente_retorna_zero(self):
        e = Estoque()
        self.assertEqual(e.consultar_quantidade("fantasma"), 0)


# --- Ciclo 2 (RED -> GREEN): validacao de quantidade na adicao ---
class TestAdicionarInvalido(unittest.TestCase):
    def test_adicionar_quantidade_zero_levanta(self):
        e = Estoque()
        with self.assertRaisesRegex(ValueError, "positiva"):
            e.adicionar_produto("x", 0)

    def test_adicionar_quantidade_negativa_levanta(self):
        e = Estoque()
        with self.assertRaisesRegex(ValueError, "positiva"):
            e.adicionar_produto("x", -1)


# --- Ciclo 3 (RED -> GREEN): remover e limites ---
class TestRemover(unittest.TestCase):
    def test_remover_diminui_saldo(self):
        e = Estoque()
        e.adicionar_produto("caderno", 20)
        e.remover_produto("caderno", 7)
        self.assertEqual(e.consultar_quantidade("caderno"), 13)

    def test_remover_ate_zero_remove_chave(self):
        e = Estoque()
        e.adicionar_produto("lapis", 2)
        e.remover_produto("lapis", 2)
        self.assertEqual(e.consultar_quantidade("lapis"), 0)
        self.assertNotIn("lapis", e.listar_produtos())

    def test_remover_mais_que_disponivel_levanta(self):
        e = Estoque()
        e.adicionar_produto("borracha", 2)
        with self.assertRaisesRegex(ValueError, "Nao e possivel remover"):
            e.remover_produto("borracha", 5)

    def test_remover_produto_inexistente_levanta(self):
        e = Estoque()
        with self.assertRaisesRegex(ValueError, "Nao e possivel remover"):
            e.remover_produto("inexistente", 1)

    def test_remover_quantidade_invalida_levanta(self):
        e = Estoque()
        e.adicionar_produto("clip", 5)
        with self.assertRaisesRegex(ValueError, "positiva"):
            e.remover_produto("clip", 0)


# --- Ciclo 4 (RED -> GREEN): listagem e produto mais estocado ---
class TestListagemEMaisEstocado(unittest.TestCase):
    def test_listar_vazio(self):
        self.assertEqual(Estoque().listar_produtos(), [])

    def test_listar_so_produtos_com_quantidade_positiva(self):
        e = Estoque()
        e.adicionar_produto("a", 1)
        e.adicionar_produto("b", 2)
        self.assertEqual(e.listar_produtos(), ["a", "b"])

    def test_produto_mais_estocado_vazio_retorna_none(self):
        self.assertIsNone(Estoque().produto_mais_estocado())

    def test_produto_mais_estocado_retorna_nome_correto(self):
        e = Estoque()
        e.adicionar_produto("p", 1)
        e.adicionar_produto("q", 99)
        self.assertEqual(e.produto_mais_estocado(), "q")

    def test_produto_mais_estocado_empate_retorna_um_dos_maximos(self):
        e = Estoque()
        e.adicionar_produto("m", 5)
        e.adicionar_produto("n", 5)
        self.assertIn(e.produto_mais_estocado(), ("m", "n"))


if __name__ == "__main__":
    unittest.main()