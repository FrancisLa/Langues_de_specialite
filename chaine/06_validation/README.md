# Validation et contrôle

Ce dossier contient les procédures, résultats et décisions permettant de
vérifier la qualité de l’enquête avant l’interprétation finale.

La validation ne correspond pas à une étape unique placée après
l’analyse. Elle traverse l’ensemble du projet :

```text
question
    ↓
conception du corpus
    ↓
acquisition
    ↓
préparation
    ↓
analyse
    ↓
validation
    ↓
interprétation
```

L’étape `06_validation/` rassemble toutefois les contrôles réalisés ou
synthétisés avant de tirer des conclusions.

L’objectif est de répondre aux questions suivantes :

> **Les données analysées correspondent-elles au corpus défini ?**

> **Les transformations, annotations et catégories sont-elles suffisamment contrôlées ?**

> **Les résultats peuvent-ils être reproduits, vérifiés ou expliqués ?**

> **Quels erreurs, contre-exemples, ambiguïtés ou effets de paramètres limitent les conclusions ?**

> **Principe :** une validation ne prouve pas automatiquement qu’une
> conclusion est vraie. Elle permet d’évaluer si les données, procédures
> et résultats sont suffisamment cohérents, transparents et contrôlés
> pour soutenir une interprétation prudente.

---

## Relation avec les autres étapes

Cette étape vérifie les choix et sorties produits dans :

```text
../01_question_et_cadre/
../02_conception_du_corpus/
../03_acquisition/
../04_preparation/
../05_analyse/
```

Elle produit des contrôles nécessaires à :

```text
../07_interpretation/
../../resultats/
../../article/
```

Les décisions, erreurs, corrections et limites importantes sont
consignées dans :

```text
../../journal/journal_de_bord.md
```

---

## Structure du dossier

```text
06_validation/
├── README.md
├── plan_validation.md
├── verification_resultat_principal.md
├── registre_controles.csv
│
├── controles_donnees/
│   ├── README.md
│   ├── controle_provenance.md
│   ├── controle_metadonnees.md
│   ├── controle_doublons.md
│   └── echantillon_controle_donnees.csv
│
├── controles_preparation/
│   ├── README.md
│   ├── controle_extraction.md
│   ├── controle_nettoyage.md
│   └── controle_segmentation.md
│
├── controles_annotations/
│   ├── README.md
│   ├── protocole_double_annotation.md
│   ├── accords_annotations.csv
│   ├── desaccords_annotations.md
│   └── guide_annotation_revise.md
│
├── analyses_erreurs/
│   ├── README.md
│   ├── erreurs_modele.csv
│   ├── erreurs_extraction.md
│   ├── erreurs_annotation.md
│   └── contre_exemples.md
│
├── tests_sensibilite/
│   ├── README.md
│   ├── sensibilite_parametres.md
│   ├── sensibilite_corpus.md
│   └── sensibilite_unites.md
│
└── reproductibilite/
    ├── README.md
    ├── protocole_reprise.md
    └── rapport_verification_pair.md
```

| Élément | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Présente l’étape de validation | Oui |
| `plan_validation.md` | Définit les contrôles prévus et leurs critères | Oui |
| `verification_resultat_principal.md` | Documente le contrôle d’un résultat central | Oui |
| `registre_controles.csv` | Consigne les vérifications réalisées | Oui |
| `controles_donnees/` | Vérifie corpus, provenance, métadonnées et doublons | Oui |
| `controles_preparation/` | Vérifie extraction, nettoyage et segmentation | Oui |
| `controles_annotations/` | Vérifie catégories, annotations et désaccords | Oui |
| `analyses_erreurs/` | Documente erreurs, cas limites et contre-exemples | Oui |
| `tests_sensibilite/` | Évalue l’effet de choix analytiques importants | Oui |
| `reproductibilite/` | Documente la reprise ou vérification d’un résultat | Oui |

Les sous-dossiers non pertinents pour un projet peuvent être retirés.
Toutefois, l’absence d’un type de contrôle doit être justifiée si ce
contrôle serait normalement nécessaire à la méthode employée.

---

# 1. Plan de validation

Le fichier principal de cette étape est :

```text
plan_validation.md
```

