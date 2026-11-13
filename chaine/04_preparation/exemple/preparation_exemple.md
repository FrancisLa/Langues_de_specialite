# Exemple de production étudiante — Préparation des données
## De l’HTML acquis aux textes nettoyés, lemmatisés et vectorisés

Projet : Thèmes et évolution des thèmes d’une revue spécialisée  
Équipe : [noms]  
Date : [date réelle du travail]  
Dossier : `chaine/04_preparation/`

> Statut : exemple pédagogique construit. Il illustre la documentation attendue à partir du README de l’étape 04 et des opérations montrées dans le notebook de la séance 5. Les nombres, dates, versions, échantillons et résultats de contrôle restent à renseigner à partir de votre exécution réelle. Aucun résultat du notebook du professeur ne doit être présenté comme un résultat personnel.

## 1. Votre projet et le rôle du notebook de démonstration

### Question de recherche

> Quels thèmes structurent les articles de recherche de la revue *Argumentation et Analyse du Discours*, et comment leur présence varie-t-elle entre les numéros ?

Une sous-question compare les thèmes des textes intégraux à ceux des titres, résumés et mots-clés. La préparation doit donc produire, pour chaque article, un texte principal, des métadonnées qui permettent de comparer les numéros et une représentation lexicale utilisable plus tard. Elle ne produit pas encore de thèmes.

### Ce que vous reprenez du cours

Le notebook de démonstration vous montre une chaîne simple : lire le tableau de la séance 4, extraire texte et métadonnées du HTML, nettoyer, lemmatiser, compter les formes, calculer un TF-IDF, puis sauvegarder.

Vous écrivez votre propre code, inspiré de ces opérations. Les noms de variables, de colonnes, de fichiers et de dossiers ci-dessous sont des exemples ; ils ne reprennent pas nécessairement ceux du notebook. Vous les définissez dans votre dictionnaire de métadonnées et votre protocole.

### Ce que le notebook ne décide pas à votre place

| Besoin du projet | Opération montrée en classe | Ce que vous devez décider ou adapter |
|---|---|---|
| Texte principal | Paragraphes HTML de certaines classes, sans numéros de paragraphes ni appels de notes | Vérifier ces repères sur vos HTML ; décider du sort des titres de section, tableaux, notes et références |
| Métadonnées | Titre, numéro, date, année, auteurs | Ajouter ce qu’exige votre question, par exemple résumé et mots-clés pour la sous-question |
| Nettoyage | Unicode, apostrophes, espaces | Contrôler ce qui disparaît ; ajouter une règle seulement après observation |
| Unité d’analyse | Un texte par article | Justifier l’article comme unité, ou choisir une unité plus fine |
| Lemmatisation | Modèle français, mots alphabétiques, mots-outils retirés | Justifier le modèle, les filtres et leurs conséquences |
| Représentation | Comptage et TF-IDF en matrices creuses | Fixer les paramètres, conserver l’ordre des lignes et des colonnes |
| Contrôle | Affichages de vérification | Choisir un échantillon, noter les erreurs et décider de valider ou corriger |

Si votre corpus n’est pas composé de pages HTML, certaines opérations ne s’appliquent pas telles quelles. Un PDF, une image ou un export structuré demandent un protocole d’extraction et des contrôles adaptés.

### Progression suivie

```text
sources et inventaire de l’étape 03
    ↓
préparation d’un sous-ensemble pilote
    ↓
contrôle de l’extraction, du nettoyage et de la représentation
    ↓
si le contrôle est concluant : préparation de tout le corpus acquis
    ↓
contrôle global et bilan des manques
    ↓
données préparées pour l’analyse
```

La préparation du pilote peut utiliser les documents déjà acquis. Elle ne prouve pas que les sélecteurs fonctionneront sur toute la revue : la présentation HTML peut varier selon les numéros, les genres ou les années.

## 2. Organisation possible de votre production

