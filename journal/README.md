# Journal de recherche

Ce dossier contient le journal de bord du projet.

Le journal documente la recherche **en train de se faire** : questions, décisions, hésitations, essais, erreurs, contrôles, révisions et conséquences méthodologiques.

Il permet de répondre à la question suivante :

> **Comment et pourquoi la démarche de recherche a-t-elle évolué ?**

Le journal n’est ni un relevé d’heures travaillées, ni une copie des messages de commit, ni une autobiographie. Il constitue une trace réflexive et méthodologique des choix qui orientent l’enquête.

---

## Fonction du journal

Le projet comprend trois livrables complémentaires :

| Livrable | Question principale |
|---|---|
| Journal de recherche | Comment et pourquoi les décisions ont-elles été prises ou révisées ? |
| Dépôt versionné | Comment les données, traitements et résultats ont-ils été produits ? |
| Article IMRAD | Que permet de conclure l’enquête ? |

Le journal complète les autres livrables :

- Le **journal** explique la genèse d’une décision.
- Le **dépôt** documente sa mise en œuvre.
- L’**article** explique sa portée scientifique.

### Exemple

Une équipe constate que les notes de bas de page contiennent des justifications pertinentes pour sa question.

| Livrable | Contenu attendu |
|---|---|
| Journal | Pourquoi l’équipe a décidé de conserver les notes, quelles alternatives elle a envisagées et quel contrôle elle a effectué |
| Dépôt | Le protocole ou script utilisé pour extraire les notes, les champs produits et les fichiers de sortie |
| Article | La justification méthodologique de l’inclusion des notes et ses conséquences pour l’interprétation |

---

## Structure du dossier

```text
journal/
├── README.md
├── journal_de_bord.md
├── bilan_reflexif_individuel_[nom].md
└── pieces_jointes/
    ├── [captures ou traces utiles, si nécessaires]
    └── README.md
```

| Fichier | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique la fonction et les règles du journal | Oui |
| `journal_de_bord.md` | Contient les entrées chronologiques du projet | Oui |
| `bilan_reflexif_individuel_[nom].md` | Présente la réflexion finale individuelle | Oui, si les règles du cours le permettent |
| `pieces_jointes/` | Contient des traces utiles, non déjà présentes ailleurs | Selon le contenu |

> Éviter de dupliquer les données, scripts ou résultats dans `journal/`.  
> Le journal doit plutôt créer des liens vers leurs emplacements dans le dépôt.

---

## Fréquence des entrées

Dans ce cours, le journal doit comporter :

- au moins **une entrée hebdomadaire** ;
- une entrée lorsqu’une décision importante est prise ;
- une entrée lorsqu’une difficulté, une erreur ou une limite modifie la démarche ;
- une entrée après un contrôle ou une rétroaction susceptible de faire évoluer le projet.

Les entrées peuvent être brèves. Leur qualité dépend de la clarté du raisonnement et de la traçabilité des décisions, non du nombre de mots.

---

## Structure d’une entrée

Chaque entrée devrait contenir les éléments suivants.

```markdown
## YYYY-MM-DD — [Étape ou titre bref]

### Étape de la recherche
[Ex. : conception du corpus, acquisition, nettoyage, annotation,
analyse, validation, rédaction.]

### Objectif ou problème
[Quel problème cherchons-nous à résoudre ?]

### Observation ou difficulté
[Que s’est-il produit ? Quels éléments justifient cette observation ?]

### Options envisagées
1. [Option 1]
2. [Option 2]
3. [Option 3, si nécessaire]

### Décision prise
[Quelle décision est retenue ?]

### Justification
[Pourquoi ce choix paraît-il le plus adéquat au regard de la question,
du corpus, des contraintes ou des résultats ?]

### Vérification ou contrôle
[Comment ce choix est-il vérifié ? Quel a été le résultat du contrôle ?]

### Conséquences
[Qu’est-ce que cette décision modifie dans le corpus, le protocole,
l’analyse, le calendrier ou l’interprétation ?]

### Traces liées
- [Lien vers le protocole, le script, le résultat ou le commit]
- [Lien vers l’inventaire ou les données concernées]
- [Lien vers une discussion, un tableau ou une figure]
```

