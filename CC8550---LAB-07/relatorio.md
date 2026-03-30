# Laboratório 07 — Test-Driven Development (TDD) — Sistema de estoque

**Disciplina:** CC8550 — Simulação e Teste de Software  
**Centro Universitário FEI**  
**Aluno:** Lucas Rebouças Silva  
**R.A.:** 22.122.048-6  
**Professor:** Luciano Rossi · 1º semestre de 2026  

---

## 1. Objetivo

Implementar a classe `Estoque` seguindo **TDD** (ciclo Red → Green → Refactor), conforme Aula 07.

---

## 2. Conformidade com a atividade (slides)

| Requisito | Atendido |
|-----------|----------|
| `adicionar_produto(nome, quantidade)` | Sim — incrementa se já existir |
| `remover_produto(nome, quantidade)` | Sim — não remove mais que o disponível |
| `consultar_quantidade(nome)` | Sim — inexistente retorna `0` |
| `listar_produtos()` | Sim — produtos com quantidade **> 0** |
| `produto_mais_estocado()` | Sim — `None` se estoque vazio |
| Não remover mais que disponível | Sim — `ValueError` |
| Adicionar existente incrementa (não substitui) | Sim |
| Quantidade ≤ 0 em adicionar/remover | Sim — `ValueError` |
| Ao menos 10 testes | Sim — **15** testes |
| Todos os testes passam | Sim (`OK`) |
| Comentários RED / GREEN / REFACTOR | Sim — [`tests/test_estoque.py`](tests/test_estoque.py) e [`src/estoque.py`](src/estoque.py) |

---

## 3. Execução dos testes

```text
python -m unittest discover tests -v
```

**Resultado verificado (2026-03-29):** 15 testes, `OK`.

---

## 4. Cobertura (`src/estoque.py`)

```text
pip install -r requirements.txt
python -m coverage run -m unittest discover tests
python -m coverage report -m --include=src/estoque.py
python -m coverage html --include=src/estoque.py -d htmlcov
```

**Saída obtida:**

```text
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
src\estoque.py      25      0   100%
----------------------------------------------
TOTAL               25      0   100%
```

Relatório HTML: [`htmlcov/index.html`](htmlcov/index.html) no navegador.

---

## 5. TDD na prática

Os testes em [`tests/test_estoque.py`](tests/test_estoque.py) estão agrupados por ciclos (adicionar/consultar, validação, remover, listagem). A produção em [`src/estoque.py`](src/estoque.py) documenta **REFACTOR** na validação unificada de quantidade positiva e na listagem ordenada.
