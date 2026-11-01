# Installer l’environnement de travail — Windows, macOS et Linux

Cours : Langues de spécialité

Ce guide permet de travailler :

- en local avec VS Code et Python ;
- dans Google Colab avec les données conservées dans Google Drive.

Suivez uniquement les instructions correspondant à votre système lorsque plusieurs versions sont proposées.

## 1. Comprendre les outils et l’organisation

| Élément | Rôle |
|---|---|
| Google Drive | Conserver les données autorisées et y accéder depuis Colab. |
| Git | Suivre l’historique des fichiers et échanger des versions avec GitHub. |
| VS Code | Modifier les fichiers Markdown, les scripts et les notebooks. |
| Python 3.12 | Version de référence pour le travail local du cours. |
| `.venv` | Environnement Python propre au projet sur votre ordinateur. |
| Google Colab | Exécuter les notebooks sur un ordinateur distant temporaire. |

Anaconda n’est pas nécessaire. Sous Windows, nous utilisons Python Install Manager. Sous macOS et Linux, nous proposons `uv` pour obtenir Python 3.12 sans remplacer le Python du système.

Les environnements Windows, macOS, Linux et Colab sont distincts. Ne copiez pas `.venv` entre ordinateurs ou dans Colab : recréez l’environnement à partir des dépendances documentées.

### Deux emplacements distincts

```text
Dossier local non synchronisé
└── GitHub/
    └── LSP_nom_prenom/
        ├── .git/
        ├── .venv/              # Ignoré par Git
        ├── chaine/
        ├── configuration/
        ├── environnement/
        └── ...

Google Drive — Mon Drive
└── LSP_nom_prenom/
    ├── donnees/
    │   ├── sources/
    │   ├── intermediaires/
    │   └── preparees/
    ├── resultats/
    └── notebooks_travail/
```

Le dépôt local contient les fichiers partageables suivis par Git. Le dossier Drive conserve les données et copies de travail destinées au passage à Colab. Ces dossiers portent éventuellement le même nom, mais n’ont pas le même rôle.

> Ne placez pas `.venv` dans Google Drive. Ne partagez pas un dossier synchronisé contenant `.git` pour remplacer les échanges par Git. Chaque membre garde sa propre copie locale du dépôt.

## 2. Préparer Google Drive

### 2.1 Pour tous les systèmes

