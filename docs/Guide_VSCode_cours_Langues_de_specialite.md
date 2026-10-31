# Guide de base — Visual Studio Code

Ce guide explique comment utiliser **Visual Studio Code** (VS Code) pour
travailler avec le dépôt du cours *Langues de spécialité*.

À la fin de ce guide, vous saurez :

1. installer VS Code ;
2. installer les extensions nécessaires ;
3. ouvrir le dépôt local du cours ;
4. ouvrir et exécuter un notebook Jupyter ;
5. lire et modifier un fichier Markdown ;
6. enregistrer votre travail.

VS Code permet d’ouvrir un dossier de projet, de modifier des fichiers
Markdown, d’exécuter des notebooks Jupyter et d’utiliser Git. Les
extensions **Python** et **Jupyter** permettent notamment d’exécuter des
notebooks `.ipynb` localement.

---

## 1. Installer VS Code

1. Allez à l’adresse : https://code.visualstudio.com/
2. Téléchargez la version correspondant à votre système :
   - Windows ;
   - macOS ;
   - Linux.
3. Installez l’application en suivant les instructions.
4. Ouvrez VS Code.

### Vérification

Après l’ouverture, vous devriez voir :

- une barre latérale à gauche ;
- une zone principale pour ouvrir des fichiers ;
- une barre d’état en bas de la fenêtre.

---

## 2. Installer les extensions

VS Code fonctionne avec des extensions. Pour ce cours, installez au minimum :

| Extension | Éditeur | Fonction |
|---|---|---|
| **Python** | Microsoft | Reconnaître et exécuter du code Python |
| **Jupyter** | Microsoft | Ouvrir et exécuter des notebooks `.ipynb` |
| **GitHub Pull Requests and Issues** | GitHub | Faciliter le travail avec GitHub, si nécessaire |

### Installer une extension

1. Cliquez sur l’icône **Extensions** dans la barre latérale gauche.
   Elle ressemble à quatre carrés.
2. Dans la zone de recherche, écrivez :
   ```text
   Python
   ```
3. Choisissez l’extension **Python** publiée par **Microsoft**.
4. Cliquez sur **Install** ou **Installer**.
5. Recherchez ensuite :
   ```text
   Jupyter
   ```
6. Choisissez l’extension **Jupyter** publiée par **Microsoft**.
7. Cliquez sur **Install** ou **Installer**.

L’extension Jupyter permet d’ouvrir et d’exécuter des notebooks Jupyter
dans VS Code. Elle nécessite un environnement Python, par exemple Anaconda,
Miniconda ou un environnement virtuel.

---

## 3. Installer Python ou Anaconda

Pour exécuter les notebooks du cours, vous devez disposer d’un
environnement Python.

### Option recommandée : Anaconda

1. Allez à l’adresse : https://www.anaconda.com/download
2. Téléchargez Anaconda pour votre système.
3. Installez Anaconda en suivant les instructions.
4. Ouvrez VS Code.

Anaconda installe Python ainsi que plusieurs outils utiles pour l’analyse
de données.

### Vérifier que VS Code reconnaît Python

1. Ouvrez VS Code.
2. Appuyez sur :
   - Windows ou Linux : `Ctrl + Maj + P`
   - macOS : `Cmd + Maj + P`
3. Écrivez :
   ```text
   Python: Select Interpreter
   ```
4. Choisissez l’environnement Anaconda ou Python installé sur votre
   ordinateur.

VS Code permet de sélectionner l’interpréteur Python à l’aide de la
commande **Python: Select Interpreter**.

---

## 4. Ouvrir le dépôt local

Si vous avez déjà cloné le dépôt du cours avec GitHub Desktop, vous pouvez
l’ouvrir directement dans VS Code.

### Ouvrir un dossier

1. Dans VS Code, choisissez **File** dans le menu supérieur.
2. Choisissez **Open Folder…**
   - Sur macOS : **Open…**
