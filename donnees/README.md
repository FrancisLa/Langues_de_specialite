# Données et corpus

Ce dossier contient la documentation, les métadonnées et, lorsque les conditions de réutilisation le permettent, les données nécessaires à l’enquête.

L’objectif n’est pas seulement de stocker des textes. Il s’agit de rendre le corpus **traçable** :

1. quels documents ont été considérés ;
2. quels documents ont été retenus ou exclus ;
3. d’où ils proviennent ;
4. comment ils ont été acquis ;
5. quelles transformations ils ont subies ;
6. quelles données peuvent être partagées ou doivent rester privées.

> **Principe :** un corpus est un ensemble de documents sélectionnés selon des critères explicites pour répondre à une question de recherche.  
> Il ne s’agit pas d’une simple collection de fichiers.

---

## Structure du dossier

```text
donnees/
├── README.md
├── inventaire.csv
├── dictionnaire_metadonnees.md
├── exclusions.csv
├── sources/
│   ├── README.md
│   └── [documents sources, si partage autorisé]
├── intermediaires/
│   ├── README.md
│   └── [fichiers extraits ou temporaires]
└── preparees/
    ├── README.md
    └── [textes préparés pour l’analyse]
```

| Élément | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Présente les données et leur statut | Oui |
| `inventaire.csv` | Répertorie les documents considérés ou retenus | Oui |
| `dictionnaire_metadonnees.md` | Définit les colonnes de l’inventaire | Oui |
| `exclusions.csv` | Documente les exclusions et leurs raisons | Oui |
| `sources/` | Données originales ou brutes | Selon les droits |
| `intermediaires/` | Fichiers extraits ou temporaires | Souvent non |
| `preparees/` | Données nettoyées, segmentées ou annotées | Selon les droits |

---

## Description générale du corpus

| Élément | Description |
|---|---|
| Titre du corpus | [Nom du corpus] |
| Version | [Ex. : v0.1] |
| Domaine ou activité spécialisée | [Ex. : santé publique, droit du travail, cybersécurité] |
| Phénomène étudié | [Ex. : modalisation, citations, recommandations, variation terminologique] |
| Question de recherche | [Insérer la question principale] |
| Langue(s) | [Ex. : français] |
| Période couverte | [Ex. : 2020–2025] |
| Genres documentaires | [Ex. : articles, rapports, décisions, communiqués, guides] |
| Unité documentaire | [Ex. : article, rapport, page Web, décision] |
| Unité d’analyse | [Ex. : document, section, paragraphe, phrase, paire de documents] |
| Taille du corpus final | [Nombre de documents, de paires, de mots ou de phrases] |
| Date de dernière mise à jour | [YYYY-MM-DD] |
| Responsable(s) | [Nom(s)] |

---

## Question et périmètre

### Objet d’étude

[Décrire le phénomène spécialisé étudié.]

Exemple :

> Le projet examine la reformulation des marques d’incertitude dans le passage d’articles scientifiques à des communiqués institutionnels liés aux mêmes recherches.

### Question de recherche

> **[Insérer la question de recherche.]**

### Population documentaire visée

[Décrire l’ensemble documentaire auquel le corpus tente de se rapporter.]

Exemple :

> Les articles scientifiques et communiqués institutionnels en français publiés entre 2020 et 2025 dans le sous-domaine retenu.

### Corpus effectivement observé

[Décrire ce qui a réellement été retenu et ce qui limite sa couverture.]

Exemple :

> Le corpus final comprend uniquement les paires article–communiqué pour lesquelles un lien explicite ou une correspondance documentée a pu être établi. Il ne représente donc pas l’ensemble de la communication scientifique en santé.

---

## Critères de sélection

### Critères d’inclusion

Un document est retenu lorsqu’il respecte les critères suivants :

- [Critère de domaine ou de sous-domaine]
- [Critère de langue]
- [Critère de période]
- [Critère de genre documentaire]
- [Critère de source]
- [Critère de qualité ou d’accessibilité]
- [Critère de lien avec un autre document, si le projet porte sur des paires]

