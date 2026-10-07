# Chaîne de recherche et de traitement

Ce dossier contient les opérations qui transforment une question de recherche et un corpus source en résultats interprétables.

La chaîne de recherche relie :

```text
Question
    ↓
Corpus
    ↓
Acquisition
    ↓
Préparation
    ↓
Analyse
    ↓
Validation
    ↓
Interprétation
```

L’objectif est de répondre à la question suivante :

> **Comment les données ont-elles été transformées, analysées, contrôlées et interprétées afin de répondre à la question de recherche ?**

> **Principe :** chaque opération doit être justifiée par la question de recherche, documentée, traçable et, lorsque possible, vérifiable ou reproductible.

La chaîne n’est pas strictement linéaire. Une erreur d’extraction, une difficulté d’accès, une ambiguïté d’annotation ou un résultat inattendu peut nécessiter de revenir à une étape précédente.

---

## Structure du dossier

```text
chaine/
├── README.md
│
├── 01_question_et_cadre/
│   ├── README.md
│   ├── question_recherche.md
│   ├── cadre_conceptuel.md
│   └── bibliographie_initiale.bib
│
├── 02_conception_du_corpus/
│   ├── README.md
│   ├── protocole_selection.md
│   ├── criteres_inclusion_exclusion.md
│   └── plan_corpus.md
│
├── 03_acquisition/
│   ├── README.md
│   ├── protocole_acquisition.md
│   ├── code/
│   └── controles/
│
├── 04_preparation/
│   ├── README.md
│   ├── 01_extraction/
│   ├── 02_nettoyage/
│   ├── 03_segmentation/
│   └── 04_annotation_ou_representation/
│
├── 05_analyse/
│   ├── README.md
│   ├── code/
│   ├── configurations/
│   └── sorties_intermediaires/
│
├── 06_validation/
│   ├── README.md
│   ├── controles_donnees/
│   ├── controles_annotations/
│   ├── analyses_erreurs/
│   └── tests_sensibilite/
│
└── 07_interpretation/
    ├── README.md
    ├── synthese_resultats.md
    ├── contre_exemples.md
    └── limites.md
```

Les dossiers inutiles pour le projet peuvent être retirés ou renommés. En revanche, une opération effectivement réalisée doit apparaître dans la chaîne, même si elle est manuelle ou réalisée avec un logiciel à interface graphique.

---

## Vue d’ensemble

| Étape | Question directrice | Entrées principales | Sorties principales |
|---|---|---|---|
| 01. Question et cadre | Que cherche-t-on à comprendre ? | Lectures, exemples, phénomènes observés | Question et concepts opérationnalisés |
| 02. Conception du corpus | Quelles données peuvent répondre à la question ? | Sources potentielles, critères | Plan de corpus et protocole de sélection |
| 03. Acquisition | Comment obtenir les documents et métadonnées ? | Sources, exports, API, téléchargements | Données sources et inventaire |
| 04. Préparation | Quelles transformations rendent les données analysables ? | Données sources | Corpus extrait, nettoyé, segmenté ou annoté |
| 05. Analyse | Quelle méthode produit les observations pertinentes ? | Corpus préparé, paramètres | Tableaux, figures, listes, modèles ou extraits |
| 06. Validation | Que faut-il contrôler avant d’interpréter ? | Données, annotations, résultats | Contrôles, erreurs, sensibilités et limites |
| 07. Interprétation | Que permettent de conclure les résultats ? | Résultats validés, extraits, cadre conceptuel | Réponse à la question et discussion |

---

## Dépendances entre les étapes

```text
01_question_et_cadre
          ↓
02_conception_du_corpus
          ↓
03_acquisition
          ↓
04_preparation
          ↓
05_analyse
          ↓
06_validation
          ↓
07_interpretation
          ↓
article/article_imrad.md
```

Cette représentation est simplifiée. Dans la pratique, les retours suivants sont possibles :

```text
Validation → Préparation
Validation → Analyse
Analyse → Conception du corpus
Interprétation → Question et cadre
```

Exemples :

- Une erreur d’extraction peut imposer de modifier le nettoyage.
- Une catégorie ambiguë peut exiger une révision du guide d’annotation.
- Un corpus inaccessible peut imposer une reformulation de la question.
- Une différence inattendue peut conduire à examiner une variable de genre, de période ou de source non prévue initialement.

