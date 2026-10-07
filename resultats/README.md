# Résultats

Ce dossier contient les sorties produites par l’analyse et retenues comme éléments de preuve dans le projet.

Les résultats peuvent prendre différentes formes :

- tableaux descriptifs ou statistiques ;
- figures et visualisations ;
- listes de documents, segments ou unités repérées ;
- concordances et extraits contextualisés ;
- résultats d’annotation ;
- résultats de classification, regroupement ou comparaison ;
- analyses d’erreurs ;
- résultats de validation ou de reproduction.

L’objectif de ce dossier est de répondre à la question suivante :

> **Quels résultats ont été produits, par quelle procédure, à partir de quelles données et comment peuvent-ils être interprétés ?**

> **Principe :** une figure, un tableau ou une sortie de modèle n’est pas une conclusion en soi.  
> Chaque résultat doit pouvoir être relié à une question, des données, une procédure, un contrôle et une interprétation.

---

## Structure du dossier

```text
resultats/
├── README.md
│
├── tableaux/
│   ├── README.md
│   ├── tableau_01_description_corpus.csv
│   ├── tableau_02_resultat_principal.csv
│   └── tableau_03_validation.csv
│
├── figures/
│   ├── README.md
│   ├── figure_01_description_corpus.png
│   ├── figure_02_resultat_principal.png
│   └── figure_03_validation.png
│
├── extraits/
│   ├── README.md
│   ├── extrait_01_exemples_typiques.md
│   ├── extrait_02_contre_exemples.md
│   └── extrait_03_erreurs_annotation.md
│
└── provisoires/
    ├── README.md
    └── [sorties temporaires ou exploratoires]
```

| Dossier | Contenu | Versionné dans Git ? |
|---|---|:---:|
| `tableaux/` | Résultats tabulaires finaux ou nécessaires à l’article | Oui |
| `figures/` | Figures retenues dans l’article ou utiles à la vérification | Oui |
| `extraits/` | Exemples contextualisés, contre-exemples et analyses qualitatives | Oui, sous réserve des droits |
| `provisoires/` | Sorties exploratoires, essais ou fichiers non retenus | En général non |
| `README.md` | Documentation du dossier | Oui |

Les résultats provisoires peuvent être exclus du dépôt avec `.gitignore` :

```gitignore
/resultats/provisoires/
/resultats/tableaux/provisoires/
/resultats/figures/provisoires/
```

Ne pas ignorer automatiquement tous les fichiers `.png`, `.csv` ou `.pdf`, car les résultats finaux doivent normalement être conservés.

---

## Résumé des résultats principaux

| Identifiant | Résultat | Question associée | Type | Statut |
|---|---|---|---|---|
| R01 | [Titre bref du résultat principal] | [Question ou sous-question] | Tableau / figure / extrait | Final |
| R02 | [Titre bref du deuxième résultat] | [Question ou sous-question] | Tableau / figure / extrait | Final |
| R03 | [Résultat de validation ou contrôle] | [Question méthodologique] | Tableau / figure / note | Final |
| R04 | [Résultat exploratoire] | [Question secondaire] | Sortie provisoire | Exploratoire |

Exemple :

| Identifiant | Résultat | Question associée | Type | Statut |
|---|---|---|---|---|
| R01 | Répartition des formulations causales dans les deux genres | Comment les formulations changent-elles entre article et communiqué ? | Tableau | Final |
| R02 | Exemples de renforcement causal dans les communiqués | Comment interpréter les changements repérés ? | Extraits contextualisés | Final |
| R03 | Contrôle manuel d’un échantillon annoté | Les catégories ont-elles été appliquées de manière cohérente ? | Tableau de validation | Final |

---

## Convention de nommage

Tous les résultats doivent porter un nom stable, informatif et cohérent.

### Format recommandé

```text
[type]_[numero]_[description_courte].[extension]
```

Exemples :

```text
tableau_01_description_corpus.csv
tableau_02_repartition_categories.csv
tableau_03_controle_annotation.csv

figure_01_repartition_documents.png
figure_02_comparaison_genres.png
figure_03_analyse_erreurs.png

extrait_01_cas_typiques.md
extrait_02_contre_exemples.md
extrait_03_cas_ambigus.md
```

