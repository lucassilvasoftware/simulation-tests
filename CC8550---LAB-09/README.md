# CC8550 - LAB 09 - Sistema Task Manager

Implementacao do Laboratorio 09 da disciplina Simulacao e Teste de Software.

## Descricao

Projeto em Python com:
- classe `Task` (regras de validacao e ciclo de vida),
- `InMemoryStorage`,
- `TaskRepository`,
- testes unitarios (`Task`) e de componente (`TaskRepository`) usando `pytest`.

## Estrutura do projeto

```text
CC8550---LAB-09/
  task_manager/
    task.py
    storage.py
    repository.py
  tests/
    test_task.py
    test_repository.py
  requirements.txt
  README.md
  relatorio.tex
  relatorio.pdf
```

## Como instalar

```bash
pip install -r requirements.txt
```

## Como testar

```bash
pytest -v
```

## Relatorio em LaTeX

Compilar o relatorio:

```bash
pdflatex relatorio.tex
```

Dependendo do ambiente, pode ser necessario executar o comando duas vezes para atualizar referencias.
