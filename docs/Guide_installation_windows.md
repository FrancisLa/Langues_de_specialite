# Installation de l’environnement de travail

Cours : Langues de spécialité

Ce guide prépare deux façons de travailler sur un même projet :

- en local, dans VS Code, avec Python installé sur votre ordinateur ;
- dans Google Colab, avec un ordinateur distant et les données conservées dans Google Drive.

Google Drive fait partie de la préparation du cours afin de permettre le passage à Colab. Nous distinguons cependant le stockage des données, le dépôt Git et l’environnement Python.

> Principe : les fichiers partageables et leur historique sont conservés dans GitHub ; les données autorisées pour cet usage sont conservées dans Google Drive ; l’environnement Python local reste sur votre ordinateur.

## 1. Comprendre l’organisation

| Élément | Où ? | Fonction |
|---|---|---|
| Dépôt personnel | Dossier local, relié à GitHub | Conserver les notebooks, scripts et documents partageables avec leur historique. |
| `.venv` | Dans le dépôt local, mais ignoré par Git | Exécuter les traitements en local avec les bibliothèques du projet. |
| Données et sorties non versionnées | Dossier du projet dans Google Drive | Retrouver les mêmes fichiers depuis Windows et Colab. |
| Environnement Colab | Ordinateur distant temporaire | Exécuter les notebooks dans le navigateur. |

L’installation de Google Drive pour ordinateur permet de retrouver les fichiers Drive sur Windows. Elle n’est pas requise techniquement pour monter Drive depuis Colab, mais elle fait partie du parcours proposé ici pour alterner entre travail local et distant.

## 2. Préparer Google Drive

### 2.1 Utiliser un compte Google

