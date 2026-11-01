# Partie 2 — Exécuter les notebooks en local

## Guide facultatif — Windows et macOS

Cours : Langues de spécialité

Ce guide s’adresse aux personnes qui souhaitent exécuter les notebooks et les scripts sur leur propre ordinateur, dans VS Code.

> Cette installation n’est pas obligatoire pour réussir le cours. Vous pouvez utiliser Google Colab sans installer Python sur votre ordinateur.

Pour ce parcours, le dépôt local et le dossier `.venv` sont conservés dans Google Drive configuré en mode miroir. Les fichiers sont donc présents sur le disque de l’ordinateur et synchronisés dans Drive.

L’environnement `.venv` reste toutefois propre à l’ordinateur qui l’a créé : le mode miroir ne le rend pas portable entre Windows, macOS ou différents ordinateurs. Colab utilise son propre environnement et ne doit pas exécuter celui de `.venv`.

## Avant de commencer

La première partie du guide doit être terminée :

- votre dépôt privé personnel ou d’équipe est créé sur GitHub ;
- il est cloné dans `Mon Drive/GitHub/<nom_du_projet>` ;
- Drive pour ordinateur est configuré en mode miroir et synchronisé ;
- VS Code ouvre la racine de ce dépôt ;
- les extensions `Python` et `Jupyter`, publiées par Microsoft, sont installées.

Remplacez `LSP_nom_prenom` par le nom de votre projet dans les exemples. Les fichiers pédagogiques seront ajoutés séparément : ne supposez pas encore la présence d’un fichier `requirements.txt`.

Les blocs `powershell` et `bash` sont à exécuter dans un terminal, pas dans une cellule Python.

## 1. Installer Python 3.12

Python 3.12 est la version de référence pour le travail local du cours.

### 1.1 Windows — Python Install Manager

