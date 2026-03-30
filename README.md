# Simulação e Testes de Software (CC8550)

**Aluno:** Lucas Rebouças Silva  
**R.A.:** 22.122.048-6

Repositório unificado dos laboratórios da disciplina CC8550 — Simulação e Teste de Software.

---

## Localização

Este repositório contém os laboratórios da disciplina em pastas na raiz:

| Pasta | Conteúdo |
|-------|----------|
| `CC8550---LAB-01/` | Laboratório 1 — Sistema de Notas |
| `CC8550---LAB-02/` | Laboratório 2 — Validação de CPF |
| `CC8550---LAB-03/` | Laboratório 3 — Cálculo de Frete |
| `CC8550---LAB-04/` | Laboratório 4 — Cobertura estrutural e relatório |
| `CC8550---LAB-05/` | Laboratório 5 — Teste de mutação |
| `CC8550---LAB-06/` | Laboratório 6 — Testes de unidade e integração (calculadora + histórico) |
| `CC8550---LAB-07/` | Laboratório 7 — TDD e sistema de estoque |

Cada pasta é um projeto independente (código, testes e documentação). Não há submódulos Git; todo o conteúdo está versionado neste repositório único.

---

## Sumário

1. **[Laboratório 1 — Sistema de Notas](CC8550---LAB-01/)**  
   Testes unitários e exceções para um sistema de notas. Cobertura de código com pytest.

2. **[Laboratório 2 — Validação de CPF](CC8550---LAB-02/)**  
   Validação e formatação de CPF com testes parametrizados, fixtures e exceções (pytest).

3. **[Laboratório 3 — Cálculo de Frete](CC8550---LAB-03/)**  
   Módulo de cálculo de frete com testes em `test_frete.py` e implementação em `frete.py`.

4. **[Laboratório 4 — Cobertura estrutural](CC8550---LAB-04/)**  
   Exercícios de cobertura, grafos de fluxo de controle, scripts e relatório em LaTeX em `relatorio/text/`.

5. **[Laboratório 5 — Teste de mutação](CC8550---LAB-05/)**  
   Caixa eletrônico, mutantes e ferramenta `mutmut`.

6. **[Laboratório 6 — Unidade e integração](CC8550---LAB-06/)**  
   Calculadora com `HistoricoRepositorio`, `unittest`, `coverage` e relatório em Markdown/LaTeX.

7. **[Laboratório 7 — TDD / Estoque](CC8550---LAB-07/)**  
   Classe `Estoque` desenvolvida com ciclo Red-Green-Refactor e `unittest`.

---

## Como usar

Entre na pasta do laboratório desejado e siga o `README.md` local (quando existir) ou os arquivos de teste (`test_*.py`). Exemplo:

```bash
cd CC8550---LAB-02
pip install -r requirements.txt
pytest -v
```