Le plan doit être préparé avant l’interprétation finale. Certains
contrôles peuvent être anticipés dès la conception du corpus ou de
l’analyse.

## Gabarit

```markdown
# Plan de validation

## Version

- Version : [v0.1]
- Date : [YYYY-MM-DD]
- Personnes responsables : [Nom(s)]

## Question principale

> [Question de recherche.]

## Résultat principal à contrôler

[Décrire le résultat qui répond directement à la question.]

## Risques méthodologiques identifiés

| Risque | Étape concernée | Conséquence possible |
|---|---|---|
| [Ex. : doublons] | Acquisition | Surreprésentation de certains documents |
| [Ex. : mauvaise segmentation] | Préparation | Erreurs dans les unités analysées |
| [Ex. : catégorie ambiguë] | Annotation | Classement incohérent |
| [Ex. : seuil arbitraire] | Analyse | Résultat sensible aux paramètres |
| [Ex. : corpus restreint] | Conception | Portée limitée de la conclusion |

## Contrôles prévus

| ID | Contrôle | Risque traité | Procédure | Critère de décision |
|---|---|---|---|---|
| V01 | Vérification des métadonnées | Erreur de source ou genre | Échantillon manuel | [Critère] |
| V02 | Contrôle d’extraction | Texte incomplet | Comparaison au document source | [Critère] |
| V03 | Double annotation | Catégorie ambiguë | Annotation indépendante | [Critère] |
| V04 | Analyse d’erreurs | Prédictions incorrectes | Examen qualitatif | [Critère] |
| V05 | Test de sensibilité | Effet de paramètre | Reprise avec valeurs alternatives | [Critère] |
| V06 | Vérification par un pair | Procédure non reproductible | Reprise d’un résultat | [Critère] |

## Limites non résolues

[Décrire les contrôles impossibles, trop coûteux ou non pertinents,
ainsi que leurs conséquences.]
```

---

# 2. Types de validation

La validation peut porter sur plusieurs dimensions.

| Dimension | Question de contrôle | Exemple |
|---|---|---|
| Conceptuelle | Les catégories représentent-elles raisonnablement le concept étudié ? | Une catégorie « causalité » distingue-t-elle l’association et l’effet direct ? |
| Corpus | Les documents retenus correspondent-ils aux critères annoncés ? | Les genres et langues sont-ils correctement attribués ? |
| Provenance | Les sources, dates et conditions d’accès sont-elles traçables ? | Chaque document possède-t-il une URL ou référence ? |
| Préparation | Les transformations préservent-elles les informations nécessaires ? | Les notes, références ou sections sont-elles correctement traitées ? |
| Annotation | Les règles sont-elles appliquées de manière cohérente ? | Les annotateurs classent-ils les mêmes passages de façon comparable ? |
| Analytique | Les calculs, modèles ou paramètres produisent-ils des résultats cohérents ? | Les dénominateurs et filtres sont-ils corrects ? |
| Reproductibilité | Une autre personne peut-elle reprendre un résultat important ? | Un pair produit-il le même tableau avec le protocole fourni ? |
| Interprétative | Les résultats soutiennent-ils réellement la conclusion ? | Les extraits et contre-exemples confirment-ils l’analyse ? |

> Une bonne performance d’annotation ou de classification ne garantit pas
> automatiquement la validité conceptuelle, la représentativité du corpus
> ou la portée d’une interprétation.

---

# 3. Contrôle des données

Sous-dossier :

```text
controles_donnees/
```

Cette étape vérifie que les documents utilisés correspondent au corpus
annoncé et que leurs métadonnées sont fiables.

## Contrôles possibles

| Contrôle | Question | Exemple de procédure |
|---|---|---|
| Présence | Les fichiers attendus sont-ils disponibles ? | Comparer inventaire et fichiers sources |
| Identifiants | Chaque document a-t-il un identifiant unique ? | Vérifier `id_document` |
| Doublons | Un même document est-il compté plusieurs fois ? | Comparer URL, DOI, titre, hash |
| Source | La provenance est-elle documentée ? | Vérifier URL, référence et date de collecte |
| Langue | La langue déclarée correspond-elle au document ? | Lecture d’un échantillon |
| Genre | Le document appartient-il au genre annoncé ? | Vérification manuelle |
| Période | La date respecte-t-elle les critères ? | Contrôle des métadonnées |
| Sous-corpus | Le document est-il affecté au bon groupe ? | Vérifier les règles de classement |
| Appariement | Les documents associés sont-ils réellement liés ? | Vérifier DOI, titre, lien explicite |
| Accès | Les conditions d’utilisation sont-elles documentées ? | Vérifier les métadonnées et README |

