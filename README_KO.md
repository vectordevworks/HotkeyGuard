# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="영어"> 영어</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="독일어"> 독일어</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="스페인어"> 스페인어</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="프랑스어"> 프랑스어</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="일본어"> 일본어</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="포르투갈어"> 포르투갈어</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="러시아어"> 러시아어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="중국어 간체"> 중국어 간체</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="터키어"> 터키어</a>

Shortcut Blocker는 선택한 키보드 단축키를 차단할 수 있는 가벼운 Windows 데스크톱 애플리케이션입니다. 특정 키 조합을 실수로 사용하는 것을 방지하는 데 도움이 됩니다.

## 개요

이 애플리케이션은 Windows 키보드 이벤트를 감시하고 선택한 단축키를 차단합니다. 앱을 실행해도 보호 기능이 자동으로 시작되지는 않습니다. 인터페이스에서 **Start** 버튼을 눌러 보호 기능을 활성화하세요.

## 기능

- **Shift + Delete 차단:** 영구 삭제 단축키를 차단합니다.
- **앱별 F1 차단:** Chrome, Microsoft Edge, Firefox, Brave, Opera 및 Windows 바탕 화면 / 파일 탐색기에서 F1을 차단합니다.
- **보호 기능 선택:** 인터페이스에서 Shift + Delete와 F1 차단을 각각 독립적으로 켜거나 끌 수 있습니다.
- **시스템 트레이로 최소화:** 애플리케이션을 시스템 트레이로 최소화할 수 있습니다.
- **다국어 지원:** 터키어, 영어, 독일어, 프랑스어, 스페인어, 포르투갈어, 러시아어, 일본어, 중국어 간체, 한국어를 지원합니다.
- **스크롤 가능한 인터페이스:** 애플리케이션 창의 내용을 스크롤할 수 있습니다.

F1은 위에 나열된 애플리케이션에서만 차단됩니다. 그 외의 애플리케이션과 게임에서는 F1을 사용할 수 있습니다.

## 요구 사항

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os`, `pathlib`는 Python 표준 라이브러리에 포함되어 있습니다.

시스템 트레이 최소화 기능을 사용하려면 Pillow와 pystray가 모두 필요합니다.

## 설치

1. 프로젝트 파일을 다운로드하거나 저장소를 복제합니다.
2. 프로젝트 폴더를 엽니다.
3. 해당 폴더에서 PowerShell을 실행합니다.
4. 필요한 Python 패키지를 설치합니다.

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` 파일 내용:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. 애플리케이션을 실행합니다.

```powershell
pyw .\ShortcutBlocker.pyw
```

또는 다음 명령을 사용할 수 있습니다.

```powershell
pythonw .\ShortcutBlocker.pyw
```

## 가상 환경 (선택 사항)

의존성 패키지를 별도의 가상 환경에 설치할 수 있습니다.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## 사용 방법

1. `ShortcutBlocker.pyw`를 실행합니다.
2. 인터페이스에서 차단할 단축키를 선택합니다.
3. **Start** 버튼을 눌러 보호 기능을 활성화합니다.
4. 애플리케이션에서 보호 상태를 확인합니다.
5. 최소화 옵션을 사용해 애플리케이션을 시스템 트레이로 보냅니다. 이 기능을 사용하려면 Pillow와 pystray가 설치되어 있어야 합니다.

언어 설정은 다음 위치에 저장됩니다.

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

이 파일에는 언어 선택이 저장됩니다. 단축키 차단 옵션은 애플리케이션에서 선택할 수 있지만, 설정 파일에 저장된다고 가정해서는 안 됩니다.

## 빌드 (EXE 만들기)

EXE를 만들려면 PyInstaller가 필요합니다. 별도로 설치하세요.

```powershell
py -m pip install pyinstaller==6.22.3
```

그런 다음 프로젝트 폴더에서 PowerShell을 열고 빌드 스크립트를 실행합니다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

스크립트는 다음 작업을 수행합니다.

1. 기본 Python 파일과 `assets\icon.png` 파일을 확인합니다.
2. PyInstaller를 사용할 수 있는지 확인합니다.
3. 기존 `dist` 및 `build` 폴더를 삭제합니다.
4. 콘솔 창이 표시되지 않는 단일 EXE 파일을 빌드합니다.
5. `assets` 폴더와 애플리케이션 아이콘을 빌드에 포함합니다.
6. EXE 파일이 생성되었는지 확인합니다.

빌드가 완료되면 애플리케이션은 다음 위치에 생성됩니다.

```text
dist\ShortcutBlocker.exe
```

## 개발자

**vectordevworks**

## 라이선스

라이선스 조건은 프로젝트 저장소의 `LICENSE` 파일을 확인하세요.
