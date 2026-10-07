# Article scientifique

Ce dossier contient le texte scientifique final du projet, ses sources bibliographiques, ses tableaux et figures intégrés, ainsi que les fichiers nécessaires à sa production.

L’article répond à la question suivante :

> **Que permet de conclure cette enquête sur les langues ou discours de spécialité ?**

Il ne constitue pas un journal chronologique du projet, ni une copie du dépôt de code. Il organise les éléments nécessaires pour que le lecteur comprenne :

1. pourquoi la question mérite d’être étudiée ;
2. comment le phénomène a été rendu observable ;
3. quelles observations ont été produites ;
4. ce que ces observations permettent — ou ne permettent pas — de conclure.

> **Principe :** l’article défend une réponse scientifique proportionnée au corpus, aux méthodes, aux contrôles et aux limites de l’enquête.

---

## Structure du dossier

```text
article/
├── README.md
├── article_imrad.docx
├── article_imrad.pdf
├── bibliographie.bib
├── tableaux/
│   ├── tableau_01_description_corpus.docx
│   └── tableau_02_resultat_principal.docx
├── figures/
│   ├── figure_01_description_corpus.png
│   └── figure_02_resultat_principal.png
└── annexes/
    ├── guide_annotation.md
    ├── checklist_remise.md
    └── declaration_contributions.md
```

| Fichier ou dossier | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Documentation du dossier | Oui |
| `article_imrad.docx` | Version éditable de l’article | Oui |
| `article_imrad.pdf` | Version finale destinée à la remise | Oui |
| `bibliographie.bib` | Références bibliographiques au format BibTeX | Oui |
| `tableaux/` | Tableaux intégrés à l’article | Oui |
| `figures/` | Figures intégrées à l’article | Oui |
| `annexes/` | Documents complémentaires nécessaires à l’évaluation | Oui |

Si le projet utilise LaTeX ou Quarto, ajouter les fichiers pertinents :

```text
article/
├── article_imrad.tex
├── article_imrad.qmd
├── references.bib
├── style.csl
└── Makefile
```

---

## Informations générales

| Élément | Valeur |
|---|---|
| Titre provisoire | [Titre du projet] |
| Type de texte | Article de recherche IMRAD |
| Langue de rédaction | [Français / anglais / autre] |
| Auteurs | [Nom 1], [Nom 2], [Nom 3] |
| Version de remise | [Ex. : v1.0] |
| Date de remise | [YYYY-MM-DD] |
| Version du dépôt | [Tag Git ou hash du commit] |
| Longueur indicative | 3 000 à 4 000 mots, hors résumé, bibliographie et annexes |
| Style bibliographique | [À préciser] |
| Statut | [Brouillon / Révision / Final] |

> Remplacer les éléments entre crochets avant la remise finale.

---

## Résumé du projet

### Objet d’étude

[Décrire le phénomène langagier, discursif ou terminologique étudié.]

### Question de recherche

> **[Insérer la question principale.]**

### Corpus

[Décrire brièvement les documents, les genres, les langues, la période et les unités d’analyse.]

### Méthode

[Décrire les opérations principales : sélection, préparation, annotation, analyse, validation.]

### Résultat principal

[Résumer le résultat central en une ou deux phrases.]

### Conclusion prudente

[Indiquer ce que le projet permet de conclure, avec une réserve importante.]

---

## Structure IMRAD

L’article suit une structure adaptée aux enquêtes empiriques : **Introduction, Méthodes, Résultats, Discussion**.

Cette structure est particulièrement utile pour séparer la raison d’être d’une étude, la manière dont elle a été conduite, les observations produites et leur interprétation. L’IMRAD est courant pour les articles de recherche originale, mais il ne constitue pas le format obligatoire de tous les travaux en TAL ou en sciences du langage. [244]

