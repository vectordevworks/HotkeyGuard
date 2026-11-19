$ErrorActionPreference = "Stop"

# ============================================================
# SHORTCUT BLOCKER - PATH CONFIGURATION
# ============================================================

# Build.ps1 dosyasinin scripts klasorunde oldugu varsayilir.
$ProjectDir = Split-Path -Parent $PSScriptRoot

$MainFile  = Join-Path $ProjectDir "HotkeyGuard.pyw"
$AssetsDir = Join-Path $ProjectDir "assets"
$IconFile  = Join-Path $AssetsDir "icon.png"

$DistDir  = Join-Path $ProjectDir "dist"
$BuildDir = Join-Path $ProjectDir "build"

$IconIcoFile = Join-Path $BuildDir "HotkeyGuard.ico"

Write-Host ""
Write-Host "========================================"
Write-Host " SHORTCUT BLOCKER - BUILD"
Write-Host " VECTORDEVWORKS"
Write-Host "========================================"
Write-Host ""

# ============================================================
# FILE CHECKS
# ============================================================

Write-Host "[1/5] Dosyalar kontrol ediliyor..."

if (!(Test-Path $MainFile)) {
    throw "Ana Python dosyasi bulunamadi: $MainFile"
}

if (!(Test-Path $AssetsDir)) {
    throw "Assets klasoru bulunamadi: $AssetsDir"
}

if (!(Test-Path $IconFile)) {
    throw "PNG icon dosyasi bulunamadi: $IconFile"
}

# ============================================================
# PYINSTALLER CHECK
# ============================================================

Write-Host "[2/5] PyInstaller kontrol ediliyor..."

python -m PyInstaller --version

if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller yuklu degil veya calistirilamadi."
}

# ============================================================
# CLEAN OLD BUILD FILES
# ============================================================

Write-Host "[3/5] Eski derleme dosyalari temizleniyor..."

Remove-Item $DistDir -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item $BuildDir -Recurse -Force -ErrorAction SilentlyContinue

New-Item -ItemType Directory -Path $BuildDir -Force | Out-Null

# ============================================================
# CONVERT PNG ICON TO ICO
# ============================================================

Write-Host "ICO simgesi hazirlaniyor..."

python -c "import sys; from PIL import Image; Image.open(sys.argv[1]).convert('RGBA').save(sys.argv[2], format='ICO', sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])" $IconFile $IconIcoFile

if ($LASTEXITCODE -ne 0 -or !(Test-Path $IconIcoFile)) {
    throw "PNG simgesi ICO formatina donusturulemedi. Pillow yuklu oldugundan emin olun: python -m pip install pillow"
}

# ============================================================
# BUILD EXE
# ============================================================

Write-Host "[4/5] EXE derleniyor..."

python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name "HotkeyGuard" `
    --icon $IconIcoFile `
    --add-data "$AssetsDir;assets" `
    --distpath $DistDir `
    --workpath $BuildDir `
    --specpath $BuildDir `
    $MainFile

if ($LASTEXITCODE -ne 0) {
    throw "Derleme basarisiz!"
}

# ============================================================
# OUTPUT CHECK
# ============================================================

Write-Host "[5/5] EXE kontrol ediliyor..."

$ExeFile = Join-Path $DistDir "HotkeyGuard.exe"

if (!(Test-Path $ExeFile)) {
    throw "EXE dosyasi olusturulamadi: $ExeFile"
}

# ============================================================
# SUCCESS
# ============================================================

Write-Host ""
Write-Host "========================================"
Write-Host " BUILD SUCCESSFUL"
Write-Host "========================================"
Write-Host ""
Write-Host "EXE: $ExeFile"
Write-Host ""