Ces révisions doivent être consignées dans :

```text
journal/journal_de_bord.md
```

---

# Règles de documentation

Chaque dossier ou sous-dossier de la chaîne doit contenir un `README.md` ou un protocole décrivant les éléments suivants.

| Élément | Question à laquelle répondre |
|---|---|
| Objectif | Pourquoi cette opération est-elle nécessaire ? |
| Lien avec la question | Quelle sous-question ou besoin méthodologique traite-t-elle ? |
| Entrées | Quelles données, fichiers ou versions sont utilisés ? |
| Procédure | Quel code, outil ou protocole est appliqué ? |
| Paramètres | Quels réglages, seuils, catégories ou règles sont retenus ? |
| Sorties | Quels fichiers ou résultats sont produits ? |
| Contrôles | Comment vérifie-t-on la qualité de l’opération ? |
| Limites | Quelles erreurs, pertes ou incertitudes restent possibles ? |
| Reprise | Comment une autre personne peut-elle refaire ou vérifier l’opération ? |

---

## Gabarit de README pour une sous-tâche

Copier ce modèle dans chaque sous-dossier nécessaire.

```markdown
# [Nom de la sous-tâche]

## Objectif

[Décrire l’opération et son rôle dans l’enquête.]

## Lien avec la question de recherche

[Expliquer pourquoi cette opération est nécessaire pour répondre à la question.]

## Entrées

| Fichier ou ressource | Description | Version |
|---|---|---|
| `[chemin]` | [Description] | [Version ou date] |

## Procédure

[Décrire les opérations réalisées.]

### Code ou protocole

```text
[Chemin vers le script, notebook ou protocole]
```

### Commande d’exécution

```bash
[Commande ou instructions]
```

## Paramètres

| Paramètre | Valeur | Justification |
|---|---|---|
| `[nom]` | `[valeur]` | [Justification] |

## Sorties

| Fichier produit | Description |
|---|---|
| `[chemin]` | [Description] |

## Contrôles

[Décrire les vérifications effectuées.]

## Limites

[Décrire les erreurs ou pertes possibles.]

## Journal associé

[Ajouter les liens vers les entrées de journal pertinentes.]

## Reproduction ou vérification

[Indiquer comment une autre personne peut refaire ou vérifier cette étape.]
```

---

# 01 — Question et cadre

```text
chaine/01_question_et_cadre/
```

Cette étape définit le problème de recherche avant le choix des outils.

## Fichiers attendus

```text
01_question_et_cadre/
├── README.md
├── question_recherche.md
├── cadre_conceptuel.md
├── operationnalisation.md
└── bibliographie_initiale.bib
```

## Contenu minimal

### `question_recherche.md`

```markdown
# Question de recherche

## Objet d’étude

[Phénomène langagier ou discursif étudié.]

## Question principale

> [Question de recherche.]

## Sous-questions

1. [Sous-question 1]
2. [Sous-question 2]

## Portée

[Ce que la question cherche à comprendre.]

## Hors périmètre

[Ce que le projet ne cherche pas à établir.]
```

### `operationnalisation.md`

```markdown
# Opérationnalisation

| Concept | Définition de travail | Observable retenu | Limite |
|---|---|---|---|
| [Concept 1] | [Définition] | [Indice textuel ou catégorie] | [Limite] |
| [Concept 2] | [Définition] | [Indice textuel ou catégorie] | [Limite] |
```

> Une notion théorique ne devient pas automatiquement une variable ou une catégorie.  
> Les règles permettant de reconnaître le phénomène doivent être explicitées.

---

# 02 — Conception du corpus

```text
chaine/02_conception_du_corpus/
```

Cette étape transforme la question de recherche en plan de données.

## Fichiers attendus

```text
02_conception_du_corpus/
├── README.md
├── protocole_selection.md
├── criteres_inclusion_exclusion.md
├── plan_corpus.md
└── sources_candidates.csv
```

## Questions à documenter

