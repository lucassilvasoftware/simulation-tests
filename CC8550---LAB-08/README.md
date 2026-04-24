# CC8550 - LAB 08: Suite de Testes para API REST

**Aluno:** Lucas Reboucas Silva  
**R.A.:** 22.122.048-6  
**Disciplina:** CC8550 - Simulacao e Teste de Software (Centro Universitario FEI)  
**Professor:** Luciano Rossi

## API escolhida

- **Nome:** DummyJSON
- **Documentacao:** [https://dummyjson.com/docs](https://dummyjson.com/docs)

## Justificativa da escolha

A DummyJSON foi escolhida por possuir endpoints HTTP claros para leitura, criacao, atualizacao e exclusao simulada de recursos, alem de endpoint de autenticacao (`/auth/login`). Isso permite cobrir os requisitos da atividade com uma unica API publica e documentada, sem chave obrigatoria.

## Estrutura do laboratorio

- `test_api.py`: suite de testes automatizados com `pytest`.
- `requirements.txt`: dependencias obrigatorias.
- `relatorio.tex`: documentacao academica em LaTeX.
- `compile_relatorio.ps1`: script para compilar o PDF do relatorio.
- `relatorio.pdf`: versao compilada do relatorio.

## Instalacao

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Execucao dos testes

```bash
pytest test_api.py -v
```

Salvar resultado:

```bash
pytest test_api.py -v > resultado.txt
```

## Testes implementados

1. **GET em colecao** (`/posts`) -> status 200 e lista nao vazia.
2. **GET em recurso existente** (`/posts/1`) -> validacao de schema com `jsonschema`.
3. **GET em recurso inexistente** (`/posts/0`) -> status 404.
4. **POST criando recurso** (`/posts/add`) -> status 201 e `id` no retorno.
5. **PATCH atualizando recurso** (`/posts/1`) -> campo `title` alterado.
6. **DELETE** (`/posts/1`) -> status 200 ou 204.
7. **Dados invalidos** (`/auth/login` sem senha) -> status 4xx (400).
8. **Autenticacao com e sem credencial** (`/auth/login`) -> sucesso com token e falha sem senha.
9. **Uso de fixture** (`@pytest.fixture`) -> payload reutilizavel nos testes.
10. **Tempo de resposta** (`/posts/1`) -> menor que 2,0 s.