1. Connectez-vous à [Google Drive](https://drive.google.com/) avec votre compte Google.
2. Si nécessaire, créez un compte depuis [la page d’inscription Google](https://accounts.google.com/signup).
3. Vérifiez que vous utilisez le compte prévu pour le cours et que vous disposez de suffisamment d’espace libre.

L’espace disponible dépend de votre compte et des fichiers déjà stockés. Un compte institutionnel peut aussi comporter des restrictions d’accès à Colab ou aux applications.

### 2.2 Installer Google Drive pour ordinateur

1. Téléchargez [Google Drive pour ordinateur](https://www.google.com/drive/download/).
2. Installez l’application.
3. Connectez-vous avec le même compte que celui que vous utiliserez dans Colab.
4. Ouvrez les préférences de Drive depuis son icône dans la zone de notification Windows.

### 2.3 Choisir la duplication des fichiers

Pour disposer d’une copie locale des fichiers :

1. Dans les préférences, ouvrez la rubrique Google Drive ou Dossiers de Drive.
2. Repérez les options de synchronisation de Mon Drive.
3. Choisissez `Dupliquer les fichiers` (`Mirror files`).
4. Choisissez ou relevez l’emplacement du dossier local.
5. Attendez la fin de la synchronisation.

La duplication conserve une copie des fichiers de Mon Drive sur l’ordinateur et dans Drive. Vérifiez que l’espace disque est suffisant : ce choix concerne Mon Drive, pas seulement le dossier du cours.

Le chemin local dépend de votre installation. Copiez son adresse dans l’Explorateur Windows plutôt que de traduire ou deviner le nom du dossier.

> Si la duplication de tout Mon Drive n’est pas possible faute d’espace, demandez un parcours adapté : accès par navigateur ou streaming avec disponibilité hors connexion des fichiers nécessaires.

### 2.4 Créer le dossier du projet dans Mon Drive

Dans Mon Drive, créez cette organisation, en remplaçant `LSP_nom_prenom` par le nom du projet :

```text
Mon Drive/
└── LSP_nom_prenom/
    ├── donnees/
    │   ├── sources/
    │   ├── intermediaires/
    │   └── preparees/
    ```
```

- `sources/` : documents tels qu’acquis, à ne pas modifier directement.
- `intermediaires/` : extractions et étapes intermédiaires.
- `preparees/` : données utilisées pour l’analyse.


Ne déposez ici que les contenus dont le stockage dans Google Drive et le traitement dans Colab sont autorisés.

La synchronisation répercute aussi les modifications et suppressions. Ce n’est pas une sauvegarde indépendante : conservez les sources et appliquez les règles de conservation du cours.

## 3. Installer Git, Python et VS Code

Les commandes `powershell` ci-dessous sont à exécuter dans un terminal PowerShell, pas dans une cellule Python. Exécutez-les une à une et attendez leur fin.

### 3.1 Git

1. Installez [Git pour Windows](https://git-scm.com/downloads/win).
2. Conservez les options par défaut, notamment l’accès à Git depuis la ligne de commande et les autres logiciels si cette option est proposée.
3. Ouvrez une nouvelle fenêtre PowerShell et vérifiez :

```powershell
git --version
```

Configurez ensuite vos informations de commit :

```powershell
git config --global user.name "Prénom Nom"
git config --global user.email "votre.adresse@example.com"
```

Remplacez les exemples par vos informations. Cette configuration n’est pas une connexion à GitHub.

### 3.2 Python Install Manager et Python 3.12

1. Installez Python Install Manager depuis [le site officiel de Python](https://www.python.org/downloads/) ou le Microsoft Store indiqué par ce site.
2. Fermez puis rouvrez PowerShell.
3. Exécutez :

```powershell
py list
py install 3.12
py -3.12 --version
```

La dernière commande doit afficher Python 3.12. Si cette version fonctionne déjà, ne la réinstallez pas.

Python 3.12 est la version de référence locale du cours. L’environnement proposé par Colab peut utiliser une autre version.

### 3.3 VS Code et les extensions

1. Installez [Visual Studio Code](https://code.visualstudio.com/).
2. Ouvrez la rubrique Extensions avec `Ctrl + Maj + X`.
3. Installez `Python` et `Jupyter`, publiées par Microsoft.
4. Installez `GitHub Pull Requests`, publié par GitHub.

Aucune extension supplémentaire n’est nécessaire pour lire et modifier les fichiers Markdown.

## 4. Ouvrir votre dépôt personnel en local

Créez d’abord votre dépôt privé personnel ou d’équipe selon le guide GitHub du cours. Ne confondez pas votre dépôt avec celui du professeur, qui fournit le gabarit.

- Déjà cloné : dans VS Code, utilisez `File` → `Open Folder…` et ouvrez sa racine.

## 5. Créer l’environnement Python local

### 5.1 Créer puis activer `.venv`

Dans `Terminal` → `New Terminal`, à la racine du dépôt, inscrivez dans le powershell :

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

La création se fait une seule fois. L’activation se répète pour les nouveaux terminaux, selon leur configuration.

Vérifiez :

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

Le résultat doit indiquer Python 3.12 et un chemin vers `.venv\Scripts\python.exe`.

### 5.2 Installer les bibliothèques

Avec `.venv` activé :

```powershell
python -m pip install --upgrade pip
python -m pip install ipykernel
```

Consultez ensuite les consignes dans `environnement/`. Si un fichier `requirements.txt` est fourni à la racine :

```powershell
python -m pip install -r requirements.txt
```

Adaptez le chemin si le fichier se trouve ailleurs. Ne lancez pas cette commande si le fichier n’existe pas.

À défaut de fichier fourni, pour le premier exemple de moissonnage :

```powershell
python -m pip install pandas requests lxml openpyxl
```

### 5.3 Exclure l’environnement de Git

Vérifiez que `.gitignore` contient une règle couvrant :

```gitignore
.venv/
```

Ne placez pas de données ni de code personnel à l’intérieur de `.venv`. Ne synchronisez pas ce dossier avec Drive et ne l’envoyez pas sur GitHub. Il doit pouvoir être recréé sur chaque ordinateur.

> `.gitignore` ne s’applique qu’à Git. Il n’empêche pas Google Drive de synchroniser un fichier et ne retire pas les fichiers déjà suivis par Git.

### 5.4 Sélectionner l’environnement dans VS Code

Pour les scripts : `Ctrl + Maj + P` → `Python: Select Interpreter` → Python 3.12 dans `.venv`.

Pour chaque notebook : `Select Kernel` → `Python Environments` → Python 3.12 dans `.venv`.

## 6. Accéder aux mêmes données depuis Windows et Colab

Le dossier du projet dans Drive est le même, mais son chemin diffère selon l’ordinateur qui exécute le code.

| Exécution | Chemin des données |
|---|---|
| Windows local | Chemin du dossier Mon Drive sur votre ordinateur. |
| Colab | `/content/drive/MyDrive/LSP_nom_prenom` après autorisation du montage. |

Le chemin du dépôt Git local est distinct du chemin des données dans Drive. 

## Documentation officielle

- [Google Drive pour ordinateur](https://www.google.com/drive/download/)
- [Duplication et streaming dans Drive](https://support.google.com/drive/answer/13401938?hl=fr)
- [Questions fréquentes sur Google Colab](https://research.google.com/colaboratory/faq.html)
- [Python sous Windows](https://docs.python.org/3/using/windows.html)
- [Environnements virtuels Python](https://docs.python.org/3/library/venv.html)
- [Notebooks dans VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
