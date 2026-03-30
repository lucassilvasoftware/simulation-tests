"""
Sistema de estoque (Atividade Aula 07 — TDD).

Metodologia:
  RED     — testes em tests/test_estoque.py escritos como especificacao;
  GREEN   — implementacao minima em cada passo (metodos em Estoque);
  REFACTOR — _validar_quantidade_positiva, listagem ordenada, remocao de chave zerada.

Sistema de estoque — TDD (Red / Green / Refactor).
"""

class Estoque:
    """Armazena quantidades por nome de produto."""

    def __init__(self) -> None:
        self._itens: dict[str, int] = {}

    def _validar_quantidade_positiva(self, quantidade: int, operacao: str) -> None:
        # REFACTOR: DRY - validacao unificada
        if quantidade <= 0:
            raise ValueError(f"{operacao}: quantidade deve ser positiva")

    def adicionar_produto(self, nome: str, quantidade: int) -> None:
        # GREEN: novo ou incremento; REFACTOR: validacao
        self._validar_quantidade_positiva(quantidade, "Adicionar produto")
        self._itens[nome] = self._itens.get(nome, 0) + quantidade

    def remover_produto(self, nome: str, quantidade: int) -> None:
        self._validar_quantidade_positiva(quantidade, "Remover produto")
        disponivel = self.consultar_quantidade(nome)
        if disponivel < quantidade:
            raise ValueError("Nao e possivel remover mais unidades do que o disponivel")
        self._itens[nome] = disponivel - quantidade
        if self._itens[nome] == 0:
            del self._itens[nome]

    def consultar_quantidade(self, nome: str) -> int:
        return self._itens.get(nome, 0)

    def listar_produtos(self) -> list[str]:
        return sorted(n for n, q in self._itens.items() if q > 0)

    def produto_mais_estocado(self) -> str | None:
        if not self._itens:
            return None
        return max(self._itens.items(), key=lambda item: item[1])[0]