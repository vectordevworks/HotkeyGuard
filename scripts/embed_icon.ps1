
$ErrorActionPreference = "Stop"

# ============================================================
# SHORTCUT BLOCKER - PATH CONFIGURATION
# ============================================================

$ProjectDir = Split-Path -Parent $PSScriptRoot

$MainFile = Join-Path $ProjectDir "ShortcutBlocker.pyw"
$IconFile = Join-Path $ProjectDir "assets\icon.png"
$DistDir = Join-Path $ProjectDir "dist"
$BuildDir = Join-Path $ProjectDir "build"

Write-Host ""
Write-Host "========================================"
Write-Host " SHORTCUT BLOCKER - BUILD"
Write-Host " VECTORDEVWORKS"
Write-Host "========================================"
Write-Host ""

# Dosya kontrolleri
if (!(Test-Path $MainFile)) {
    throw "Ana Python dosyasi bulunamadi: $MainFile"
}

if (!(Test-Path $IconFile)) {
    throw "Icon dosyasi bulunamadi: $IconFile"
}

# PyInstaller kontrolü
python -m PyInstaller --version

if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller yuklu degil."
}

# Eski derleme dosyalarını temizle
Write-Host "[1/4] Eski derleme dosyalari temizleniyor..."

Remove-Item $DistDir -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item $BuildDir -Recurse -Force -ErrorAction SilentlyContinue

# EXE derleme
Write-Host "[2/4] EXE derleniyor..."

python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name "ShortcutBlocker" `
    --icon $IconFile `
    --add-data "assets;assets" `
    $MainFile

if ($LASTEXITCODE -ne 0) {
    throw "Derleme basarisiz!"
}

# Çıktı kontrolü
Write-Host "[3/4] EXE kontrol ediliyor..."

$ExeFile = Join-Path $DistDir "ShortcutBlocker.exe"

if (!(Test-Path $ExeFile)) {
    throw "EXE dosyasi olusturulamadi."
}

# Tamamlandı
Write-Host "[4/4] Derleme tamamlandi!"

Write-Host ""
Write-Host "========================================"
Write-Host " BUILD SUCCESSFUL"
Write-Host "========================================"
Write-Host ""
Write-Host "EXE: $ExeFile"
Write-Host ""