## Échantillonnage de contrôle

Un contrôle peut porter sur l’ensemble du corpus ou sur un échantillon.

```markdown
# Échantillon de contrôle des données

## Population contrôlée

[Décrire le corpus ou sous-corpus.]

## Méthode d’échantillonnage

- [ ] Exhaustive
- [ ] Aléatoire simple
- [ ] Stratifiée
- [ ] Raisonnée
- [ ] Centrée sur les cas à risque
- [ ] Autre : [préciser]

## Taille de l’échantillon

[n] documents sur [N] documents.

## Dimensions vérifiées

- [ ] Identifiant
- [ ] Source
- [ ] Date
- [ ] Langue
- [ ] Genre
- [ ] Sous-corpus
- [ ] Relation avec une paire
- [ ] Texte accessible
- [ ] Conditions d’accès

## Résultats

[Décrire les erreurs et corrections.]
```

Les vérifications d’échantillons après les étapes de collecte,
conversion, nettoyage ou tokenisation permettent d’identifier des
problèmes tels que contenu manquant, caractères altérés, sur-nettoyage ou
erreurs de nommage. [387]

---

# 4. Contrôle de la préparation

Sous-dossier :

```text
controles_preparation/
```

Ces contrôles portent sur les transformations effectuées dans :

```text
../04_preparation/
```

## Questions de contrôle

| Étape | Question |
|---|---|
| Extraction | Le texte extrait correspond-il au document source ? |
| Nettoyage | Les éléments supprimés ou conservés correspondent-ils aux règles ? |
| Encodage | Les accents, caractères et symboles sont-ils lisibles ? |
| Déduplication | Les doublons ont-ils été correctement identifiés ? |
| Segmentation | Les frontières de phrases ou sections sont-elles correctes ? |
| Annotation linguistique | Les lemmes, POS ou entités sont-ils plausibles sur le corpus ? |
| Représentation | Les filtres, unités et variables correspondent-ils au protocole ? |

## Gabarit

```markdown
# Contrôle de [nom de la transformation]

## Version contrôlée

- Données : [version]
- Code ou protocole : [version Git]
- Date : [YYYY-MM-DD]

## Échantillon

[n] documents ou [n] unités.

## Méthode

[Comparer les sorties aux sources ou aux règles attendues.]

## Résultats

| Élément contrôlé | Correct | Incorrect | Ambigu | Commentaire |
|---|---:|---:|---:|---|
| [Élément] | [n] | [n] | [n] | [Commentaire] |

## Erreurs détectées

[Décrire les erreurs.]

## Décision

- [ ] Valider la transformation.
- [ ] Corriger les erreurs ponctuelles.
- [ ] Réviser le protocole.
- [ ] Reprendre la transformation.
- [ ] Limiter l’interprétation.
```

---

# 5. Validation des annotations

Sous-dossier :

```text
controles_annotations/
```

Cette section est nécessaire lorsqu’un projet utilise une annotation
manuelle, semi-automatique ou automatique.

```text
texte
    ↓
guide d’annotation
    ↓
application des catégories
    ↓
accords et désaccords
    ↓
révision éventuelle du guide
    ↓
annotation retenue
```

## 5.1 Annotation manuelle

Une annotation manuelle doit documenter :

- l’unité annotée ;
- les catégories ;
- le guide d’annotation ;
- les exemples et contre-exemples ;
- les personnes responsables ;
- la formation éventuelle ;
- l’annotation indépendante ;
- les désaccords ;
- les règles de résolution ;
- la version finale de l’annotation.

## Accord interannotateur

L’accord entre annotateurs peut renseigner sur la cohérence avec laquelle
un guide est appliqué.