### Critères d’exclusion

Un document est exclu lorsqu’il :

- [Ne correspond pas au domaine défini]
- [Ne respecte pas la période retenue]
- [N’est pas dans la langue étudiée]
- [Ne contient pas de texte exploitable]
- [Est un doublon]
- [N’est pas accessible légalement ou techniquement]
- [Ne peut pas être relié de manière suffisamment fiable à son document associé]
- [Relève d’un genre non retenu]

Les exclusions sont documentées dans :

```text
donnees/exclusions.csv
```

---

## Provenance des données

| Source | Type de documents | Méthode d’acquisition | Statut d’accès | Date de consultation |
|---|---|---|---|---|
| [Source 1] | [Ex. : articles scientifiques] | [Ex. : export, téléchargement, API] | [Ouvert / institutionnel / restreint] | [YYYY-MM-DD] |
| [Source 2] | [Ex. : communiqués] | [Ex. : téléchargement manuel] | [Ouvert / restreint] | [YYYY-MM-DD] |
| [Source 3] | [Ex. : métadonnées] | [Ex. : API ou catalogue] | [Ouvert] | [YYYY-MM-DD] |

La documentation détaillée de l’acquisition se trouve dans :

```text
chaine/03_acquisition/
```

Chaque document retenu possède un identifiant unique dans :

```text
donnees/inventaire.csv
```

---

## Inventaire des documents

Le fichier `inventaire.csv` constitue le registre principal du corpus.

### Exemple de structure

```csv
id_document;id_paire;titre;source;url;date_publication;date_collecte;langue;genre;sous_corpus;statut;fichier_source;fichier_prepare;conditions_acces
D001;P001;Titre de l'article;Nom de la source;[https://exemple.org/article;2024-01-15;2026-10-07;fr;article;scientifique;retenu;article_001.pdf;article_001.txt;ouvert](https://exemple.org/article;2024-01-15;2026-10-07;fr;article;scientifique;retenu;article_001.pdf;article_001.txt;ouvert)
D002;P001;Titre du communiqué;Nom de l'institution;[https://exemple.org/communique;2024-02-02;2026-10-07;fr;communique;institutionnel;retenu;communique_001.html;communique_001.txt;ouvert](https://exemple.org/communique;2024-02-02;2026-10-07;fr;communique;institutionnel;retenu;communique_001.html;communique_001.txt;ouvert)
```

### Identifiants

| Champ | Rôle |
|---|---|
| `id_document` | Identifiant unique et stable du document |
| `id_paire` | Identifiant commun à des documents associés, si pertinent |
| `fichier_source` | Nom du fichier original ou de son équivalent local |
| `fichier_prepare` | Nom du fichier préparé pour l’analyse |
| `statut` | État du document : retenu, exclu, à vérifier, inaccessible, doublon, etc. |

> Les identifiants ne doivent pas changer après le début de l’analyse, même si le titre ou l’URL d’un document change.

---

## Dictionnaire des métadonnées

La signification détaillée de chaque colonne est documentée dans :

```text
donnees/dictionnaire_metadonnees.md
```

Exemple minimal :

| Colonne | Type | Description | Exemple |
|---|---|---|---|
| `id_document` | Texte | Identifiant unique du document | `D001` |
| `id_paire` | Texte | Identifiant d’une paire documentaire | `P001` |
| `titre` | Texte | Titre fourni par la source | `Titre de l'article` |
| `source` | Texte | Plateforme ou institution d’origine | `Nom de la source` |
| `url` | URL | Adresse de consultation ou de récupération | `https://...` |
| `date_publication` | Date | Date attribuée par la source | `2024-01-15` |
| `date_collecte` | Date | Date de récupération par l’équipe | `2026-10-07` |
| `langue` | Texte | Langue du document | `fr` |
| `genre` | Texte | Type de document | `article` |
| `sous_corpus` | Texte | Groupe analytique du document | `scientifique` |
| `statut` | Texte | État dans le protocole de sélection | `retenu` |
| `conditions_acces` | Texte | Conditions de consultation ou partage | `ouvert` |

