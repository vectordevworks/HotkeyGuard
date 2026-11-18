# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="Anglais"> Anglais</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Allemand"> Allemand</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Espagnol"> Espagnol</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="Japonais"> Japonais</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="Coréen"> Coréen</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Portugais"> Portugais</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Russe"> Russe</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="Chinois simplifié"> Chinois simplifié</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Turc"> Turc</a>

Shortcut Blocker est une application de bureau légère pour Windows qui permet de bloquer certains raccourcis clavier. Elle aide à éviter l'utilisation accidentelle de combinaisons de touches spécifiques.

## Présentation

L'application surveille les événements du clavier Windows et bloque les raccourcis sélectionnés. La protection ne s'active pas automatiquement à l'ouverture de l'application : cliquez sur **Démarrer** dans l'interface pour l'activer.

## Fonctionnalités

- **Blocage de Shift + Delete :** bloque le raccourci de suppression définitive.
- **Blocage de F1 selon l'application :** bloque F1 dans Chrome, Microsoft Edge, Firefox, Brave, Opera et sur le Bureau Windows / dans l'Explorateur de fichiers.
- **Protections sélectionnables :** activez ou désactivez séparément le blocage de Shift + Delete et de F1 dans l'interface.
- **Réduction dans la zone de notification :** permet de réduire l'application dans la zone de notification.
- **Plusieurs langues :** turc, anglais, allemand, français, espagnol, portugais, russe, japonais, chinois simplifié et coréen.
- **Interface défilante :** le contenu de la fenêtre peut défiler.

F1 est bloquée uniquement dans les applications indiquées ci-dessus. Dans les autres applications et les jeux, F1 reste disponible.

## Prérequis

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` et `pathlib` font partie de la bibliothèque standard de Python.

Pillow et pystray sont tous deux nécessaires pour utiliser la réduction dans la zone de notification.

## Installation

1. Téléchargez les fichiers du projet ou clonez le dépôt.
2. Ouvrez le dossier du projet.
3. Ouvrez PowerShell dans ce dossier.
4. Installez les packages Python nécessaires :

```powershell
py -m pip install -r requirements.txt
```

Contenu de `requirements.txt` :

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Lancez l'application :

```powershell
pyw .\ShortcutBlocker.pyw
```

Vous pouvez également utiliser :

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Environnement virtuel (Facultatif)

Vous pouvez isoler les dépendances dans un environnement virtuel :

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Utilisation

1. Exécutez `ShortcutBlocker.pyw`.
2. Sélectionnez dans l'interface les raccourcis que vous souhaitez bloquer.
3. Cliquez sur **Démarrer** pour activer la protection.
4. Consultez l'état de la protection dans l'application.
5. Utilisez l'option de réduction pour placer l'application dans la zone de notification. Pillow et pystray doivent être installés pour cette fonction.

La préférence de langue est enregistrée ici :

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Ce fichier enregistre le choix de langue. Les options de blocage peuvent être sélectionnées dans l'application ; il ne faut pas supposer qu'elles sont enregistrées dans le fichier de configuration.

## Compilation (Créer un EXE)

PyInstaller est nécessaire pour créer l'EXE. Installez-le séparément :

```powershell
py -m pip install pyinstaller==6.22.3
```

Ouvrez ensuite PowerShell dans le dossier du projet et exécutez le script de compilation :

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

Le script effectue les opérations suivantes :

1. Vérifie le fichier Python principal et `assets\icon.png`.
2. Vérifie que PyInstaller est disponible.
3. Supprime les anciens dossiers `dist` et `build`.
4. Compile un EXE unique sans fenêtre de console.
5. Inclut le dossier `assets` et l'icône de l'application.
6. Vérifie que le fichier EXE a bien été créé.

Après la compilation, l'application se trouve ici :

```text
dist\ShortcutBlocker.exe
```

## Développeur

**vectordevworks**

## Licence

Consultez le fichier `LICENSE` du dépôt pour connaître les conditions de licence.
