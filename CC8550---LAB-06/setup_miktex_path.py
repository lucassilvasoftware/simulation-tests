"""
Localiza pdflatex (MiKTeX no Windows), adiciona o diretório ao PATH da sessão
e opcionalmente compila relatorio.tex.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def candidate_dirs() -> list[Path]:
    local = os.environ.get("LOCALAPPDATA", "")
    return [
        Path(r"C:\Program Files\MiKTeX\miktex\bin\x64"),
        Path(local) / "Programs" / "MiKTeX" / "miktex" / "bin" / "x64",
        Path(r"C:\Program Files\MiKTeX 24\miktex\bin\x64"),
    ]


def find_pdflatex() -> Path | None:
    which = shutil.which("pdflatex")
    if which:
        return Path(which)
    for d in candidate_dirs():
        exe = d / "pdflatex.exe"
        if exe.is_file():
            return exe
    return None


def prepend_path(bin_dir: Path) -> None:
    sep = os.pathsep
    os.environ["PATH"] = str(bin_dir) + sep + os.environ.get("PATH", "")


def main() -> int:
    parser = argparse.ArgumentParser(description="MiKTeX: PATH da sessão + compile opcional")
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Executa pdflatex duas vezes em relatorio.tex (diretório do script)",
    )
    args = parser.parse_args()

    exe = find_pdflatex()
    if not exe:
        print("pdflatex não encontrado (PATH nem pastas padrão MiKTeX).", file=sys.stderr)
        print("Instale MiKTeX ou adicione o binário ao PATH do sistema.", file=sys.stderr)
        return 1

    prepend_path(exe.parent)
    print(f"OK: usando {exe}")
    print(f"PATH (início da sessão): ...{exe.parent}")

    if args.compile:
        root = Path(__file__).resolve().parent
        tex = root / "relatorio.tex"
        if not tex.is_file():
            print(f"Arquivo não encontrado: {tex}", file=sys.stderr)
            return 1
        for i in range(2):
            print(f"pdflatex passagem {i + 1}/2...")
            r = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", str(tex.name)],
                cwd=root,
            )
            if r.returncode != 0:
                return r.returncode
        pdf = root / "relatorio.pdf"
        print(f"PDF gerado (se sem erros LaTeX): {pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
