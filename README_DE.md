# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> Englisch</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Spanisch"> Spanisch</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Französisch"> Französisch</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="Japanisch"> Japanisch</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="Koreanisch"> Koreanisch</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Portugiesisch"> Portugiesisch</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Russisch"> Russisch</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="Vereinfachtes Chinesisch"> Vereinfachtes Chinesisch</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkisch"> Türkisch</a>

Shortcut Blocker ist eine schlanke Windows-Desktopanwendung, mit der ausgewählte Tastenkombinationen blockiert werden können. Sie hilft dabei, die versehentliche Verwendung bestimmter Tastenkombinationen zu verhindern.

## Überblick

Die Anwendung überwacht Windows-Tastaturereignisse und blockiert die ausgewählten Tastenkombinationen. Der Schutz wird beim Start der Anwendung nicht automatisch aktiviert. Klicken Sie dazu in der Oberfläche auf **Start**.

## Funktionen

- **Shift + Delete blockieren:** Blockiert die Tastenkombination zum endgültigen Löschen.
- **Anwendungsspezifische F1-Sperre:** Blockiert F1 in Chrome, Microsoft Edge, Firefox, Brave, Opera sowie auf dem Windows-Desktop / im Datei-Explorer.
- **Individuell auswählbarer Schutz:** Shift + Delete und F1 können in der Oberfläche unabhängig voneinander aktiviert oder deaktiviert werden.
- **In den Infobereich minimieren:** Die Anwendung kann in den Infobereich der Taskleiste minimiert werden.
- **Mehrsprachigkeit:** Türkisch, Englisch, Deutsch, Französisch, Spanisch, Portugiesisch, Russisch, Japanisch, vereinfachtes Chinesisch und Koreanisch.
- **Bildlauf in der Oberfläche:** Der Inhalt des Anwendungsfensters kann gescrollt werden.

F1 wird nur in den oben aufgeführten Anwendungen blockiert. In anderen Anwendungen und Spielen bleibt F1 verfügbar.

## Voraussetzungen

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` und `pathlib` gehören zur Python-Standardbibliothek.

Für die Funktion zum Minimieren in den Infobereich werden sowohl Pillow als auch pystray benötigt.

## Installation

1. Laden Sie die Projektdateien herunter oder klonen Sie das Repository.
2. Öffnen Sie den Projektordner.
3. Starten Sie PowerShell in diesem Ordner.
4. Installieren Sie die benötigten Python-Pakete:

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
pyw .\ShortcutBlocker.pyw
```

Alternativ:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Virtuelle Umgebung (Optional)

Sie können die Abhängigkeiten in einer separaten virtuellen Umgebung verwalten:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Verwendung

1. Führen Sie `ShortcutBlocker.pyw` aus.
2. Wählen Sie in der Oberfläche die Tastenkombinationen aus, die blockiert werden sollen.
3. Klicken Sie auf **Start**, um den Schutz zu aktivieren.
4. Überprüfen Sie den Schutzstatus in der Anwendung.
5. Verwenden Sie die Minimieren-Option, um die Anwendung in den Infobereich zu verschieben. Dafür müssen Pillow und pystray installiert sein.

Die Spracheinstellung wird hier gespeichert:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Diese Datei speichert die Sprachauswahl. Die Optionen zur Tastenkombinationssperre können in der Anwendung ausgewählt werden; es wird nicht vorausgesetzt, dass diese Optionen in der Konfigurationsdatei gespeichert werden.

## Build (EXE erstellen)

Zum Erstellen der EXE wird PyInstaller benötigt. Installieren Sie es separat:

```powershell
py -m pip install pyinstaller==6.22.3
```

Öffnen Sie anschließend PowerShell im Projektordner und führen Sie das Build-Skript aus:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

Das Skript führt folgende Schritte aus:

1. Prüft die Python-Hauptdatei und `assets\icon.png`.
2. Überprüft, ob PyInstaller verfügbar ist.
3. Löscht die alten Ordner `dist` und `build`.
4. Erstellt eine einzelne EXE-Datei ohne Konsolenfenster.
5. Fügt den Ordner `assets` und das Anwendungssymbol zum Build hinzu.
6. Überprüft, ob die EXE erstellt wurde.

Nach erfolgreichem Build befindet sich die Anwendung hier:

```text
dist\ShortcutBlocker.exe
```

## Entwickler

**vectordevworks**

## Lizenz

Die Lizenzbedingungen finden Sie in der Datei `LICENSE` im Projekt-Repository.