```text
chaine/04_preparation/
├── README.md
├── protocole_preparation.md
├── registre_transformations.csv
│
├── 01_extraction/
│   ├── protocole_extraction.md
│   ├── code/
│   │   └── extraction_html.py
│   └── controles/
│       └── controle_extraction.md
│
├── 02_nettoyage/
│   ├── protocole_nettoyage.md
│   ├── regles_nettoyage.md
│   ├── code/
│   │   └── nettoyage.py
│   └── controles/
│       └── controle_nettoyage.md
│
├── 03_segmentation/
│   ├── protocole_segmentation.md
│   └── controles/
│       └── controle_segmentation.md
│
└── 04_annotation_ou_representation/
    ├── protocole_representation.md
    ├── code/
    │   └── representation.py
    └── controles/
        └── controle_representation.md

donnees/
├── inventaire.csv
├── sources/
├── intermediaires/
│   └── documents_extraits.csv
└── preparees/
    ├── corpus_prepare.csv
    ├── vocabulaire.csv
    ├── matrice_comptage.npz
    └── matrice_tfidf.npz

journal/
└── journal_de_bord.md
```

Les noms des scripts sont illustratifs : vous pouvez regrouper le travail dans votre propre notebook, tant que chaque étape reste identifiable. Les sous-dossiers conservent leurs `README.md`, mais ceux-ci peuvent rester brefs et renvoyer aux protocoles.

Le dossier `donnees/sources/` n’est jamais modifié. Les fichiers contenant des textes complets ou des données dérivées sont stockés dans l’espace autorisé ; ils restent hors Git si la redistribution n’est pas vérifiée. Une étape sans produit distinct, comme ici la segmentation en articles, est documentée dans son protocole sans créer de fichier artificiel.

Le guide d’annotation n’est pas créé dans cet exemple, car il n’y a pas d’annotation analytique manuelle. Les lemmes et catégories grammaticales sont produits automatiquement ; ce choix est documenté dans le protocole de représentation.

## 3. `protocole_preparation.md` — exemple renseigné

### Version

- Version : `v0.1-pilote`, puis `v1.0-corpus-acquis` après contrôle.
- Date : [date réelle].
- Personnes responsables : [noms].
- Version du plan : [date, version ou commit].
- Inventaire de départ : [version ou date de `donnees/inventaire.csv`].

### Objectif

Produire, pour chaque article retenu dans l’inventaire, un texte principal nettoyé, des métadonnées liées par un identifiant stable, une version lemmatisée et deux matrices lexicales : comptage et TF-IDF.

### Relation avec la question

La question demande de repérer des thèmes lexicaux et de comparer leur présence entre numéros. L’article est donc retenu comme unité principale, car les numéros sont comparés par ensembles d’articles. La lemmatisation regroupe certaines formes fléchies ; le retrait des mots-outils réduit leur poids dans une représentation destinée à des regroupements thématiques.

### Données d’entrée

| Jeu de données | Emplacement | Version | Description |
|---|---|---|---|
| Inventaire | `donnees/inventaire.csv` | [version] | Documents, statuts et chemins de l’acquisition |
| Sources HTML | `donnees/sources/html/` | [version de l’acquisition] | Pages sources non modifiées |
| Plan et critères | `chaine/02_conception_du_corpus/` | [version] | Périmètre, genres, langues et métadonnées visées |

### Données de sortie

| Jeu de données | Emplacement | Format | Description |
|---|---|---|---|
| Documents extraits | `donnees/intermediaires/documents_extraits.csv` | CSV | Texte principal brut extrait, métadonnées et statut d’extraction |
| Corpus préparé | `donnees/preparees/corpus_prepare.csv` | CSV | Un article par ligne, texte nettoyé, texte lemmatisé et ordre des matrices |
| Vocabulaire | `donnees/preparees/vocabulaire.csv` | CSV | Termes dans l’ordre des colonnes, occurrences et IDF |
| Matrice de comptage | `donnees/preparees/matrice_comptage.npz` | Matrice creuse | Occurrences par article et par terme |
| Matrice TF-IDF | `donnees/preparees/matrice_tfidf.npz` | Matrice creuse | Pondération calculée à partir du comptage |

