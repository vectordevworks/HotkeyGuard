# Bloqueador de Atajos de Teclado

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Inglés"> Inglés
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Alemán"> Alemán
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Francés"> Francés
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonés"> Japonés
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugués"> Portugués
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Ruso"> Ruso
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chino simplificado"> Chino simplificado
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco
</a>

Shortcut Blocker es una aplicación de escritorio ligera basada en Python que permite bloquear determinados atajos de teclado en Windows. Su sencilla interfaz gráfica facilita la prevención de atajos activados accidentalmente y la gestión de las protecciones seleccionadas.

## Descripción general

La aplicación supervisa los eventos del teclado de Windows y bloquea los atajos que seleccione. La protección no se activa automáticamente al iniciar la aplicación; debe hacer clic en el botón **Iniciar** desde la interfaz.

## Características

- **Bloqueo de Shift + Delete:** Bloquea el atajo utilizado para eliminar archivos de forma permanente.
- **Bloqueo de F1 específico por aplicación:** Bloquea la tecla F1 en Chrome, Microsoft Edge, Firefox, Brave, Opera, así como en el Escritorio de Windows y el Explorador de archivos.
- **Protecciones seleccionables:** Puede activar o desactivar de forma independiente los bloqueos de Shift + Delete y F1 desde la interfaz.
- **Minimizar en la bandeja del sistema:** Permite minimizar la aplicación en la bandeja del sistema.
- **Compatibilidad con varios idiomas:** Compatible con turco, inglés, alemán, francés, español, portugués, ruso, japonés, chino simplificado y coreano.
- **Interfaz con desplazamiento:** El contenido de la ventana de la aplicación se puede desplazar.

El bloqueo de F1 solo está activo en las aplicaciones mencionadas anteriormente. La tecla F1 no se bloquea en otras aplicaciones ni en juegos.

## Requisitos

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` y `pathlib` forman parte de la biblioteca estándar de Python.

Para utilizar la función de minimización en la bandeja del sistema, se necesitan tanto Pillow como pystray.

## Instalación

1. Descargue los archivos del proyecto en su ordenador o clone el repositorio.
2. Abra la carpeta del proyecto.
3. Abra PowerShell en esta carpeta.
4. Instale los paquetes de Python necesarios:

```powershell
py -m pip install -r requirements.txt
```

Contenido del archivo `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Inicie la aplicación:

```powershell
pyw .\ShortcutBlocker.pyw
```

Como alternativa, puede utilizar:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Entorno virtual (Opcional)

Puede mantener las dependencias de Python aisladas de otros proyectos mediante un entorno virtual:

1. Cree un entorno virtual:

```powershell
py -m venv .venv
```

2. Active el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instale las dependencias necesarias:

```powershell
py -m pip install -r requirements.txt
```

4. Desactive el entorno virtual cuando termine:

```powershell
deactivate
```

## Uso

1. Ejecute el archivo `ShortcutBlocker.pyw`.
2. Seleccione en la interfaz los atajos que desea bloquear.
3. Haga clic en **Iniciar** para activar la protección.
4. Consulte el estado de la protección desde la interfaz de la aplicación.
5. Utilice la opción de minimizar para enviar la aplicación a la bandeja del sistema. Para utilizar esta función, Pillow y pystray deben estar instalados.

La preferencia de idioma se almacena en la siguiente ubicación:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Este archivo almacena únicamente la selección de idioma. Las opciones de bloqueo de atajos se pueden seleccionar en los ajustes de la aplicación; no debe suponerse que estas opciones se guardan en el archivo de configuración.

## Creación del archivo EXE

PyInstaller se utiliza para convertir la aplicación Python en un único archivo EXE.

### 1. Instalación de PyInstaller

Instale la versión 6.22.3 de PyInstaller:

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. Abrir la carpeta del proyecto

Abra PowerShell en la carpeta del proyecto.

### 3. Ejecutar el script de compilación

Ejecute el siguiente comando para iniciar el script `embed_icon.ps1`:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** Se utiliza `-ExecutionPolicy Bypass` porque Windows puede impedir la ejecución de scripts de PowerShell debido a la directiva de ejecución vigente. Esta configuración solo se aplica al proceso de PowerShell iniciado y no modifica los ajustes de seguridad de todo el sistema.

### 4. Proceso de compilación

El script de compilación realiza las siguientes operaciones:

1. Comprueba el archivo principal de Python y el archivo `assets\icon.png`.
2. Verifica que PyInstaller esté disponible.
3. Elimina las carpetas anteriores `dist` y `build`.
4. Genera la aplicación como un único archivo EXE sin mostrar una ventana de consola.
5. Incluye la carpeta `assets` y el icono de la aplicación en la compilación.
6. Comprueba el archivo EXE generado.

### 5. Resultado de la compilación

Una vez completada correctamente la compilación, el archivo EXE se crea en la siguiente ubicación:

```text
dist\ShortcutBlocker.exe
```

**Pasos para compilar una nueva versión:**

1. Abra PowerShell.
2. Asegúrese de que PyInstaller esté instalado.
3. Acceda a la carpeta del proyecto.
4. Ejecute el script de compilación.
5. Encontrará el archivo EXE generado en la carpeta `dist`.

## Desarrollador

**vectordevworks**

## Licencia

Consulte el archivo `LICENSE` del repositorio del proyecto para conocer las condiciones de la licencia.
