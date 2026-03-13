# Como compilar o relatório

O relatório é o arquivo **main.tex**. O PDF final é gerado com LaTeX.

## Pré-requisito

- **LaTeX instalado** (pdflatex no PATH). Se ainda não tiver:
  - **Windows:** `winget install MiKTeX.MiKTeX` (depois abra um terminal novo)
  - Ou baixe [MiKTeX](https://miktex.org/) ou [TeX Live](https://www.tug.org/texlive/)

## Compilar

Na pasta **relatorio/text/** (onde está o main.tex):

```bash
pdflatex main.tex
pdflatex main.tex
```

(O segundo comando atualiza sumário e referências.)

Ou use o script na raiz do projeto:

```bash
# Na raiz do projeto (CC8550---LAB-04)
.\compile_relatorio.ps1
```

O PDF gerado fica em **relatorio/text/main.pdf**.

## Figuras

- As **figuras dos GFC** geradas pelo Python estão em **relatorio/figuras/** (ex1_gfc.pdf … ex7_gfc.pdf).
- O **main.tex** hoje desenha os GFC com **TikZ** (dentro do próprio LaTeX). O `\graphicspath{{../figuras/}}` já está configurado; se quiser usar os PDFs gerados pelo script no lugar do TikZ, basta trocar cada bloco `\begin{tikzpicture}...\end{tikzpicture}` correspondente por `\includegraphics[width=\textwidth]{exN_gfc}` (N = 1 a 7).
