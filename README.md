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

Shortcut Blocker is a lightweight Python-based desktop application that allows you to block specific keyboard shortcuts on Windows. Its simple graphical interface helps you keep accidentally triggered shortcuts under control and easily manage the protections you choose.

## Overview

The application monitors Windows keyboard events and blocks the shortcuts you select. Shortcut protection does not start automatically when the application launches; you must click the **Start** button in the interface.

## Features

- **Shift + Delete blocking:** Blocks the permanent deletion shortcut.
- **Application-specific F1 blocking:** Blocks the F1 key in Chrome, Microsoft Edge, Firefox, Brave, Opera, and Windows Desktop / File Explorer.
- **Selectable protections:** You can independently enable or disable Shift + Delete and F1 blocking through the interface.
- **Minimize to system tray:** You can minimize the application to the system tray.
- **Multilingual support:** Supports Turkish, English, German, French, Spanish, Portuguese, Russian, Japanese, Simplified Chinese, and Korean.
- **Scrollable interface:** The contents of the application window can be scrolled.

F1 blocking is only active in the applications listed above. The F1 key is not blocked in other applications or games.

## Requirements

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os`, and `pathlib` are part of the Python standard library.

Both Pillow and pystray are required to use the minimize-to-system-tray feature.

## Installation

1. Download the project files to your computer or clone the repository.
2. Open the project folder.
3. Open PowerShell in this folder.
4. Install the required Python packages:

```powershell
py -m pip install -r requirements.txt
```

Contents of `requirements.txt`:

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

You can keep Python dependencies isolated from other projects by using a virtual environment:

1. Create a virtual environment:

```powershell
py -m venv .venv
```

2. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install the required dependencies:

```powershell
py -m pip install -r requirements.txt
```

4. Deactivate the virtual environment when you are finished:

```powershell
deactivate
```

## Usage

1. Run the `ShortcutBlocker.pyw` file.
2. Select the shortcuts you want to block in the interface.
3. Click the **Start** button to enable protection.
4. Monitor the protection status through the application interface.
5. Use the minimize option to send the application to the system tray. Pillow and pystray must be installed for this feature.

The language preference is stored at the following location:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

This file stores the language selection. Shortcut blocking options can be selected in the application settings; do not assume that these options are saved to the config file.

## Building (Creating an EXE)

PyInstaller is used to convert the Python application into a single EXE file.

### 1. Installing PyInstaller

Install PyInstaller version 6.22.3:

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. Navigating to the Project Folder

Open PowerShell in the project folder.

### 3. Running the Build Script

Run the following command to start the `embed_icon.ps1` script:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Note:** `-ExecutionPolicy Bypass` is used because Windows may prevent PowerShell scripts from running due to its execution policy. This setting applies only to the launched PowerShell process. System-wide security settings are not changed.

### 4. Build Process

The build script performs the following operations:

1. Checks the main Python file and the `assets\icon.png` file.
2. Verifies that PyInstaller is available.
3. Cleans up the old `dist` and `build` folders.
4. Builds the application as a single-file EXE without a console window.
5. Includes the `assets` folder and application icon in the build.
6. Checks the generated EXE file.

### 5. Build Output

After the build completes successfully, the EXE file is created at the following location:

```text
dist\ShortcutBlocker.exe
```

**Steps to follow when building a new version:**

1. Open PowerShell.
2. Make sure PyInstaller is installed.
3. Navigate to the project folder.
4. Run the build script.
5. Retrieve the generated EXE file from the `dist` folder.

## Developer

**vectordevworks**

## License

See the `LICENSE` file in the project repository for licensing terms.