- Quel domaine ou quelle activité spécialisée est étudiée ?
- Quels genres documentaires sont pertinents ?
- Quelle période est retenue ?
- Quelles langues sont incluses ou exclues ?
- Quelle est l’unité documentaire ?
- Quelle est l’unité d’analyse ?
- Quels documents seront comparés ?
- Quelles métadonnées doivent être collectées ?
- Quels critères permettent d’inclure ou d’exclure un document ?
- Quelle taille ou quel volume est réaliste pour le projet ?

## Exemple de plan de corpus

```markdown
# Plan de corpus

| Élément | Décision |
|---|---|
| Domaine | [Domaine] |
| Sous-domaine | [Sous-domaine] |
| Genres | [Genres retenus] |
| Langue(s) | [Langues] |
| Période | [Période] |
| Unité documentaire | [Article, rapport, etc.] |
| Unité d’analyse | [Phrase, paragraphe, etc.] |
| Comparaison principale | [Sous-corpus A vs B] |
| Taille visée | [Nombre de documents ou unités] |
```

---

# 03 — Acquisition

```text
chaine/03_acquisition/
```

Cette étape documente l’obtention des données sources et des métadonnées.

## Fichiers attendus

```text
03_acquisition/
├── README.md
├── protocole_acquisition.md
├── code/
│   ├── telecharger_documents.py
│   └── extraire_metadonnees.py
├── controles/
│   └── controle_acquisition.md
└── sources_consultees.csv
```

## Modes d’acquisition possibles

| Mode | Exemple |
|---|---|
| Collecte manuelle | Téléchargement contrôlé de documents |
| Export | Export CSV depuis une base ou plateforme |
| API | Récupération structurée de données |
| Moissonnage | Extraction automatisée de pages accessibles |
| Corpus existant | Réutilisation d’un corpus documenté |
| Numérisation | OCR ou transcription de documents non numériques |

## Informations à conserver

- Source et URL.
- Date de consultation ou collecte.
- Méthode utilisée.
- Conditions d’accès et de réutilisation.
- Identifiant attribué au document.
- Échecs ou documents inaccessibles.
- Métadonnées récupérées.
- Version des données acquises.

## Important

Ne pas contourner les restrictions d’accès, les contrôles techniques ou les conditions d’utilisation.

Le respect d’un fichier `robots.txt` peut orienter une collecte automatisée, mais ne remplace pas une autorisation de réutilisation ou de redistribution des contenus.

---

# 04 — Préparation

```text
chaine/04_preparation/
```

Cette étape rend les données exploitables pour l’analyse.

```text
04_preparation/
├── README.md
├── 01_extraction/
├── 02_nettoyage/
├── 03_segmentation/
└── 04_annotation_ou_representation/
```

## 04.01 — Extraction

```text
04_preparation/01_extraction/
```

Objectif : passer du format source — HTML, PDF, XML, image ou export — à un contenu structuré exploitable.

Exemples :

- Extraire le texte principal d’une page HTML.
- Extraire le texte d’un PDF.
- Identifier les titres, auteurs, dates et sections.
- Extraire des notes ou références dans des champs distincts.
- Appliquer une reconnaissance optique de caractères à un document image.

### Contrôles possibles

- Vérifier que les fichiers ne sont pas vides.
- Comparer un échantillon au document source.
- Vérifier la présence des accents et caractères spéciaux.
- Vérifier que les métadonnées correspondent au document.
- Contrôler les erreurs de lecture de PDF ou d’OCR.

---

## 04.02 — Nettoyage

```text
04_preparation/02_nettoyage/
```

Objectif : retirer, corriger ou séparer des éléments selon des règles explicites.

Exemples :

- Retirer menus, publicités ou éléments de navigation.
- Supprimer des doublons.
- Normaliser l’encodage en UTF-8.
- Uniformiser les espaces ou caractères.
- Retirer ou conserver les références bibliographiques.
- Retirer ou conserver les notes de bas de page.
- Corriger des erreurs d’extraction manifestes.

> Le nettoyage n’est pas une opération neutre.  
> Supprimer un élément revient à décider qu’il ne sera pas analysé.

Chaque suppression ou normalisation importante doit être justifiée par la question de recherche.

---

## 04.03 — Segmentation

```text
04_preparation/03_segmentation/
```

Objectif : découper les documents en unités d’analyse.

Unités possibles :

