# Environnement d’exécution

Ce dossier documente l’environnement informatique utilisé pour préparer, analyser et reproduire les résultats du projet.

L’objectif est de permettre à une autre personne de répondre aux questions suivantes :

1. Quel système et quels logiciels ont été utilisés ?
2. Quelles bibliothèques, versions et ressources linguistiques sont nécessaires ?
3. Comment installer un environnement compatible ?
4. Comment vérifier que l’environnement fonctionne ?
5. Quelle version de l’environnement a produit les résultats finaux ?

> **Principe :** le code seul ne suffit pas toujours à reproduire un résultat.  
> Les versions de logiciels, bibliothèques, modèles, paramètres et données peuvent modifier les sorties.

---

## Structure du dossier

```text
environnement/
├── README.md
├── requirements.txt          # Dépendances Python, si Python est utilisé
├── environment.yml           # Environnement Conda, si Conda est utilisé
├── requirements-r.txt        # Dépendances R, si R est utilisé
├── session_info.txt          # Information sur la session R
├── modele_spacy.txt          # Modèle spaCy et version, si pertinent
└── verification_environnement.py
```

Tous ces fichiers ne sont pas obligatoires. Conserver seulement ceux qui correspondent réellement au projet.

| Fichier | Utilité | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Documentation de l’environnement | Oui |
| `requirements.txt` | Paquets Python requis | Oui |
| `environment.yml` | Environnement Conda complet | Oui |
| `requirements-r.txt` | Paquets R requis | Oui |
| `session_info.txt` | Versions de R et des paquets utilisés | Oui |
| `modele_spacy.txt` | Nom et version d’un modèle spaCy | Oui |
| `verification_environnement.py` | Test de fonctionnement minimal | Oui |
| `.venv/`, `venv/`, `env/` | Environnement local installé | Non |

Les environnements virtuels eux-mêmes ne doivent pas être ajoutés au dépôt :

```gitignore
.venv/
venv/
env/
```

---

## Configuration utilisée

| Élément | Version ou valeur |
|---|---|
| Système d’exploitation | [Ex. : Windows 11 / macOS 15 / Ubuntu 24.04] |
| Architecture | [Ex. : x86_64 / arm64] |
| Langage principal | [Ex. : Python 3.12.7] |
| Gestionnaire d’environnement | [Ex. : `venv`, Conda, renv, aucun] |
| Langage secondaire | [Ex. : R 4.4.2, si pertinent] |
| Outil de versionnement | [Ex. : Git 2.47.1] |
| Éditeur ou IDE | [Ex. : VS Code 1.xx, RStudio 2024.xx, facultatif] |
| Date de vérification | [YYYY-MM-DD] |
| Version du dépôt | [Tag Git ou hash du commit] |

> Remplacer les valeurs entre crochets avant la remise finale.

---

# Option A — Environnement Python avec `venv`

Cette option convient aux projets réalisés principalement en Python.

## Création de l’environnement

Depuis la racine du projet :

### macOS ou Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```bat
py -m venv .venv
.\.venv\Scripts\activate.bat
```

Une fois l’environnement activé, installer les dépendances :

```bash
python -m pip install --upgrade pip
python -m pip install -r environnement/requirements.txt
```

---

## Exemple de `requirements.txt`

Conserver uniquement les dépendances réellement nécessaires.

```text
pandas==2.2.3
numpy==2.1.2
scikit-learn==1.5.2
spacy==3.8.2
pyyaml==6.0.2
matplotlib==3.9.2
jupyterlab==4.3.0
```

Si le projet utilise des notebooks :

```text
ipykernel==6.29.5
jupyterlab==4.3.0
```

Après toute modification contrôlée des dépendances, mettre à jour le fichier :

```bash
python -m pip freeze > environnement/requirements.txt
```

> Vérifier ensuite que ce fichier ne contient pas de dépendances inutiles, propres à un autre projet ou installées accidentellement.

---

# Option B — Environnement Conda

Utiliser cette option seulement si le projet repose effectivement sur Conda ou Miniconda.

## Création de l’environnement

```bash
conda env create -f environnement/environment.yml
conda activate nom_environnement
```

## Exemple de `environment.yml`

```yaml
name: corpus-discours-specialite

channels:
  - conda-forge
  - defaults

dependencies:
  - python=3.12
  - pandas=2.2
  - numpy=2.1
  - scikit-learn=1.5
  - matplotlib=3.9
  - pip
  - pip:
      - spacy==3.8.2
      - pyyaml==6.0.2
```

Pour exporter un environnement Conda existant :

```bash
conda env export --from-history > environnement/environment.yml
```

L’option `--from-history` produit généralement un fichier plus lisible, car elle conserve surtout les dépendances explicitement choisies.

---

# Option C — Environnement R

Cette section est pertinente si le projet utilise R, RStudio, Quarto ou R Markdown.

## Informations de session

À la fin d’une analyse R, exécuter :

```r
sessionInfo()
```

Puis enregistrer la sortie dans :

```text
environnement/session_info.txt
```

Exemple :

```r
capture.output(
  sessionInfo(),
  file = "environnement/session_info.txt"
)
```

## Exemple de `requirements-r.txt`

```text
tidyverse
readr
dplyr
stringr
xml2
rvest
udpipe
quanteda
tm
text2vec
here
renv
```

## Option recommandée : `renv`

Pour un projet R exigeant une plus grande stabilité :

```r
install.packages("renv")
renv::init()
```

Puis, après installation des paquets réellement nécessaires :

```r
renv::snapshot()
```

Le projet contiendra alors notamment :

```text
renv.lock
renv/
```

Pour restaurer l’environnement sur un autre ordinateur :

```r
renv::restore()
```

---

# Modèles linguistiques

Les modèles linguistiques doivent être documentés séparément des bibliothèques, car leur version peut affecter les annotations.

## Exemple pour spaCy

Créer un fichier :

```text
environnement/modele_spacy.txt
```

Contenu suggéré :

```text
Bibliothèque : spaCy
Version de spaCy : 3.8.2
Modèle : fr_core_news_md
Version du modèle : [à compléter]
Langue : français
Composantes utilisées :
- tokenisation
- segmentation en phrases
- lemmatisation
- étiquetage morphosyntaxique
- analyse de dépendances
- reconnaissance d’entités nommées

