# GardeRaccourcis

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Anglais"> Anglais
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Allemand"> Allemand
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Espagnol"> Espagnol
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonais"> Japonais
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coréen"> Coréen
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugais"> Portugais
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russe"> Russe
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chinois simplifié"> Chinois simplifié
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turc"> Turc
</a>

GardeRaccourcis est une application de bureau légère développée en Python qui vous permet de bloquer certains raccourcis clavier sous Windows. Son interface graphique simple et intuitive vous aide à éviter les déclenchements accidentels de raccourcis et à gérer facilement les protections de votre choix.

## Présentation générale

L'application surveille les événements du clavier sous Windows et bloque les raccourcis que vous sélectionnez. La protection ne s'active pas automatiquement au démarrage de l'application ; vous devez cliquer sur le bouton **Démarrer** dans l'interface.

## Fonctionnalités

- **Blocage de Shift + Delete :** Bloque le raccourci permettant de supprimer définitivement des fichiers.
- **Blocage de F1 spécifique à chaque application :** Bloque la touche F1 dans Chrome, Microsoft Edge, Firefox, Brave et Opera, ainsi que sur le Bureau Windows et dans l'Explorateur de fichiers.
- **Protections sélectionnables :** Vous pouvez activer ou désactiver indépendamment le blocage de Shift + Delete et celui de F1 depuis l'interface.
- **Réduction dans la zone de notification système :** Permet de réduire l'application dans la zone de notification de la barre des tâches.
- **Prise en charge multilingue :** Prend en charge le turc, l'anglais, l'allemand, le français, l'espagnol, le portugais, le russe, le japonais, le chinois simplifié et le coréen.
- **Interface avec défilement :** Le contenu de la fenêtre de l'application peut défiler.

Le blocage de F1 est uniquement actif dans les applications mentionnées ci-dessus. La touche F1 n'est pas bloquée dans les autres applications ni dans les jeux.

## Configuration requise

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` et `pathlib` font partie de la bibliothèque standard de Python.

Pillow et pystray sont tous deux nécessaires pour utiliser la fonction de réduction dans la zone de notification système.

## Installation

1. Téléchargez les fichiers du projet sur votre ordinateur ou clonez le dépôt.
2. Ouvrez le dossier du projet.
3. Ouvrez PowerShell dans ce dossier.
4. Installez les paquets Python nécessaires :

```powershell
py -m pip install -r requirements.txt
```

Contenu du fichier `requirements.txt` :

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Lancez l'application :

```powershell
pyw .\HotkeyGuard.pyw
```

Vous pouvez également utiliser la commande suivante :

```powershell
pythonw .\HotkeyGuard.pyw
```

## Environnement virtuel (Facultatif)

Vous pouvez isoler les dépendances Python des autres projets à l'aide d'un environnement virtuel :

1. Créez un environnement virtuel :

```powershell
py -m venv .venv
```

2. Activez l'environnement virtuel :

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Installez les dépendances nécessaires :

```powershell
py -m pip install -r requirements.txt
```

4. Désactivez l'environnement virtuel lorsque vous avez terminé :

```powershell
deactivate
```

## Utilisation

1. Exécutez le fichier `HotkeyGuard.pyw`.
2. Sélectionnez dans l'interface les raccourcis que vous souhaitez bloquer.
3. Cliquez sur **Démarrer** pour activer la protection.
4. Consultez l'état de la protection depuis l'interface de l'application.
5. Utilisez l'option de réduction pour placer l'application dans la zone de notification de la barre des tâches. Pillow et pystray doivent être installés pour utiliser cette fonctionnalité.

La préférence linguistique est enregistrée à l'emplacement suivant :

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Ce fichier enregistre uniquement la sélection de la langue. Les options de blocage des raccourcis peuvent être sélectionnées dans les paramètres de l'application ; il ne faut pas supposer que ces options sont enregistrées dans le fichier de configuration.

## Création du fichier EXE

PyInstaller est utilisé pour convertir l'application Python en un seul fichier EXE.

### 1. Installation de PyInstaller

Installez la version 6.22.3 de PyInstaller :

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. Ouvrir le dossier du projet

Ouvrez PowerShell dans le dossier du projet.

### 3. Exécuter le script de compilation

Exécutez la commande suivante pour lancer le script `embed_icon.ps1` :

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Remarque :** `-ExecutionPolicy Bypass` est utilisé car Windows peut empêcher l'exécution des scripts PowerShell en raison de la stratégie d'exécution en vigueur. Ce paramètre s'applique uniquement au processus PowerShell lancé et ne modifie pas les paramètres de sécurité globaux du système.

### 4. Processus de compilation

Le script de compilation effectue les opérations suivantes :

1. Vérifie le fichier Python principal et le fichier `assets\icon.png`.
2. Vérifie que PyInstaller est disponible.
3. Supprime les anciens dossiers `dist` et `build`.
4. Génère l'application sous la forme d'un fichier EXE unique, sans afficher de fenêtre de console.
5. Inclut le dossier `assets` et l'icône de l'application dans la compilation.
6. Vérifie le fichier EXE généré.

### 5. Résultat de la compilation

Une fois la compilation terminée avec succès, le fichier EXE est créé à l'emplacement suivant :

```text
dist\HotkeyGuard.exe
```

**Étapes à suivre pour compiler une nouvelle version :**

1. Ouvrez PowerShell.
2. Assurez-vous que PyInstaller est installé.
3. Accédez au dossier du projet.
4. Exécutez le script de compilation.
5. Le fichier EXE généré se trouve dans le dossier `dist`.

## Développeur

**vectordevworks**

## Licence

Consultez le fichier `LICENSE` dans le dépôt du projet pour connaître les conditions de licence.