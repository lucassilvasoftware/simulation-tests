# Compila relatorio.tex na raiz do LAB-08 (duas passagens).
# Uso: .\compile_relatorio.ps1

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$tex = Join-Path $root "relatorio.tex"

if (-not (Test-Path $tex)) {
    Write-Error "Arquivo nao encontrado: $tex"
}

$pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
if (-not $pdflatex) {
    $candidates = @(
        "C:\Program Files\MiKTeX\miktex\bin\x64",
        (Join-Path $env:LOCALAPPDATA "Programs\MiKTeX\miktex\bin\x64")
    )
    foreach ($dir in $candidates) {
        if (Test-Path (Join-Path $dir "pdflatex.exe")) {
            $env:Path = $dir + ";" + $env:Path
            break
        }
    }
    $pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
}

if (-not $pdflatex) {
    Write-Host "pdflatex nao encontrado. Instale o MiKTeX ou ajuste o PATH." -ForegroundColor Yellow
    exit 1
}

Push-Location $root
try {
    Write-Host "Compilando relatorio.tex..." -ForegroundColor Cyan
    & pdflatex -interaction=nonstopmode relatorio.tex
    if ($LASTEXITCODE -ne 0) { throw "pdflatex falhou ($LASTEXITCODE)" }
    & pdflatex -interaction=nonstopmode relatorio.tex
    if ($LASTEXITCODE -ne 0) { throw "pdflatex falhou ($LASTEXITCODE)" }
    Write-Host "OK: $(Join-Path $root 'relatorio.pdf')" -ForegroundColor Green
}
finally {
    Pop-Location
}
