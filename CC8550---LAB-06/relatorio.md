# Laboratório 06 — Testes de unidade e integração

**Disciplina:** CC8550 — Simulação e Teste de Software  
**Centro Universitário FEI**  
**Aluno:** Lucas Rebouças Silva  
**R.A.:** 22.122.048-6  
**Professor:** Luciano Rossi  

---

## 1. Objetivo

Desenvolver e executar testes de unidade e de integração para uma calculadora que persiste o histórico de operações via `HistoricoRepositorio`, aplicando *test doubles* (stub e mock) conforme a Atividade 06.

---

## 2. Execução dos testes

Comando utilizado (na pasta `CC8550---LAB-06`):

```text
python -m unittest discover tests -v
```

**Resultado:** 59 testes executados, todos com sucesso (`OK`).

Arquivos:

- `tests/test_unidade.py` — Parte 1 (entrada/saída, tipagem, limites, mensagens, fluxos).
- `tests/test_integracao.py` — Parte 2 (repositório real).
- `tests/test_doubles.py` — Parte 3 (stub e mock).

---

## 3. Cobertura de código (`calculadora.py`)

Comandos:

```text
pip install -r requirements.txt
python -m coverage run -m unittest discover tests
python -m coverage report -m --include=src/calculadora.py
```

### 3.1 Saída obtida

```text
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src\calculadora.py      43      0   100%
--------------------------------------------------
TOTAL                   43      0   100%
```

### 3.2 Linhas cobertas e não cobertas

- **Linhas cobertas:** todas as 43 declarações em `src/calculadora.py` foram executadas pelos testes.
- **Linhas não cobertas:** nenhuma (`Missing` vazio).
- **Justificativa:** a suíte exercita todos os ramos de validação de tipo (`isinstance`), o ramo de divisão por zero, todas as operações bem-sucedidas com `salvar`, e `obter_ultimo_resultado` no estado inicial (`resultado == 0`).

Relatório HTML opcional: `python -m coverage html` gera `htmlcov/index.html`.

---

## 4. Bug intencional e correção (`potencia`)

### 4.1 Problema

No código-base do PDF, o método `potencia` calculava corretamente com `base ** expoente`, mas **registrava no histórico** uma string com o operador de **multiplicação** (`*`) em vez de **potenciação** (`**`):

```text
self.repositorio.salvar(f"{base} * {expoente} = {resultado}")  # incorreto
```

Isso tornava o histórico semanticamente errado (ex.: `2 * 8 = 256` em vez de `2 ** 8 = 256`).

### 4.2 Correção

Substituição pela string coerente com a operação:

```text
self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")
```

### 4.3 Como os testes ajudaram

Testes de **mock** que verificam o argumento exato passado a `salvar()` na potência detectam a divergência entre o comportamento esperado (operador `**`) e o texto incorreto com `*`. Após a correção, `assert_called_once_with("2 ** 8 = 256")` passa a refletir o contrato desejado.

---

## 5. Comportamento com `bool` (tipagem)

Em Python, `bool` é subclasse de `int`. A validação `isinstance(x, (int, float))` **aceita** valores booleanos; por exemplo, `somar(True, False)` resulta em `1` e gera entrada no histórico.

Isso **não é necessariamente desejável** para um domínio “apenas números reais”, mas é **consistente** com a semântica atual do código. Uma API mais rigorosa poderia rejeitar `bool` explicitamente (`isinstance(x, bool)`), o que mudaria o contrato e exigiria novos testes.

---

## 6. Reflexão: Stub vs Mock

- **Stub (ex.: `MagicMock` usado apenas para não acionar I/O real):** substitui o repositório para que a calculadora possa ser testada sem dependências externas. O foco está no **resultado** das operações (valor retornado, último resultado). O stub pode até configurar retornos fictícios (`total.return_value = 0`) sem que o objeto real exista.

- **Mock (mesma classe `MagicMock`, usado com asserções de interação):** além de isolar dependências, permite **verificar comportamento**: se `salvar` foi chamado, quantas vezes, e com qual string exata; e se **não** foi chamado quando uma exceção ocorre antes do registro (ex.: `TypeError` ou `ValueError` na divisão por zero).

Na prática, **stub** responde “o suficiente para o teste seguir”; **mock** responde “foi chamado do jeito certo?”. Os testes de mock do item `potencia` são especialmente úteis para capturar erros no **texto** persistido, não só no valor numérico.

---

## 7. Print simulado — cobertura 100%

```text
...........................................................
----------------------------------------------------------------------
Ran 59 tests in 0.022s

OK

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src\calculadora.py      43      0   100%
--------------------------------------------------
TOTAL                   43      0   100%
```

*(Valores de tempo podem variar conforme a máquina.)*

---

## 8. Conformidade com o enunciado (Atividade 06)

| Requisito (PDF) | Atendido |
|-----------------|----------|
| `src/repositorio.py` — `HistoricoRepositorio` | Sim — [`src/repositorio.py`](src/repositorio.py) |
| `src/calculadora.py` — operações + bug da `potencia` corrigido (`**` no histórico) | Sim — [`src/calculadora.py`](src/calculadora.py) |
| Parte 1 — unidade (entrada/saída, tipagem incl. `bool`, limites, divisão zero, mensagens `assertRaisesRegex`, fluxos) + extras por categoria | Sim — [`tests/test_unidade.py`](tests/test_unidade.py) |
| Parte 2 — integração com repositório real | Sim — [`tests/test_integracao.py`](tests/test_integracao.py) |
| Parte 3 — stub e mock (`salvar` em todas operações; exceção não chama `salvar`) | Sim — [`tests/test_doubles.py`](tests/test_doubles.py) |
| Cobertura 100% em `calculadora.py` | Sim — ver seção 3 e execução verificada abaixo |
| `relatorio.md` com resultados, cobertura, bug, reflexão stub vs mock | Sim (este arquivo) |
| `requirements.txt`, `README.md` | Sim |

Artefatos extras do workspace: `relatorio.tex`, `setup_miktex_path.py`, `compile_relatorio.ps1` (LaTeX / MiKTeX).

---

## 9. Execução verificada (gerada em 2026-03-29)

Comandos executados na pasta do laboratório:

```text
pip install -r requirements.txt
python -m unittest discover tests -v
python -m coverage run -m unittest discover tests
python -m coverage report -m --include=src/calculadora.py
python -m coverage html --include=src/calculadora.py -d htmlcov
```

**Resultado:** 59 testes, `OK`. Cobertura em `src/calculadora.py`: **100%** (43 statements, 0 miss).

Relatório HTML interativo: abrir [`htmlcov/index.html`](htmlcov/index.html) no navegador após gerar com o último comando.