Éviter les noms vagues ou instables :

```text
resultat_final.csv
figure_finale_v2.png
test.png
graphique_nouveau.png
tableau_bon.csv
```

Si une nouvelle version d’un résultat doit être conservée temporairement :

```text
figure_02_comparaison_genres_v01.png
figure_02_comparaison_genres_v02.png
```

Une fois le résultat final retenu, utiliser un nom stable :

```text
figure_02_comparaison_genres.png
```

La version exacte du dépôt ayant produit le résultat final doit être indiquée dans le README du sous-dossier, dans l’article ou dans le journal.

---

## Traçabilité des résultats

Chaque résultat final doit être relié à :

1. une question de recherche ou sous-question ;
2. un corpus ou sous-corpus identifié ;
3. une procédure d’analyse ;
4. une version des données ;
5. une version du code ou du protocole ;
6. un contrôle ou une limite pertinente ;
7. une interprétation dans l’article.

### Tableau de traçabilité

| Résultat | Données | Procédure | Validation | Article |
|---|---|---|---|---|
| `tableau_01_description_corpus.csv` | `donnees/inventaire.csv` | `chaine/03_acquisition/` | Vérification des métadonnées | Méthodes |
| `tableau_02_resultat_principal.csv` | `donnees/preparees/` | `chaine/05_analyse/` | `chaine/06_validation/` | Résultats |
| `figure_02_resultat_principal.png` | `tableau_02_resultat_principal.csv` | `chaine/05_analyse/` | Lecture de cohérence | Résultats |
| `extrait_01_exemples_typiques.md` | Corpus préparé | Sélection documentée | Retour au document source | Résultats / Discussion |

---

## Tableaux

Les tableaux sont stockés dans :

```text
resultats/tableaux/
```

Chaque tableau doit comporter :

- un titre informatif ;
- des noms de colonnes explicites ;
- des identifiants de documents, de paires ou d’unités lorsque pertinent ;
- une date ou une version de production ;
- un lien vers la procédure qui l’a généré ;
- une indication de son statut : descriptif, analytique, validation ou exploratoire.

### Format recommandé pour un README de tableau

Créer un fichier associé si le tableau est complexe :

```text
resultats/tableaux/tableau_02_repartition_categories.md
```

Exemple :

```markdown
# Tableau 02 — Répartition des catégories par genre documentaire

## Question associée

Comment les catégories [nom des catégories] se répartissent-elles
dans les documents de type [genre A] et [genre B] ?

## Données utilisées

- Version du corpus : `v0.3`
- Sous-corpus : [description]
- Unité d’analyse : [phrase / paragraphe / document]
- Nombre d’unités analysées : [n]

## Procédure

Script ou protocole :

```text
chaine/05_analyse/produire_tableau_02.py
```

## Colonnes

| Colonne | Description |
|---|---|
| `genre` | Type documentaire |
| `categorie` | Catégorie analytique |
| `n` | Nombre d’unités |
| `proportion` | Proportion dans le sous-corpus |
| `version_corpus` | Version des données utilisée |

## Contrôle

[Ex. : les totaux ont été vérifiés par rapport à l’inventaire
et à la sortie d’annotation.]

## Limites

[Ex. : les proportions dépendent de la segmentation automatique
et des critères de catégorisation.]

## Utilisation dans l’article

- Article IMRAD, section Résultats.
- Tableau [numéro] dans la version finale.
```

---

## Figures

Les figures sont stockées dans :

```text
resultats/figures/
```

Chaque figure doit être accompagnée de son fichier de données ou du tableau qui l’a produite.

### Principes de production

Une figure doit :

- avoir un titre ou une légende complète ;
- identifier les unités, variables et groupes comparés ;
- indiquer les effectifs lorsque pertinent ;
- utiliser des couleurs lisibles et accessibles ;
- éviter de masquer les données importantes ;
- ne pas exagérer une différence par le choix d’échelle ;
- être liée à une question de recherche explicite.

### Convention de formats

| Format | Usage recommandé |
|---|---|
| `.png` | Figure matricielle ou capture destinée à l’article |
| `.svg` | Figure vectorielle modifiable |
| `.pdf` | Figure destinée à un document scientifique |
| `.csv` | Données sous-jacentes à une figure |
| `.py` / `.R` | Script de production de la figure |

