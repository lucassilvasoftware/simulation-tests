# Scripts - CC8550 Aula 04

## Uso

- **Testes:** na pasta `scripts/`, execute:
  ```bash
  python -m pytest test_exercicios.py -v
  ```

- **Gerar GFC (grafos):** na raiz do projeto ou em `scripts/`:
  ```bash
  python scripts/gerar_grafos.py
  ```
  Saída em `relatorio/figuras/` (PDF se o Graphviz estiver instalado; caso contrário, arquivos `.dot`).
  Para instalar o Graphviz no Windows: `winget install Graphviz.Graphviz` (e reinicie o terminal).

- **Dependências:** `pip install -r scripts/requirements.txt`
