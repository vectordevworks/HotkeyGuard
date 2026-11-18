# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="Inglés"> Inglés</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Alemán"> Alemán</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Francés"> Francés</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="Japonés"> Japonés</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Portugués"> Portugués</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Ruso"> Ruso</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="Chino simplificado"> Chino simplificado</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco</a>

Shortcut Blocker es una aplicación de escritorio ligera para Windows que permite bloquear determinados atajos de teclado. Ayuda a evitar el uso accidental de combinaciones de teclas específicas.

## Descripción general

La aplicación supervisa los eventos del teclado de Windows y bloquea los atajos que selecciones. La protección no se activa automáticamente al abrir la aplicación; debes pulsar **Iniciar** en la interfaz.

## Características

- **Bloqueo de Shift + Delete:** Bloquea el atajo de eliminación permanente.
- **Bloqueo de F1 según la aplicación:** Bloquea F1 en Chrome, Microsoft Edge, Firefox, Brave, Opera y el Escritorio de Windows / Explorador de archivos.
- **Protecciones seleccionables:** Puedes activar o desactivar por separado el bloqueo de Shift + Delete y F1 desde la interfaz.
- **Minimizar a la bandeja del sistema:** Permite minimizar la aplicación a la bandeja del sistema.
- **Varios idiomas:** Turco, inglés, alemán, francés, español, portugués, ruso, japonés, chino simplificado y coreano.
- **Interfaz desplazable:** El contenido de la ventana se puede desplazar.

F1 solo se bloquea en las aplicaciones indicadas. En las demás aplicaciones y en los juegos, F1 sigue disponible.

## Requisitos

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` y `pathlib` forman parte de la biblioteca estándar de Python.

Para utilizar la función de minimización a la bandeja del sistema se necesitan tanto Pillow como pystray.

## Instalación

1. Descarga los archivos del proyecto o clona el repositorio.
2. Abre la carpeta del proyecto.
3. Abre PowerShell dentro de esa carpeta.
4. Instala los paquetes de Python necesarios:

```powershell
py -m pip install -r requirements.txt
```

Contenido de `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Inicia la aplicación:

```powershell
pyw .\ShortcutBlocker.pyw
```

También puedes usar:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Entorno virtual (Opcional)

Puedes mantener las dependencias en un entorno virtual independiente:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Uso

1. Ejecuta `ShortcutBlocker.pyw`.
2. Selecciona en la interfaz los atajos que quieras bloquear.
3. Pulsa **Iniciar** para activar la protección.
4. Consulta el estado de la protección en la aplicación.
5. Usa la opción de minimizar para enviar la aplicación a la bandeja del sistema. Para ello, Pillow y pystray deben estar instalados.

La preferencia de idioma se guarda en:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Este archivo guarda la selección de idioma. Las opciones de bloqueo se pueden seleccionar en la aplicación; no se debe asumir que se guardan en el archivo de configuración.

## Compilación (Crear un EXE)

Se necesita PyInstaller para crear el EXE. Instálalo por separado:

```powershell
py -m pip install pyinstaller==6.22.3
```

Después, abre PowerShell en la carpeta del proyecto y ejecuta el script de compilación:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

El script realiza estas tareas:

1. Comprueba el archivo principal de Python y `assets\icon.png`.
2. Verifica que PyInstaller esté disponible.
3. Elimina las carpetas antiguas `dist` y `build`.
4. Compila un único archivo EXE sin ventana de consola.
5. Incluye la carpeta `assets` y el icono de la aplicación.
6. Comprueba que el EXE se haya creado correctamente.

Al finalizar, la aplicación estará en:

```text
dist\ShortcutBlocker.exe
```

## Desarrollador

**vectordevworks**

## Licencia

Consulta el archivo `LICENSE` del repositorio del proyecto para conocer las condiciones de licencia.