1. Connectez-vous à [Google Drive](https://drive.google.com/) avec le compte que vous utiliserez aussi dans Colab.
2. Si nécessaire, [créez un compte Google](https://accounts.google.com/signup).
3. Vérifiez l’espace libre et les éventuelles restrictions du compte institutionnel.
4. Dans Mon Drive, créez le dossier `LSP_nom_prenom` et les sous-dossiers présentés plus haut.

Le nom est un exemple : remplacez-le par celui de votre projet dans tout le guide.

Ne stockez et ne traitez dans Drive ou Colab que les données autorisées pour cet usage. Un espace privé n’annule pas les restrictions de confidentialité ou de licence.

### 2.2 Windows et macOS : installer Drive pour ordinateur

1. Téléchargez [Google Drive pour ordinateur](https://www.google.com/drive/download/).
2. Ouvrez l’installateur correspondant à votre système et terminez l’installation.
3. Connectez-vous avec le compte prévu pour le cours.
4. Ouvrez les préférences depuis l’icône Drive : zone de notification sous Windows, barre des menus sous macOS.
5. Repérez les options de synchronisation de Mon Drive.
6. Pour conserver une copie locale complète, choisissez la duplication des fichiers (`Mirror files`).
7. Vérifiez l’espace disque disponible et attendez la fin de la synchronisation.

La duplication concerne les fichiers de Mon Drive, pas seulement ceux du cours. Si vous manquez d’espace, demandez un parcours adapté, par exemple le streaming avec les fichiers nécessaires disponibles hors connexion.

Relevez le chemin réel du dossier dans l’Explorateur Windows ou le Finder. Il dépend de votre installation : ne traduisez pas vous-même `My Drive` et ne supposez pas une lettre de lecteur ou un chemin universel.

> La synchronisation répercute aussi les suppressions. Elle n’est pas une sauvegarde indépendante.

### 2.3 Linux : utiliser Drive dans le navigateur

Google ne fournit pas d’application officielle Drive pour ordinateur sous Linux. Le parcours de base utilise donc [Drive dans le navigateur](https://drive.google.com/).

Deux possibilités :

- Pour Colab uniquement : aucune synchronisation locale n’est nécessaire. Colab accède directement à Drive après autorisation.
- Pour travailler aussi en local : téléchargez les données nécessaires dans un dossier local, puis téléversez les nouvelles sorties autorisées lorsque vous repassez à Colab.

Pour le parcours local Linux, créez par exemple :

```text
/home/VotreNom/DonneesCours/LSP_nom_prenom/
```

Conservez la même organisation `donnees/sources/`, `donnees/intermediaires/`, `donnees/preparees/` et `resultats/`.

> Ce dossier Linux n’est pas automatiquement synchronisé avec Drive. Les transferts sont manuels. Notez la version des fichiers utilisés et vérifiez-les avant de changer d’environnement. Un outil tiers de synchronisation ou de montage peut être envisagé avec l’enseignant, mais n’est pas requis ici.

## 3. Installer Git

Les commandes suivantes vont dans un terminal, pas dans une cellule Python. Copiez une commande à la fois et attendez sa fin.

| Système | Terminal utilisé dans le guide |
|---|---|
| Windows | PowerShell |
| macOS | Terminal, avec zsh ou bash |
| Linux | Terminal, avec bash ou zsh |

### 3.1 Windows

Installez [Git pour Windows](https://git-scm.com/downloads/win). Conservez les options par défaut, notamment l’accès à Git depuis la ligne de commande et les autres logiciels si cette option est proposée.

Ouvrez une nouvelle fenêtre PowerShell :

```powershell
git --version
```

### 3.2 macOS

Dans le Terminal :

```bash
git --version
```

Si macOS propose d’installer les outils de ligne de commande, acceptez et attendez la fin de l’installation. Vous pouvez aussi demander cette installation avec :

```bash
xcode-select --install
```

Vérifiez ensuite de nouveau `git --version`.

### 3.3 Linux

Utilisez le gestionnaire de paquets de votre distribution.

Ubuntu ou Debian :

```bash
sudo apt update
sudo apt install git
```

Fedora :

```bash
sudo dnf install git
```

Autres distributions : consultez [les instructions Git pour Linux](https://git-scm.com/downloads/linux) ou demandez de l’aide. Vérifiez ensuite :

```bash
git --version
```

### 3.4 Tous les systèmes : identifier l’auteur des commits

Remplacez les exemples :

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "votre.adresse@example.com"
```

Ces commandes fonctionnent aussi dans PowerShell. Vous pouvez utiliser l’adresse `noreply` fournie dans les paramètres GitHub. Ce n’est pas une connexion à GitHub et aucun mot de passe ne doit être saisi ici.

GitHub Desktop peut être conservé pour les opérations Git sous Windows et macOS. Il n’existe pas de version officielle pour Linux : le présent guide peut être suivi avec Git et VS Code sur les trois systèmes.

## 4. Installer Python 3.12

### 4.1 Windows : Python Install Manager

1. Installez Python Install Manager depuis [le site Python](https://www.python.org/downloads/) ou le Microsoft Store indiqué par ce site.
2. Fermez puis rouvrez PowerShell.
3. Exécutez :

```powershell
py list
py install 3.12
py -3.12 --version
```

La dernière commande doit afficher Python 3.12. Si cette version fonctionne déjà, ne la réinstallez pas.

Si les commandes de gestion ne sont pas reconnues, une ancienne installation peut utiliser `py`. Le nouveau gestionnaire fournit également `pymanager list` et `pymanager install 3.12`. Demandez de l’aide avant de désinstaller un logiciel existant.

### 4.2 macOS et Linux : installer Python avec uv

`uv` est un gestionnaire tiers permettant d’installer une version de Python et de créer un environnement de projet sans modifier le Python fourni par le système.

1. Consultez [la page officielle d’installation de uv](https://docs.astral.sh/uv/getting-started/installation/).
2. Pour le parcours proposé ici, utilisez l’installateur officiel dans le Terminal :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Cette commande télécharge et exécute un script d’installation. Utilisez uniquement l’adresse officielle ; sur un ordinateur institutionnel, vérifiez que cette méthode est autorisée. La documentation propose aussi d’inspecter le script et d’autres méthodes d’installation.

3. Fermez puis rouvrez le Terminal et vérifiez :

```bash
uv --version
```

4. Installez Python 3.12 :

```bash
uv python install 3.12
uv python list --only-installed
```

Si `uv` reste introuvable, suivez les instructions de chemin d’accès affichées par l’installateur, puis demandez de l’aide si nécessaire. Ne remplacez pas le Python système.

Les distributions de Python téléchargées par uv proviennent du projet `python-build-standalone` d’Astral, et non des installateurs de python.org.

> Si vous disposez déjà d’un Python 3.12 fonctionnel installé par une autre méthode, vous pouvez créer l’environnement avec `python3.12 -m venv .venv` au lieu d’installer uv. Vérifiez d’abord `python3.12 --version`. Sous certaines distributions Linux, le module `venv` doit être installé séparément ; demandez le paquet adapté à votre distribution.

## 5. Installer VS Code et ouvrir le dépôt

### 5.1 Installer l’application et les extensions

1. Téléchargez [VS Code](https://code.visualstudio.com/) pour votre système et votre processeur.
2. Sous Windows, lancez l’installateur ; sous macOS, placez l’application dans Applications ; sous Linux, suivez les instructions du paquet adapté à votre distribution.
3. Dans VS Code, ouvrez la rubrique Extensions.
4. Installez `Python` et `Jupyter`, publiées par Microsoft.

Aucune extension supplémentaire n’est nécessaire pour l’aperçu Markdown.

| Action | Windows / Linux | macOS |
|---|---|---|
| Palette de commandes | `Ctrl + Maj + P` | `Cmd + Maj + P` |
| Extensions | `Ctrl + Maj + X` | `Cmd + Maj + X` |
| Enregistrer | `Ctrl + S` | `Cmd + S` |

### 5.2 Ouvrir votre dépôt personnel

Créez d’abord le dépôt privé personnel ou d’équipe selon le guide GitHub du cours. Le dépôt `FrancisLa/Langues_de_specialite` fournit le gabarit ; ce n’est pas votre dépôt de remise.

- Dépôt déjà cloné : ouvrez sa racine avec `File` → `Open Folder…`, ou `Open…` selon le système.
- Dépôt pas encore cloné : lancez `Git: Clone` depuis la palette, collez l’URL de votre dépôt et suivez l’authentification demandée. Choisissez un dossier parent local, hors synchronisation Drive ou OneDrive.

Exemples de chemins finaux :

```text
Windows : C:/Users/VotreNom/GitHub/LSP_nom_prenom
macOS   : /Users/VotreNom/GitHub/LSP_nom_prenom
Linux   : /home/VotreNom/GitHub/LSP_nom_prenom
```

Dans `Terminal` → `New Terminal`, vérifiez le dossier courant :

Windows :

```powershell
Get-Location
```

macOS et Linux :

```bash
pwd
```

Puis, sur les trois systèmes :

```bash
git status
git remote -v
```

Vous devez être à la racine du dépôt et `origin` doit correspondre au dépôt personnel ou d’équipe. Ces commandes ne prouvent pas que vous avez les droits d’écriture : ceux-ci seront vérifiés lors des échanges avec GitHub.

## 6. Créer l’environnement local .venv

Effectuez cette étape dans le terminal, à la racine du dépôt. Ne créez pas l’environnement dans Drive. La création se fait une seule fois par projet et par ordinateur.

### 6.1 Windows

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l’activation, utilisez directement l’exécutable, sans modifier immédiatement la politique de sécurité :

```powershell
.\.venv\Scripts\python.exe --version
```

Dans les commandes Python suivantes, remplacez alors `python` par `.\.venv\Scripts\python.exe`.

### 6.2 macOS et Linux — avec uv

```bash
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
```

L’option `--seed` installe notamment pip pour les commandes communes ci-dessous. Le script d’activation indiqué convient à bash et zsh.

Sans activation, vous pouvez appeler directement :

```bash
./.venv/bin/python --version
```

### 6.3 Tous les systèmes : vérifier puis installer

Après activation :

```bash
python --version
python -c "import sys; print(sys.executable)"
```

Résultat attendu : Python 3.12, avec un exécutable dans `.venv/Scripts/` sous Windows ou `.venv/bin/` sous macOS et Linux.

Installez le noyau Jupyter :

```bash
python -m pip install --upgrade pip
python -m pip install ipykernel
```

Consultez ensuite les consignes dans `environnement/`. Si un fichier `requirements.txt` est fourni à la racine :

```bash
python -m pip install -r requirements.txt
```

Adaptez le chemin à l’emplacement réel ; ne lancez pas cette commande si le fichier n’existe pas. À défaut de fichier fourni, pour le premier exemple de moissonnage uniquement :

```bash
python -m pip install pandas requests lxml openpyxl
```

Ne faites pas `sudo pip install`. Les bibliothèques du projet doivent être installées dans son environnement, pas dans le Python système.

### 6.4 Vérifier .gitignore

Le `.gitignore` du dépôt doit contenir une règle couvrant :

```gitignore
.venv/
```

Ce dossier ne doit pas être envoyé sur GitHub. `.gitignore` n’agit pas sur Drive et ne retire pas les fichiers déjà suivis par Git.

### 6.5 Sélectionner l’environnement dans VS Code

Pour les scripts : palette → `Python: Select Interpreter` → Python 3.12 dans `.venv`.

Pour chaque notebook : `Select Kernel` → `Python Environments` → Python 3.12 dans `.venv`.

Si nécessaire, recherchez l’exécutable manuellement :

```text
Windows : .venv/Scripts/python.exe
macOS   : .venv/bin/python
Linux   : .venv/bin/python
```

Testez dans une cellule Python :

```python
import platform
import sys

print("Version de Python :", platform.python_version())
print("Exécutable :", sys.executable)
```

Le résultat doit correspondre à la `.venv` du projet. Le choix de l’interpréteur des scripts et celui du noyau des notebooks sont à vérifier séparément.

## 7. Accéder aux données depuis le notebook

### 7.1 Choisir le stockage selon le contexte

| Contexte | Données accessibles depuis |
|---|---|
| Windows local | Dossier Drive synchronisé, ou stockage local autorisé. |
| macOS local | Dossier Drive synchronisé, ou stockage local autorisé. |
| Linux local, parcours de base | Dossier contenant les fichiers téléchargés manuellement depuis Drive. |
| Colab, quel que soit votre ordinateur personnel | Drive monté dans l’environnement distant. |

Dans Colab, le système d’exécution est distant : le fait que votre ordinateur personnel soit Windows ou macOS ne change pas le chemin `/content/drive/MyDrive`.

### 7.2 Cellule commune de configuration

Renseignez uniquement le chemin local correspondant à votre système. Conservez la même organisation interne des dossiers.

```python
from pathlib import Path
import platform

# True dans VS Code en local ; False dans Google Colab.
IS_LOCAL = False
NOM_PROJET = "LSP_nom_prenom"

if IS_LOCAL:
    systeme = platform.system()

    racines_locales = {
        # Chemins à adapter d’après votre installation Drive.
        "Windows": Path(r"C:\CHEMIN_A_REMPLACER\Mon Drive"),
        "Darwin": Path("/CHEMIN_A_REMPLACER/Mon Drive"),
        # Parcours Linux sans synchronisation automatique.
        "Linux": Path.home() / "DonneesCours",
    }

    if systeme not in racines_locales:
        raise RuntimeError(f"Système non prévu : {systeme}")

    racine_stockage = racines_locales[systeme]
else:
    from google.colab import drive
    drive.mount("/content/drive")
    racine_stockage = Path("/content/drive/MyDrive")

chemin_stockage = racine_stockage / NOM_PROJET

if not chemin_stockage.is_dir():
    raise FileNotFoundError(
        f"Dossier introuvable : {chemin_stockage}. "
        "Vérifiez le chemin, le compte Google et la présence des données."
    )

chemin_sources = chemin_stockage / "donnees" / "sources"
chemin_intermediaires = chemin_stockage / "donnees" / "intermediaires"
chemin_preparees = chemin_stockage / "donnees" / "preparees"
chemin_resultats_stockage = chemin_stockage / "resultats"

print("Stockage :", chemin_stockage)
print("Sources :", chemin_sources)
```

`Darwin` est le nom renvoyé par Python pour macOS. Les chemins du stockage des données ne désignent pas la racine du dépôt Git.

Gardez les chemins personnels dans la configuration locale selon les règles du cours ; ne publiez pas d’informations sensibles.

## 8. Travailler dans Google Colab — tous les systèmes

1. Ouvrez [Google Colab](https://colab.research.google.com/) avec le compte qui contient vos données.
2. Importez votre notebook `.ipynb`, ou ouvrez sa copie conservée dans Drive.
3. Si vous l’ouvrez depuis GitHub, enregistrez une copie dans Drive avant modification.
4. Rangez la copie de travail dans `LSP_nom_prenom/notebooks_travail/`.
5. Réglez `IS_LOCAL = False` et exécutez la cellule de montage.
6. Autorisez l’accès à Drive et vérifiez les chemins affichés.

> Après montage, le code du notebook peut accéder aux fichiers de Drive. N’exécutez que des cellules dont vous connaissez la provenance et les effets.

Colab n’utilise pas votre `.venv` locale. Si nécessaire, installez les bibliothèques de l’exercice dans une cellule, par exemple :

```python
%pip install pandas requests lxml openpyxl
```

Suivez les dépendances du notebook concerné. Une nouvelle session peut nécessiter de reconnecter Drive et de réinstaller les bibliothèques. Affichez la version de Python utilisée : Colab ne garantit pas votre version locale 3.12.

### Tester une sortie durable

Après configuration des chemins :

```python
chemin_resultats_stockage.mkdir(parents=True, exist_ok=True)
fichier_test = chemin_resultats_stockage / "test_stockage.txt"

if not fichier_test.exists():
    fichier_test.write_text(
        "Fichier fictif pour vérifier l’accès au stockage.\n",
        encoding="utf-8",
    )

print("Fichier de test :", fichier_test)
```

- Dans Colab, retrouvez ce fichier dans Drive depuis le navigateur.
- Sous Windows ou macOS avec Drive synchronisé, attendez sa présence sur l’ordinateur.
- Sous Linux sans outil de synchronisation, téléchargez ou téléversez manuellement la version nécessaire. La création dans le dossier local n’actualise pas Drive.

Les fichiers créés seulement dans l’espace temporaire de Colab peuvent disparaître. Les variables en mémoire ne sont pas automatiquement sauvegardées dans Drive.

## 9. Reprendre le travail et envoyer les versions

### 9.1 Début d’une séance locale

1. Ouvrez le bon dépôt dans VS Code.
2. Vérifiez les modifications en cours, puis récupérez les nouveautés avant de modifier les fichiers :

```bash
git status
git pull
```

3. Activez `.venv` dans le nouveau terminal :

Windows :

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS et Linux :

```bash
source .venv/bin/activate
```

4. Vérifiez le noyau du notebook, réglez `IS_LOCAL = True` et contrôlez les chemins.
5. Vérifiez la synchronisation des données, ou leurs versions et transferts manuels sous Linux.

En cas de conflit ou de refus Git, conservez les fichiers et demandez de l’aide. Ne forcez pas l’envoi et ne supprimez pas des fichiers pour débloquer la situation.

### 9.2 Passer de Colab au dépôt Git

Drive ne crée pas de commit et n’effectue pas de push. Un notebook modifié dans Colab n’actualise pas automatiquement votre dépôt local.

1. Enregistrez la copie Colab dans Drive.
2. Téléchargez le notebook ou récupérez sa copie synchronisée.
3. Comparez les versions avant tout remplacement, notamment en équipe.
4. Placez la version retenue dans le sous-dossier approprié de `chaine/` du dépôt local.
5. Examinez les sorties : aucun secret ni contenu non partageable ne doit être publié.
6. Copiez seulement les résultats partageables retenus dans `resultats/` du dépôt.
7. Créez le commit et envoyez-le selon le guide GitHub du cours.

Ne modifiez pas simultanément les copies locale et Colab du même notebook. Notez quelle version est active. Sous Linux sans synchronisation, les données et résultats doivent également être transférés manuellement si vous souhaitez les retrouver dans l’autre environnement.

Documentez dans le projet la provenance, la version et l’emplacement autorisé des données, sans publier de secrets.

## 10. Vérification finale et dépannage

- [ ] Git est disponible avec `git --version`.
- [ ] Le dépôt personnel ou d’équipe est ouvert, pas celui du professeur.
- [ ] `.venv` utilise Python 3.12 et contient `ipykernel`.
- [ ] Les dépendances nécessaires sont installées.
- [ ] Le bon noyau est sélectionné dans chaque notebook.
- [ ] Le compte Google et le dossier Drive sont corrects.
- [ ] Le parcours Linux prévoit les transferts manuels, s’il n’y a pas de synchronisation.
- [ ] `.venv` n’est ni suivi par Git ni synchronisé dans Drive.
- [ ] Les fichiers conservés dans le nuage sont autorisés.
- [ ] Le notebook retenu est dans le dépôt local avant le commit et le push.

| Problème | Action sûre |
|---|---|
| Commande installée mais introuvable | Fermer puis rouvrir le terminal et VS Code ; vérifier les instructions de l’installateur. |
| PowerShell bloque l’activation | Utiliser directement `.venv/Scripts/python.exe`, sans changer la sécurité par défaut. |
| Mauvaise version Python | Sélectionner explicitement l’interpréteur et le noyau de `.venv`. |
| Bibliothèque absente | L’installer dans l’environnement qui exécute réellement le notebook. |
| Chemin Drive incorrect | Copier le chemin réel depuis le gestionnaire de fichiers ; ne pas traduire son nom. |
| Drive ne se synchronise pas sous Linux | Le parcours navigateur ne synchronise rien automatiquement ; transférer les fichiers nécessaires. |
| Notebook absent de GitHub | Vérifier l’emplacement local, le commit, le push et les règles d’exclusion. |

Ne recréez pas `.venv` et ne réinstallez pas tous les outils à chaque séance. Recréez l’environnement en cas de changement d’ordinateur ou de déplacement qui invalide ses chemins.

## Documentation officielle

- [Git](https://git-scm.com/downloads)
- [VS Code](https://code.visualstudio.com/download)
- [Python sous Windows](https://docs.python.org/3/using/windows.html)
- [Environnements Python](https://docs.python.org/3/tutorial/venv.html)
- [Installer uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Installer Python avec uv](https://docs.astral.sh/uv/guides/install-python/)
- [Drive : systèmes compatibles](https://support.google.com/drive/answer/2375082)
- [Drive pour ordinateur](https://www.google.com/drive/download/)
- [Google Colab : questions fréquentes](https://research.google.com/colaboratory/faq.html)
- [Notebooks Jupyter dans VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