Installez Python Install Manager depuis [le site Python](https://www.python.org/downloads/) ou le Microsoft Store indiqué par ce site. Fermez puis rouvrez PowerShell :

```powershell
py list
py install 3.12
py -3.12 --version
```

Le résultat de la dernière commande doit commencer par `Python 3.12`. Si cette version fonctionne déjà, ne la réinstallez pas.

Si `py list` ou `py install` n’est pas reconnu, une ancienne installation peut utiliser `py`. Le gestionnaire récent fournit aussi `pymanager list` et `pymanager install 3.12`. Demandez de l’aide avant toute désinstallation.

### 1.2 macOS — Python avec uv

`uv` est un gestionnaire tiers qui permet d’installer Python sans remplacer le Python du système. Consultez [la documentation officielle d’installation](https://docs.astral.sh/uv/getting-started/installation/).

L’installateur proposé pour le Terminal :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Cette commande télécharge et exécute un script. Utilisez uniquement l’adresse officielle et vérifiez que l’installation est autorisée sur l’ordinateur. La documentation propose l’inspection du script et d’autres méthodes.

Rouvrez le Terminal :

```bash
uv --version
uv python install 3.12
```

Les distributions téléchargées par uv proviennent du projet `python-build-standalone` d’Astral. Un Python 3.12 déjà installé peut aussi être utilisé avec `python3.12 -m venv`.

## 2. Ouvrir le bon dossier de travail

1. Dans VS Code, ouvrez la racine du dépôt dans Drive avec `File` → `Open Folder…`, ou `Open…` selon le système.
2. Ouvrez `Terminal` → `New Terminal`.
3. Vérifiez le dossier courant.

Windows PowerShell :

```powershell
Get-Location
```

macOS :

```bash
pwd
```

Le chemin doit se terminer par `GitHub/LSP_nom_prenom` et correspondre au dossier contenant votre README et `.git`.

Le chemin local de Mon Drive dépend de l’installation. Copiez le vrai chemin depuis l’Explorateur Windows ou le Finder ; ne supposez pas une lettre de lecteur ou un nom universel.

> Toutes les commandes utilisant `.venv` dans ce guide supposent que le terminal se trouve à la racine du dépôt.

## 3. Exclure .venv de Git avant sa création

Dans VS Code, ouvrez le fichier `.gitignore` à la racine du dépôt. S’il n’existe pas, créez ce fichier texte avec ce nom exact, sans extension `.txt`.

Ajoutez cette ligne si aucune règle existante ne couvre déjà `.venv` :

```gitignore
.venv/
```

Enregistrez sans supprimer les autres règles.

| Service | Traitement de `.venv` |
|---|---|
| Google Drive | Peut synchroniser le dossier avec le reste du projet. |
| Git et GitHub | Doivent l’ignorer grâce à `.gitignore`. |
| Colab | Ne doit pas utiliser cet environnement local. |

> `.gitignore` n’empêche pas la synchronisation Drive et ne retire pas les fichiers déjà suivis par Git. Si `.venv` apparaît déjà dans un commit, demandez de l’aide.

## 4. Créer et activer .venv dans le projet

La création se fait une seule fois pour cette copie du projet sur cet ordinateur.

### 4.1 Windows

À la racine du dépôt, dans PowerShell :

```powershell
py -3.12 -m venv .venv
```

Puis activez l’environnement :

```powershell
.\.venv\Scripts\Activate.ps1
```

Le terminal affiche généralement `(.venv)` au début de la ligne.

### 4.2 macOS

À la racine du dépôt, dans le Terminal :

```bash
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
```

L’option `--seed` installe notamment pip.

Si Python 3.12 est déjà installé par une autre méthode, la création peut se faire à la place avec :

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Choisissez une seule méthode ; ne lancez pas les deux créations successivement. Sans activation, utilisez directement :

```bash
./.venv/bin/python --version
```

### 4.3 Vérifier l’environnement

Avec l’environnement activé, sur les deux systèmes :

```bash
python --version
python -c "import sys; print(sys.executable)"
```

Le résultat doit afficher Python 3.12 et un exécutable dans :

```text
Windows : <dépôt dans Drive>/.venv/Scripts/python.exe
macOS   : <dépôt dans Drive>/.venv/bin/python
```

Vérifiez également l’exclusion par Git :

```bash
git check-ignore .venv/pyvenv.cfg
```

Le chemin `.venv/pyvenv.cfg` doit s’afficher. Si rien ne s’affiche, vérifiez le `.gitignore`, le dossier courant et l’état du suivi Git avant tout commit. Ne sélectionnez pas les fichiers de l’environnement pour les envoyer.

## 5. Installer le noyau et les dépendances

Avec l’environnement activé :

```bash
python -m pip install --upgrade pip
python -m pip install ipykernel
```

`ipykernel` permet d’exécuter les cellules Python des notebooks avec cet environnement. Il est distinct de l’extension Jupyter de VS Code.

Les bibliothèques des activités seront installées au moment opportun. Si un fichier de dépendances est fourni plus tard, utilisez son chemin réel depuis la racine du dépôt, par exemple :

```bash
python -m pip install -r requirements.txt
```

N’exécutez cette dernière commande que si le fichier existe et correspond aux consignes.

Attendez que l’installation soit terminée avant de laisser Drive achever sa synchronisation. N’installez pas de bibliothèques simultanément dans cette même copie depuis plusieurs ordinateurs.

## 6. Sélectionner .venv dans VS Code

### 6.1 Pour les scripts

1. Ouvrez la palette : `Ctrl + Maj + P` sous Windows, `Cmd + Maj + P` sous macOS.
2. Lancez `Python: Select Interpreter`.
3. Choisissez Python 3.12 dans `.venv`.

### 6.2 Pour les notebooks

1. Ouvrez le notebook `.ipynb`.
2. Cliquez sur `Select Kernel`.
3. Choisissez les environnements Python, puis Python 3.12 dans `.venv`.

Vérifiez le noyau dans chaque notebook. La sélection de l’interpréteur des scripts ne garantit pas que les notebooks utilisent tous le même environnement.

## 7. Tester le travail local

### 7.1 Créer un notebook d’essai

1. Dans VS Code, lancez `File -> New File -> Jupyter Notebook`.
2. Enregistrez le fichier que vous pouvez nommer `test_environnement.ipynb` dans un nouveau dossier que vous pouvez nommer **test** à la racine du dépôt, s’il n’existe pas déjà.
3. Choisissez le noyau de `.venv`.
4. Exécutez :

```python
import platform
import sys

print("Version de Python :", platform.python_version())
print("Exécutable :", sys.executable)
print("Environnement virtuel :", sys.prefix != sys.base_prefix)
```

En local, le chemin doit pointer vers `.venv` et la dernière valeur doit être `True`.

Enregistrez, fermez le notebook et attendez sa synchronisation dans Drive.

### 7.2 Ouvrir le même fichier dans Colab

1. Dans le navigateur, ouvrez Mon Drive → `GitHub` → votre dépôt.
2. Ouvrez le notebook avec `Google Colaboratory`.
3. Si l’application n’est pas proposée, recherchez-la dans la connexion d’applications de Drive, selon les autorisations institutionnelles.
4. Vérifiez qu’il s’agit du fichier du dépôt, et non d’une copie enregistrée ailleurs.
5. Exécutez la cellule d’information.

Colab utilise son propre Python. Il peut avoir une autre version que Python 3.12 et n’utilise pas `.venv`, même si ce dossier est visible dans Drive.

N’activez pas `.venv` et ne lancez pas ses exécutables depuis Colab. Les bibliothèques nécessaires doivent être installées dans la session Colab selon les consignes de l’activité.

### 7.3 Définir le dossier de travail commun

Cette cellule peut être reprise dans les notebooks après adaptation :

```python
from pathlib import Path
import platform
import os

# True dans VS Code ; False dans Google Colab.
IS_LOCAL = False
NOM_PROJET = "LSP_nom_prenom"

if IS_LOCAL:
    racines_locales = {
        "Windows": Path(r"C:\CHEMIN_A_REMPLACER\Mon Drive"),
        "Darwin": Path("/CHEMIN_A_REMPLACER/Mon Drive"),
    }
    systeme = platform.system()
    if systeme not in racines_locales:
        raise RuntimeError(f"Système non prévu : {systeme}")
    racine_drive = racines_locales[systeme]
else:
    from google.colab import drive
    drive.mount("/content/drive")
    racine_drive = Path("/content/drive/MyDrive")

chemin_projet = racine_drive / "GitHub" / NOM_PROJET

if not chemin_projet.is_dir():
    raise FileNotFoundError(
        f"Dossier introuvable : {chemin_projet}. "
        "Vérifiez le chemin, le compte Google et la synchronisation."
    )

os.chdir(chemin_projet)
print("Dossier de travail :", Path.cwd())
```

`Darwin` désigne macOS. En local, utilisez `IS_LOCAL = True` et le vrai chemin de Mon Drive. Dans Colab, utilisez `False` et autorisez le montage.

Ne manipulez pas `.git` et ne faites pas d’opérations Git sur ce dossier depuis Colab. Réalisez les commits, les récupérations et les envois depuis l’ordinateur, dans Desktop.

Les variables en mémoire ne sont pas sauvegardées dans Drive automatiquement. Les sorties durables doivent être enregistrées dans les emplacements autorisés, pas seulement dans l’espace temporaire de Colab.

## 8. Routine de travail

### Début de séance

1. Vérifiez qu’aucune autre session ne modifie la même copie.
2. Attendez la fin de la synchronisation Drive.
3. Dans Desktop, examinez les changements, puis faites Fetch et Pull si nécessaire et sans conflit.
4. En local, activez l’environnement et sélectionnez son noyau.
5. Ouvrez le notebook dans VS Code ou Colab, pas dans les deux simultanément.

Activation Windows :

```powershell
.\.venv\Scripts\Activate.ps1
```

Activation macOS :

```bash
source .venv/bin/activate
```

### Fin de séance

1. Enregistrez les fichiers et vérifiez les sorties.
2. Si vous êtes dans Colab, vérifiez l’emplacement d’enregistrement et fermez sa session d’édition.
3. Attendez que les fichiers modifiés soient disponibles sur l’ordinateur.
4. Dans Desktop, sélectionnez uniquement les fichiers utiles et autorisés ; `.venv` ne doit pas être ajouté.
5. Créez un commit, faites `Push origin`, puis vérifiez GitHub.
6. Laissez Drive terminer sa synchronisation.

Drive synchronise des fichiers ; Git échange des commits. L’un ne remplace pas l’autre.

## 9. Limites du miroir et protection des fichiers

Le mode miroir permet d’utiliser un dossier local, mais ne transforme pas l’environnement en installation universelle.

- Utilisez cette `.venv` sur l’ordinateur où elle a été créée.
- Ne réutilisez pas sa copie synchronisée sur un autre ordinateur, même si Drive l’a entièrement téléchargée.
- Si vous changez d’ordinateur, de système ou de chemin du projet, faites recréer un environnement adapté. Ne lancez pas deux recréations concurrentes dans la même copie synchronisée.
- Ne partagez pas cette copie Drive du dépôt entre équipiers ; chaque personne garde son propre clone.
- Un environnement contient de nombreux fichiers et peut augmenter le temps de synchronisation et l’espace utilisé. Le miroir ne garantit pas que tous ses éléments seront synchronisés sans problème.
- Si Drive crée des copies conflictuelles ou si Python ne retrouve plus ses fichiers, conservez votre code et vos données et demandez de l’aide pour recréer l’environnement. Il est recréable ; vos sources ne doivent jamais être stockées à l’intérieur.

N’ajoutez aucun mot de passe, token ou contenu non autorisé au dépôt. Inspectez aussi les sorties des notebooks. Un fichier privé ou ignoré par Git peut tout de même être stocké dans Drive : cette conservation doit être autorisée.

## 10. Résultat attendu et checklist

```text
Mon Drive/
└── GitHub/
    └── LSP_nom_prenom/
        ├── .git/
        ├── .gitignore
        ├── .venv/                   # Local, synchronisé par Drive, ignoré par Git
        ├── README.md
        └── test_environnement.ipynb
```

Les contenus pédagogiques du cours seront ajoutés séparément.

- [ ] Drive utilise le mode miroir et dispose d’espace suffisant.
- [ ] VS Code ouvre la racine du bon dépôt.
- [ ] `.venv/` est exclu par `.gitignore` avant le commit.
- [ ] Python 3.12 fonctionne dans `.venv`.
- [ ] `ipykernel` est installé dans cet environnement.
- [ ] VS Code utilise le bon interpréteur et le bon noyau.
- [ ] Colab utilise son propre environnement, pas `.venv`.
- [ ] Je ne modifie pas simultanément le même notebook dans deux environnements.
- [ ] Je sais enregistrer, attendre la synchronisation, commiter et envoyer.

Vous pouvez quitter un environnement activé dans le terminal avec :

```bash
deactivate
```

Si vous préférez travailler uniquement dans Colab, il n’est pas nécessaire de terminer cette installation locale.

## Documentation officielle

- [Python sous Windows](https://docs.python.org/3/using/windows.html)
- [Environnements virtuels Python](https://docs.python.org/3/library/venv.html)
- [Installation de uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Environnements dans uv](https://docs.astral.sh/uv/pip/environments/)
- [Duplication et streaming dans Drive](https://support.google.com/drive/answer/13401938?hl=fr)
- [Notebooks dans VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
