"""
CC8550 - Aula 04: Geração dos Grafos de Fluxo de Controle (GFC) com Graphviz.
Gera PDF em relatorio/figuras/ (caminho relativo à raiz do projeto).
Requer: pip install graphviz e Graphviz instalado no sistema.
"""
import os
import sys
from pathlib import Path

# No Windows, se dot não estiver no PATH, tenta o instalador winget padrão
if sys.platform == "win32":
    _graphviz_bin = Path(r"C:\Program Files\Graphviz\bin")
    if _graphviz_bin.is_dir() and "Graphviz" not in os.environ.get("PATH", ""):
        os.environ["PATH"] = str(_graphviz_bin) + os.pathsep + os.environ.get("PATH", "")

# Diretório de saída: relatorio/figuras/ (raiz do projeto = pai de scripts/)
RAIZ = Path(__file__).resolve().parent.parent
OUT_DIR = RAIZ / "relatorio" / "figuras"


def _digraph():
    """Cria um Digraph do graphviz (import sob demanda para não quebrar sem o pacote)."""
    try:
        from graphviz import Digraph
        return Digraph
    except ImportError:
        raise ImportError("Instale graphviz: pip install graphviz. E instale o binário Graphviz no sistema.")


def gfc_ex1():
    """Exercício 1: verificar(n) - 9 nós, 10 arestas, V(G)=3."""
    D = _digraph()(format="pdf", name="Ex1")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("d1", "n > 0?", shape="diamond")
    D.node("d2", "n % 2 == 0?", shape="diamond")
    D.node("r1", "Return Par positivo", shape="box")
    D.node("r2", "Return Impar positivo", shape="box")
    D.node("d3", "n < 0?", shape="diamond")
    D.node("r3", "Return Negativo", shape="box")
    D.node("r4", "Return Zero", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "d1")
    D.edge("d1", "d2", label="V")
    D.edge("d1", "d3", label="F")
    D.edge("d2", "r1", label="V")
    D.edge("d2", "r2", label="F")
    D.edge("d3", "r3", label="V")
    D.edge("d3", "r4", label="F")
    for n in ["r1", "r2", "r3", "r4"]:
        D.edge(n, "saida")
    return D, 3


def gfc_ex2():
    """Exercício 2: classificar(x) - 7 nós, 8 arestas, V(G)=3."""
    D = _digraph()(format="pdf", name="Ex2")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("d1", "x > 100?", shape="diamond")
    D.node("r1", "Return Alto", shape="box")
    D.node("d2", "x > 50?", shape="diamond")
    D.node("r2", "Return Medio", shape="box")
    D.node("r3", "Return Baixo", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "d1")
    D.edge("d1", "r1", label="V")
    D.edge("d1", "d2", label="F")
    D.edge("d2", "r2", label="V")
    D.edge("d2", "r3", label="F")
    for n in ["r1", "r2", "r3"]:
        D.edge(n, "saida")
    return D, 3


def gfc_ex3():
    """Exercício 3: acesso(idade, membro) - 5 nós, 6 arestas, V(G)=2."""
    D = _digraph()(format="pdf", name="Ex3")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("d1", "idade>=18 AND membro?", shape="diamond")
    D.node("r1", "Return Permitido", shape="box")
    D.node("r2", "Return Negado", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "d1")
    D.edge("d1", "r1", label="V")
    D.edge("d1", "r2", label="F")
    D.edge("r1", "saida")
    D.edge("r2", "saida")
    return D, 2


def gfc_ex4():
    """Exercício 4: somar_ate(n) - 6 nós, 7 arestas, V(G)=2."""
    D = _digraph()(format="pdf", name="Ex4")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("init", "soma = 0", shape="box")
    D.node("loop", "for i in range(n)", shape="diamond")
    D.node("body", "soma += i", shape="box")
    D.node("ret", "return soma", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "init")
    D.edge("init", "loop")
    D.edge("loop", "body", label="iter")
    D.edge("body", "loop")
    D.edge("loop", "ret", label="sai")
    D.edge("ret", "saida")
    return D, 2