| Mesure | Fonction | Limite |
|---|---|---|
| Accord brut | Proportion de décisions identiques | Ne tient pas compte de l’accord attendu par hasard |
| Kappa de Cohen | Accord corrigé pour le hasard, deux annotateurs | Dépend des distributions des catégories |
| Alpha de Krippendorff | Accord pour plusieurs annotateurs ou données incomplètes | Demande des choix de configuration explicites |
| Accord intra-annotateur | Stabilité d’un même annotateur dans le temps | Ne mesure pas l’accord entre personnes |

L’accord interannotateur ne prouve pas à lui seul que les catégories sont
conceptuellement valides. Il renseigne surtout sur la cohérence
d’application du schéma d’annotation. [385][389]

## Gabarit

```markdown
# Protocole de double annotation

## Unité annotée

[Phrase, paragraphe, contexte de citation, etc.]

## Guide utilisé

[Chemin vers le guide et numéro de version.]

## Échantillon

- Taille : [n] unités
- Mode de sélection : [aléatoire / stratifié / raisonné]
- Sous-corpus couverts : [description]

## Annotateurs

| Annotateur | Rôle | Formation ou consignes |
|---|---|---|
| A1 | [Rôle] | [Description] |
| A2 | [Rôle] | [Description] |

## Conditions d’annotation

[Préciser indépendance, interface, ordre, contexte fourni, etc.]

## Mesure d’accord

[Accord brut, kappa, alpha ou autre.]

## Résultats

| Catégorie | Accord | Désaccord | Commentaire |
|---|---:|---:|---|
| [Catégorie] | [n ou score] | [n] | [Commentaire] |

## Désaccords

[Décrire les désaccords principaux.]

## Révision du guide

[Indiquer les modifications éventuelles.]

## Décision finale

[Décrire comment l’annotation retenue est produite.]
```

---

## 5.2 Annotation automatique ou LLM

Lorsqu’un outil automatique, un modèle linguistique ou un LLM produit
des annotations, il doit être évalué sur un échantillon de référence ou
par un contrôle humain approprié.

Documenter :

- le modèle ou l’outil ;
- sa version ou date d’accès ;
- les données d’entrée ;
- les prompts ou paramètres, lorsque pertinents ;
- les catégories produites ;
- l’échantillon contrôlé ;
- la référence humaine utilisée ;
- les métriques ou critères de comparaison ;
- les erreurs fréquentes ;
- la décision d’usage : aide exploratoire, préannotation, classification
  finale ou autre.

## Gabarit

```markdown
# Validation de l’annotation automatique

## Outil ou modèle

- Nom : [Nom]
- Version ou date d’accès : [Information]
- Mode d’accès : [API / bibliothèque / interface / local]

## Tâche

[Décrire l’annotation ou classification produite.]

## Données contrôlées

- Taille : [n] unités
- Corpus : [description]
- Référence humaine : [description]

## Méthode de comparaison

[Décrire la comparaison entre sorties automatiques et référence.]

## Résultats

| Catégorie ou métrique | Résultat |
|---|---:|
| [Précision] | [Valeur] |
| [Rappel] | [Valeur] |
| [F1] | [Valeur] |
| [Accord] | [Valeur] |

## Analyse d’erreurs

[Décrire les erreurs fréquentes, cas ambigus et limites.]

## Décision d’usage

[Préciser comment les sorties sont utilisées dans le projet.]
```

> Les usages de LLM et d’IA doivent être documentés dans le journal de
> recherche, ainsi que dans les fichiers de configuration, les protocoles
> et l’article lorsque l’outil intervient dans les méthodes, données,
> annotations ou résultats.

---

# 6. Analyse d’erreurs et contre-exemples

Sous-dossier :

```text
analyses_erreurs/
```

L’analyse d’erreurs permet de comprendre les limites d’une méthode, d’un
modèle, d’une catégorie ou d’une transformation.

Elle ne consiste pas seulement à compter les erreurs. Elle cherche à
répondre à la question :

> **Quelles erreurs se produisent, dans quelles conditions, et quelles conséquences ont-elles pour l’interprétation ?**

## Types d’erreurs possibles