| Section | Question du lecteur | Contenu attendu |
|---|---|---|
| Introduction | Pourquoi cette question est-elle importante ? | Phénomène, contexte, travaux pertinents, lacune, question et hypothèses éventuelles |
| Méthodes | Comment le phénomène a-t-il été étudié ? | Corpus, sélection, acquisition, préparation, catégories, analyses, validation, accès aux ressources |
| Résultats | Qu’a-t-on observé ? | Résultats descriptifs, analytiques, tableaux, figures, extraits et contrôles nécessaires |
| Discussion | Que signifient les résultats ? | Réponse à la question, interprétation, comparaison avec les travaux, limites et perspectives |

---

# 1. Introduction

## Fonction

L’introduction part d’un problème dans les langues ou discours de spécialité et conduit progressivement à une question de recherche précise.

Elle ne doit pas seulement présenter un domaine général.

Éviter :

```markdown
Les textes médicaux sont importants.
Nous allons utiliser Python pour les analyser.
```

Préférer :

```markdown
Les documents [genre A] et [genre B] remplissent des fonctions
différentes dans la circulation d’un savoir spécialisé. Pourtant,
on connaît encore mal comment [phénomène précis] varie entre eux.
Cette étude examine donc [question].
```

## Éléments attendus

- Le phénomène spécialisé étudié.
- Sa pertinence scientifique, professionnelle ou sociale.
- Les travaux antérieurs pertinents.
- Ce que ces travaux permettent déjà de comprendre.
- La lacune, limite ou question non résolue.
- Le cadre conceptuel retenu.
- La question principale et, si nécessaire, les sous-questions ou hypothèses.
- L’annonce concise de la contribution du projet.

## Structure suggérée

```markdown
## Introduction

### Contexte et phénomène

[Présenter le domaine, les genres ou la pratique spécialisée.]

### Travaux antérieurs

[Présenter les références nécessaires à la compréhension du problème.]

### Problème de recherche

[Identifier ce qui reste à comprendre.]

### Question et contribution

> [Question de recherche.]

Cette étude contribue en [décrire ce qui est effectivement apporté].
```

## Vérifications

- [ ] L’introduction distingue un thème large et un objet précis.
- [ ] La question peut être étudiée avec le corpus annoncé.
- [ ] Les références sont réellement consultées et pertinentes.
- [ ] La contribution annoncée correspond aux résultats réels.
- [ ] Aucun résultat détaillé n’est présenté prématurément.

---

# 2. Méthodes

## Fonction

La section Méthodes explique comment la question a été rendue observable et étudiée.

Elle doit permettre à un lecteur de comprendre :

- les données utilisées ;
- les critères de sélection ;
- les transformations appliquées ;
- les catégories ou variables étudiées ;
- les méthodes et paramètres retenus ;
- les contrôles effectués ;
- les limites méthodologiques importantes.

Elle ne remplace pas la documentation technique détaillée du dépôt, mais elle ne peut pas non plus se réduire à :

```markdown
Le code est disponible sur GitHub.
```

## Structure suggérée

```markdown
## Méthodes

### Question et design de l’étude

[Décrire l’approche : qualitative, quantitative, mixte,
exploratoire, comparative, etc.]

### Corpus

[Décrire le domaine, les genres, langues, période, sources,
taille, unités et sous-corpus.]

### Sélection et acquisition

[Présenter les critères d’inclusion et d’exclusion, les sources
et les procédures d’acquisition.]

### Préparation des données

[Décrire les opérations importantes : extraction, nettoyage,
segmentation, annotation ou représentation.]

### Opérationnalisation

[Définir les catégories, variables ou observables.]

### Analyse

[Décrire les méthodes utilisées, leurs paramètres et leur rapport
à la question.]

### Validation et contrôles

[Présenter les vérifications, analyses d’erreurs, contre-exemples
ou tests de sensibilité.]

### Ressources et reproductibilité

[Indiquer la version du dépôt, le statut des données et la manière
de vérifier les résultats dans les limites autorisées.]
```

## Liens avec le dépôt

