# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="英语"> 英语</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="德语"> 德语</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="西班牙语"> 西班牙语</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="法语"> 法语</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日语"> 日语</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="韩语"> 韩语</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="葡萄牙语"> 葡萄牙语</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="俄语"> 俄语</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="土耳其语"> 土耳其语</a>

Shortcut Blocker 是一款轻量级 Windows 桌面应用，可用于屏蔽选定的键盘快捷键，帮助防止意外触发特定按键组合。

## 概述

应用会监视 Windows 键盘事件，并屏蔽你选择的快捷键。应用启动时不会自动启用保护功能；请在界面中点击 **Start** 按钮来启用。

## 功能

- **屏蔽 Shift + Delete：** 屏蔽永久删除快捷键。
- **按应用屏蔽 F1：** 在 Chrome、Microsoft Edge、Firefox、Brave、Opera 以及 Windows 桌面 / 文件资源管理器中屏蔽 F1。
- **可选保护项目：** 可以在界面中分别启用或关闭 Shift + Delete 和 F1 屏蔽。
- **最小化到系统托盘：** 可以将应用最小化到系统托盘。
- **多语言支持：** 支持土耳其语、英语、德语、法语、西班牙语、葡萄牙语、俄语、日语、简体中文和韩语。
- **可滚动界面：** 应用窗口内容支持滚动。

F1 仅在上述应用中被屏蔽。在其他应用和游戏中，F1 仍然可用。

## 环境要求

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`、`ctypes`、`json`、`math`、`os` 和 `pathlib` 均属于 Python 标准库。

使用最小化到系统托盘功能时，需要同时安装 Pillow 和 pystray。

## 安装

1. 下载项目文件或克隆代码仓库。
2. 打开项目文件夹。
3. 在该文件夹中打开 PowerShell。
4. 安装所需的 Python 软件包：

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` 文件内容：

```text
Pillow==13.0.0
pystray==0.19.5
```

5. 启动应用：

```powershell
pyw .\ShortcutBlocker.pyw
```

也可以使用：

```powershell
pythonw .\ShortcutBlocker.pyw
```

## 虚拟环境（可选）

你可以将依赖项安装在独立的虚拟环境中：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## 使用方法

1. 运行 `ShortcutBlocker.pyw`。
2. 在界面中选择要屏蔽的快捷键。
3. 点击 **Start** 启用保护功能。
4. 在应用中查看保护状态。
5. 使用最小化选项将应用移至系统托盘。此功能需要安装 Pillow 和 pystray。

语言偏好保存在以下位置：

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

该文件保存语言选择。快捷键屏蔽选项可在应用中选择；请勿假设这些选项也会保存到配置文件中。

## 构建（创建 EXE）

创建 EXE 需要 PyInstaller。请单独安装：

```powershell
py -m pip install pyinstaller==6.22.3
```

然后在项目文件夹中打开 PowerShell，并运行构建脚本：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

脚本将执行以下操作：

1. 检查主 Python 文件和 `assets\icon.png`。
2. 检查 PyInstaller 是否可用。
3. 删除旧的 `dist` 和 `build` 文件夹。
4. 构建一个不显示控制台窗口的单文件 EXE。
5. 将 `assets` 文件夹和应用图标包含在构建结果中。
6. 检查 EXE 是否成功生成。

构建成功后，应用位于：

```text
dist\ShortcutBlocker.exe
```

## 开发者

**vectordevworks**

## 许可证

有关许可条款，请参阅项目仓库中的 `LICENSE` 文件。