| Type | Exemple |
|---|---|
| Faux positif | Une phrase est classée comme recommandation alors qu’elle ne l’est pas |
| Faux négatif | Une recommandation n’est pas détectée |
| Erreur d’extraction | Une note de bas de page est absente ou mal associée |
| Erreur de segmentation | Deux phrases sont fusionnées ou une phrase est coupée incorrectement |
| Erreur de métadonnée | Genre, date ou langue mal attribué |
| Erreur de catégorie | Un énoncé corrélationnel est classé causal |
| Erreur de pairage | Deux documents non liés sont considérés comme associés |
| Erreur de représentation | Un terme composé est séparé de manière inadéquate |
| Cas ambigu | Le passage relève de plusieurs catégories possibles |
| Contre-exemple | Le passage contredit une tendance interprétée comme générale |

## Gabarit

```markdown
# Analyse d’erreurs

## Résultat ou méthode concernée

[Décrire l’analyse.]

## Échantillon d’erreurs

[n] erreurs ou [n] cas examinés.

## Typologie

| Type d’erreur | Nombre | Exemple | Conséquence |
|---|---:|---|---|
| [Type] | [n] | [Exemple] | [Conséquence] |

## Exemples contextualisés

### Erreur E01

- Document : [ID]
- Segment : [ID]
- Sortie produite : [Valeur]
- Valeur attendue ou interprétation corrigée : [Valeur]
- Explication : [Description]

## Conséquences méthodologiques

[Expliquer si les erreurs imposent une correction, une reprise,
une limitation ou une révision de l’interprétation.]
```

## Contre-exemples

Les contre-exemples sont particulièrement importants pour éviter une
interprétation sélectionnant uniquement les cas favorables à une
hypothèse.

Créer si pertinent :

```text
analyses_erreurs/contre_exemples.md
```

Un contre-exemple peut :

- remettre en cause une généralisation ;
- suggérer une variable non contrôlée ;
- révéler une catégorie insuffisante ;
- montrer un effet de genre, de source ou de période ;
- imposer une interprétation plus prudente ;
- conduire à une nouvelle sous-question.

---

# 7. Tests de sensibilité

Sous-dossier :

```text
tests_sensibilite/
```

Les tests de sensibilité examinent si un résultat change fortement
lorsqu’un choix méthodologique raisonnable varie.

Ils sont particulièrement utiles lorsque l’analyse dépend :

- d’un seuil ;
- d’un filtre ;
- d’une règle de nettoyage ;
- d’une période ;
- d’une taille minimale ;
- d’une unité d’analyse ;
- d’un modèle ;
- d’une graine aléatoire ;
- d’un paramètre de regroupement ;
- d’une stratégie de sélection ;
- d’une représentation textuelle.

## Exemples

| Choix initial | Variation à tester | Question |
|---|---|---|
| Retirer les notes | Conserver les notes séparément | Les notes modifient-elles le résultat ? |
| Segmentation par phrase | Segmentation par paragraphe | La conclusion dépend-elle de l’unité ? |
| Seuil de fréquence = 5 | Seuils = 3 et 10 | Le résultat dépend-il du seuil ? |
| Une période | Période réduite ou élargie | La tendance est-elle temporellement stable ? |
| Corpus complet | Sous-corpus stratifié | Quelques sources dominent-elles le résultat ? |
| Modèle A | Modèle B | Le résultat dépend-il fortement du modèle ? |
| Graine 42 | Plusieurs graines | Les résultats sont-ils stables ? |

## Gabarit

```markdown
# Test de sensibilité

## Résultat concerné

[Décrire le résultat principal ou secondaire.]

## Choix initial

[Décrire le choix ou paramètre retenu.]

## Variante testée

[Décrire la valeur ou procédure alternative.]

## Motivation

[Expliquer pourquoi cette variation est raisonnable.]

## Résultats comparés

| Configuration | Résultat | Écart | Interprétation |
|---|---:|---:|---|
| Initiale | [Valeur] | — | [Description] |
| Variante 1 | [Valeur] | [Écart] | [Description] |
| Variante 2 | [Valeur] | [Écart] | [Description] |

## Conclusion

[Indiquer si le résultat est robuste, sensible ou indéterminé.]
```

> Un résultat sensible n’est pas nécessairement inutilisable. Il doit
> toutefois être interprété avec prudence et cette sensibilité doit être
> expliquée dans l’article.

---

# 8. Reproductibilité et vérification par un pair

Sous-dossier :

```text
reproductibilite/
```

L’objectif est de vérifier qu’un résultat central peut être repris ou
contrôlé à partir des documents disponibles.

La reproductibilité peut être limitée par :

