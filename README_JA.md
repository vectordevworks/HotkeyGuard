<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="英語"> 英語
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="ドイツ語"> ドイツ語
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="スペイン語"> スペイン語
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="フランス語"> フランス語
</a>
|
<strong>
  <img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語
</strong>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="韓国語"> 韓国語
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="ポルトガル語"> ポルトガル語
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="ロシア語"> ロシア語
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="トルコ語"> トルコ語
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="簡体字中国語"> 簡体字中国語
</a>

### ホットキーガードは、Windows上で特定のキーボードショートカットを無効にできる、Pythonベースの軽量なデスクトップアプリケーションです。シンプルなグラフィカルインターフェースにより、誤って実行されるショートカットを制御し、必要な保護機能を簡単に管理できます。
## 概要

このアプリケーションはWindowsのキーボードイベントを監視し、選択したショートカットをブロックします。アプリケーションの起動時に保護機能が自動的に有効になることはありません。保護を開始するには、インターフェースの **開始** ボタンをクリックする必要があります。

## 機能

- **Shift + Deleteのブロック：** ファイルを完全に削除するショートカットをブロックします。
- **アプリケーションごとのF1キーのブロック：** Chrome、Microsoft Edge、Firefox、Brave、Opera、およびWindowsのデスクトップとエクスプローラーでF1キーをブロックします。
- **保護機能の個別設定：** インターフェースからShift + DeleteとF1のブロックを個別に有効または無効にできます。
- **タスクトレイへの最小化：** アプリケーションをタスクトレイに最小化できます。
- **多言語対応：** トルコ語、英語、ドイツ語、フランス語、スペイン語、ポルトガル語、ロシア語、日本語、簡体字中国語、韓国語に対応しています。
- **スクロール可能なインターフェース：** アプリケーションウィンドウ内のコンテンツをスクロールできます。

F1キーのブロック機能は、上記のアプリケーションでのみ有効です。その他のアプリケーションやゲームでは、F1キーはブロックされません。

## 動作要件

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`、`ctypes`、`json`、`math`、`os`、`pathlib`はPython標準ライブラリに含まれています。

タスクトレイへの最小化機能を使用するには、Pillowとpystrayの両方が必要です。

## インストール

1. プロジェクトファイルをコンピューターにダウンロードするか、リポジトリをクローンします。
2. プロジェクトフォルダーを開きます。
3. そのフォルダーでPowerShellを起動します。
4. 必要なPythonパッケージをインストールします。

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt`の内容：

```text
Pillow==13.0.0
pystray==0.19.5
```

5. アプリケーションを起動します。

```powershell
pyw .\HotkeyGuard.pyw
```

または、次のコマンドでも起動できます。

```powershell
pythonw .\HotkeyGuard.pyw
```

## 仮想環境（任意）

仮想環境を使用すると、Pythonの依存関係を他のプロジェクトから分離して管理できます。

1. 仮想環境を作成します。

```powershell
py -m venv .venv
```

2. 仮想環境を有効にします。

```powershell
.\.venv\Scripts\Activate.ps1
```

3. 必要な依存関係をインストールします。

```powershell
py -m pip install -r requirements.txt
```

4. 作業が終了したら、仮想環境を終了します。

```powershell
deactivate
```

## 使用方法

1. `HotkeyGuard.pyw`ファイルを実行します。
2. インターフェースからブロックするショートカットを選択します。
3. **開始** ボタンをクリックして保護機能を有効にします。
4. アプリケーションのインターフェースで保護状態を確認します。
5. 最小化オプションを使用して、アプリケーションをタスクトレイに移動します。この機能を使用するには、Pillowとpystrayがインストールされている必要があります。

言語設定は次の場所に保存されます。

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

このファイルには言語の選択のみが保存されます。ショートカットのブロック設定はアプリケーション内で選択できますが、設定ファイルに保存されるとは限りません。

## ビルド（EXEファイルの作成）

PyInstallerを使用して、Pythonアプリケーションを単一のEXEファイルに変換します。

### 2. プロジェクトフォルダーを開く

プロジェクトフォルダーでPowerShellを起動します。

### 3. ビルドスクリプトの実行

次のコマンドを実行して、`embed_icon.ps1`スクリプトを起動します。

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** Windowsの実行ポリシーによってPowerShellスクリプトの実行が制限される場合があるため、`-ExecutionPolicy Bypass`を使用します。この設定は起動したPowerShellプロセスにのみ適用され、システム全体のセキュリティ設定は変更されません。

### 4. ビルドの実行

ビルドスクリプトは次の処理を実行します。

1. メインのPythonファイルと`assets\icon.png`ファイルの存在を確認します。
2. PyInstallerが利用可能であることを確認します。
3. 既存の`dist`フォルダーと`build`フォルダーを削除します。
4. コンソールウィンドウを表示しない単一ファイルのEXEとしてアプリケーションをビルドします。
5. `assets`フォルダーとアプリケーションのアイコンをビルドに含めます。
6. 生成されたEXEファイルを確認します。

### 5. ビルド結果

ビルドが正常に完了すると、EXEファイルは次の場所に作成されます。

```text
dist\HotkeyGuard.exe
```

**新しいバージョンをビルドする手順：**

1. PowerShellを起動します。
2. PyInstallerがインストールされていることを確認します。
3. プロジェクトフォルダーに移動します。
4. ビルドスクリプトを実行します。
5. `dist`フォルダーから生成されたEXEファイルを取得します。

## 開発者

**vectordevworks**

## ライセンス

ライセンス条件については、プロジェクトリポジトリ内の`LICENSE`ファイルを参照してください。