### Étapes réalisées

1. Extraction du texte principal et des métadonnées à partir des HTML.
2. Nettoyage technique du texte extrait.
3. Choix de l’article comme unité d’analyse.
4. Lemmatisation automatique et sélection des lemmes alphabétiques non vides.
5. Construction des matrices de comptage et TF-IDF.
6. Contrôles par étape et contrôle global.

### Décisions importantes

- Le texte principal contient les paragraphes de texte, de citation et de liste ; il exclut les menus et les éléments de navigation.
- Notes, références, titres de section et tableaux ne sont pas intégrés au texte principal de cette version. Cette exclusion est consignée dans le journal et dans les limites.
- Titre, résumé et mots-clés sont conservés dans des champs séparés pour la sous-question.
- Les majuscules, accents, ponctuations et nombres restent dans le texte nettoyé. Les choix de réduction lexicale sont faits seulement dans la version lemmatisée.
- Aucun filtre propre au sujet ne retire des mots très fréquents comme *discours* ou *argumentation* avant l’analyse.

### Contrôles

Chaque étape a un rapport dans son dossier `controles/`. Un contrôle global vérifie que les lignes, identifiants, métadonnées et matrices restent alignés. Les contrôles automatiques complètent la lecture d’un échantillon ; ils ne la remplacent pas.

### Limites

- La sélection de paragraphes repose sur des classes HTML qui peuvent changer selon les numéros ou les genres.
- Le modèle de lemmatisation peut se tromper, notamment sur les termes spécialisés, les noms propres et les formes ambiguës.
- Les matrices ne conservent pas l’ordre des mots ni la structure des phrases.
- Le TF-IDF dépend du corpus utilisé ; l’ajout ou le retrait d’articles produit une nouvelle version.

## 4. Extraction — `01_extraction/`

### `protocole_extraction.md` — décisions et champs

Le format traité est le HTML conservé à l’étape 03. L’extraction produit un seul fichier intermédiaire, qui reste lié à l’inventaire par `id_document`.

| Champ | Contenu | Remarque de méthode |
|---|---|---|
| `id_document` | Identifiant stable de l’inventaire | Clé de jointure ; jamais recalculée à partir du rang |
| `titre` | Titre de l’article | Si absent, laisser vide et signaler |
| `numero` | Numéro de la revue | Distinct d’un éventuel volume |
| `date_publication_brute` | Date telle qu’elle est trouvée | Ne pas remplacer par la date de collecte |
| `annee` | Année dérivée de la date brute | Vide si la date n’a pas la forme attendue |
| `auteurs` | Noms réunis dans l’ordre rencontré | Ne pas séparer sur les virgules d’un nom |
| `resume_fr`, `mots_cles_fr` | Champs utiles à la sous-question | À ajouter et contrôler dans votre code |
| `texte_principal_brut` | Paragraphes retenus, séparés par une ligne vide | Version avant nettoyage |
| `statut_extraction` | `extrait`, `html_absent`, `texte_vide`, `a_verifier` | Un texte vide n’est jamais une extraction réussie |

Règle d’exclusion de cette version : menus, boutons, numéros de paragraphes et appels de notes ne font pas partie du texte étudié. Les notes et références ne sont pas transmises au texte principal ; elles ne sont pas non plus étudiées dans cette version.

Un document sans HTML récupéré garde sa ligne dans les statuts de préparation. Il n’est pas supprimé silencieusement et il n’entre pas dans les matrices.

### Contrôle de l’extraction

Le rapport `controles/controle_extraction.md` indique l’échantillon réellement lu. Il couvre des numéros différents, un article court, un article long, un article avec citations ou listes, et un cas où une métadonnée est absente. Pour chaque cas, comparer le début et la fin du texte au HTML ou à la page ouverte dans le navigateur.