- les droits d’accès aux données ;
- les données non partageables ;
- les dépendances logicielles ;
- les modèles externes ;
- les coûts d’API ;
- les ressources matérielles ;
- les opérations manuelles ;
- les services dont les sorties varient avec le temps.

Ces limites doivent être documentées ; elles ne doivent pas être
dissimulées.

## Vérification minimale attendue

Au moins un résultat central doit être vérifié par :

- un membre de l’équipe autre que la personne l’ayant produit ;
- un pair ;
- l’enseignant ;
- ou une procédure indépendante documentée.

La personne qui vérifie doit pouvoir :

1. identifier les données nécessaires ;
2. installer ou activer l’environnement ;
3. suivre les instructions ;
4. exécuter un script ou appliquer un protocole ;
5. retrouver un tableau, une figure ou un extrait ;
6. signaler les écarts, blocages ou ambiguïtés.

## Gabarit

```markdown
# Rapport de vérification par un pair

## Résultat vérifié

[Nom du tableau, de la figure ou de l’extrait.]

## Personne ayant produit le résultat

[Nom.]

## Personne ayant effectué la vérification

[Nom.]

## Date

[YYYY-MM-DD]

## Données et version

- Version du corpus : [Version]
- Version du dépôt : [Tag ou commit]
- Environnement : [Description]

## Procédure suivie

1. [Étape]
2. [Étape]
3. [Étape]

## Résultat obtenu

[Décrire le résultat retrouvé.]

## Comparaison avec le résultat attendu

- [ ] Identique
- [ ] Différence mineure expliquée
- [ ] Différence importante
- [ ] Impossible à reproduire

## Problèmes rencontrés

[Décrire les problèmes.]

## Corrections apportées

[Décrire les corrections, si nécessaire.]

## Conclusion

[Valider, corriger, limiter ou reprendre le résultat.]
```

Les études sur la reproductibilité en TAL soulignent l’importance de
documenter les données, les séparations de jeux de données, les
paramètres, les versions de logiciels, les métriques et les détails
d’exécution. [383][388]

---

# 9. Vérification du résultat principal

Le fichier suivant est obligatoire :

```text
verification_resultat_principal.md
```

Il synthétise les contrôles essentiels du résultat qui répond le plus
directement à la question de recherche.

## Gabarit

```markdown
# Vérification du résultat principal

## Question de recherche

> [Question principale.]

## Résultat principal

[Décrire le résultat.]

## Données utilisées

| Élément | Description |
|---|---|
| Corpus | [Description] |
| Version | [Version] |
| Sous-corpus | [Description] |
| Unité d’analyse | [Description] |
| Taille | [n documents / segments / paires] |

## Procédure de production

- Script ou protocole : [Chemin]
- Configuration : [Chemin]
- Version du dépôt : [Tag ou commit]
- Environnement : [Chemin]

## Contrôles effectués

| ID | Contrôle | Résultat | Conséquence |
|---|---|---|---|
| V01 | [Contrôle] | [Résultat] | [Conséquence] |
| V02 | [Contrôle] | [Résultat] | [Conséquence] |
| V03 | [Contrôle] | [Résultat] | [Conséquence] |

## Erreurs et contre-exemples

[Décrire les principaux problèmes ou limites.]

## Test de sensibilité

[Indiquer si le résultat dépend d’un choix important.]

## Reprise ou vérification

[Indiquer qui a vérifié le résultat et avec quel résultat.]

## Conclusion de validation

[Indiquer ce que le résultat permet de soutenir et les limites qui
doivent être rappelées dans l’article.]
```

---

# 10. Validation des LLM et outils d’IA

Lorsqu’un LLM ou un outil d’IA participe à l’acquisition, à la
préparation, à l’annotation, à l’analyse ou à l’évaluation, la validation
doit porter sur ses sorties, pas seulement sur le fait qu’il a été
utilisé.

Documenter :

- l’outil, le modèle, la version ou la date d’accès ;
- la tâche réalisée ;
- les données transmises ;
- les prompts ou gabarits de prompts ;
- les paramètres ;
- les sorties produites ;
- la référence humaine ou le contrôle utilisé ;
- les erreurs et cas ambigus ;
- les limites de confidentialité ;
- les limites de reproductibilité ;
- les changements intervenus entre des versions du modèle ;
- la décision finale quant à l’usage de ses sorties.

