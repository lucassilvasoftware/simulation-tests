#!/usr/bin/env python3
"""
Script para gerar visualizacoes dos grafos de fluxo de controle.
Requer: pip install matplotlib networkx
"""

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

def criar_grafo_exercicio1():
    """Grafo do Exercicio 1 - Caminhos Independentes"""
    G = nx.DiGraph()
    pos = {
        'entrada': (0, 5),
        'd1': (0, 4),
        'd2': (-1.5, 3),
        'r1': (-1.5, 2),
        'r2': (0, 2),
        'd3': (1.5, 3),
        'r3': (1.5, 2),
        'r4': (3, 2),
        'saida': (1.5, 0),
    }
    
    G.add_edges_from([
        ('entrada', 'd1'),
        ('d1', 'd2'), ('d1', 'd3'),
        ('d2', 'r1'), ('d2', 'r2'),
        ('d3', 'r3'), ('d3', 'r4'),
        ('r1', 'saida'), ('r2', 'saida'), ('r3', 'saida'), ('r4', 'saida'),
    ])
    
    return G, pos, 'Exercicio 1 - Caminhos Independentes'

def criar_grafo_exercicio2():
    """Grafo do Exercicio 2 - Cobertura C0 e C1"""
    G = nx.DiGraph()
    pos = {
        'entrada': (0, 4),
        'd1': (0, 3),
        'r1': (-1, 2),
        'd2': (1, 2),
        'r2': (1, 1),
        'r3': (3, 1),
        'saida': (1, 0),
    }
    
    G.add_edges_from([
        ('entrada', 'd1'),
        ('d1', 'r1'), ('d1', 'd2'),
        ('d2', 'r2'), ('d2', 'r3'),
        ('r1', 'saida'), ('r2', 'saida'), ('r3', 'saida'),
    ])
    
    return G, pos, 'Exercicio 2 - Cobertura de Comandos e Ramos'

def criar_grafo_exercicio3():
    """Grafo do Exercicio 3 - Cobertura de Condicao"""
    G = nx.DiGraph()
    pos = {
        'entrada': (0, 3),
        'd1': (0, 2),
        'r1': (-1, 1),
        'r2': (1, 1),
        'saida': (0, 0),
    }
    
    G.add_edges_from([
        ('entrada', 'd1'),
        ('d1', 'r1'), ('d1', 'r2'),
        ('r1', 'saida'), ('r2', 'saida'),
    ])
    
    return G, pos, 'Exercicio 3 - Cobertura de Condicao'

def criar_grafo_exercicio4():
    """Grafo do Exercicio 4 - Teste de Ciclo"""
    G = nx.DiGraph()
    pos = {
        'entrada': (0, 5),
        'init': (0, 4),
        'loop': (0, 3),
        'soma': (0, 2),
        'return': (2, 3),
        'saida': (2, 0),
    }
    
    G.add_edges_from([
        ('entrada', 'init'),
        ('init', 'loop'),
        ('loop', 'soma'), ('loop', 'return'),
        ('soma', 'loop'),
        ('return', 'saida'),
    ])
    
    return G, pos, 'Exercicio 4 - Teste de Ciclo'

def plotar_grafo(G, pos, titulo, nome_arquivo):
    """Plota e salva um grafo"""
    plt.figure(figsize=(10, 8))
    
    # Desenhar no??s
    node_colors = []
    for node in G.nodes():
        if 'entrada' in node or 'saida' in node:
            node_colors.append('#90EE90')  # Verde
        elif 'd' in node:
            node_colors.append('#FFB6C1')  # Rosa (decisao)
        else:
            node_colors.append('#87CEEB')  # Azul (retorno)
    
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000)
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, 
                          arrowsize=20, arrowstyle='->', width=2)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Salvo: {nome_arquivo}")

def main():
    """Gera todos os grafos"""
    print("Gerando visualizacoes dos grafos de fluxo de controle...\n")
    
    grafos = [
        criar_grafo_exercicio1(),
        criar_grafo_exercicio2(),
        criar_grafo_exercicio3(),
        criar_grafo_exercicio4(),
    ]
    
    for i, (G, pos, titulo) in enumerate(grafos, 1):
        nome = f'grafo_ex{i}.png'
        plotar_grafo(G, pos, titulo, nome)
    
    print("\nGrafos gerados com sucesso!")
    print("Arquivos PNG criados:")
    print("  - grafo_ex1.png: Exercicio 1")
    print("  - grafo_ex2.png: Exercicio 2")
    print("  - grafo_ex3.png: Exercicio 3")
    print("  - grafo_ex4.png: Exercicio 4")
    print("\nNota: Os exercicios 5, 6 e 7 possuem grafos no relatorio.tex")

if __name__ == '__main__':
    main()
