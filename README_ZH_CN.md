# 快捷键拦截器

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="英语"> 英语
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="德语"> 德语
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="西班牙语"> 西班牙语
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="法语"> 法语
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="日语"> 日语
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="韩语"> 韩语
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="葡萄牙语"> 葡萄牙语
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="俄语"> 俄语
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="土耳其语"> 土耳其语
</a>

Shortcut Blocker 是一款使用 Python 开发的轻量级 Windows 桌面应用，可用于拦截指定的键盘快捷键。通过简洁直观的图形界面，您可以管理可能被意外触发的快捷键，并根据需要启用或禁用相应的保护功能。

## 概述

该应用通过监控 Windows 键盘事件来拦截您选择的快捷键。应用启动后不会自动启用保护功能，您需要在界面中点击 **启动** 按钮来开启保护。

## 功能特点

- **拦截 Shift + Delete：** 拦截用于永久删除文件的快捷键。
- **针对特定应用程序拦截 F1：** 在 Chrome、Microsoft Edge、Firefox、Brave、Opera 以及 Windows 桌面和文件资源管理器中拦截 F1 键。
- **可选保护功能：** 您可以通过应用界面分别启用或禁用 Shift + Delete 和 F1 拦截功能。
- **最小化到系统托盘：** 支持将应用最小化到系统托盘。
- **多语言支持：** 支持土耳其语、英语、德语、法语、西班牙语、葡萄牙语、俄语、日语、简体中文和韩语。
- **可滚动界面：** 支持滚动查看应用窗口中的内容。

F1 拦截功能仅在上述指定应用程序中生效。在其他应用程序和游戏中，F1 键不会被拦截。

## 系统要求

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`、`ctypes`、`json`、`math`、`os` 和 `pathlib` 均属于 Python 标准库，无需单独安装。

若要使用最小化到系统托盘的功能，则需要同时安装 Pillow 和 pystray。

## 安装

1. 将项目文件下载到计算机，或克隆项目仓库。
2. 打开项目文件夹。
3. 在该文件夹中打开 PowerShell。
4. 安装所需的 Python 依赖包：

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` 文件内容如下：

```text
Pillow==13.0.0
pystray==0.19.5
```

5. 启动应用：

```powershell
pyw .\ShortcutBlocker.pyw
```

或者：

```powershell
pythonw .\ShortcutBlocker.pyw
```

## 虚拟环境（可选）

您可以使用虚拟环境将本项目的 Python 依赖项与其他项目隔离。

1. 创建虚拟环境：

```powershell
py -m venv .venv
```

2. 激活虚拟环境：

```powershell
.\.venv\Scripts\Activate.ps1
```

3. 安装所需的依赖包：

```powershell
py -m pip install -r requirements.txt
```

4. 使用完毕后，停用虚拟环境：

```powershell
deactivate
```

## 使用方法

1. 运行 `ShortcutBlocker.pyw` 文件。
2. 在应用界面中选择需要拦截的快捷键。
3. 点击 **启动** 按钮以启用保护功能。
4. 通过应用界面查看当前的保护状态。
5. 使用最小化选项将应用移至系统托盘。使用此功能需要安装 Pillow 和 pystray。

语言偏好设置保存在以下位置：

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

该文件仅用于保存语言选择。快捷键拦截选项可以在应用界面中进行设置，请注意，这些选项不会保存到上述配置文件中。

## 构建（生成 EXE 文件）

您可以使用 PyInstaller 将 Python 应用程序打包为独立的 EXE 文件。

### 1. 安装 PyInstaller

安装 PyInstaller 6.22.3：

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. 打开项目文件夹

在项目文件夹中打开 PowerShell。

### 3. 运行构建脚本

运行以下命令以执行 `embed_icon.ps1` 脚本：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** Windows 的执行策略可能会阻止 PowerShell 脚本运行，因此需要使用 `-ExecutionPolicy Bypass`。此设置仅对当前启动的 PowerShell 进程有效，不会更改系统范围的执行策略或安全设置。

### 4. 构建过程

构建脚本将自动执行以下操作：

1. 检查主 Python 文件和 `assets\icon.png` 文件是否存在。
2. 检查 PyInstaller 是否可用。
3. 清理旧的 `dist` 和 `build` 文件夹。
4. 将应用程序打包为单文件 EXE，并隐藏控制台窗口。
5. 将 `assets` 文件夹和应用程序图标包含在构建文件中。
6. 检查生成的 EXE 文件是否成功创建。

### 5. 构建输出

构建成功后，EXE 文件将生成在以下位置：

```text
dist\ShortcutBlocker.exe
```

**重新构建新版本时，请按照以下步骤操作：**

1. 打开 PowerShell。
2. 确认已安装 PyInstaller。
3. 进入项目文件夹。
4. 运行构建脚本。
5. 在 `dist` 文件夹中找到生成的 EXE 文件。

## 开发者

**vectordevworks**

## 许可证

有关许可证的详细条款，请参阅项目仓库中的 `LICENSE` 文件。