# CC8550 — Lab 06: Testes de unidade e integração (Calculadora + histórico)

**Aluno:** Lucas Rebouças Silva  
**R.A.:** 22.122.048-6  
**Disciplina:** CC8550 — Simulação e Teste de Software · Centro Universitário FEI

## Estrutura

- `src/repositorio.py` — `HistoricoRepositorio`
- `src/calculadora.py` — `Calculadora` (operações e registro no repositório)
- `tests/` — unidade (`test_unidade.py`), integração (`test_integracao.py`), doubles (`test_doubles.py`)

## Dependências

```bash
pip install -r requirements.txt
```

## Executar testes

```bash
python -m unittest discover tests -v
```

## Cobertura (coverage.py)

```bash
coverage run -m unittest discover tests
coverage report -m
coverage html
```

Relatório HTML em `htmlcov/index.html`.

## Compilar relatório LaTeX (opcional)

Com MiKTeX instalado:

```powershell
.\compile_relatorio.ps1
```

Ou:

```bash
python setup_miktex_path.py --compile
```
