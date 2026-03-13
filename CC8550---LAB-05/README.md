# CC8550 — Lab 05: Teste de Mutação (Caixa Eletrônico)

## Estrutura

- `caixa_eletronico.py` — código original (5 funcionalidades)
- `caixa_eletronico_mutante.py` — cópia com mutantes manuais
- `test_caixa_eletronico.py` — testes pytest (10 testes)
- `relatorio/text/main.tex` — relatório em LaTeX

## Comandos

```powershell
# Instalar dependências
pip install -r requirements.txt

# 1) Testes no código original (devem passar todos)
python -m pytest -v

# 2) Testes no código mutante: editar test_caixa_eletronico.py
#    trocar "from caixa_eletronico import" por "from caixa_eletronico_mutante import"
#    e rodar: python -m pytest -v

# 3) Mutação automática (mutmut): no Windows requer WSL
#    No WSL/Linux: mutmut run   e depois  mutmut results
```

**Nota:** O `mutmut` não tem suporte nativo ao Windows ([issue #397](https://github.com/boxed/mutmut/issues/397)). Para rodar no seu PC, use WSL ou um ambiente Linux.

## Relatório PDF

```powershell
.\compile_relatorio.ps1
```

O PDF será gerado em `relatorio\text\main.pdf`.
