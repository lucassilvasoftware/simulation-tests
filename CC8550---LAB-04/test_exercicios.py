"""
Simulação e Teste de Software (CC8550)
Testes para Aula 04 - Critérios de cobertura estrutural

Aluno: Lucas Rebouças Silva
R.A: 22.122.048-6
"""

import pytest
from exercicios import (
    verificar, classificar, acesso, somar_ate,
    percorrer_matriz, analisar, desconto
)


# ============================================================================
# EXERCÍCIO 1 - Testes para Caminhos Independentes
# ============================================================================
class TestExercicio1:
    """
    Complexidade Ciclomática V(G) = 3
    Caminhos Independentes:
    1. n = 0 -> "Zero"
    2. n > 0 e n é par -> "Par positivo"
    3. n > 0 e n é impar -> "Impar positivo"
    4. n < 0 -> "Negativo"
    
    Nota: Existem 4 caminhos, então são necessários 4 testes para cobertura
    completa de todos os caminhos.
    """
    
    def test_zero(self):
        """Caminho 1: n = 0"""
        assert verificar(0) == "Zero"
    
    def test_par_positivo(self):
        """Caminho 2: n > 0 e n é par"""
        assert verificar(2) == "Par positivo"
        assert verificar(4) == "Par positivo"
        assert verificar(100) == "Par positivo"
    
    def test_impar_positivo(self):
        """Caminho 3: n > 0 e n é impar"""
        assert verificar(1) == "Impar positivo"
        assert verificar(3) == "Impar positivo"
        assert verificar(99) == "Impar positivo"
    
    def test_negativo(self):
        """Caminho 4: n < 0"""
        assert verificar(-1) == "Negativo"
        assert verificar(-100) == "Negativo"


# ============================================================================
# EXERCÍCIO 2 - Testes para Cobertura de Comandos (C0) e Ramos (C1)
# ============================================================================
class TestExercicio2:
    """
    Complexidade Ciclomática V(G) = 2
    
    Caminhos Independentes:
    1. x > 100 -> "Alto"
    2. 50 < x <= 100 -> "Medio"
    3. x <= 50 -> "Baixo"
    
    C0 (Cobertura de Comandos): 3 testes são suficientes para executar
    todos os comandos (3 returns diferentes).
    
    C1 (Cobertura de Ramos): 3 testes são necessários para cobrir todos
    os ramos da decisão.
    """
    
    def test_cobertura_alto(self):
        """C0 e C1: Ramo x > 100"""
        assert classificar(150) == "Alto"
        assert classificar(101) == "Alto"
    
    def test_cobertura_medio(self):
        """C0 e C1: Ramo 50 < x <= 100"""
        assert classificar(75) == "Medio"
        assert classificar(51) == "Medio"
        assert classificar(100) == "Medio"
    
    def test_cobertura_baixo(self):
        """C0 e C1: Ramo x <= 50"""
        assert classificar(50) == "Baixo"
        assert classificar(25) == "Baixo"
        assert classificar(0) == "Baixo"
        assert classificar(-10) == "Baixo"


# ============================================================================
# EXERCÍCIO 3 - Testes para Cobertura de Condição (CC)
# ============================================================================
class TestExercicio3:
    """
    Complexidade Ciclomática V(G) = 1
    Há UMA decisão com duas condições: (idade >= 18) AND (membro)
    
    Cobertura de Condição (CC):
    Todas as combinações da condição composta (idade >= 18) AND (membro):
    1. idade >= 18: True,  membro: True  -> "Permitido"
    2. idade >= 18: True,  membro: False -> "Negado"
    3. idade >= 18: False, membro: True  -> "Negado"
    4. idade >= 18: False, membro: False -> "Negado"
    
    São necessários 4 testes para cobrir todas as combinações (CC).
    
    Cobertura de Ramos (C1):
    Apenas 2 testes são suficientes para cobrir os dois ramos:
    - Ramo True (permissão): idade >= 18 AND membro
    - Ramo False (negação): qualquer outro caso
    """
    
    def test_cc_todas_verdadeiras(self):
        """CC: idade >= 18 (True), membro (True)"""
        assert acesso(18, True) == "Permitido"
        assert acesso(25, True) == "Permitido"
    
    def test_cc_idade_verdade_membro_falso(self):
        """CC: idade >= 18 (True), membro (False)"""
        assert acesso(20, False) == "Negado"
    
    def test_cc_idade_falso_membro_verdade(self):
        """CC: idade >= 18 (False), membro (True)"""
        assert acesso(17, True) == "Negado"
    
    def test_cc_todas_falsas(self):
        """CC: idade >= 18 (False), membro (False)"""
        assert acesso(16, False) == "Negado"
    
    def test_c1_ramo_permitido(self):
        """C1: Ramo True"""
        assert acesso(30, True) == "Permitido"
    
    def test_c1_ramo_negado(self):
        """C1: Ramo False"""
        assert acesso(20, False) == "Negado"


