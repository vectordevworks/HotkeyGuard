# TastenkürzelSchutz

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Englisch"> Englisch
</a>
|
<strong>
  <img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch
</strong>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Spanisch"> Spanisch
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Französisch"> Französisch
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japanisch"> Japanisch
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Koreanisch"> Koreanisch
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugiesisch"> Portugiesisch
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russisch"> Russisch
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Vereinfachtes Chinesisch"> Vereinfachtes Chinesisch
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkisch"> Türkisch
</a>

Der TastenkürzelSchutz ist eine schlanke, Python-basierte Desktopanwendung, mit der Sie bestimmte Tastenkombinationen unter Windows blockieren können. Die übersichtliche grafische Benutzeroberfläche hilft Ihnen dabei, versehentlich ausgelöste Tastenkombinationen zu verhindern und die gewünschten Schutzfunktionen einfach zu verwalten.

## Überblick

Die Anwendung überwacht Windows-Tastaturereignisse und blockiert die von Ihnen ausgewählten Tastenkombinationen. Der Schutz wird beim Start der Anwendung nicht automatisch aktiviert. Sie müssen dazu in der Benutzeroberfläche auf **Starten** klicken.

## Funktionen

- **Shift + Delete blockieren:** Blockiert die Tastenkombination zum endgültigen Löschen.
- **Anwendungsspezifische F1-Sperre:** Blockiert die F1-Taste in Chrome, Microsoft Edge, Firefox, Brave, Opera sowie auf dem Windows-Desktop und im Datei-Explorer.
- **Individuell auswählbare Schutzfunktionen:** Sie können die Sperren für Shift + Delete und F1 unabhängig voneinander über die Benutzeroberfläche aktivieren oder deaktivieren.
- **In den Infobereich minimieren:** Sie können die Anwendung in den Infobereich der Taskleiste minimieren.
- **Mehrsprachige Unterstützung:** Unterstützt Türkisch, Englisch, Deutsch, Französisch, Spanisch, Portugiesisch, Russisch, Japanisch, vereinfachtes Chinesisch und Koreanisch.
- **Scrollbare Benutzeroberfläche:** Der Inhalt des Anwendungsfensters kann gescrollt werden.

Die F1-Sperre ist nur in den oben genannten Anwendungen aktiv. In anderen Anwendungen und Spielen wird die F1-Taste nicht blockiert.

## Anforderungen

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` und `pathlib` gehören zur Python-Standardbibliothek.

Für die Funktion zum Minimieren in den Infobereich werden sowohl Pillow als auch pystray benötigt.

## Installation

1. Laden Sie die Projektdateien auf Ihren Computer herunter oder klonen Sie das Repository.
2. Öffnen Sie den Projektordner.
3. Öffnen Sie PowerShell in diesem Ordner.
4. Installieren Sie die erforderlichen Python-Pakete:

```powershell
py -m pip install -r requirements.txt
```

Inhalt der Datei `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Starten Sie die Anwendung:

```powershell
pyw .\HotkeyGuard.pyw
```

Alternativ können Sie folgenden Befehl verwenden:

```powershell
pythonw .\HotkeyGuard.pyw
```

## Virtuelle Umgebung (Optional)

Mit einer virtuellen Umgebung können Sie die Python-Abhängigkeiten getrennt von anderen Projekten verwalten:

1. Erstellen Sie eine virtuelle Umgebung:

```powershell
py -m venv .venv
```

2. Aktivieren Sie die virtuelle Umgebung:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Installieren Sie die erforderlichen Abhängigkeiten:

```powershell
py -m pip install -r requirements.txt
```

4. Deaktivieren Sie die virtuelle Umgebung, wenn Sie fertig sind:

```powershell
deactivate
```

## Verwendung

1. Führen Sie die Datei `HotkeyGuard.pyw` aus.
2. Wählen Sie in der Benutzeroberfläche die Tastenkombinationen aus, die Sie blockieren möchten.
3. Klicken Sie auf **Starten**, um den Schutz zu aktivieren.
4. Überprüfen Sie den Schutzstatus über die Anwendungsoberfläche.
5. Verwenden Sie die Minimierungsoption, um die Anwendung in den Infobereich der Taskleiste zu verschieben. Dafür müssen Pillow und pystray installiert sein.

Die Spracheinstellung wird unter folgendem Pfad gespeichert:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Diese Datei speichert ausschließlich die Sprachauswahl. Die Optionen zur Tastenkombinationssperre können in den Anwendungseinstellungen ausgewählt werden. Es wird nicht davon ausgegangen, dass diese Optionen in der Konfigurationsdatei gespeichert werden.

## Erstellung der EXE-Datei

Mit PyInstaller können Sie die Python-Anwendung in eine einzelne EXE-Datei umwandeln.

### 1. PyInstaller installieren

Installieren Sie PyInstaller in Version 6.22.3:

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. Zum Projektordner wechseln

Öffnen Sie PowerShell im Projektordner.

### 3. Build-Skript ausführen

Führen Sie den folgenden Befehl aus, um das Skript `embed_icon.ps1` zu starten:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Hinweis:** `-ExecutionPolicy Bypass` wird verwendet, da Windows die Ausführung von PowerShell-Skripten aufgrund der geltenden Ausführungsrichtlinie verhindern kann. Diese Einstellung gilt ausschließlich für den gestarteten PowerShell-Prozess. Die systemweiten Sicherheitseinstellungen werden dadurch nicht geändert.

### 4. Build-Prozess

Das Build-Skript führt folgende Schritte aus:

1. Überprüft die Haupt-Python-Datei und die Datei `assets\icon.png`.
2. Stellt sicher, dass PyInstaller verfügbar ist.
3. Löscht die vorhandenen Ordner `dist` und `build`.
4. Erstellt die Anwendung als einzelne EXE-Datei ohne Konsolenfenster.
5. Bindet den Ordner `assets` und das Anwendungssymbol in den Build ein.
6. Überprüft die erstellte EXE-Datei.

### 5. Build-Ausgabe

Nach erfolgreichem Abschluss des Build-Vorgangs wird die EXE-Datei unter folgendem Pfad erstellt:

```text
dist\HotkeyGuard.exe
```

**Vorgehensweise zum Erstellen einer neuen Version:**

1. Öffnen Sie PowerShell.
2. Stellen Sie sicher, dass PyInstaller installiert ist.
3. Wechseln Sie zum Projektordner.
4. Führen Sie das Build-Skript aus.
5. Die erstellte EXE-Datei finden Sie im Ordner `dist`.

## Entwickler

**vectordevworks**

## Lizenz

Die geltenden Lizenzbedingungen finden Sie in der Datei `LICENSE` im Projekt-Repository.