Conserver si possible :

```text
figure_02_comparaison_genres.png
figure_02_comparaison_genres.csv
produire_figure_02.py
```

### Exemple de README de figure

```markdown
# Figure 02 — Comparaison des catégories entre genres

## Question associée

[Question ou sous-question.]

## Description

Cette figure compare la proportion de [catégorie] dans les documents
de type [genre A] et [genre B].

## Données sources

```text
resultats/tableaux/tableau_02_repartition_categories.csv
```

## Procédure de production

```text
chaine/05_analyse/produire_figure_02.py
```

## Version

- Corpus : `v0.3`
- Dépôt : commit `[HASH]`
- Date : `[YYYY-MM-DD]`

## Interprétation prudente

[Ex. : la figure décrit une différence observée dans le corpus étudié.
Elle ne permet pas, à elle seule, d’attribuer la différence à une
intention des auteurs.]
```

---

## Extraits et retour aux textes

Les résultats quantitatifs ou automatiques doivent être examinés à partir des textes dont ils proviennent.

Les extraits sont stockés dans :

```text
resultats/extraits/
```

Chaque extrait doit comprendre :

- un identifiant de document ;
- un identifiant de segment ou d’unité ;
- le texte ou un extrait autorisé ;
- les métadonnées pertinentes ;
- la catégorie ou le résultat associé ;
- un lien vers le document source ou sa référence ;
- une justification de son choix.

### Exemple : `extrait_01_cas_typiques.md`

```markdown
# Extraits 01 — Cas typiques de [phénomène étudié]

## Critère de sélection

Les extraits suivants illustrent des cas considérés comme typiques
de la catégorie [nom]. Ils sont sélectionnés après retour au texte
et vérification du contexte immédiat.

***

## Extrait E001

| Champ | Valeur |
|---|---|
| Document | `D014` |
| Paire | `P007` |
| Genre | `communique` |
| Catégorie | `causalite_directe` |
| Segment | `S023` |
| Source | [Référence ou URL] |

> [Extrait autorisé ou paraphrase, selon les droits.]

### Justification

[Expliquer pourquoi cet extrait illustre la catégorie et comment
il contribue à répondre à la question.]

### Limite ou réserve

[Indiquer tout élément contextuel qui complique l’interprétation.]
```

### Contre-exemples et cas ambigus

Les contre-exemples sont particulièrement importants. Ils permettent de vérifier que l’analyse ne sélectionne pas uniquement les exemples favorables à l’hypothèse.

Créer, si pertinent :

```text
resultats/extraits/extrait_02_contre_exemples.md
resultats/extraits/extrait_03_cas_ambigus.md
resultats/extraits/extrait_04_erreurs_modele.md
```

> Un résultat robuste ne consiste pas uniquement à présenter les cas les plus spectaculaires ; il doit aussi examiner les cas qui résistent à l’interprétation initiale.

---

## Résultats exploratoires

Les résultats exploratoires peuvent être utiles au raisonnement, mais doivent être distingués des résultats présentés comme répondant directement à la question de recherche.

| Type | Description | Statut dans l’article |
|---|---|---|
| Confirmatoire | Produit selon une procédure définie avant l’analyse principale | Peut soutenir une réponse principale |
| Exploratoire | Produit après observation des données ou pour générer des hypothèses | Doit être explicitement présenté comme exploratoire |
| Diagnostic | Sert à comprendre une erreur, une distribution ou un problème technique | Peut figurer dans les Méthodes, Résultats ou annexes |
| Provisoire | Essai non retenu ou sortie temporaire | Ne doit pas être présenté comme résultat final |

Les résultats exploratoires sont conservés, si utile, dans :

```text
resultats/provisoires/
```

Ils doivent être documentés dans le journal de recherche s’ils ont influencé une décision méthodologique.

---

## Validation des résultats

Les résultats doivent être contrôlés selon des méthodes adaptées à la question et aux outils employés.

### Exemples de contrôles