def gfc_ex5():
    """Exercício 5: percorrer_matriz(m, n) - 7 nós, 9 arestas, V(G)=3."""
    D = _digraph()(format="pdf", name="Ex5")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("init", "posicoes = []", shape="box")
    D.node("loop1", "for i in range(m)", shape="diamond")
    D.node("loop2", "for j in range(n)", shape="diamond")
    D.node("body", "append((i,j))", shape="box")
    D.node("ret", "return posicoes", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "init")
    D.edge("init", "loop1")
    D.edge("loop1", "loop2", label="i<m")
    D.edge("loop2", "body", label="j<n")
    D.edge("body", "loop2")
    D.edge("loop2", "loop1")
    D.edge("loop1", "ret", label="sai")
    D.edge("ret", "saida")
    return D, 3


def gfc_ex6():
    """Exercício 6: analisar(numeros) - V(G)=4."""
    D = _digraph()(format="pdf", name="Ex6")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("init", "total = 0", shape="box")
    D.node("loop", "for n in numeros", shape="diamond")
    D.node("d1", "n>0 AND n%2==0?", shape="diamond")
    D.node("soma", "total += n", shape="box")
    D.node("d2", "n < 0?", shape="diamond")
    D.node("sub", "total -= 1", shape="box")
    D.node("cont", "continue", shape="box")
    D.node("d3", "total > 10?", shape="diamond")
    D.node("r1", "Return Acima", shape="box")
    D.node("r2", "Return Abaixo", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "init")
    D.edge("init", "loop")
    D.edge("loop", "d1", label="iter")
    D.edge("d1", "soma", label="V")
    D.edge("d1", "d2", label="F")
    D.edge("d2", "sub", label="V")
    D.edge("d2", "cont", label="F")
    D.edge("soma", "d3")
    D.edge("sub", "d3")
    D.edge("cont", "d3")
    D.edge("loop", "d3", label="sai")
    D.edge("d3", "r1", label="V")
    D.edge("d3", "r2", label="F")
    D.edge("r1", "saida")
    D.edge("r2", "saida")
    return D, 4


def gfc_ex7():
    """Exercício 7: desconto(preco, cliente_vip) - V(G)=2."""
    D = _digraph()(format="pdf", name="Ex7")
    D.attr(rankdir="TB", fontname="Arial")
    D.node("entrada", "Entrada", shape="ellipse")
    D.node("d2", "total = preco", shape="box")
    D.node("d3", "cliente_vip?", shape="diamond")
    D.node("d4", "desconto = preco*0.2", shape="box")
    D.node("d5", "total = preco - desc", shape="box")
    D.node("d6", "total < 50?", shape="diamond")
    D.node("d7", "total = 50", shape="box")
    D.node("d8", "return total", shape="box")
    D.node("saida", "Saída", shape="ellipse")
    D.edge("entrada", "d2")
    D.edge("d2", "d3")
    D.edge("d3", "d4", label="V")
    D.edge("d3", "d6", label="F")
    D.edge("d4", "d5")
    D.edge("d5", "d6")
    D.edge("d6", "d7", label="V")
    D.edge("d6", "d8", label="F")
    D.edge("d7", "d8")
    D.edge("d8", "saida")
    return D, 2


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    geradores = [
        (1, gfc_ex1),
        (2, gfc_ex2),
        (3, gfc_ex3),
        (4, gfc_ex4),
        (5, gfc_ex5),
        (6, gfc_ex6),
        (7, gfc_ex7),
    ]
    for num, func in geradores:
        g, vg = func()
        path = OUT_DIR / f"ex{num}_gfc"
        try:
            g.render(path, cleanup=True)
            print(f"Exercício {num}: gerado {path}.pdf  V(G) = {vg}")
        except Exception as e:
            exc_name = type(e).__name__
            if "ExecutableNotFound" in exc_name or "dot" in str(e).lower() or "PATH" in str(e):
                dot_path = path.with_suffix(".dot")
                g.save(str(dot_path))
                print(f"Exercício {num}: Graphviz (dot) não encontrado. Salvo {dot_path}  V(G) = {vg}")
                print("  Instale Graphviz (ex.: winget install Graphviz.Graphviz) e execute de novo para gerar PDF.")
            else:
                raise
    print(f"\nSaída em: {OUT_DIR}")


if __name__ == "__main__":
    main()
