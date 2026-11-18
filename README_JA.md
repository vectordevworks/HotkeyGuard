# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="英語"> 英語</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="ドイツ語"> ドイツ語</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="スペイン語"> スペイン語</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="フランス語"> フランス語</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="韓国語"> 韓国語</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="ポルトガル語"> ポルトガル語</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="ロシア語"> ロシア語</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="簡体字中国語"> 簡体字中国語</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="トルコ語"> トルコ語</a>

Shortcut Blocker は、選択したキーボードショートカットをブロックできる、Windows 向けの軽量デスクトップアプリケーションです。特定のキー操作を誤って実行することを防ぎます。

## 概要

このアプリケーションは Windows のキーボードイベントを監視し、選択されたショートカットをブロックします。アプリケーションを起動しても保護機能は自動的に有効になりません。インターフェースの **Start** ボタンをクリックして有効にしてください。

## 機能

- **Shift + Delete のブロック：** 完全削除のショートカットをブロックします。
- **アプリごとの F1 ブロック：** Chrome、Microsoft Edge、Firefox、Brave、Opera、および Windows デスクトップ / エクスプローラーで F1 をブロックします。
- **保護機能の選択：** Shift + Delete と F1 のブロックを、それぞれ個別に有効・無効にできます。
- **システムトレイへの最小化：** アプリケーションをシステムトレイに最小化できます。
- **多言語対応：** トルコ語、英語、ドイツ語、フランス語、スペイン語、ポルトガル語、ロシア語、日本語、簡体字中国語、韓国語に対応しています。
- **スクロール可能な画面：** アプリケーションウィンドウの内容をスクロールできます。

F1 は上記のアプリケーションでのみブロックされます。それ以外のアプリケーションやゲームでは F1 を使用できます。

## 必要条件

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`、`ctypes`、`json`、`math`、`os`、`pathlib` は Python 標準ライブラリに含まれています。

システムトレイへの最小化機能を使用するには、Pillow と pystray の両方が必要です。

## インストール

1. プロジェクトファイルをダウンロードするか、リポジトリをクローンします。
2. プロジェクトフォルダーを開きます。
3. そのフォルダーで PowerShell を起動します。
4. 必要な Python パッケージをインストールします。

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` の内容：

```text
Pillow==13.0.0
pystray==0.19.5
```

5. アプリケーションを起動します。

```powershell
pyw .\ShortcutBlocker.pyw
```

または、次のコマンドも使用できます。

```powershell
pythonw .\ShortcutBlocker.pyw
```

## 仮想環境（任意）

依存パッケージを専用の仮想環境にインストールできます。

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## 使い方

1. `ShortcutBlocker.pyw` を実行します。
2. インターフェースでブロックするショートカットを選択します。
3. **Start** をクリックして保護を有効にします。
4. アプリケーションで保護状態を確認します。
5. 最小化オプションを使用して、アプリケーションをシステムトレイに移動します。この機能には Pillow と pystray が必要です。

言語設定は次の場所に保存されます。

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

このファイルには言語選択が保存されます。ショートカットのブロック設定はアプリケーション内で選択できますが、設定ファイルに保存されるとは限りません。

## ビルド（EXE の作成）

EXE の作成には PyInstaller が必要です。別途インストールしてください。

```powershell
py -m pip install pyinstaller==6.22.3
```

次に、プロジェクトフォルダーで PowerShell を開き、ビルドスクリプトを実行します。

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

スクリプトは次の処理を行います。

1. メインの Python ファイルと `assets\icon.png` を確認します。
2. PyInstaller が利用可能か確認します。
3. 古い `dist` および `build` フォルダーを削除します。
4. コンソールウィンドウを表示しない単一ファイルの EXE を作成します。
5. `assets` フォルダーとアプリケーションアイコンをビルドに含めます。
6. EXE が作成されたことを確認します。

ビルドが成功すると、アプリケーションは次の場所に生成されます。

```text
dist\ShortcutBlocker.exe
```

## 開発者

**vectordevworks**

## ライセンス

ライセンス条件については、プロジェクトリポジトリ内の `LICENSE` ファイルを確認してください。
