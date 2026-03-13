# Validação de CPF

Validação e formatação de CPF com testes unitários em pytest. Simulação e Teste de Software (CC8550).

## Conteúdo

| Arquivo      | Descrição                          |
|-------------|-------------------------------------|
| cpf.py      | `validar_cpf()`, `formatar_cpf()`   |
| test_cpf.py | 18 testes (parametrização, fixtures, exceções) |
| conftest.py | Fixtures `cpfs_validos`, `cpfs_invalidos`     |

## Resultados

- **Testes:** 18 (todos em `test_cpf.py`; sem classes, funções parametrizadas e com fixtures).
- **Cobertura:** 97% no módulo `cpf` (pytest-cov).

<img width="1184" height="586" alt="image" src="https://github.com/user-attachments/assets/b28b87ca-2752-488e-9d95-ca7dd5d6bc01" />

## Comandos

```bash
pip install -r requirements.txt
pytest -v test_cpf.py
pytest -v test_cpf.py --cov=cpf --cov-report=term-missing
```

## Uso do módulo

```python
from cpf import validar_cpf, formatar_cpf

validar_cpf("313.402.809-30")   # True
formatar_cpf("12345678909")     # "123.456.789-09"
```

`formatar_cpf()` levanta `ValueError` para CPF inválido.