---

## Versions des données

Les données sont séparées selon leur statut de transformation.

| Version | Emplacement | Description |
|---|---|---|
| Source | `donnees/sources/` | Fichiers tels qu’acquis ou téléchargés |
| Intermédiaire | `donnees/intermediaires/` | Textes extraits, fichiers temporaires, résultats de conversion |
| Préparée | `donnees/preparees/` | Textes nettoyés, segmentés, annotés ou représentés pour l’analyse |
| Résultat | `resultats/` | Tableaux, figures, extraits et sorties analytiques |

### Règle de conservation

Les données sources ne doivent pas être modifiées directement.

```text
source → extraction → nettoyage → segmentation/annotation → analyse
```

Toute transformation doit être documentée dans :

```text
chaine/04_preparation/
```

---

## Préparation des données

### Transformations réalisées

| Étape | Description | Procédure | Sortie |
|---|---|---|---|
| Extraction | [Ex. : extraction du texte depuis HTML ou PDF] | [Script ou protocole] | [Texte brut] |
| Nettoyage | [Ex. : retrait des menus ou éléments non textuels] | [Script ou protocole] | [Texte nettoyé] |
| Normalisation | [Ex. : encodage UTF-8, espaces, caractères] | [Script ou protocole] | [Texte normalisé] |
| Segmentation | [Ex. : découpage en phrases] | [Outil ou règle] | [Unités d’analyse] |
| Annotation | [Ex. : lemmes, POS, catégories analytiques] | [Modèle ou guide] | [Données annotées] |
| Représentation | [Ex. : TF-IDF, embeddings, n-grammes] | [Script ou configuration] | [Matrice ou vecteurs] |

### Informations conservées

[Indiquer les éléments gardés et les raisons.]

Exemple :

- Le titre est conservé pour identifier le document.
- Les références bibliographiques sont conservées, car le projet étudie les citations.
- Les notes de bas de page sont conservées dans un champ séparé, car elles peuvent contenir des justifications.
- Les menus de navigation, publicités et liens de partage sont retirés.
- Les tableaux sont [conservés / retirés / extraits séparément], selon leur pertinence pour la question.

### Informations perdues ou modifiées

[Indiquer les transformations irréversibles ou susceptibles d’affecter l’interprétation.]

Exemple :

- La mise en page originale du PDF n’est pas conservée dans le fichier texte.
- Certaines notes marginales ou tableaux peuvent ne pas être correctement extraits.
- La segmentation automatique peut introduire des erreurs dans les titres, abréviations ou références.

---

## Contrôle de qualité

### Vérifications prévues

- [ ] Vérification de l’encodage UTF-8.
- [ ] Contrôle des fichiers vides.
- [ ] Détection des doublons.
- [ ] Vérification d’un échantillon de textes extraits.
- [ ] Vérification de la correspondance entre métadonnées et contenu.
- [ ] Contrôle de la relation entre les documents d’une même paire.
- [ ] Vérification des erreurs de segmentation.
- [ ] Contrôle de cohérence des catégories ou annotations.

### Échantillon de contrôle

| Élément contrôlé | Taille de l’échantillon | Procédure | Résultat | Date |
|---|---:|---|---|---|
| [Ex. : texte extrait] | [n] documents | [Lecture manuelle] | [Résultat] | [YYYY-MM-DD] |
| [Ex. : paires de documents] | [n] paires | [Vérification des liens] | [Résultat] | [YYYY-MM-DD] |
| [Ex. : annotations] | [n] unités | [Double annotation] | [Résultat] | [YYYY-MM-DD] |

Les contrôles détaillés sont documentés dans :

```text
chaine/06_validation/
```

---

## Accès, droits et confidentialité

### Statut de partage

Choisir et compléter l’une des situations suivantes.

#### Option A — Données incluses dans le dépôt

Les données peuvent être redistribuées selon :

```text
[Nom de la licence ou conditions d’utilisation]
```

Les documents sont disponibles dans :