| Élément vérifié | Résultat | Erreur ou limite | Action |
|---|---|---|---|
| Texte principal : début, fin, citations, listes | [à renseigner] | [par exemple élément manquant ou ajouté] | [corriger, accepter ou documenter] |
| Menus et navigation absents | [à renseigner] | [le cas échéant] | [correction] |
| Texte situé après un appel de note | [à renseigner] | [le cas échéant] | [correction] |
| Titre, numéro, année, auteurs | [à renseigner] | [valeurs absentes ou ambiguës] | [correction] |
| Résumé et mots-clés | [à renseigner] | [langues, absence, doublons] | [correction] |
| Documents sans texte ou métadonnées | [nombre et identifiants] | [cause] | [décision] |

## 5. Nettoyage — `02_nettoyage/`

### `regles_nettoyage.md`

Le nettoyage distingue ce qui fait partie du document étudié (décidé à l’extraction) et ce qui doit être normalisé pour que les outils fonctionnent. Dans cette version, il reste volontairement léger.

| Règle | Opération | Raison | Risque ou précaution |
|---|---|---|---|
| N01 | Normaliser Unicode en NFC | Uniformiser des caractères visuellement identiques | Vérifier accents et caractères spéciaux |
| N02 | Remplacer l’apostrophe courbe par une apostrophe droite | Faciliter l’analyse des élisions | Vérifier citations et noms propres |
| N03 | Remplacer l’espace insécable par une espace | Éviter des découpages artificiels | Contrôler les nombres et signes |
| N04 | Réduire les espaces horizontaux répétés | Normaliser la mise en page | Conserver les fins de paragraphe |
| N05 | Supprimer les espaces au début et à la fin | Normaliser les frontières | Aucune |

Choix explicites : on ne met pas encore le texte en minuscules, on ne retire pas la ponctuation, les chiffres ou les accents, on ne reconstitue pas les mots coupés par un trait d’union et on ne supprime pas les parenthèses. Toute nouvelle règle est testée sur des exemples avant d’être ajoutée, puis consignée avec sa version.

### Règle détaillée — Notes et références hors du texte principal

#### Décision

Les notes de bas de page et les références bibliographiques ne sont pas intégrées au texte principal analysé dans cette version.

#### Justification

La question porte sur les thèmes développés dans le corps des articles. Les références contiennent beaucoup de noms propres, de titres et de lieux de publication qui pourraient dominer certaines fréquences sans répondre directement à la question.

#### Limite

Cette décision empêche d’étudier les notes, les citations bibliographiques et leur rôle argumentatif. Elle peut aussi retirer des explications importantes situées dans les notes. Si la question change, il faudra extraire ces éléments dans des champs distincts ou les réintégrer, puis créer une nouvelle version.

#### Contrôle

Comparer [n] articles contenant beaucoup de notes ou de références avec la page d’origine. Vérifier que le corps de l’article reste complet et que l’exclusion ne retire pas des paragraphes du corpus étudié.

### Contrôle du nettoyage

Lisez des paires avant/après au lieu de vous fier aux seules longueurs. Une réduction de taille signale un changement, pas une erreur. Vérifiez aussi le caractère de remplacement `�`, qui indique un problème d’encodage à examiner.

| Élément vérifié | Résultat | Erreur ou limite | Action |
|---|---|---|---|
| Comparaison avant/après de passages variés | [à renseigner] | [suppression ou déformation éventuelle] | [correction] |
| Accents, guillemets et apostrophes | [à renseigner] | [le cas échéant] | [correction] |
| Négations, chiffres et ponctuation conservés | [à renseigner] | [le cas échéant] | [correction] |
| Documents dont la taille change beaucoup | [identifiants] | [cause] | [décision] |
| Textes identiques ou presque identiques | [identifiants] | [doublon, republication, extraction répétée] | [conserver, signaler ou exclure avec justification] |

## 6. Segmentation — `03_segmentation/`

### `protocole_segmentation.md`

L’unité d’analyse retenue est l’article. Cette unité correspond à la comparaison entre numéros : chaque article compte comme une observation, avec son numéro et son année.

