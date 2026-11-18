# Shortcut Blocker

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="German"> German
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Spanish"> Spanish
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="French"> French
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japanese"> Japanese
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Korean"> Korean
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portuguese"> Portuguese
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russian"> Russian
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Simplified Chinese"> Simplified Chinese
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turkish"> Turkish
</a>

Shortcut Blocker is a lightweight Windows desktop application that lets you block selected keyboard shortcuts. It helps prevent accidental use of specific key combinations.

## Overview

The application monitors Windows keyboard events and blocks the shortcuts you select. Protection does not start automatically when the application opens; click **Start** in the interface to enable it.

## Features

- **Shift + Delete blocking:** Blocks the permanent-delete shortcut.
- **Application-specific F1 blocking:** Blocks F1 in Chrome, Microsoft Edge, Firefox, Brave, Opera, and Windows Desktop / File Explorer.
- **Selectable protections:** Enable or disable Shift + Delete and F1 blocking independently in the interface.
- **Minimize to system tray:** Minimize the application to the system tray.
- **Multiple languages:** Turkish, English, German, French, Spanish, Portuguese, Russian, Japanese, Simplified Chinese, and Korean.
- **Scrollable interface:** The application window content can be scrolled.

F1 is blocked only in the applications listed above. F1 remains available in other applications and games.

## Requirements

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os`, and `pathlib` are part of the Python standard library.

Both Pillow and pystray are required for the system-tray feature.

## Installation

1. Download the project files or clone the repository.
2. Open the project folder.
3. Open PowerShell in that folder.
4. Install the required Python packages:

```powershell
py -m pip install -r requirements.txt
```

The contents of `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Launch the application:

```powershell
pyw .\ShortcutBlocker.pyw
```

Alternatively:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Virtual Environment (Optional)

You can keep the dependencies in a separate virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Usage

1. Run `ShortcutBlocker.pyw`.
2. Select the shortcuts you want to block in the interface.
3. Click **Start** to enable protection.
4. Monitor the protection status in the application.
5. Use the minimize option to send the application to the system tray. Pillow and pystray must be installed for this feature.

The language preference is stored at:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

This file stores the language selection. Shortcut-blocking options can be selected in the application; do not assume these options are saved to the config file.

## Building (Creating an EXE)

PyInstaller is required to create the EXE. Install it separately:

```powershell
py -m pip install pyinstaller==6.22.3
```

Then open PowerShell in the project folder and run the build script:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

The script:

1. Checks the main Python file and `assets\icon.png`.
2. Verifies that PyInstaller is available.
3. Removes the old `dist` and `build` folders.
4. Builds a single-file EXE without a console window.
5. Includes the `assets` folder and application icon in the build.
6. Checks that the EXE was created.

After a successful build, the application is located at:

```text
dist\ShortcutBlocker.exe
```

## Developer

**vectordevworks**

## License

See the `LICENSE` file in the project repository for licensing terms.