| Type de résultat | Contrôle possible |
|---|---|
| Métadonnées | Vérification manuelle d’un échantillon de documents |
| Extraction de texte | Comparaison du texte extrait avec la source |
| Annotation manuelle | Double annotation, discussion des désaccords |
| Annotation automatique | Analyse d’erreurs sur un échantillon |
| Classification | Jeu de validation, mesures de performance, inspection des erreurs |
| Regroupement | Lecture des segments, cohérence des groupes, sensibilité aux paramètres |
| Statistiques descriptives | Vérification des dénominateurs, totaux et doublons |
| Figure | Comparaison avec le tableau source et vérification des échelles |
| Extraits | Retour au contexte du document source |

Les résultats de validation sont stockés dans :

```text
resultats/tableaux/
resultats/figures/
resultats/extraits/
```

et documentés plus largement dans :

```text
chaine/06_validation/
```

---

## Limites d’interprétation

Chaque résultat doit être interprété à la lumière de ses limites.

Exemples :

- Une fréquence élevée ne prouve pas qu’un terme est central sur le plan conceptuel.
- Une cooccurrence ne prouve pas une relation causale ou argumentative.
- Une différence entre deux sous-corpus peut dépendre du genre, de la période, de la source ou de la taille des corpus.
- Une classification automatique peut contenir des erreurs.
- Un extrait illustratif ne représente pas nécessairement l’ensemble du corpus.
- Une association observée ne permet pas automatiquement d’inférer une intention, une cause ou une généralisation hors du corpus.

Les limites méthodologiques générales sont discutées dans :

```text
article/article_imrad.md
```

et les décisions ayant mené aux résultats sont consignées dans :

```text
journal/journal_de_bord.md
```

---

## Correspondance avec l’article IMRAD

| Élément de l’article | Éléments du dépôt |
|---|---|
| Méthodes | Protocoles dans `chaine/`, inventaire dans `donnees/`, environnement dans `environnement/` |
| Résultats | Tableaux, figures et extraits dans `resultats/` |
| Discussion | Limites, contrôles, contre-exemples et résultats exploratoires |
| Annexes | Résultats supplémentaires, guide d’annotation, analyses d’erreurs |

Chaque tableau, figure ou extrait cité dans l’article doit être identifiable dans ce dossier.

Exemple de renvoi dans l’article :

```markdown
La répartition des catégories est présentée au tableau 2
(`resultats/tableaux/tableau_02_repartition_categories.csv`).
Des extraits contextualisés sont fournis dans
`resultats/extraits/extrait_01_cas_typiques.md`.
```

---

## Reproduire un résultat central

Indiquer ici une procédure minimale pour produire ou vérifier le résultat principal.

### Exemple

```bash
# Depuis la racine du projet

# 1. Activer l’environnement
source .venv/bin/activate

# 2. Produire le tableau principal
python chaine/05_analyse/produire_tableau_02.py

# 3. Produire la figure associée
python chaine/05_analyse/produire_figure_02.py
```

Fichiers attendus :

```text
resultats/tableaux/tableau_02_repartition_categories.csv
resultats/figures/figure_02_comparaison_categories.png
```

Vérification :

```text
- Le tableau doit contenir [nombre] lignes.
- Les proportions doivent totaliser [valeur attendue] dans chaque groupe.
- La figure doit correspondre aux valeurs du tableau.
- Les extraits associés doivent être vérifiés dans les documents sources.
```

---

## Checklist avant remise

- [ ] Chaque résultat final possède un nom stable et informatif.
- [ ] Chaque tableau ou figure est relié à une procédure d’analyse.
- [ ] Les données sources de chaque figure sont conservées.
- [ ] Les dénominateurs et unités d’analyse sont explicités.
- [ ] Les résultats exploratoires sont distingués des résultats principaux.
- [ ] Des extraits contextualisés accompagnent les analyses lorsque pertinent.
- [ ] Les contre-exemples, cas ambigus ou erreurs sont examinés.
- [ ] Les contrôles de qualité sont documentés.
- [ ] Les fichiers finaux correspondent à la version du dépôt évaluée.
- [ ] Les résultats sont cohérents avec l’article IMRAD.
- [ ] Aucun document soumis à des restrictions de diffusion n’est publié sans autorisation.