# ============================================================================
# EXERCÍCIO 4 - Testes para Ciclos
# ============================================================================
class TestExercicio4:
    """
    Complexidade Ciclomática V(G) = 2
    
    Estratégia de teste de ciclos:
    1. Laço ignorado (0 iterações): n = 0
    2. Laço executado uma única vez: n = 1
    3. Laço executado várias vezes: n > 1
    """
    
    def test_laco_ignorado(self):
        """Laço ignorado: 0 iterações, soma = 0"""
        assert somar_ate(0) == 0
    
    def test_laco_uma_iteracao(self):
        """Laço executado uma única vez: i = 0, soma = 0"""
        assert somar_ate(1) == 0
    
    def test_laco_duas_iteracoes(self):
        """Laço executado duas vezes: i = 0, 1, soma = 0 + 1 = 1"""
        assert somar_ate(2) == 1
    
    def test_laco_varias_iteracoes(self):
        """Laço executado várias vezes"""
        # range(5) = 0, 1, 2, 3, 4
        # soma = 0 + 1 + 2 + 3 + 4 = 10
        assert somar_ate(5) == 10
        # range(10) = 0 a 9
        # soma = 0 + 1 + ... + 9 = 45
        assert somar_ate(10) == 45


# ============================================================================
# EXERCÍCIO 5 - Testes para Ciclos Aninhados
# ============================================================================
class TestExercicio5:
    """
    Complexidade Ciclomática V(G) = 3
    
    Estratégia de teste para ciclos aninhados:
    1. Ambos os laços são ignorados (0 x 0)
    2. Apenas laço j é ignorado (m x 0)
    3. Um laço executa uma vez, outro várias (1 x n, m x 1)
    4. Ambos os laços executam várias vezes (m x n)
    """
    
    def test_ambos_lacos_ignorados(self):
        """Ambos os laços ignorados: 0 x 0"""
        resultado = percorrer_matriz(0, 0)
        assert resultado == []
        assert len(resultado) == 0
    
    def test_apenas_coluna_ignorada(self):
        """Apenas laço j ignorado: m x 0"""
        resultado = percorrer_matriz(3, 0)
        assert resultado == []
        assert len(resultado) == 0
    
    def test_apenas_linha_ignorada(self):
        """Apenas laço i ignorado: 0 x n"""
        resultado = percorrer_matriz(0, 3)
        assert resultado == []
        assert len(resultado) == 0
    
    def test_uma_linha_varias_colunas(self):
        """Uma linha executa uma vez, várias colunas: 1 x 3"""
        resultado = percorrer_matriz(1, 3)
        assert resultado == [(0, 0), (0, 1), (0, 2)]
        assert len(resultado) == 3  # 1 * 3 = 3 iterações
    
    def test_varias_linhas_uma_coluna(self):
        """Várias linhas, uma coluna executa uma vez: 3 x 1"""
        resultado = percorrer_matriz(3, 1)
        assert resultado == [(0, 0), (1, 0), (2, 0)]
        assert len(resultado) == 3  # 3 * 1 = 3 iterações
    
    def test_ambos_lacos_varias_iteracoes(self):
        """Ambos os laços executam várias vezes: 2 x 3"""
        resultado = percorrer_matriz(2, 3)
        esperado = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        assert resultado == esperado
        assert len(resultado) == 6  # 2 * 3 = 6 iterações
    
    def test_matriz_4x5(self):
        """Matriz 4 x 5"""
        resultado = percorrer_matriz(4, 5)
        assert len(resultado) == 20  # 4 * 5 = 20 iterações
        assert resultado[0] == (0, 0)
        assert resultado[-1] == (3, 4)