```text
donnees/sources/
```

#### Option B — Données non incluses, mais récupérables

Les données ne sont pas incluses dans ce dépôt, mais une personne autorisée peut les récupérer en suivant :

```text
chaine/03_acquisition/
```

L’inventaire et les métadonnées permettent d’identifier les documents nécessaires.

#### Option C — Données non partageables

Les données ne sont pas incluses dans le dépôt pour les raisons suivantes :

- [Droits d’auteur ou licence restrictive]
- [Accès institutionnel]
- [Données sensibles ou personnelles]
- [Autre raison]

Le dépôt fournit néanmoins :

- l’inventaire des documents ;
- les métadonnées ;
- les critères de sélection ;
- les protocoles de traitement ;
- les scripts ou procédures ;
- les résultats partageables ;
- une procédure de vérification partielle.

### Informations à ne jamais déposer

Ne pas ajouter au dépôt :

- mots de passe ;
- clés API ;
- jetons d’accès ;
- données personnelles non autorisées ;
- documents sous licence dont la redistribution est interdite ;
- copies de travail non anonymisées ;
- fichiers contenant des informations d’identification non nécessaires à l’analyse.

Ces éléments doivent être exclus dans `.gitignore`.

---

## Limites du corpus

[Décrire les limites connues.]

Exemples :

- Le corpus ne couvre que les documents accessibles en ligne.
- Certains genres ou institutions sont sous-représentés.
- Les documents sans métadonnées complètes ont été exclus.
- Le corpus porte sur une période limitée.
- Les liens entre documents associés ne sont pas toujours explicitement fournis.
- L’extraction de PDF peut perdre certaines informations de structure.
- Les documents retenus ne permettent pas d’inférer les intentions des auteurs.

> Les limites du corpus ne constituent pas nécessairement des erreurs : elles déterminent la portée des conclusions.

---

## Reproduire ou vérifier les données

### Reproduction complète

[Décrire les conditions nécessaires.]

Exemple :

```text
1. Obtenir un accès institutionnel à la base [nom].
2. Consulter le protocole dans `chaine/03_acquisition/`.
3. Télécharger les documents indiqués dans `inventaire.csv`.
4. Exécuter les scripts dans `chaine/04_preparation/`.
5. Vérifier les sorties à l’aide des contrôles dans `chaine/06_validation/`.
```

### Vérification partielle

Même si les sources ne peuvent pas être redistribuées, une personne peut vérifier :

- les critères de sélection ;
- les métadonnées ;
- la structure du corpus ;
- les scripts ou protocoles ;
- les paramètres d’analyse ;
- les tableaux et figures finaux ;
- les extraits cités dans l’article, dans les limites des droits applicables.

---

## Références liées au corpus

- [Référence décrivant la source ou la base de données]
- [Référence méthodologique sur le corpus]
- [Référence théorique sur le domaine ou le genre]
- [Référence sur les conditions de réutilisation, si nécessaire]

---

## Journal de recherche associé

Les décisions relatives aux données sont consignées dans :

```text
journal/journal_de_bord.md
```

Le journal doit notamment documenter :

- les difficultés d’accès ;
- les critères modifiés ;
- les documents inattendus ;
- les exclusions ;
- les erreurs d’extraction ;
- les changements apportés aux transformations ;
- les contrôles effectués ;
- les conséquences de ces décisions sur la question ou les conclusions.

---

## Checklist avant remise

- [ ] La question de recherche est indiquée.
- [ ] Les critères d’inclusion et d’exclusion sont explicités.
- [ ] Chaque document retenu possède un identifiant stable.
- [ ] L’inventaire des documents est disponible.
- [ ] Les métadonnées sont définies.
- [ ] Les données sources et préparées sont séparées.
- [ ] Les transformations sont documentées.
- [ ] Les droits d’accès et de partage sont précisés.
- [ ] Les données sensibles ou non redistribuables sont exclues du dépôt.
- [ ] Les limites du corpus sont discutées.
- [ ] Le lien entre données, scripts, résultats et article est traçable.