| Élément méthodologique | Emplacement détaillé |
|---|---|
| Question et cadre | `chaine/01_question_et_cadre/` |
| Plan de corpus | `chaine/02_conception_du_corpus/` |
| Acquisition | `chaine/03_acquisition/` |
| Préparation | `chaine/04_preparation/` |
| Analyse | `chaine/05_analyse/` |
| Validation | `chaine/06_validation/` |
| Description des données | `donnees/README.md` |
| Environnement logiciel | `environnement/README.md` |
| Paramètres partagés | `configuration/` |

## Vérifications

- [ ] Les critères de corpus sont explicites.
- [ ] Les unités d’analyse sont définies.
- [ ] Les catégories sont opérationnalisées.
- [ ] Les paramètres importants sont indiqués.
- [ ] Les choix de préparation susceptibles d’affecter les résultats sont décrits.
- [ ] Les contrôles sont mentionnés.
- [ ] Les données et le dépôt sont accessibles ou leur accès est documenté.
- [ ] Les limitations de reproductibilité sont honnêtement signalées.

---

# 3. Résultats

## Fonction

La section Résultats présente les observations qui répondent à la question de recherche.

Elle répond à :

> **Qu’a-t-on observé dans le corpus étudié ?**

Elle ne doit pas interpréter longuement les résultats, expliquer les intentions des auteurs ou répéter la revue de littérature.

## Éléments attendus

- Description utile du corpus final.
- Résultat principal répondant directement à la question.
- Résultats secondaires nécessaires à la compréhension.
- Tableaux, figures ou extraits contextualisés.
- Résultats des contrôles nécessaires à l’interprétation.
- Contre-exemples ou cas ambigus lorsque pertinents.
- Dénominateurs, unités d’analyse et effectifs explicites.

## Structure suggérée

```markdown
## Résultats

### Description du corpus final

[Nombre de documents, unités, paires, langues, genres, etc.]

### Résultat principal

[Présenter le résultat répondant directement à la question.]

### Résultats complémentaires

[Présenter seulement les observations nécessaires.]

### Vérification et cas limites

[Présenter les contrôles, erreurs, contre-exemples ou cas ambigus
nécessaires pour apprécier la portée du résultat.]
```

## Règles de rédaction

- Donner les unités et dénominateurs.
- Donner un titre informatif à chaque tableau et figure.
- Commenter ce que montre un tableau au lieu de répéter toutes ses cellules.
- Distinguer résultats planifiés, exploratoires et diagnostiques.
- Garder les résultats exploratoires utiles, mais les identifier comme tels.
- Relier les sorties quantitatives à des extraits contextualisés lorsque nécessaire.
- Ne pas introduire de nouvelles données dans la Discussion.

## Correspondance avec le dépôt

| Résultat dans l’article | Fichier du dépôt |
|---|---|
| Tableau 1 | `resultats/tableaux/tableau_01_description_corpus.csv` |
| Tableau 2 | `resultats/tableaux/tableau_02_resultat_principal.csv` |
| Figure 1 | `resultats/figures/figure_01_resultat_principal.png` |
| Extraits | `resultats/extraits/extrait_01_exemples_et_contre_exemples.md` |
| Validation | `chaine/06_validation/` |

## Vérifications

- [ ] Chaque résultat répond à la question ou rend son interprétation possible.
- [ ] Les unités, effectifs et dénominateurs sont explicites.
- [ ] Les figures correspondent à leurs tableaux sources.
- [ ] Les extraits sont liés à leurs documents et contextes.
- [ ] Les résultats exploratoires sont signalés.
- [ ] Les résultats de validation pertinents sont inclus.
- [ ] Aucun résultat non produit par le dépôt n’est présenté comme résultat du projet.

---

# 4. Discussion

## Fonction

La Discussion répond à :

> **Que signifient les résultats, et jusqu’où permettent-ils d’aller ?**

Elle ne doit pas répéter les résultats ni transformer une association observée en preuve d’une intention, d’une causalité ou d’une généralisation non étudiée.

## Éléments attendus

