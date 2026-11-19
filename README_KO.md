<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="영어"> 영어
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="독일어"> 독일어
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="스페인어"> 스페인어
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="프랑스어"> 프랑스어
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="일본어"> 일본어
</a>
|
<strong>
  <img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어
</strong>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="포르투갈어"> 포르투갈어
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="러시아어"> 러시아어
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="터키어"> 터키어
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="중국어 간체"> 중국어 간체
</a>

### 단축키지킴이는 Windows에서 특정 키보드 단축키를 차단할 수 있는 Python 기반의 가벼운 데스크톱 애플리케이션입니다. 간단한 그래픽 인터페이스를 통해 실수로 실행될 수 있는 단축키를 제어하고 원하는 보호 기능을 쉽게 관리할 수 있습니다.

## 개요

이 애플리케이션은 Windows의 키보드 이벤트를 모니터링하고 사용자가 선택한 단축키를 차단합니다. 애플리케이션을 실행해도 보호 기능이 자동으로 활성화되지는 않습니다. 보호 기능을 시작하려면 인터페이스에서 **시작** 버튼을 클릭해야 합니다.

## 주요 기능

- **Shift + Delete 차단:** 파일을 영구적으로 삭제하는 단축키를 차단합니다.
- **애플리케이션별 F1 키 차단:** Chrome, Microsoft Edge, Firefox, Brave, Opera 및 Windows 바탕 화면과 파일 탐색기에서 F1 키를 차단합니다.
- **개별 보호 기능 설정:** 인터페이스에서 Shift + Delete와 F1 차단 기능을 각각 독립적으로 활성화하거나 비활성화할 수 있습니다.
- **시스템 트레이로 최소화:** 애플리케이션을 시스템 트레이로 최소화할 수 있습니다.
- **다국어 지원:** 터키어, 영어, 독일어, 프랑스어, 스페인어, 포르투갈어, 러시아어, 일본어, 중국어 간체 및 한국어를 지원합니다.
- **스크롤 가능한 인터페이스:** 애플리케이션 창의 내용을 스크롤할 수 있습니다.

F1 차단 기능은 위에 명시된 애플리케이션에서만 활성화됩니다. 그 외의 애플리케이션이나 게임에서는 F1 키가 차단되지 않습니다.

## 시스템 요구 사항

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` 및 `pathlib`은 Python 표준 라이브러리에 포함되어 있습니다.

시스템 트레이 기능을 사용하려면 Pillow와 pystray가 모두 필요합니다.

## 설치

1. 프로젝트 파일을 컴퓨터에 다운로드하거나 저장소를 클론합니다.
2. 프로젝트 폴더를 엽니다.
3. 해당 폴더에서 PowerShell을 실행합니다.
4. 필요한 Python 패키지를 설치합니다.

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` 파일의 내용:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. 애플리케이션을 실행합니다.

```powershell
pyw .\HotkeyGuard.pyw
```

또는 다음 명령을 사용할 수 있습니다.

```powershell
pythonw .\HotkeyGuard.pyw
```

## 가상 환경 (선택 사항)

가상 환경을 사용하면 Python 의존성을 다른 프로젝트와 분리하여 관리할 수 있습니다.

1. 가상 환경을 생성합니다.

```powershell
py -m venv .venv
```

2. 가상 환경을 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

3. 필요한 의존성을 설치합니다.

```powershell
py -m pip install -r requirements.txt
```

4. 작업을 마치면 가상 환경을 비활성화합니다.

```powershell
deactivate
```

## 사용 방법

1. `HotkeyGuard.pyw` 파일을 실행합니다.
2. 인터페이스에서 차단하려는 단축키를 선택합니다.
3. 보호 기능을 활성화하려면 **시작** 버튼을 클릭합니다.
4. 애플리케이션 인터페이스에서 보호 상태를 확인합니다.
5. 최소화 옵션을 사용하여 애플리케이션을 시스템 트레이로 이동합니다. 이 기능을 사용하려면 Pillow와 pystray가 설치되어 있어야 합니다.

언어 설정은 다음 위치에 저장됩니다.

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

이 파일에는 언어 선택 정보만 저장됩니다. 단축키 차단 옵션은 애플리케이션 내에서 선택할 수 있지만, 해당 설정이 설정 파일에 저장된다고 가정해서는 안 됩니다.

## 빌드 (EXE 파일 생성)

PyInstaller를 사용하여 Python 애플리케이션을 단일 EXE 파일로 변환합니다.

### 2. 프로젝트 폴더 열기

프로젝트 폴더에서 PowerShell을 실행합니다.

### 3. 빌드 스크립트 실행

다음 명령을 실행하여 `embed_icon.ps1` 스크립트를 시작합니다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**참고:** Windows의 실행 정책으로 인해 PowerShell 스크립트 실행이 제한될 수 있으므로 `-ExecutionPolicy Bypass`를 사용합니다. 이 설정은 새로 시작된 PowerShell 프로세스에만 적용되며 시스템 전체의 보안 설정은 변경하지 않습니다.

### 4. 빌드 과정

빌드 스크립트는 다음 작업을 수행합니다.

1. 메인 Python 파일과 `assets\icon.png` 파일이 존재하는지 확인합니다.
2. PyInstaller를 사용할 수 있는지 확인합니다.
3. 기존 `dist` 및 `build` 폴더를 삭제합니다.
4. 콘솔 창이 표시되지 않는 단일 파일 EXE로 애플리케이션을 빌드합니다.
5. `assets` 폴더와 애플리케이션 아이콘을 빌드에 포함합니다.
6. 생성된 EXE 파일이 정상적으로 만들어졌는지 확인합니다.

### 5. 빌드 결과

빌드가 성공적으로 완료되면 EXE 파일이 다음 위치에 생성됩니다.

```text
dist\HotkeyGuard.exe
```

**새 버전을 빌드하는 방법:**

1. PowerShell을 실행합니다.
2. PyInstaller가 설치되어 있는지 확인합니다.
3. 프로젝트 폴더로 이동합니다.
4. 빌드 스크립트를 실행합니다.
5. `dist` 폴더에서 생성된 EXE 파일을 확인합니다.

## 개발자

**vectordevworks**

## 라이선스

라이선스 조건에 대한 자세한 내용은 프로젝트 저장소의 `LICENSE` 파일을 참조하세요.