- document ;
- titre ;
- résumé ;
- section ;
- paragraphe ;
- phrase ;
- groupe de phrases ;
- contexte de citation ;
- paire de documents ;
- tour de parole.

### Exemple

```markdown
# Décision de segmentation

Les documents sont segmentés en phrases parce que la question porte
sur la formulation de relations causales à l’échelle de l’énoncé.

Les titres et références sont exclus de cette segmentation, mais
conservés dans les métadonnées.
```

### Contrôles possibles

- Vérifier la segmentation des abréviations.
- Vérifier les listes, tableaux et titres.
- Comparer un échantillon avec le document source.
- Vérifier que les identifiants document–section–phrase sont conservés.

---

## 04.04 — Annotation ou représentation

```text
04_preparation/04_annotation_ou_representation/
```

Cette sous-étape est conditionnelle : elle dépend de la question et de la méthode.

### Annotation

L’annotation ajoute une information linguistique ou analytique.

Exemples :

- lemmes ;
- catégories grammaticales ;
- dépendances syntaxiques ;
- entités nommées ;
- catégories discursives ;
- relations argumentatives ;
- marques d’incertitude ;
- fonctions de citation ;
- catégories terminologiques.

### Représentation

La représentation transforme les unités textuelles en caractéristiques exploitables par une méthode.

Exemples :

- formes ou lemmes ;
- n-grammes ;
- fréquences ;
- matrice document-terme ;
- TF-IDF ;
- vecteurs de plongement ;
- représentations par segments ;
- variables descriptives ou métadonnées.

### Documentation attendue

| Élément | Exemple |
|---|---|
| Outil ou modèle | spaCy, TXM, modèle d’embedding, règle manuelle |
| Version | Version exacte du logiciel ou du modèle |
| Unité | Phrase, paragraphe, document |
| Paramètres | Langue, seuil, longueur de n-gramme, etc. |
| Catégories | Guide d’annotation ou définitions |
| Sortie | Fichier annoté, matrice, tableau ou vecteurs |
| Contrôle | Échantillon vérifié, analyse d’erreurs, double annotation |

---

# 05 — Analyse

```text
chaine/05_analyse/
```

Cette étape applique une méthode permettant de répondre à la question de recherche.

## Fichiers attendus

```text
05_analyse/
├── README.md
├── code/
├── configurations/
├── sorties_intermediaires/
└── produire_resultats_principaux.py
```

## Méthodes possibles

| Objectif | Méthodes possibles |
|---|---|
| Décrire le corpus | Fréquences, distributions, statistiques descriptives |
| Examiner les usages | Concordances, cooccurrences, lecture contextualisée |
| Comparer des sous-corpus | Spécificités, proportions, tests adaptés, comparaison qualitative |
| Étudier la structure | Segmentation, analyse de genres, identification de mouvements rhétoriques |
| Étudier les relations | Réseaux, cooccurrences, citations, relations syntaxiques ou sémantiques |
| Repérer des catégories | Annotation manuelle, règles, classification supervisée |
| Explorer des regroupements | Clustering, réduction dimensionnelle, modélisation thématique |
| Mesurer des similarités | TF-IDF, embeddings, distances ou similarité cosinus |

## Documentation minimale

Chaque méthode doit préciser :

- la question à laquelle elle répond ;
- les données et versions utilisées ;
- l’unité d’analyse ;
- les paramètres ;
- les sorties produites ;
- le statut du résultat : principal, secondaire, exploratoire ou diagnostique ;
- les conditions de validité de l’interprétation.

> Une méthode n’est pas choisie parce qu’elle est disponible dans une bibliothèque.  
> Elle est choisie parce qu’elle répond à une question sur le corpus.

---

# 06 — Validation

```text
chaine/06_validation/
```

Cette étape vérifie les données, traitements, annotations, résultats et interprétations.

## Fichiers attendus

```text
06_validation/
├── README.md
├── controles_donnees/
├── controles_annotations/
├── analyses_erreurs/
├── tests_sensibilite/
└── verification_resultat_principal.md
```

## Types de validation