# ============================================================================
# EXERCÍCIO 6 - Testes Completos (Integrador)
# ============================================================================
class TestExercicio6:
    """
    Complexidade Ciclomática V(G) = 4
    
    Fluxos:
    1. Ciclo com n > 0 e n % 2 == 0 -> total += n
    2. Ciclo com n < 0 -> total -= 1
    3. Ciclo com outros casos -> continue
    4. Decisão final: total > 10 -> "Acima", senão "Abaixo"
    
    Testes cobrem:
    - C0: Cobertura de comandos
    - C1: Cobertura de ramos
    - CC: Cobertura de condições
    - Comportamentos do laço: 0, 1 e várias iterações
    """
    
    def test_lista_vazia(self):
        """Laço ignorado (0 iterações): total = 0 -> "Abaixo" """
        assert analisar([]) == "Abaixo"
    
    def test_um_par_positivo(self):
        """1 iteração: um número par positivo"""
        # total = 0 + 2 = 2 -> "Abaixo"
        assert analisar([2]) == "Abaixo"
    
    def test_um_impar_positivo(self):
        """1 iteração: um número impar positivo -> continue"""
        # total = 0 (não muda) -> "Abaixo"
        assert analisar([1]) == "Abaixo"
    
    def test_um_negativo(self):
        """1 iteração: um número negativo"""
        # total = 0 - 1 = -1 -> "Abaixo"
        assert analisar([-5]) == "Abaixo"
    
    def test_multiplos_pares_positivos(self):
        """Várias iterações: múltiplos pares positivos -> total > 10"""
        # total = 0 + 6 + 8 = 14 -> "Acima"
        assert analisar([6, 8]) == "Acima"
    
    def test_mix_pares_impares_positivos(self):
        """Várias iterações: mistura de pares e ímpares"""
        # 4 (par), 3 (ímpar->continue), 8 (par) -> total = 4 + 8 = 12
        assert analisar([4, 3, 8]) == "Acima"
    
    def test_pares_com_negativos(self):
        """Várias iterações: pares e negativos"""
        # 6 (par), -2 (negativo -> -1), 8 (par)
        # total = 6 - 1 + 8 = 13 -> "Acima"
        assert analisar([6, -2, 8]) == "Acima"
    
    def test_total_baixo(self):
        """Total não ultrapassa 10"""
        # 2 (par), 4 (par), 1 (impar) -> total = 2 + 4 = 6 -> "Abaixo"
        assert analisar([2, 4, 1]) == "Abaixo"
    
    def test_somente_negativos(self):
        """Apenas negativos"""
        # -1, -1, -1 -> total = -3 -> "Abaixo"
        assert analisar([-1, -1, -1]) == "Abaixo"
    
    def test_zero_e_pares(self):
        """Zero (continua) e pares"""
        # 0 (continue), 6 (par), 8 (par) -> total = 14 -> "Acima"
        assert analisar([0, 6, 8]) == "Acima"


