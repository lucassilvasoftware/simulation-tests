# Cobertura estrutural (caixa-branca) — guia de estudo

Linguagem direta para fixar a matéria da Aula 04.

---

## O que é teste caixa-branca?

No teste **caixa-branca** (estrutural) a gente **olha o código por dentro**. O objetivo é escolher casos de teste com base na **estrutura** do programa (ifs, laços, ramos), e não só na especificação. É o oposto do teste caixa-preta, em que só importa a entrada e a saída.

---

## Grafo de Fluxo de Controle (GFC)

O **GFC** é um desenho do “caminho do controle” no programa: **por onde** o fluxo pode passar, sem se importar com os dados em si.

- **Nós (vértices):**
  - **Entrada** e **Saída**: início e fim da função.
  - **Decisão**: um `if`, `elif` ou condição do `for`/`while` — em geral desenhado como **losango** (tem dois caminhos: V e F).
  - **Comando**: um bloco de ação (atribuição, `return`, `continue`) — em geral **retângulo**.
- **Arestas (setas):** indicam “quem vem depois de quem”. De cada decisão saem duas arestas: uma para o ramo **verdadeiro** e outra para o **falso**.

Montar o GFC: coloque Entrada no topo, leia o código de cima para baixo, crie um losango para cada decisão e um retângulo para cada ação; todas as sequências que terminam a função vão para o nó Saída.

---

## Complexidade ciclomática V(G)

A **complexidade ciclomática** mede quantos “caminhos independentes” existem no programa.

**Fórmula:**  
`V(G) = arestas − nós + 2`  
(considerando um único componente conexo; em uma função, p = 1.)

**Alternativa:**  
`V(G) = número de decisões + 1`

**O que isso significa:** V(G) dá um **mínimo** de testes necessários para exercitar caminhos estruturalmente diferentes. Não garante que você testou tudo, mas menos que isso deixa caminhos sem cobertura.

---

## Caminhos independentes

São caminhos no GFC que **não são combinação linear** de outros. Em termos práticos: cada um “acrescenta” uma nova região ou desvio. O número de caminhos independentes é exatamente **V(G)**. Uma suíte de testes que cubra todos os caminhos independentes atinge uma cobertura estrutural forte (cobertura de caminhos básica).

---

## Cobertura de comandos (C0)

**Regra:** toda **linha** (todo comando/statement) do programa deve ser **executada pelo menos uma vez**.

É o critério mais fraco: só exige que nenhuma linha fique sem ser tocada. Não exige que todos os ramos dos `if` tenham sido exercitados.

---

## Cobertura de ramos (C1)

**Regra:** todo **ramo** de cada decisão deve ser executado. Ou seja: para cada `if`/`elif`/`else`, pelo menos um teste em que a condição seja **verdadeira** e outro em que seja **falsa**.

C1 é mais forte que C0: para cobrir ramos você acaba executando todos os comandos, mas além disso garante que cada “sim/não” de cada decisão foi testado. Em geral C1 exige **no mínimo** tantos testes quanto C0, às vezes mais.

---

## Cobertura de condição (CC)

**Regra:** em condições **compostas** (com `and` ou `or`), cada **subcondição** deve assumir os valores **verdadeiro** e **falso** em algum teste.

Exemplo: `if idade >= 18 and membro`. C1 só exige que a decisão inteira seja V em um teste e F em outro. CC exige que “idade >= 18” seja V e F, e que “membro” seja V e F (em combinações possíveis). Com duas condições binárias, isso pode exigir até 2² = 4 testes.

**Diferença para C1:** C1 olha a decisão como um todo; CC olha **cada pedaço** da condição. CC é mais rigoroso e pode exigir mais casos de teste.

---

## Teste de ciclos

Para **laços** (for/while), é importante testar:

1. **Zero iterações** — o laço não entra (ex.: `range(0)`).
2. **Uma iteração** — o laço executa exatamente uma vez.
3. **Várias iterações** — o laço executa mais de uma vez.

Assim você cobre “não entrar”, “entrar uma vez” e “repetir”, que são comportamentos estruturais diferentes. Em laços aninhados, o número total de passagens pelo corpo é o **produto** das dimensões (ex.: m×n).

---

## Fluxo de dados (def e uso)

- **Definição (def):** ponto onde uma variável **recebe** um valor (atribuição, parâmetro, etc.).
- **Uso (use):** ponto onde o **valor** da variável é lido (em uma expressão, condição ou return).
- **Par def-uso (du-pair):** um par (definição, uso) tal que existe um caminho no programa da def até o use sem nova definição da mesma variável no meio.

**All-Defs:** para cada definição, existe pelo menos um teste que “cobre” essa def até algum uso (ou seja, exercita um caminho def→uso).

**All-Uses:** para cada uso, existe pelo menos um teste em que esse uso é alcançado por alguma definição (cobre pelo menos um du-pair que termina nesse uso).

Pode existir **par def-uso que C1 não cobre**: C1 só garante ramos (V/F), não garante que um valor definido em um ramo seja usado em outro caminho específico. All-Defs/All-Uses olham o fluxo de dados explicitamente.

---

## Hierarquia dos critérios

Em termos de rigor (e em geral de quantidade de testes):

**C0 (comandos) ≤ C1 (ramos) ≤ CC (condições) ≤ cobertura de caminhos**

- C0: menos exigente.
- C1: padrão industrial para cobertura estrutural.
- CC: mais exigente em condições compostas.
- Cobertura de caminhos: pode ser exponencial no número de decisões.

**All-Defs** e **All-Uses** são critérios de **fluxo de dados**; não ficam na mesma “reta” que C0/C1/CC, mas em geral All-Defs é alcançável com um conjunto de testes de tamanho razoável, e All-Uses pode exigir mais testes que C1.

---

## Resumo em uma frase por conceito

| Conceito | Em uma linha |
|----------|----------------|
| Caixa-branca | Teste baseado na estrutura do código. |
| GFC | Grafo que mostra por onde o controle pode passar (nós = entrada, saída, decisão, comando; arestas = sequência). |
| V(G) | Número de caminhos independentes; mínimo de testes para cobrir estruturalmente. |
| C0 | Toda linha executada ao menos uma vez. |
| C1 | Todo ramo (V e F) de cada decisão executado. |
| CC | Cada subcondição (em and/or) assume V e F em algum teste. |
| Ciclos | Testar 0, 1 e várias iterações. |
| Def/uso | Def = onde a variável recebe valor; uso = onde o valor é lido; All-Defs/All-Uses cobrem pares def→uso. |