| Élément à contrôler | Exemple de validation |
|---|---|
| Données sources | Vérifier un échantillon contre les documents originaux |
| Métadonnées | Vérifier titres, dates, genres et identifiants |
| Extraction | Comparer texte extrait et texte source |
| Nettoyage | Vérifier ce qui a été supprimé ou conservé |
| Segmentation | Vérifier les frontières de phrases ou sections |
| Annotation manuelle | Double annotation et discussion des désaccords |
| Annotation automatique | Analyse d’erreurs sur un échantillon |
| Classification | Jeu de test, mesures adaptées, inspection des erreurs |
| Regroupement | Retour aux textes, cohérence des groupes, stabilité |
| Statistiques | Vérifier totaux, dénominateurs, doublons et unités |
| Visualisation | Comparer figure, tableau source et légende |
| Interprétation | Examiner contre-exemples et explications concurrentes |

## Résultat central

Le projet doit sélectionner au moins un résultat central et expliquer comment il peut être vérifié.

```markdown
# Vérification du résultat principal

## Résultat vérifié

[Décrire le résultat.]

## Données utilisées

[Préciser le corpus, version et sous-corpus.]

## Procédure

[Préciser script ou protocole.]

## Contrôle

[Décrire la vérification.]

## Résultat du contrôle

[Présenter le résultat.]

## Limites restantes

[Préciser ce qui n’est pas résolu.]
```

---

# 07 — Interprétation

```text
chaine/07_interpretation/
```

Cette étape relie les résultats validés à la question de recherche et au cadre conceptuel.

## Fichiers attendus

```text
07_interpretation/
├── README.md
├── synthese_resultats.md
├── contre_exemples.md
├── limites.md
└── discussion_preliminaire.md
```

## Questions à traiter

- Que montrent les résultats ?
- Quelle réponse apportent-ils à la question ?
- Quels extraits ou observations soutiennent cette réponse ?
- Quelles explications concurrentes restent possibles ?
- Quelles limites du corpus ou de la méthode restreignent la conclusion ?
- Que faudrait-il collecter ou analyser pour renforcer l’enquête ?
- Quels résultats doivent être présentés comme exploratoires ?

> L’interprétation ne consiste pas à répéter les tableaux ou les figures.  
> Elle consiste à expliquer leur signification, leur portée et leurs limites.

---

## Articulation avec les autres dossiers

| Dossier | Fonction dans la chaîne |
|---|---|
| `journal/` | Explique la genèse des décisions et révisions |
| `configuration/` | Contient les paramètres partagés du projet |
| `environnement/` | Documente les logiciels, versions et modèles |
| `donnees/` | Décrit le corpus, sa provenance et ses transformations |
| `resultats/` | Conserve les sorties finales, tableaux, figures et extraits |
| `article/` | Présente l’enquête selon une logique scientifique IMRAD |

---

## Journal des changements

Les changements importants doivent être consignés dans le journal de recherche.

Exemples :

| Changement | Où le documenter |
|---|---|
| Révision de la question | `journal/` et `01_question_et_cadre/` |
| Modification des critères de sélection | `journal/` et `02_conception_du_corpus/` |
| Changement de source | `journal/` et `03_acquisition/` |
| Modification du nettoyage | `journal/` et `04_preparation/02_nettoyage/` |
| Révision des catégories | `journal/` et `04_preparation/04_annotation_ou_representation/` |
| Nouveau paramètre de modèle | `journal/`, `configuration/` et `05_analyse/` |
| Découverte d’une erreur | `journal/` et `06_validation/` |
| Révision d’une conclusion | `journal/`, `07_interpretation/` et `article/` |

---

## Checklist avant remise

- [ ] Chaque sous-tâche réalisée est représentée dans la chaîne.
- [ ] Chaque dossier pertinent possède un README ou protocole.
- [ ] Les entrées, procédures, paramètres et sorties sont documentés.
- [ ] Les scripts et protocoles comportent des noms explicites.
- [ ] Les données sources ne sont pas modifiées directement.
- [ ] Les transformations importantes sont traçables.
- [ ] Les résultats peuvent être reliés à une procédure d’analyse.
- [ ] Au moins un résultat central a été contrôlé.
- [ ] Les limites sont documentées avant la rédaction de l’article.
- [ ] Les révisions importantes sont consignées dans le journal.
- [ ] La chaîne correspond effectivement à ce qui a été fait.