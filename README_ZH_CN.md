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
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="土耳其语"> 土耳其语
</a>
|
<strong>
  <img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文
</strong>

### 快捷键拦截器是一款基于 Python 开发的轻量级 Windows
桌面应用程序，可用于屏蔽指定的键盘快捷键。通过简洁的图形界面，您可以控制意外触发的快捷键，并轻松管理所选的防护功能。

## 概述

该应用程序会监控 Windows
键盘事件，并屏蔽您选择的快捷键。应用程序启动时不会自动启用快捷键防护；您需要在界面中点击
**"开始防护"** 按钮。

## 功能特点

-   **屏蔽 Shift + Delete：** 屏蔽永久删除快捷键。
-   **针对特定应用程序屏蔽 F1：** 在 Chrome、Microsoft
    Edge、Firefox、Brave、Opera、Windows 桌面和文件资源管理器中屏蔽 F1
    键。
-   **可选防护功能：** 您可以在界面中分别启用或禁用 Shift + Delete
    屏蔽和 F1 屏蔽。
-   **最小化到系统托盘：** 可以将应用程序最小化到系统托盘。
-   **多语言支持：**
    支持土耳其语、英语、德语、法语、西班牙语、葡萄牙语、俄语、日语、简体中文和韩语。
-   **可滚动界面：** 可以滚动查看应用程序窗口中的内容。

F1 屏蔽功能仅在上述列出的应用程序中生效。在其他应用程序或游戏中，F1
键不会被屏蔽。

## 系统要求

-   Windows
-   Python
-   Pillow 13.0.0
-   pystray 0.19.5

`tkinter`、`ctypes`、`json`、`math`、`os` 和 `pathlib` 均属于 Python
标准库。

使用最小化到系统托盘功能时，必须安装 Pillow 和 pystray。

## 安装

1.  将项目文件下载到计算机，或克隆项目仓库。
2.  打开项目文件夹。
3.  在该文件夹中打开 PowerShell。
4.  安装所需的 Python 软件包：

``` powershell
py -m pip install -r requirements.txt
```

`requirements.txt` 文件内容：

``` text
Pillow==13.0.0
pystray==0.19.5
```

5.  启动应用程序：

``` powershell
pyw .\ShortcutBlocker.pyw
```

也可以使用以下命令：

``` powershell
pythonw .\ShortcutBlocker.pyw
```

## 虚拟环境（可选）

您可以使用虚拟环境隔离不同项目的 Python 依赖项：

1.  创建虚拟环境：

``` powershell
py -m venv .venv
```

2.  激活虚拟环境：

``` powershell
.\.venv\Scripts\Activate.ps1
```

3.  安装所需依赖项：

``` powershell
py -m pip install -r requirements.txt
```

4.  完成后退出虚拟环境：

``` powershell
deactivate
```

## 使用方法

1.  运行 `ShortcutBlocker.pyw` 文件。
2.  在应用程序界面中选择要屏蔽的快捷键。
3.  点击 **"开始防护"** 按钮以启用防护。
4.  通过应用程序界面查看防护状态。
5.  使用最小化选项将应用程序移至系统托盘。使用此功能必须安装 Pillow 和
    pystray。

语言偏好设置保存在以下位置：

``` text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

此文件用于保存语言选择。快捷键屏蔽选项可在应用程序设置中选择；请勿假定这些选项也会保存到该配置文件中。

## 构建（创建 EXE 文件）

使用 PyInstaller 将 Python 应用程序打包为单个 EXE 文件。

### 2. 进入项目文件夹

在项目文件夹中打开 PowerShell。

### 3. 运行构建脚本

运行以下命令以启动 `embed_icon.ps1` 脚本：

``` powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** 使用 `-ExecutionPolicy Bypass` 是因为 Windows
可能会根据执行策略阻止 PowerShell 脚本运行。此设置仅适用于当前启动的
PowerShell 进程，不会更改系统范围的安全设置。

### 4. 构建过程

构建脚本将执行以下操作：

1.  检查主 Python 文件和 `assets\icon.png` 文件是否存在。
2.  确认 PyInstaller 是否可用。
3.  清理旧的 `dist` 和 `build` 文件夹。
4.  将应用程序构建为不显示控制台窗口的单文件 EXE。
5.  将 `assets` 文件夹和应用程序图标包含在构建结果中。
6.  检查生成的 EXE 文件。

### 5. 构建输出

构建成功后，EXE 文件将生成在以下位置：

``` text
dist\ShortcutBlocker.exe
```

**构建新版本时，请按以下步骤操作：**

1.  打开 PowerShell。
2.  确保已安装 PyInstaller。
3.  进入项目文件夹。
4.  运行构建脚本。
5.  从 `dist` 文件夹中获取生成的 EXE 文件。

## 开发者

**vectordevworks**

## 许可证

有关许可条款，请参阅项目仓库中的 `LICENSE` 文件。