3. Allez dans votre dossier Google Drive.
4. Ouvrez le dossier :
   ```text
   GitHub/
   ```
5. Sélectionnez le dossier du dépôt, par exemple :
   ```text
   Langues_de_specialite
   ```
6. Cliquez sur **Select Folder** ou **Ouvrir**.

VS Code affichera alors l’arborescence du dépôt dans la barre latérale
gauche.

### Structure attendue

```text
Langues_de_specialite/
├── chaine/
├── configuration/
├── donnees/
├── docs/
├── environnement/
├── journal/
├── notebooks/
└── resultats/
```

> **Important :** ouvrez toujours le dossier racine du dépôt, et non un
> fichier isolé. Cela permet à VS Code de reconnaître les dossiers, les
> scripts et les fichiers du projet.

---

## 5. Ouvrir un notebook

Les notebooks du cours ont l’extension :

```text
.ipynb
```

### Ouvrir un notebook existant

1. Dans la barre latérale gauche, ouvrez le dossier contenant le notebook.
2. Double-cliquez sur le fichier `.ipynb`.
3. Le notebook s’ouvre dans VS Code.

### Choisir le noyau Python

Avant d’exécuter un notebook, choisissez le noyau (*kernel*).

1. En haut à droite du notebook, cliquez sur **Select Kernel**.
2. Choisissez **Python Environments**.
3. Sélectionnez votre environnement Anaconda ou Python.

Le sélecteur de noyau de VS Code permet de choisir l’environnement Python
qui exécutera les cellules du notebook. L’extension Jupyter requiert
notamment le paquet `ipykernel` dans l’environnement choisi.

### Exécuter une cellule

1. Cliquez dans une cellule de code.
2. Cliquez sur le bouton ▶ à gauche de la cellule.
3. Attendez la fin de l’exécution.
4. Passez à la cellule suivante.

Vous pouvez aussi utiliser :

- `Maj + Entrée` : exécuter la cellule et passer à la suivante ;
- `Ctrl + Entrée` : exécuter la cellule sans passer à la suivante.

---

## 6. Travailler avec un notebook

Un notebook contient deux types principaux de cellules :

| Type de cellule | Contenu | Usage |
|---|---|---|
| **Markdown** | Texte, titres, listes, tableaux, liens | Expliquer la démarche et documenter le travail |
| **Code** | Code Python | Réaliser une opération ou produire un résultat |

### Exécuter toutes les cellules

1. Ouvrez le notebook.
2. Dans le menu supérieur, cliquez sur **Run All** ou **Exécuter tout**.

Attention : n’exécutez pas toutes les cellules sans avoir vérifié le
contenu du notebook et les données utilisées.

### Enregistrer un notebook

1. Choisissez **File**.
2. Choisissez **Save**.
3. Vous pouvez aussi utiliser :
   - Windows ou Linux : `Ctrl + S`
   - macOS : `Cmd + S`

---

## 7. Travailler avec les fichiers Markdown

Les fichiers Markdown ont l’extension :

```text
.md
```

Ils servent notamment à rédiger :

- les guides ;
- les README ;
- les journaux de recherche ;
- la documentation des données ;
- les explications méthodologiques.

### Ouvrir un fichier Markdown

1. Dans la barre latérale gauche, ouvrez le dossier `docs/`, `journal/`
   ou `donnees/`.
2. Double-cliquez sur un fichier `.md`.
3. Le fichier s’ouvre en mode texte.

### Afficher l’aperçu Markdown

Pour voir le rendu du fichier :

1. Ouvrez un fichier `.md`.
2. Cliquez sur l’icône d’aperçu en haut à droite de la fenêtre.
3. Vous pouvez aussi utiliser :
   - Windows ou Linux : `Ctrl + Maj + V`
   - macOS : `Cmd + Maj + V`

### Éléments Markdown utiles

