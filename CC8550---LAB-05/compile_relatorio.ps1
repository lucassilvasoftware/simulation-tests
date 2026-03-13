# Compila o relatorio LaTeX (main.tex) em relatorio/text/
# Uso: .\compile_relatorio.ps1   (na raiz do projeto)
# Requer: LaTeX instalado (MiKTeX ou TeX Live). Ex.: winget install MiKTeX.MiKTeX

$ErrorActionPreference = "Stop"
$textDir = Join-Path $PSScriptRoot "relatorio\text"
$mainTex = Join-Path $textDir "main.tex"

if (-not (Test-Path $mainTex)) {
    Write-Error "Arquivo nao encontrado: $mainTex"
}
$pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
if (-not $pdflatex) {
    $miktexBin = Join-Path $env:LOCALAPPDATA "Programs\MiKTeX\miktex\bin\x64"
    if (Test-Path (Join-Path $miktexBin "pdflatex.exe")) {
        $env:Path = $miktexBin + ";" + $env:Path
    } else {
        Write-Host "pdflatex nao encontrado. Instale LaTeX (ex.: winget install MiKTeX.MiKTeX) e tente novamente." -ForegroundColor Yellow
        exit 1
    }
}

Push-Location $textDir
try {
    Write-Host "Compilando main.tex (pdflatex)..." -ForegroundColor Cyan
    & pdflatex -interaction=nonstopmode main.tex
    if ($LASTEXITCODE -ne 0) { throw "pdflatex falhou com codigo $LASTEXITCODE" }
    Write-Host "Segunda passagem (sumario/refs)..." -ForegroundColor Cyan
    & pdflatex -interaction=nonstopmode main.tex
    if ($LASTEXITCODE -ne 0) { throw "pdflatex falhou com codigo $LASTEXITCODE" }
    $pdf = Join-Path $textDir "main.pdf"
    Write-Host "OK. Relatorio gerado: $pdf" -ForegroundColor Green
} finally {
    Pop-Location
}