Les usages de LLM et IA doivent également être consignés dans :

```text
../../journal/journal_de_bord.md
```

et être cohérents avec :

```text
../../article/annexes/declaration_outils_assistance.md
```

---

# 11. Articulation avec les résultats et l’article

| Élément | Emplacement |
|---|---|
| Plan de validation | `chaine/06_validation/plan_validation.md` |
| Contrôles des données | `chaine/06_validation/controles_donnees/` |
| Contrôles de préparation | `chaine/06_validation/controles_preparation/` |
| Accord d’annotation | `chaine/06_validation/controles_annotations/` |
| Erreurs et contre-exemples | `chaine/06_validation/analyses_erreurs/` |
| Tests de sensibilité | `chaine/06_validation/tests_sensibilite/` |
| Reproductibilité | `chaine/06_validation/reproductibilite/` |
| Résultats finaux | `resultats/` |
| Discussion des limites | `article/article_imrad.md` |
| Décisions méthodologiques | `journal/journal_de_bord.md` |

Les résultats de validation peuvent apparaître :

| Type de résultat | Emplacement possible dans l’article |
|---|---|
| Description du contrôle principal | Méthodes |
| Accord ou performance utile à la lecture des résultats | Résultats |
| Erreurs et contre-exemples importants | Résultats ou Discussion |
| Sensibilité des conclusions | Résultats ou Discussion |
| Limites non résolues | Discussion |
| Détails techniques complets | Annexe ou dépôt |

---

# 12. Journal de recherche associé

Les décisions de validation doivent être documentées dans :

```text
../../journal/journal_de_bord.md
```

Le journal doit notamment consigner :

- les contrôles ajoutés ou abandonnés ;
- les erreurs détectées ;
- les corrections de données ;
- les désaccords d’annotation ;
- les changements du guide ;
- les résultats de validation inattendus ;
- les tests de sensibilité ;
- les problèmes de reprise ;
- les révisions de conclusions ;
- les limites reconnues avant la rédaction finale.

## Exemple d’entrée de journal

```markdown
## YYYY-MM-DD — Vérification des annotations de causalité

### Observation

Le contrôle de vingt phrases annotées montre que plusieurs formulations
avec « peut contribuer à » ont été classées tantôt comme corrélations,
tantôt comme causalités conditionnelles.

### Problème

Le guide d’annotation ne précise pas suffisamment le rôle des verbes de
contribution accompagnés d’un modal.

### Options envisagées

1. Conserver les annotations actuelles.
2. Fusionner les catégories.
3. Clarifier la règle et reprendre l’annotation des cas concernés.

### Décision

Nous retenons l’option 3.

### Justification

La distinction entre association et causalité conditionnelle est
directement liée à la question. Une fusion des catégories réduirait la
capacité du corpus à répondre à cette question.

### Contrôle

Deux annotateurs appliquent la règle révisée à un nouvel échantillon.

### Conséquences

Le guide d’annotation est mis à jour. Les résultats précédents sont
recalculés. La version antérieure est conservée dans le registre des
transformations.
```

---

# Checklist avant de passer à l’interprétation

- [ ] Le plan de validation est documenté.
- [ ] Les données et métadonnées ont été contrôlées.
- [ ] Les transformations de préparation ont été vérifiées.
- [ ] Les erreurs d’extraction, de nettoyage ou de segmentation sont documentées.
- [ ] Les annotations manuelles ou automatiques ont été contrôlées.
- [ ] Les désaccords ou erreurs sont analysés.
- [ ] Les cas ambigus et contre-exemples sont examinés.
- [ ] Les paramètres importants ont fait l’objet d’un test de sensibilité lorsque nécessaire.
- [ ] Les dénominateurs, unités et filtres sont vérifiés.
- [ ] Au moins un résultat principal a été repris ou vérifié.
- [ ] Les usages de LLM et IA sont validés et documentés.
- [ ] Les limites non résolues sont explicitées.
- [ ] Les résultats finaux peuvent être reliés aux données et procédures.
- [ ] Les conclusions possibles ont été révisées à la lumière des contrôles.
- [ ] Les résultats sont prêts pour `07_interpretation/`.