```markdown
# Titre principal

## Sous-titre

Texte normal.

**Texte en gras**

*Texte en italique*

- Élément de liste
- Autre élément de liste

1. Première étape
2. Deuxième étape

| Colonne 1 | Colonne 2 |
|---|---|
| Valeur 1 | Valeur 2 |

[Lien vers GitHub](https://github.com/FrancisLa/Langues_de_specialite)

```python
print("Exemple de code")
```
```

---

## 8. Créer un nouveau notebook

1. Choisissez **File**.
2. Choisissez **New File…**
3. Donnez un nom se terminant par :
   ```text
   .ipynb
   ```
   Par exemple :
   ```text
   01_acquisition.ipynb
   ```
4. Enregistrez le fichier dans le dossier approprié du projet.
5. Ajoutez une première cellule Markdown pour décrire l’objectif du notebook.
6. Ajoutez ensuite des cellules de code.

### Nommer un notebook

Utilisez un nom court, explicite et sans espace :

```text
01_acquisition.ipynb
02_preparation.ipynb
03_analyse.ipynb
04_validation.ipynb
```

Évitez :

```text
Mon notebook final.ipynb
essai 2.ipynb
notebook_final_v3.ipynb
```

---

## 9. Travailler avec Git dans VS Code

Si vous utilisez déjà GitHub Desktop, vous pouvez continuer à l’utiliser
pour les opérations Git.

VS Code permet aussi de :

- voir les fichiers modifiés ;
- créer un commit ;
- envoyer les modifications avec un `push` ;
- récupérer les modifications avec un `pull`.

### Voir les modifications

1. Cliquez sur l’icône **Source Control** dans la barre latérale gauche.
   Elle ressemble à une branche.
2. Les fichiers modifiés apparaissent dans la liste.

### Créer un commit

1. Écrivez un message dans le champ prévu à cet effet.
2. Cliquez sur **Commit**.

### Envoyer les modifications

1. Après avoir créé un commit, cliquez sur **Sync Changes** ou **Push**.

### Récupérer les modifications

1. Cliquez sur **Sync Changes** ou **Pull**.

> **Attention :** avant un `push`, vérifiez qu’aucun mot de passe, token,
> clé API ou document non autorisé n’est inclus.

---

## 10. Problèmes fréquents

| Problème | Solution probable |
|---|---|
| Le notebook ne s’ouvre pas | Vérifier que l’extension Jupyter est installée |
| Aucun noyau Python n’est proposé | Installer Anaconda ou Python, puis redémarrer VS Code |
| `Select Kernel` n’affiche pas Anaconda | Utiliser `Python: Select Interpreter` et choisir l’environnement Anaconda |
| Le code ne s’exécute pas | Vérifier que le noyau est sélectionné et que la cellule ne contient pas d’erreur |
| Les fichiers Markdown ne s’affichent pas en aperçu | Installer l’extension Markdown All in One, si nécessaire |
| Le dépôt n’apparaît pas dans VS Code | Ouvrir le dossier racine du dépôt, et non un fichier seul |
| Les modifications ne sont pas visibles dans Git | Vérifier que le dossier ouvert est bien le dépôt cloné |

---

## 11. Routine de travail recommandée

```text
1. Ouvrir VS Code.
2. Ouvrir le dossier du dépôt.
3. Faire un Pull avec GitHub Desktop ou VS Code.
4. Ouvrir le notebook ou le fichier Markdown nécessaire.
5. Travailler et enregistrer régulièrement.
6. Vérifier les fichiers modifiés.
7. Créer un commit clair.
8. Faire un Push.
```

### Exemple de message de commit

```text
Ajout du guide VS Code
Correction du chemin Google Drive
Mise à jour du notebook d’acquisition
Documentation des critères d’exclusion
```

---

## 12. Références utiles

- [Documentation de VS Code](https://code.visualstudio.com/docs)
- [Notebooks Jupyter dans VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Gestion des noyaux Jupyter dans VS Code](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
- [Extension Jupyter pour VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Dépôt du cours](https://github.com/FrancisLa/Langues_de_specialite)