# ============================================================================
# EXERCÍCIO 7 - Testes para Fluxo de Dados
# ============================================================================
class TestExercicio7:
    """
    Análise de Definições (def) e Usos (use):
    
    Variáveis e seus def-uso:
    
    total:
      - def: linha 2 (total = preco)
      - use: linha 5 (total = preco - desconto)
      - use: linha 6 (if total < 50)
      - def: linha 7 (total = 50)
      - use: linha 8 (return total)
    
    desconto (ou desconto_valor):
      - def: linha 4 (desconto = preco * 0.2)
      - use: linha 5 (total = preco - desconto)
    
    preco:
      - use: linha 2 (total = preco) [parâmetro]
      - use: linha 4 (desconto = preco * 0.2)
      - use: linha 5 (total = preco - desconto)
    
    cliente_vip:
      - use: linha 3 (if cliente_vip) [parâmetro]
    
    Pares def-uso (du-pairs):
    1. (2, 5): total definido na linha 2, usado na linha 5
    2. (2, 6): total definido na linha 2, usado na linha 6
    3. (2, 8): total definido na linha 2, usado na linha 8 (via linha 7)
    4. (5, 6): total redefinido na linha 5, usado na linha 6
    5. (5, 8): total redefinido na linha 5, usado na linha 8
    6. (7, 8): total redefinido na linha 7, usado na linha 8
    7. (4, 5): desconto definido na linha 4, usado na linha 5
    
    All-Defs: Pelo menos uma def-use para cada definição
    All-Uses: Todas as definições e seus usos devem ser cobertos
    """
    
    def test_alldef_cliente_nao_vip_preco_alto(self):
        """All-Defs: não VIP, preço alto"""
        # Cobre def em linha 2
        resultado = desconto(100, False)
        assert resultado == 100
    
    def test_alldef_cliente_nao_vip_preco_baixo(self):
        """All-Defs: não VIP, preço baixo (testa linha 7)"""
        # Cobre def em linha 2 e 7
        resultado = desconto(40, False)
        assert resultado == 50
    
    def test_alldef_cliente_vip_preco_alto(self):
        """All-Defs: cliente VIP, preço alto"""
        # Cobre def em linha 2 e 5
        resultado = desconto(100, True)
        assert resultado == 80.0
    
    def test_alldef_cliente_vip_preco_baixo(self):
        """All-Defs: cliente VIP, preço baixo"""
        # Cobre def em linha 2, 5 e 7
        resultado = desconto(40, True)
        assert resultado == 50
    
    def test_alluses_vip_desconto_pequeno(self):
        """All-Uses: VIP com desconto resultando em valor < 50"""
        # Cobre: def(2), use(5), def(5), use(6), def(7), use(8)
        resultado = desconto(60, True)
        assert resultado == 50
    
    def test_alluses_vip_desconto_grande(self):
        """All-Uses: VIP com desconto resultando em valor >= 50"""
        # Cobre: def(2), use(5), def(5), use(6), use(8)
        resultado = desconto(100, True)
        assert resultado == 80.0
    
    def test_alluses_nao_vip(self):
        """All-Uses: não VIP (pula linha 4 e 5)"""
        # Cobre: def(2), use(6), use(8)
        resultado = desconto(60, False)
        assert resultado == 60
    
    def test_pares_def_uso_especificos(self):
        """Testa pares def-uso específicos"""
        # (2, 6): def em 2, use em 6
        resultado1 = desconto(30, False)
        assert resultado1 == 50
        
        # (5, 8): def em 5, use em 8
        resultado2 = desconto(150, True)
        assert resultado2 == 120.0
        
        # (7, 8): def em 7, use em 8
        resultado3 = desconto(40, False)
        assert resultado3 == 50


# ============================================================================
# Testes de Integração
# ============================================================================
class TestIntegracao:
    """Testes adicionais de integração e edge cases"""
    
    def test_exercicio1_valores_limites(self):
        """Testa valores limites para ex1"""
        assert verificar(-1) == "Negativo"
        assert verificar(1) == "Impar positivo"
        assert verificar(2) == "Par positivo"
    
    def test_exercicio2_valores_limites(self):
        """Testa valores limites para ex2"""
        assert classificar(100) == "Medio"
        assert classificar(101) == "Alto"
        assert classificar(50) == "Baixo"
        assert classificar(51) == "Medio"
    
    def test_exercicio3_valores_limites(self):
        """Testa valores limites para ex3"""
        assert acesso(18, True) == "Permitido"  # Limite exato
        assert acesso(17, True) == "Negado"     # Um abaixo do limite


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
