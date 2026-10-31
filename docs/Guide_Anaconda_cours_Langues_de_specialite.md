# Créer un environnement Python pour le projet

Ce guide explique comment créer un environnement Python propre au projet,
plutôt que d’installer les bibliothèques directement dans l’environnement
`base` d’Anaconda.

Un **environnement** est un espace isolé qui contient :

- une version de Python ;
- les bibliothèques nécessaires au projet ;
- leurs dépendances.

L’utilisation d’un environnement propre au projet évite que les
bibliothèques d’un projet modifient celles d’un autre projet.

Anaconda recommande de créer un environnement avec `conda create`, puis de
l’activer avec `conda activate`.

---

## 1. Pourquoi ne pas utiliser `base` ?

L’environnement `base` est l’environnement installé par défaut avec
Anaconda ou Miniconda.

Il est préférable de ne pas y installer les bibliothèques du projet, car :

- les projets peuvent nécessiter des versions différentes d’une même
  bibliothèque ;
- une mise à jour dans `base` peut affecter plusieurs projets ;
- un environnement isolé facilite la reproduction du projet ;
- il est plus facile de supprimer ou de recréer un environnement de projet.

---

## 2. Ouvrir un terminal Anaconda

### Windows

1. Cliquez sur le menu **Démarrer**.
2. Recherchez **Anaconda Prompt**.
3. Ouvrez **Anaconda Prompt**.

### macOS

1. Ouvrez le Terminal.
2. Si la commande `conda` n’est pas reconnue, ouvrez **Anaconda Prompt**
   depuis Anaconda Navigator ou initialisez Conda pour votre interpréteur.

### Linux

1. Ouvrez un terminal.
2. Vérifiez que Conda est disponible :

```bash
conda --version
```

---

## 3. Créer l’environnement du projet

Dans le terminal, exécutez la commande suivante.

Remplacez `langues_de_specialite` par le nom de votre projet si nécessaire.

```bash
conda create --name langues_de_specialite python=3.12 ipykernel
```

Cette commande crée un environnement nommé `langues_de_specialite`, avec :

- Python version 3.12 ;
- `ipykernel`, nécessaire pour exécuter des notebooks Jupyter dans VS Code.

Lorsque Conda demande une confirmation, répondez :

```text
y
```

La documentation de Conda indique que `conda create --name <nom>` crée un
environnement et que l’option `python=3.12` permet d’installer une version
précise de Python.

---

## 4. Activer l’environnement

Après sa création, activez l’environnement :

```bash
conda activate langues_de_specialite
```

Votre invite de commande devrait alors indiquer le nom de l’environnement :

```text
(langues_de_specialite)
```

L’activation permet de travailler dans cet environnement.

---

## 5. Installer les bibliothèques du projet

Avec l’environnement activé, installez les bibliothèques nécessaires.

Pour le notebook de moissonnage du cours :

```bash
conda install pandas requests lxml openpyxl
```

Vous pouvez aussi utiliser `pip` dans un environnement Conda :

```bash
pip install pandas requests lxml openpyxl
```

Ne pas utiliser `pip install` sans avoir activé l’environnement du projet.

---

## 6. Vérifier l’environnement

### Vérifier la version de Python

```bash
python --version
```

Résultat attendu :

```text
Python 3.12.x
```

### Vérifier les environnements disponibles

```bash
conda env list
```

L’environnement actif est indiqué par un astérisque :

```text
base                  /home/VotreNom/anaconda3
langues_de_specialite * /home/VotreNom/anaconda3/envs/langues_de_specialite
```

### Vérifier les bibliothèques installées

```bash
conda list
```

---

## 7. Utiliser l’environnement dans VS Code

1. Ouvrez VS Code.
2. Ouvrez le dossier du dépôt du projet.
3. Ouvrez un notebook `.ipynb`.
4. En haut à droite, cliquez sur **Select Kernel**.
5. Choisissez **Python Environments**.
6. Sélectionnez l’environnement :

```text
langues_de_specialite
```

VS Code détecte les environnements Conda et permet de les sélectionner avec
la commande **Python: Select Interpreter** ou depuis la barre d’état.

### Si l’environnement n’apparaît pas

1. Fermez VS Code.
2. Rouvrez VS Code.
3. Ouvrez de nouveau le dossier du projet.
4. Utilisez la commande :

```text
Python: Select Interpreter
```

5. Choisissez l’environnement `langues_de_specialite`.

---

## 8. Exécuter un notebook

1. Ouvrez un notebook `.ipynb`.
2. Vérifiez que le noyau sélectionné est :

```text
langues_de_specialite
```

3. Exécutez les cellules dans l’ordre.
4. Enregistrez le notebook régulièrement.

Pour exécuter une cellule :

- cliquez sur ▶ ;
- ou utilisez `Maj + Entrée`.

---

## 9. Désactiver ou supprimer un environnement

### Désactiver l’environnement

Lorsque vous avez terminé :

```bash
conda deactivate
```

Vous revenez alors à l’environnement `base`.

### Supprimer un environnement

Si un environnement n’est plus nécessaire :

```bash
conda remove --name langues_de_specialite --all
```

Cette opération supprime l’environnement et les bibliothèques installées
dans celui-ci. Elle ne supprime pas les fichiers de votre projet.

---

## 10. Routine recommandée

À chaque séance de travail :

```text
1. Ouvrir Anaconda Prompt ou un terminal.
2. Activer l’environnement du projet.
3. Ouvrir VS Code.
4. Ouvrir le dossier du projet.
5. Sélectionner le noyau de l’environnement dans le notebook.
6. Travailler et enregistrer.
```

### Commandes essentielles

| Commande | Fonction |
|---|---|
| `conda create --name langues_de_specialite python=3.12 ipykernel` | Créer l’environnement |
| `conda activate langues_de_specialite` | Activer l’environnement |
| `conda deactivate` | Quitter l’environnement |
| `conda env list` | Lister les environnements |
| `conda list` | Lister les bibliothèques installées |
| `python --version` | Afficher la version de Python |

---

## 11. Problèmes fréquents

| Problème | Solution probable |
|---|---|
| `conda: command not found` | Utiliser Anaconda Prompt ou vérifier l’installation d’Anaconda/Miniconda |
| L’environnement n’apparaît pas dans VS Code | Redémarrer VS Code, puis utiliser `Python: Select Interpreter` |
| Le notebook ne s’exécute pas | Vérifier que `ipykernel` est installé dans l’environnement |
| Les bibliothèques ne sont pas trouvées | Vérifier que l’environnement est activé avant l’installation |
| Mauvaise version de Python | Recréer l’environnement avec `python=3.12` |

---

## 12. Règle à retenir

> Ne pas installer les bibliothèques du projet dans `base`.
>
> Créer un environnement propre au projet, l’activer, puis sélectionner
> cet environnement dans VS Code.