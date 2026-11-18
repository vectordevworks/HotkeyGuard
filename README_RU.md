# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="Английский"> Английский</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Немецкий"> Немецкий</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Испанский"> Испанский</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Французский"> Французский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="Японский"> Японский</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="Корейский"> Корейский</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Португальский"> Португальский</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="Упрощённый китайский"> Упрощённый китайский</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Турецкий"> Турецкий</a>

Shortcut Blocker — это лёгкое настольное приложение для Windows, позволяющее блокировать выбранные сочетания клавиш. Оно помогает предотвратить случайное использование определённых сочетаний клавиш.

## Обзор

Приложение отслеживает события клавиатуры Windows и блокирует выбранные сочетания клавиш. Защита не включается автоматически при запуске приложения: для её активации нажмите **Start** в интерфейсе.

## Возможности

- **Блокировка Shift + Delete:** блокирует сочетание клавиш для безвозвратного удаления.
- **Блокировка F1 в определённых приложениях:** блокирует F1 в Chrome, Microsoft Edge, Firefox, Brave, Opera, а также на рабочем столе Windows / в Проводнике.
- **Выбор защиты:** блокировку Shift + Delete и F1 можно независимо включать и отключать в интерфейсе.
- **Сворачивание в системный трей:** приложение можно свернуть в системный трей.
- **Несколько языков:** турецкий, английский, немецкий, французский, испанский, португальский, русский, японский, упрощённый китайский и корейский.
- **Прокручиваемый интерфейс:** содержимое окна приложения можно прокручивать.

Клавиша F1 блокируется только в перечисленных выше приложениях. В остальных приложениях и играх F1 остаётся доступной.

## Требования

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` и `pathlib` входят в стандартную библиотеку Python.

Для сворачивания приложения в системный трей необходимы и Pillow, и pystray.

## Установка

1. Скачайте файлы проекта или клонируйте репозиторий.
2. Откройте папку проекта.
3. Запустите PowerShell в этой папке.
4. Установите необходимые пакеты Python:

```powershell
py -m pip install -r requirements.txt
```

Содержимое `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Запустите приложение:

```powershell
pyw .\ShortcutBlocker.pyw
```

Также можно использовать:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Виртуальное окружение (Необязательно)

Зависимости можно установить в отдельное виртуальное окружение:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Использование

1. Запустите `ShortcutBlocker.pyw`.
2. Выберите в интерфейсе сочетания клавиш, которые нужно блокировать.
3. Нажмите **Start**, чтобы включить защиту.
4. Следите за состоянием защиты в приложении.
5. Используйте команду сворачивания, чтобы переместить приложение в системный трей. Для этой функции должны быть установлены Pillow и pystray.

Выбранный язык сохраняется по следующему пути:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Этот файл сохраняет выбранный язык. Параметры блокировки можно выбирать в приложении; не следует считать, что они сохраняются в файле конфигурации.

## Сборка (Создание EXE)

Для создания EXE требуется PyInstaller. Установите его отдельно:

```powershell
py -m pip install pyinstaller==6.22.3
```

Затем откройте PowerShell в папке проекта и запустите скрипт сборки:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

Скрипт выполняет следующие действия:

1. Проверяет основной файл Python и `assets\icon.png`.
2. Проверяет доступность PyInstaller.
3. Удаляет старые папки `dist` и `build`.
4. Создаёт единый EXE-файл без окна консоли.
5. Добавляет папку `assets` и значок приложения в сборку.
6. Проверяет, что EXE-файл создан.

После успешной сборки приложение будет находиться здесь:

```text
dist\ShortcutBlocker.exe
```

## Разработчик

**vectordevworks**

## Лицензия

Условия лицензии указаны в файле `LICENSE` в репозитории проекта.