Commande d’installation :
python -m spacy download fr_core_news_md
```

Vérifier la version du modèle :

```bash
python -m spacy info fr_core_news_md
```

Le modèle doit également être mentionné dans la section Méthodes de l’article si ses annotations jouent un rôle dans les résultats.

---

# Vérification de l’environnement

Le projet devrait contenir une vérification minimale permettant de confirmer que les dépendances essentielles sont installées.

## Exemple : `verification_environnement.py`

```python
import sys
import pandas
import numpy
import sklearn

print(f"Python : {sys.version}")
print(f"pandas : {pandas.__version__}")
print(f"numpy : {numpy.__version__}")
print(f"scikit-learn : {sklearn.__version__}")

try:
    import spacy
    print(f"spaCy : {spacy.__version__}")

    nlp = spacy.load("fr_core_news_md")
    doc = nlp("Cette phrase permet de vérifier le modèle linguistique.")
    print("Modèle spaCy : fr_core_news_md")
    print("Nombre de tokens :", len(doc))

except ImportError:
    print("spaCy n’est pas installé.")
except OSError:
    print("Le modèle fr_core_news_md n’est pas installé.")
```

Exécuter le test depuis la racine du projet :

```bash
python environnement/verification_environnement.py
```

Résultat attendu :

```text
Python : 3.x.x
pandas : x.x.x
numpy : x.x.x
scikit-learn : x.x.x
spaCy : x.x.x
Modèle spaCy : fr_core_news_md
Nombre de tokens : [nombre positif]
```

Si le modèle spaCy n’est pas requis, retirer cette partie du script.

---

# Installation minimale

Pour reproduire une analyse Python standard :

```bash
git clone [URL_DU_DEPOT]
cd [NOM_DU_DEPOT]

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r environnement/requirements.txt

python environnement/verification_environnement.py
```

Sous Windows PowerShell :

```powershell
git clone [URL_DU_DEPOT]
cd [NOM_DU_DEPOT]

py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r environnement/requirements.txt

python environnement\verification_environnement.py
```

---

# Mise à jour de l’environnement

Toute modification importante de l’environnement doit être documentée.

| Événement | Action attendue |
|---|---|
| Ajout d’une bibliothèque | Mettre à jour `requirements.txt` ou `environment.yml` |
| Changement de version d’un modèle | Mettre à jour `modele_spacy.txt` et le journal |
| Modification d’une dépendance influençant les résultats | Vérifier si les analyses doivent être relancées |
| Changement d’ordinateur | Exécuter `verification_environnement.py` |
| Résultat final produit | Noter les versions utilisées dans l’article et le dépôt |

Documenter les changements importants :

1. Dans le message de commit.
2. Dans le journal de recherche.
3. Dans ce fichier, si la modification est durable.
4. Dans la section Méthodes de l’article, si elle affecte les résultats.

---

# Limites connues

- Les résultats peuvent varier selon le système d’exploitation, la version des bibliothèques, les modèles linguistiques ou le matériel.
- Certains outils nécessitent des téléchargements supplémentaires, des modèles externes ou un accès Internet.
- Les données sous licence ou non redistribuables peuvent empêcher une reproduction complète ; le projet doit alors documenter une procédure de vérification partielle.
- L’environnement documenté permet de reproduire ou vérifier les traitements du projet, mais ne garantit pas automatiquement qu’un résultat est scientifiquement valide.

---

# Checklist avant remise

- [ ] Le fichier `README.md` décrit l’environnement effectivement utilisé.
- [ ] Les versions de Python, R et des bibliothèques sont documentées.
- [ ] Les modèles linguistiques sont identifiés avec leur version.
- [ ] `requirements.txt`, `environment.yml` ou `renv.lock` est présent si nécessaire.
- [ ] L’environnement local (`.venv/`, `venv/`, `env/`) est ignoré par Git.
- [ ] Le script de vérification fonctionne sur au moins un poste.
- [ ] Les résultats finaux sont associés à une version identifiable du dépôt.
- [ ] Aucun mot de passe, jeton ou secret n’est présent dans ce dossier.
- [ ] Les différences entre installation locale et environnement final sont consignées dans le journal.

---

# Références méthodologiques

- Wilson, G., et al. (2017). *Good enough practices in scientific computing*. PLOS Computational Biology, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510
- Arvan, M., Pina, L., & Parde, N. (2022). *Reproducibility in Computational Linguistics: Is Source Code Enough?* EMNLP 2022. https://aclanthology.org/2022.emnlp-main.150/
- ACL Rolling Review. *Responsible NLP Research Checklist*. https://aclrollingreview.org/responsibleNLPresearch/