---

## Exemple d’entrée

```markdown
## 2026-10-21 — Conservation des notes de bas de page

### Étape de la recherche
Préparation et nettoyage du corpus.

### Objectif ou problème
Déterminer quels éléments textuels doivent être conservés dans
les documents analysés.

### Observation ou difficulté
Lors de la vérification de cinq documents, nous avons constaté que
certaines notes de bas de page contenaient des références, des réserves
méthodologiques et des justifications directement pertinentes pour
notre question sur la mobilisation des sources.

### Options envisagées
1. Retirer toutes les notes, car elles ne font pas partie du texte principal.
2. Conserver toutes les notes dans le texte principal.
3. Extraire les notes dans un champ distinct lié au paragraphe ou à la
   page où elles apparaissent.

### Décision prise
Nous retenons l’option 3 : les notes sont conservées dans un champ
distinct, sans être mélangées automatiquement au texte principal.

### Justification
Cette option conserve une information potentiellement pertinente sans
modifier artificiellement la structure du texte principal. Elle permet
également de distinguer les analyses portant sur le corps du texte de
celles portant sur les notes.

### Vérification ou contrôle
Nous vérifions manuellement l’extraction des notes dans dix documents.
Nous comparons les notes extraites aux documents sources et vérifions
leur association avec le document concerné.

### Conséquences
Le protocole de nettoyage est modifié. Les notes deviennent une variable
documentée dans les métadonnées. Une analyse complémentaire sera
nécessaire pour déterminer si elles sont intégrées au corpus principal
ou étudiées séparément.

### Traces liées
- [Protocole d’extraction](../chaine/04_preparation/01_extraction/README.md)
- [Inventaire du corpus](../donnees/inventaire.csv)
- [Commit correspondant](../../commit/[HASH_DU_COMMIT])
```

---

## Types d’entrées attendues

| Type d’entrée | Exemple |
|---|---|
| Délimitation de la question | Réduction d’un thème trop vaste en phénomène observable |
| Décision sur le corpus | Inclusion ou exclusion d’un genre documentaire |
| Acquisition | Difficulté d’accès, changement de source ou révision du protocole |
| Nettoyage | Conservation ou suppression de titres, notes, références ou tableaux |
| Annotation | Modification d’une catégorie ou clarification d’un cas limite |
| Représentation | Choix entre formes, lemmes, n-grammes, TF-IDF ou embeddings |
| Analyse | Changement de méthode, de paramètre ou d’unité d’analyse |
| Validation | Découverte d’une erreur, analyse d’un contre-exemple ou reproduction d’un résultat |
| Interprétation | Révision d’une conclusion après retour au texte ou discussion d’une limite |
| Rétroaction | Prise en compte d’un commentaire de pair ou de l’enseignant |

---

## Entrées à éviter

Les entrées suivantes sont trop vagues :

```markdown
Nous avons travaillé sur le projet.
```

```markdown
Nous avons nettoyé les données pendant trois heures.
```

```markdown
Le script ne fonctionnait pas.
```

Préférer une formulation documentée :

```markdown
Le script supprimait les notes de bas de page en même temps que
les éléments de navigation. Cette suppression affecte notre objet
d’étude, car plusieurs notes contiennent des justifications.
Nous avons donc séparé l’extraction du texte principal et celle
des notes, puis vérifié dix documents.
```

---

## Travail individuel et travail d’équipe

### Décisions communes

Dans un projet collectif, les décisions concernant le corpus, le code,
les catégories et l’analyse peuvent être inscrites dans un journal commun.

Chaque entrée commune doit identifier les personnes qui y ont contribué :

```markdown
**Personnes impliquées :** [Nom 1], [Nom 2]
```

### Réflexion individuelle

Chaque étudiant doit toutefois conserver une trace de sa contribution,
de ses apprentissages et de ses décisions personnelles.

Le bilan final individuel permet notamment de préciser :

- les tâches auxquelles la personne a contribué ;
- les décisions qu’elle a proposées ou révisées ;
- les difficultés rencontrées ;
- les apprentissages méthodologiques ;
- les limites que la personne considère encore importantes.

---