Les paragraphes et les phrases ne sont pas conservés comme unités distinctes dans cette version. Le modèle linguistique peut segmenter le texte pour l’annoter, mais ces frontières ne sont pas utilisées pour l’analyse et ne sont pas exportées.

Conséquences :
- les matrices comparent des articles complets, pas des passages ;
- on ne peut pas retrouver directement une phrase ou un paragraphe à partir d’un poids TF-IDF ;
- une analyse plus fine demanderait de reprendre l’extraction ou la segmentation avec identifiants de paragraphes ou de phrases.

Informations conservées pour chaque unité : `id_document`, numéro, année, titre, auteurs et position dans `corpus_prepare.csv`. Si la question était modifiée pour étudier des passages, des définitions ou des citations, on créerait `donnees/preparees/segments.csv`, avec un identifiant de segment, son ordre et sa position dans le texte nettoyé.

### Contrôle de la segmentation

| Élément vérifié | Résultat | Erreur ou limite | Action |
|---|---|---|---|
| Un `id_document` par article, sans doublon | [à renseigner] | [le cas échéant] | [correction] |
| Numéro et année présents ou signalés | [à renseigner] | [valeurs absentes] | [décision] |
| Articles inclus et exclus de la représentation | [nombre et motifs] | [le cas échéant] | [décision] |

## 7. Annotation et représentation — `04_annotation_ou_representation/`

### Annotation automatique : lemmes et catégories

Un modèle linguistique français annote chaque token : forme, lemme, catégorie grammaticale, traits morphologiques et dépendance. Dans le notebook, ces informations sont d’abord examinées sur un court exemple, puis le corpus est parcouru pour construire une colonne de lemmes.

Pour ce projet, vous pouvez conserver seulement la colonne `texte_lemmatise`, mais vous documentez ce que cette réduction perd : ordre des phrases, catégories grammaticales, négations retirées avec les mots-outils et formes originales. Si vous voulez réutiliser les catégories ou les relations syntaxiques, conservez une table de tokens liée à `id_document`.

Aucun guide d’annotation n’est requis, car aucune annotation analytique manuelle n’est produite. Le contrôle est une analyse d’erreurs sur un échantillon.

### `protocole_representation.md`

| Élément | Décision du projet |
|---|---|
| Unité représentée | Article |
| Texte de départ | Texte nettoyé, avec casse, accents et ponctuation |
| Modèle linguistique | [nom du modèle et version relevés dans l’environnement] |
| Éléments retenus | Lemmes dont le token est alphabétique |
| Éléments filtrés | Ponctuation, espaces, nombres, tokens non alphabétiques et mots-outils du modèle |
| Normalisation | Lemmes en minuscules |
| Comptage | Matrice article × terme, valeurs entières |
| Seuils de fréquence | [aucun, ou valeurs justifiées] |
| N-grammes | Aucun dans cette version |
| Pondération | TF-IDF calculé à partir du comptage, avec normalisation L2 |
| Format | Matrices creuses `.npz`, vocabulaire dans l’ordre des colonnes |
| Ordre des lignes | `ligne_matrice` dans `corpus_prepare.csv` |

Cette configuration est un point de départ. Un vectoriseur peut aussi appliquer ses propres règles de découpage : par exemple, la configuration par défaut de `CountVectorizer` ignore les tokens d’un seul caractère. Vérifiez cet effet et documentez-le, surtout si des abréviations ou des symboles sont pertinents.

Le filtre des mots-outils doit être justifié. Il réduit le poids de mots très fréquents, mais peut retirer des négations, des connecteurs et des marqueurs argumentatifs. Pour un projet sur l’argumentation, un autre choix serait probable.

### Contrôle de la représentation

