# CC8550 — Lab 07: Test-Driven Development (TDD) — Sistema de estoque

**Aluno:** Lucas Rebouças Silva  
**R.A.:** 22.122.048-6  
**Disciplina:** CC8550 — Simulação e Teste de Software · Centro Universitário FEI  
**Professor:** Luciano Rossi · 1º semestre de 2026

## Objetivo

Implementar a classe `Estoque` seguindo **TDD** (ciclo Red → Green → Refactor), conforme Aula 07. Os comentários nos arquivos indicam onde houve **RED** (teste primeiro), **GREEN** (código mínimo) e **REFACTOR** (consolidação sem mudar comportamento).

## Estrutura

| Arquivo | Descrição |
|---------|-----------|
| [`src/estoque.py`](src/estoque.py) | Classe `Estoque` com as operações pedidas |
| [`tests/test_estoque.py`](tests/test_estoque.py) | Suíte com **15** testes (mínimo exigido: 10) |

## Operações

1. `adicionar_produto(nome, quantidade)` — novo produto ou incremento se já existir  
2. `remover_produto(nome, quantidade)` — remove unidades (não pode exceder o disponível)  
3. `consultar_quantidade(nome)` — retorna `0` se inexistente  
4. `listar_produtos()` — nomes com quantidade **> 0** (ordenados alfabeticamente)  
5. `produto_mais_estocado()` — nome com maior quantidade, ou `None` se vazio  

## Regras de negócio

- Quantidade em adicionar/remover deve ser **> 0** (`ValueError` caso contrário)  
- Não é possível remover mais do que o disponível (`ValueError`)  
- Adicionar produto já existente **incrementa** a quantidade  
- Estoque vazio: `produto_mais_estocado()` retorna `None`  

## Como executar

```bash
cd CC8550---LAB-07
pip install -r requirements.txt
python -m unittest discover tests -v
```

Cobertura (opcional):

```bash
python -m coverage run -m unittest discover tests
python -m coverage report -m --include=src/estoque.py
python -m coverage html --include=src/estoque.py -d htmlcov
```

**Relatório** em Markdown: [`relatorio.md`](relatorio.md) (conformidade + execução verificada). Relatório HTML de cobertura: `htmlcov/index.html`.

Dependências: `unittest` (padrão) e `coverage` (para relatório de cobertura).

## Critério TDD

Cada método da classe foi coberto por testes escritos como especificação executável; a sequência **RED → GREEN → REFACTOR** está documentada em comentários em `tests/test_estoque.py` e `src/estoque.py`.