## Bilan réflexif final

Le syllabus prévoit un bilan individuel de **500 à 800 mots**.

Créer un fichier nommé selon le modèle suivant :

```text
journal/bilan_reflexif_individuel_nom_prenom.md
```

### Structure suggérée

```markdown
# Bilan réflexif individuel

## Mon rôle dans le projet
[Décrire les contributions réelles.]

## Évolution de la question et du corpus
[Expliquer les principales révisions.]

## Décision méthodologique importante
[Présenter une décision, ses alternatives, sa justification et ses effets.]

## Contrôle, erreur ou difficulté significative
[Décrire ce qui a été appris à partir d’un problème ou d’une vérification.]

## Limites restantes
[Identifier honnêtement les limites de l’enquête.]

## Apprentissages transférables
[Expliquer ce qui pourra être réutilisé dans un autre projet.]
```

---

## Liens avec Git

Le journal est versionné dans Git, mais il ne remplace pas les commits.

| Élément | Rôle |
|---|---|
| Commit Git | Indique qu’un fichier ou un ensemble de fichiers a changé |
| Message de commit | Résume techniquement la modification |
| Journal de recherche | Explique la raison méthodologique ou scientifique de la modification |

### Exemple

Message de commit :

```text
Conserve les notes de bas de page dans les données extraites
```

Entrée de journal :

```text
Nous avons conservé les notes dans un champ séparé parce qu’elles
contiennent des justifications pertinentes à notre question. Cette
décision est vérifiée sur un échantillon de dix documents.
```

Le message de commit décrit le changement ; le journal explique la logique de recherche.

---

## Confidentialité et prudence

Le journal ne doit pas contenir :

- mots de passe, clés API ou jetons d’accès ;
- données personnelles non nécessaires au projet ;
- documents sous licence copiés intégralement sans autorisation ;
- commentaires personnels sur des collègues ou étudiants ;
- informations confidentielles sur les sources ou partenaires.

Si une décision concerne une donnée sensible ou non partageable, la
documenter de manière générale :

```markdown
Une source institutionnelle soumise à des conditions d’accès restrictives
a été retenue. Les documents ne sont pas déposés dans Git ; la procédure
d’accès est documentée dans `donnees/README.md`.
```

---

## Utilisation d’outils d’assistance

Si un outil d’assistance, y compris une IA générative, est utilisé de
manière substantielle, le journal doit indiquer :

- l’outil utilisé ;
- l’objectif de son utilisation ;
- la nature de la sortie obtenue ;
- la vérification humaine effectuée ;
- les conséquences éventuelles pour le projet.

Exemple :

```markdown
Un outil d’assistance a été utilisé pour proposer une structure initiale
de script d’extraction. Le code a été relu, adapté et exécuté sur un
échantillon de cinq documents. Les sorties ont été comparées aux sources
avant d’être intégrées au protocole.
```

> Une sortie proposée par un outil ne constitue pas automatiquement
> une observation valide du corpus.

---

## Checklist avant remise

- [ ] Le journal contient une entrée initiale sur l’objet ou la question.
- [ ] Une entrée est présente pour chaque semaine de travail significatif.
- [ ] Les décisions importantes sont expliquées et justifiées.
- [ ] Les contrôles et résultats de vérification sont documentés.
- [ ] Les entrées contiennent des liens vers les fichiers ou résultats pertinents.
- [ ] Les changements de question, corpus ou méthode sont traçables.
- [ ] Les contributions collectives et individuelles sont distinguées.
- [ ] Le bilan réflexif individuel est présent.
- [ ] Aucune information sensible ou secrète n’est déposée.
- [ ] Le journal est cohérent avec le dépôt et l’article IMRAD.

---

## Références méthodologiques

- Schnell, S. (2015). *Ten Simple Rules for a Computational Biologist’s Laboratory Notebook*. PLOS Computational Biology, 11(9), e1004385. https://doi.org/10.1371/journal.pcbi.1004385
- Wilson, G., et al. (2017). *Good enough practices in scientific computing*. PLOS Computational Biology, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510
- ACL Rolling Review. *Responsible NLP Research Checklist*. https://aclrollingreview.org/responsibleNLPresearch/