| Élément vérifié | Résultat | Erreur ou limite | Action |
|---|---|---|---|
| Nombre de lignes égal au nombre d’articles représentés | [à renseigner] | [le cas échéant] | [correction] |
| Ordre des lignes conforme à `ligne_matrice` | [à renseigner] | [le cas échéant] | [correction] |
| Ordre des colonnes conforme à `vocabulaire.csv` | [à renseigner] | [le cas échéant] | [correction] |
| Articles sans lemme retenu | [identifiants] | [cause] | [décision] |
| Termes les plus fréquents | [liste lue et commentée] | [résidus, formes isolées, bruit] | [décision] |
| Lemmes problématiques dans un échantillon de phrases | [exemples] | [erreur de lemme, catégorie ou terme spécialisé] | [correction ou limite] |
| Relecture des matrices et index sauvegardés | [à renseigner] | [le cas échéant] | [correction] |

## 8. `registre_transformations.csv` — exemple

Ce registre trace les opérations et renvoie aux protocoles et contrôles, sans recopier leurs contenus. Les valeurs entre crochets sont à renseigner. Utilisez le séparateur défini dans le README de l’étape.

```csv
id_transformation;date;etape;entree;sortie;procedure;version_code;parametres;responsable;controle;statut;commentaire
T001;[YYYY-MM-DD];extraction;donnees/sources/html/;donnees/intermediaires/documents_extraits.csv;chaine/04_preparation/01_extraction/code/extraction_html.py;[commit];protocole_extraction.md#v0.1;[nom];chaine/04_preparation/01_extraction/controles/controle_extraction.md;a_verifier;[à compléter]
T002;[YYYY-MM-DD];nettoyage;donnees/intermediaires/documents_extraits.csv;donnees/preparees/corpus_prepare.csv;chaine/04_preparation/02_nettoyage/code/nettoyage.py;[commit];regles_nettoyage.md#N01-N05;[nom];chaine/04_preparation/02_nettoyage/controles/controle_nettoyage.md;a_verifier;[à compléter]
T003;[YYYY-MM-DD];annotation;donnees/preparees/corpus_prepare.csv;donnees/preparees/corpus_prepare.csv;chaine/04_preparation/04_annotation_ou_representation/code/representation.py;[commit];lemmes_alphabetiques_sans_mots_outils;[nom];chaine/04_preparation/04_annotation_ou_representation/controles/controle_representation.md;a_verifier;[modèle et version à relever]
T004;[YYYY-MM-DD];representation;donnees/preparees/corpus_prepare.csv;donnees/preparees/matrice_comptage.npz;chaine/04_preparation/04_annotation_ou_representation/code/representation.py;[commit];protocole_representation.md#comptage;[nom];chaine/04_preparation/04_annotation_ou_representation/controles/controle_representation.md;a_verifier;[à compléter]
T005;[YYYY-MM-DD];representation;donnees/preparees/matrice_comptage.npz;donnees/preparees/matrice_tfidf.npz;chaine/04_preparation/04_annotation_ou_representation/code/representation.py;[commit];protocole_representation.md#tfidf;[nom];chaine/04_preparation/04_annotation_ou_representation/controles/controle_representation.md;a_verifier;[recalculé si le corpus change]
```

Quand un contrôle humain est terminé, vous changez le statut ; l’exécution du code ne suffit pas à rendre une transformation `valide`. Si vous refaites la préparation sur le corpus complet, ajoutez de nouvelles lignes plutôt que d’écraser celles du pilote.

## 9. Deux entrées de journal de recherche

### [Date] — Définir le texte étudié et les champs séparés

**Observation.** [Ce que vous avez vu dans les HTML : paragraphes de texte, citations, listes, notes, références, titres, résumés et mots-clés.]

**Options envisagées.**
1. Prendre tout le texte de la page.
2. Retenir seulement les paragraphes du corps de l’article.
3. Retenir le corps et extraire résumé et mots-clés dans des champs distincts.

**Décision illustrée.** Option 3. Notes, références, titres de section et tableaux ne sont pas intégrés à cette version.

**Justification.** La question porte sur les thèmes du corps de l’article et sa sous-question compare le corps aux résumés et mots-clés. Tout le texte de la page ajouterait aussi des éléments de navigation.

**Contrôle.** [Échantillon lu, cas particuliers et résultat.]