- Réponse explicite à la question de recherche.
- Interprétation des résultats.
- Articulation avec le cadre conceptuel et les travaux antérieurs.
- Explications concurrentes possibles.
- Forces et limites du corpus et des méthodes.
- Portée réelle des conclusions.
- Perspectives de recherche ou d’amélioration.

## Structure suggérée

```markdown
## Discussion

### Réponse à la question

[Formuler la réponse principale avec prudence.]

### Interprétation

[Expliquer la signification des observations.]

### Mise en relation avec les travaux antérieurs

[Comparer avec les études pertinentes.]

### Explications concurrentes

[Présenter les autres causes ou interprétations possibles.]

### Limites

[Discuter les limites du corpus, des catégories, des méthodes
et de la généralisation.]

### Perspectives

[Identifier ce qu’une étude ultérieure pourrait faire autrement
ou approfondir.]
```

## Formulations prudentes

Préférer :

```text
Dans le corpus étudié, les résultats suggèrent que…
```

```text
Cette différence peut être liée à…
```

```text
L’interprétation doit être limitée par…
```

```text
Ces observations ne permettent pas d’établir…
```

Éviter :

```text
Les auteurs veulent nécessairement…
```

```text
Cette méthode prouve que…
```

```text
Tous les documents de ce domaine…
```

```text
Cette association démontre une relation causale…
```

## Vérifications

- [ ] La Discussion répond réellement à la question.
- [ ] Les conclusions sont proportionnées au corpus.
- [ ] Les limites sont précises et non purement formelles.
- [ ] Les explications concurrentes sont examinées.
- [ ] Les intentions ou causalités non observées ne sont pas affirmées.
- [ ] Les perspectives découlent des limites et résultats réels.

---

# Résumé, titre et mots-clés

## Titre

Le titre doit annoncer le phénomène, le corpus ou la comparaison centrale, sans promettre plus que l’étude ne démontre.

### Exemples de structures

```text
[Phénomène] dans [type de discours] : une analyse de corpus de [documents]
```

```text
De [genre A] à [genre B] : étude des [phénomène] dans un corpus [domaine]
```

```text
[Phénomène] et [fonction discursive] dans [corpus] : une enquête exploratoire
```

Éviter :

```text
Analyse de textes spécialisés avec Python
```

```text
Étude très intéressante sur la santé
```

## Résumé

Le résumé est rédigé après stabilisation du texte principal. Il doit pouvoir être compris sans consulter le dépôt.

### Structure suggérée

```markdown
### Contexte

[Pourquoi le phénomène est-il important ?]

### Objectif

[Quelle question est étudiée ?]

### Méthodes

[Quel corpus, quelle méthode et quels contrôles principaux ?]

### Résultats

[Quel résultat principal ?]

### Discussion ou conclusion

[Que peut-on conclure, avec quelle limite importante ?]
```

## Mots-clés

Prévoir trois à cinq mots-clés :

```text
[langues de spécialité]
[analyse de corpus]
[phénomène étudié]
[domaine]
[méthode, si pertinente]
```

---

# Bibliographie et citations

## Références

La bibliographie complète est conservée dans :

```text
article/bibliographie.bib
```

ou, si BibTeX n’est pas utilisé :

```text
article/references_formatees.md
```

Les références doivent être :

- réellement consultées ;
- citées dans le texte ;
- cohérentes avec le style demandé ;
- complètes ;
- vérifiées avant remise.

Ne pas citer une source simplement parce qu’elle a été suggérée par un outil ou une autre personne sans l’avoir consultée.

## Sources à distinguer

| Type de source | Usage |
|---|---|
| Théorique | Définir les concepts et le cadre |
| Méthodologique | Justifier les décisions de corpus, d’annotation ou d’analyse |
| Empirique | Comparer les résultats à des travaux antérieurs |
| Documentaire | Décrire les sources du corpus |
| Technique | Documenter un outil, modèle ou bibliothèque si nécessaire |

---

# Tableaux, figures et annexes

## Tableaux et figures

Les tableaux et figures doivent être produits à partir de fichiers documentés dans :