**Conséquences.** L’étude des notes et des références n’est pas possible avec cette version. La limite est mentionnée dans le protocole et dans la future section Méthodes.

**Trace.** Lien vers le protocole d’extraction, le contrôle et la version du code.

### [Date] — Choisir la lemmatisation et le filtrage

**Observation.** [Exemples de formes, lemmes, catégories et mots fréquents dans l’échantillon examiné.]

**Options envisagées.**
1. Utiliser les formes originales.
2. Utiliser les lemmes de tous les tokens alphabétiques.
3. Utiliser les lemmes alphabétiques sans mots-outils.

**Décision illustrée.** Option 3 pour la première représentation destinée à un regroupement thématique ; les textes nettoyés restent conservés.

**Justification.** La question porte sur le contenu thématique. La lemmatisation regroupe certaines formes fléchies, et le filtrage réduit l’effet des mots grammaticaux.

**Contrôle.** [Lemmes erronés, termes absents, négations retirées, mots-outils retirés et conséquence observée.]

**Conséquences.** La représentation convient mal à l’étude des négations, connecteurs ou marqueurs argumentatifs. Si la question change, il faut créer une nouvelle version.

**Trace.** Lien vers le protocole de représentation et le contrôle correspondant.

### Si vous utilisez un outil d’IA

Pour une assistance substantielle, notamment pour une expression régulière, un sélecteur ou un script, indiquez dans le journal :
- l’outil et la tâche ;
- les données transmises ;
- le prompt ou la règle ;
- la sortie conservée ou rejetée ;
- les vérifications faites.

Ne transmettez pas à un service externe des textes dont l’usage n’est pas autorisé. Le modèle linguistique local utilisé pour lemmatiser est documenté dans l’environnement et le protocole ; ce n’est pas la même chose qu’une transmission de données à un service externe.

## 10. Traçabilité et préparation à l’analyse

Chaque résultat futur doit pouvoir être relié à son origine :

```text
résultat
    ↓
script ou protocole d’analyse
    ↓
matrice, vocabulaire et corpus_prepare.csv
    ↓
transformations du registre
    ↓
id_document
    ↓
donnees/inventaire.csv
    ↓
donnees/sources/html/[id_document].html
```

À la fin de cette étape, l’analyse thématique pourra utiliser les matrices pour comparer des articles ou des numéros, puis revenir aux textes pour interpréter les résultats. Cet exemple s’arrête avant cette étape : les fréquences, poids TF-IDF et regroupements ne sont pas des thèmes avant interprétation et validation.

La section Méthodes de l’article devra décrire seulement les transformations qui affectent l’interprétation : texte retenu, exclusions, nettoyage, modèle, filtres, représentation, contrôles et limites. Le détail vit dans les protocoles et le registre ; vous le résumez sans le recopier.

### Checklist de la production

- [ ] Votre code est inspiré de la démonstration, mais adapté et expliqué pour votre projet.
- [ ] Les sources restent inchangées et séparées des données intermédiaires et préparées.
- [ ] Le protocole général renvoie au plan et à l’inventaire sans recopier leurs contenus.
- [ ] Les éléments conservés, séparés ou exclus sont justifiés.
- [ ] Les métadonnées utiles restent liées aux documents par un identifiant stable.
- [ ] Les règles de nettoyage sont testées sur des exemples avant d’être appliquées.
- [ ] L’unité d’analyse est justifiée et ses conséquences sont documentées.
- [ ] Les choix de lemmatisation, de filtres et de pondération sont expliqués.
- [ ] Les matrices sont accompagnées de leur vocabulaire et de l’ordre des documents.
- [ ] Les contrôles utilisent un échantillon réellement lu, avec erreurs et décisions.
- [ ] Le registre n’indique pas `valide` avant la fin d’un contrôle.
- [ ] Les décisions importantes et les usages substantiels d’IA sont consignés dans le journal.
- [ ] Les données contenant des textes complets ne sont pas envoyées dans Git sans droit de redistribution.