```text
resultats/
```

Ne pas modifier manuellement une valeur dans un tableau ou une figure après production sans documenter la modification.

Chaque tableau ou figure doit avoir :

- un numéro ;
- un titre informatif ;
- une légende suffisante ;
- une source ou une procédure de production ;
- une mention des unités et effectifs pertinents.

## Annexes

Les annexes peuvent contenir :

- un guide d’annotation ;
- des détails méthodologiques ;
- une analyse d’erreurs ;
- des résultats supplémentaires ;
- un exemple de protocole ;
- une déclaration de contributions ;
- une déclaration d’utilisation d’outils d’assistance.

Ne pas placer dans les annexes une information nécessaire pour comprendre le résultat principal : elle doit apparaître dans le corps de l’article.

---

# Contributions et responsabilité

Créer :

```text
article/annexes/declaration_contributions.md
```

Exemple :

```markdown
# Déclaration des contributions

| Personne | Contribution |
|---|---|
| [Nom 1] | Conception de la question, revue de littérature, rédaction |
| [Nom 2] | Acquisition du corpus, préparation des données |
| [Nom 3] | Analyse, visualisation, validation et révision |

Tous les auteurs ont relu et approuvé la version finale.
```

Dans un travail collectif, les contributions doivent refléter le travail effectivement réalisé.

---

# Utilisation d’outils d’assistance

Les usages substantiels d’outils d’assistance, y compris des IA génératives, doivent être déclarés dans :

```text
article/annexes/declaration_outils_assistance.md
```

Exemple :

```markdown
# Déclaration d’utilisation d’outils d’assistance

Un outil d’assistance a été utilisé pour :

- proposer une structure initiale de code ;
- suggérer des reformulations de passages ;
- expliquer des messages d’erreur.

Les auteurs ont vérifié les références, le code, les données,
les résultats et les formulations finales. Aucun résultat,
référence ou citation n’a été retenu sans contrôle.
```

Les auteurs demeurent responsables de l’ensemble du contenu soumis.

---

# Version finale et remise

Avant la remise :

1. Créer une version identifiable du dépôt :

```bash
git tag -a v1.0 -m "Version finale remise du projet"
git push origin v1.0
```

2. Inscrire la version dans l’article :

```markdown
Version du dépôt : `v1.0`
Commit correspondant : `[HASH]`
```

3. Vérifier que les tableaux, figures et résultats cités dans l’article correspondent bien à cette version.

4. Produire le PDF final :

```text
article/article_imrad.pdf
```

5. Vérifier la cohérence entre :

```text
article/
resultats/
chaine/
donnees/
environnement/
journal/
```

---

# Checklist avant remise

## Contenu scientifique

- [ ] Le titre décrit le phénomène et le corpus avec précision.
- [ ] Le résumé présente la question, la méthode, le résultat et la limite principale.
- [ ] L’introduction mène à une question étudiable.
- [ ] Les Méthodes rendent le corpus et les choix analytiques compréhensibles.
- [ ] Les Résultats présentent les observations sans surinterprétation.
- [ ] Les tableaux, figures et extraits sont reliés aux fichiers du dépôt.
- [ ] La Discussion répond à la question et délimite la portée des conclusions.
- [ ] Les limites et explications concurrentes sont explicites.

## Traçabilité

- [ ] La version du dépôt est indiquée.
- [ ] Les scripts ou protocoles de production sont accessibles.
- [ ] Les données et conditions d’accès sont documentées.
- [ ] Les résultats peuvent être reliés à leur procédure de production.
- [ ] Les fichiers de l’article correspondent aux résultats finaux.

## Rédaction et éthique

- [ ] Les références sont vérifiées et réellement consultées.
- [ ] Les contributions sont déclarées.
- [ ] Les usages substantiels d’outils d’assistance sont déclarés.
- [ ] Aucun texte protégé, renseignement personnel ou donnée non partageable n’est inclus sans autorisation.
- [ ] Les règles institutionnelles et les consignes de remise sont respectées.
