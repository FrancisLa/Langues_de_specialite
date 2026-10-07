# Question de recherche et cadre conceptuel

Ce dossier constitue le point de départ de l’enquête.

Il documente le passage entre :

```text
intérêt général
    ↓
objet d’étude
    ↓
problème de recherche
    ↓
question de recherche
    ↓
cadre conceptuel
    ↓
observables et catégories
```

L’objectif est de répondre aux questions suivantes :

> **Quel phénomène des langues ou discours de spécialité voulons-nous comprendre ?**

> **Pourquoi ce phénomène mérite-t-il une enquête ?**

> **Comment passer d’un concept théorique à des observations possibles dans un corpus ?**

> **Quelles limites devons-nous reconnaître avant de collecter ou d’analyser les données ?**

> **Principe :** une question de recherche ne doit pas être formulée à partir d’un outil disponible.  
> Elle doit guider le choix du corpus, des unités d’analyse, des catégories et des méthodes.

---

## Structure du dossier

```text
01_question_et_cadre/
├── README.md
├── question_recherche.md
├── cadre_conceptuel.md
├── operationnalisation.md
├── bibliographie_initiale.bib
├── bibliographie_initiale.md
└── exemples_preliminaires.md
```

| Fichier | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique le rôle du dossier et les attentes | Oui |
| `question_recherche.md` | Formule l’objet, le problème, la question et le périmètre | Oui |
| `cadre_conceptuel.md` | Définit les notions nécessaires à l’enquête | Oui |
| `operationnalisation.md` | Traduit les concepts en catégories, règles et observables | Oui |
| `bibliographie_initiale.bib` | Contient les références bibliographiques de départ | Oui |
| `bibliographie_initiale.md` | Présente les références commentées ou prioritaires | Oui |
| `exemples_preliminaires.md` | Conserve des exemples initiaux ayant orienté le projet | Oui, si les droits le permettent |

---

# 1. De l’intérêt à la question

## Intérêt général

Un intérêt général constitue un point de départ, mais pas encore une
question de recherche.

Exemples d’intérêts trop généraux :

```text
La médecine.
```

```text
Le droit.
```

```text
La communication scientifique.
```

```text
Les discours politiques.
```

```text
Les textes en cybersécurité.
```

Ces thèmes doivent être délimités par un phénomène, des documents, un
contexte, une période, une langue, une communauté ou une comparaison.

---

## Objet d’étude

L’objet d’étude désigne le phénomène plus précis que le projet souhaite
comprendre.

Exemples :

```text
Les formulations de recommandation dans les guides de santé.
```

```text
Les fonctions des citations dans les rapports d’expertise.
```

```text
La variation des désignations d’une cyberattaque entre documents
techniques et documents de vulgarisation.
```

```text
Les marques d’incertitude dans les articles scientifiques et les
communiqués institutionnels associés.
```

```text
La manière dont des décisions judiciaires répondent aux objections
soulevées par les parties.
```

> L’objet d’étude n’est pas encore une question : il identifie le
> phénomène à comprendre.

---

## Question de recherche

Une question de recherche précise ce que l’enquête cherche à établir,
décrire, comparer ou interpréter.

Elle doit être :

- pertinente pour les langues ou discours de spécialité ;
- assez précise pour orienter une collecte ;
- liée à des documents accessibles ;
- compatible avec le temps et les ressources disponibles ;
- formulée sans présupposer la méthode ou le résultat ;
- susceptible d’être éclairée par des observations empiriques.

### Exemples de formulations

| Objet | Formulation de question |
|---|---|
| Variation terminologique | Comment les désignations de [concept] varient-elles entre [genre A] et [genre B] dans [domaine] ? |
| Positionnement | Comment les auteurs expriment-ils l’incertitude dans [genre] entre [période A] et [période B] ? |
| Médiation scientifique | Comment la force des formulations causales change-t-elle entre des articles et leurs communiqués associés ? |
| Argumentation | Comment les rapports d’expertise mobilisent-ils des sources pour justifier des recommandations ? |
| Genre professionnel | Comment les manuels techniques organisent-ils les consignes de sécurité destinées à différents publics ? |
| Citation | Quelles fonctions discursives remplissent les citations dans [type de document] ? |

### Exemples à éviter ou à réviser

| Formulation | Problème | Révision possible |
|---|---|---|
| Étudier les textes médicaux avec Python | Nomme un domaine et un outil, mais pas un phénomène | Comment les recommandations sont-elles formulées dans des guides médicaux destinés à deux publics ? |
| Faire une analyse avec spaCy | L’outil n’est pas une question | Quels patrons linguistiques caractérisent les consignes de sécurité dans ce corpus ? |
| Voir si les communiqués exagèrent | « Exagèrent » doit être défini ; le corpus et la référence manquent | Comment les formulations causales diffèrent-elles entre les articles et les communiqués associés ? |
| Étudier la littérature grise | Domaine documentaire trop vaste | Comment les rapports d’expertise mobilisent-ils les citations scientifiques dans un sous-domaine défini ? |
| Comparer les mots les plus fréquents | Méthode sans enjeu interprétatif explicite | Quels termes ou expressions distinguent les documents destinés aux experts de ceux destinés au grand public ? |

---

# 2. Distinctions essentielles

Le projet doit distinguer les niveaux suivants.

| Niveau | Question correspondante | Exemple |
|---|---|---|
| Thème | De quoi parle-t-on en général ? | La communication scientifique en santé |
| Objet d’étude | Quel phénomène veut-on comprendre ? | La reformulation des relations causales |
| Question | Que cherche-t-on à savoir ? | Comment la force causale varie-t-elle entre article et communiqué ? |
| Corpus | Quels documents rendent cette question observable ? | Paires article–communiqué explicitement associées |
| Unité d’analyse | À quelle échelle observe-t-on le phénomène ? | Phrase, paragraphe ou paire de documents |
| Observable | Quel indice permet de repérer le phénomène ? | Énoncé corrélationnel, causal conditionnel ou causal direct |
| Méthode | Comment traite-t-on les observations ? | Annotation et comparaison contextualisée |
| Outil | Avec quoi réalise-t-on certaines opérations ? | Tableur, concordancier, script Python ou R |
| Résultat | Qu’a-t-on observé ? | Répartition des catégories dans les deux genres |
| Interprétation | Que permettent de conclure ces résultats ? | Le corpus étudié présente [tendance], sous telles limites |

> Un outil n’est pas une question.  
> Une fréquence n’est pas une interprétation.  
> Un corpus n’est pas automatiquement représentatif de tout un domaine.

---

# 3. Pertinence pour les langues et discours de spécialité

Le projet doit expliciter son lien avec les langues ou discours de
spécialité.

Une langue de spécialité ne se réduit pas à un vocabulaire technique.
L’enquête peut notamment porter sur :

- les objets et pratiques propres à un domaine ;
- les désignations et variations terminologiques ;
- les constructions syntaxiques ou phraséologiques ;
- les relations sémantiques ;
- les degrés de certitude ou de modalisation ;
- les genres discursifs ;
- les fonctions rhétoriques ;
- la structure argumentative ;
- les citations et l’intertextualité ;
- les recommandations, instructions ou prescriptions ;
- les reformulations entre différents publics ;
- la circulation d’un savoir entre communautés spécialisées.

Pour chaque projet, compléter :

```markdown
## Lien avec les langues et discours de spécialité

### Domaine ou activité

[Décrire le domaine, le sous-domaine ou l’activité concernée.]

### Communauté(s) ou public(s)

[Identifier les producteurs, destinataires ou communautés concernés.]

### Genre(s) documentaire(s)

[Identifier les genres étudiés.]

### Phénomène langagier ou discursif

[Décrire le phénomène étudié.]

### Intérêt de l’enquête

[Expliquer pourquoi il est utile de l’étudier dans ce contexte.]
```

---

# 4. Formulation de la question

Le fichier principal de cette étape est :

```text
question_recherche.md
```

Utiliser le gabarit suivant.

```markdown
# Question de recherche

## Titre provisoire

[Donner un titre précis, mais révisable.]

## Intérêt général

[Décrire le domaine ou le problème de départ.]

## Objet d’étude

[Décrire le phénomène spécialisé étudié.]

## Problème de recherche

[Expliquer ce qui reste à comprendre, ce qui varie, ce qui est
mal documenté ou ce qui justifie une enquête.]

## Question principale

> [Formuler une question précise.]

## Sous-questions

1. [Sous-question 1]
2. [Sous-question 2]
3. [Sous-question 3, si nécessaire]

## Hypothèses ou attentes initiales

[Indiquer les hypothèses, attentes ou intuitions.
Si le projet est exploratoire, le préciser explicitement.]

## Corpus envisagé

[Décrire les documents nécessaires de manière provisoire.]

## Unité d’analyse envisagée

[Document, section, paragraphe, phrase, paire de documents, contexte de
citation, tour de parole, etc.]

## Méthodes envisagées

[Décrire les opérations possibles sans les présenter comme déjà fixées.]

## Faisabilité

[Identifier les sources, accès, compétences, contraintes de temps
et difficultés anticipées.]

## Hors périmètre

[Indiquer ce que le projet ne cherche pas à établir.]
```

---

# 5. Cadre conceptuel

Le cadre conceptuel définit les notions qui permettent de poser et
d’interpréter la question.

Le fichier correspondant est :

```text
cadre_conceptuel.md
```

## Gabarit

```markdown
# Cadre conceptuel

## Concept 1 — [Nom du concept]

### Définition de travail

[Définir le concept à partir de sources.]

### Références

- [Référence 1]
- [Référence 2]

### Pertinence pour la question

[Expliquer pourquoi le concept est nécessaire.]

### Difficultés ou ambiguïtés

[Décrire les limites, débats ou sens concurrents.]

***

## Concept 2 — [Nom du concept]

### Définition de travail

[Définition.]

### Références

- [Référence 1]
- [Référence 2]

### Pertinence pour la question

[Explication.]

### Difficultés ou ambiguïtés

[Limites.]
```

## Règles de travail

Le cadre conceptuel doit :

- définir les notions effectivement utilisées ;
- citer les sources ayant servi aux définitions ;
- distinguer les concepts voisins ;
- reconnaître les ambiguïtés importantes ;
- expliquer le rapport entre les concepts et le corpus ;
- éviter de présenter une définition comme universelle lorsqu’elle dépend
  d’une tradition ou d’un domaine.

Le cadre conceptuel ne doit pas devenir une revue de littérature
exhaustive. Il doit fournir les concepts nécessaires pour concevoir
l’enquête.

---

# 6. Opérationnalisation

L’opérationnalisation constitue le passage entre les concepts et les
observations possibles dans le corpus.

Elle répond à la question :

> **Comment reconnaître, identifier ou mesurer ce phénomène dans des documents ?**

Le fichier correspondant est :

```text
operationnalisation.md
```

## Gabarit

```markdown
# Opérationnalisation

| Concept | Définition de travail | Observable | Unité d’analyse | Règle de décision | Exemple | Cas limite |
|---|---|---|---|---|---|---|
| [Concept 1] | [Définition] | [Indice repérable] | [Phrase, document, etc.] | [Règle] | [Exemple] | [Ambiguïté] |
| [Concept 2] | [Définition] | [Indice repérable] | [Unité] | [Règle] | [Exemple] | [Ambiguïté] |
```

## Exemple : formulations causales

| Concept | Définition de travail | Observable | Règle de décision |
|---|---|---|---|
| Corrélation | Relation d’association sans causalité explicite | « X est associé à Y » | Classer comme corrélation si aucun verbe ou mécanisme causal n’est affirmé |
| Causalité conditionnelle | Relation causale exprimée avec réserve | « X pourrait contribuer à Y » | Classer comme causale conditionnelle si un marqueur de possibilité ou condition limite la relation |
| Causalité directe | Relation causale affirmée | « X entraîne Y » | Classer comme causale directe si une relation de production ou cause est explicitement affirmée |

## Questions de contrôle

Avant de stabiliser une opérationnalisation, vérifier :

- [ ] La règle peut-elle être appliquée à des documents réels ?
- [ ] L’unité d’analyse est-elle appropriée ?
- [ ] Les catégories sont-elles mutuellement exclusives ou peuvent-elles coexister ?
- [ ] Les cas ambigus sont-ils prévus ?
- [ ] Un autre lecteur pourrait-il comprendre la règle ?
- [ ] L’observable est-il réellement lié au concept ?
- [ ] Les limites de l’indicateur sont-elles explicites ?
- [ ] Les règles peuvent-elles être testées sur un petit échantillon ?

> Dans une enquête par corpus, les définitions opérationnelles doivent
> être explicites : la tokenisation, la segmentation, les métadonnées,
> les catégories d’annotation et les variables analytiques correspondent
> toutes à des décisions sur ce qui compte comme donnée. [319]

---

# 7. Cadre de l’Introduction

L’Introduction de l’article final peut être préparée dès cette étape.

Le modèle CARS de John Swales constitue un repère utile pour concevoir
une introduction de recherche. Il décrit trois mouvements fréquents :

```text
1. Établir un territoire
2. Établir une niche
3. Occuper cette niche
```

| Mouvement | Fonction dans l’Introduction | Question à traiter |
|---|---|---|
| Établir un territoire | Présenter le domaine et les travaux pertinents | Pourquoi le phénomène est-il important ? |
| Établir une niche | Identifier un problème, une limite, une lacune ou une question | Que reste-t-il à comprendre ? |
| Occuper la niche | Annoncer l’étude, sa question et sa contribution | Que va faire cette enquête ? |

Le modèle ne doit pas être appliqué mécaniquement. Il sert à vérifier que
l’Introduction ne commence pas directement par une méthode ou un outil,
et qu’elle conduit progressivement à une question pertinente. [309][313]

## Gabarit d’Introduction provisoire

```markdown
## Introduction provisoire

### Domaine et phénomène

[Présenter le domaine spécialisé et le phénomène étudié.]

### Travaux et état des connaissances

[Présenter les travaux nécessaires à la compréhension du problème.]

### Problème ou lacune

[Identifier ce qui reste à comprendre ou ce qui motive l’enquête.]

### Question de recherche

> [Formuler la question.]

### Contribution attendue

[Expliquer ce que l’enquête apportera, sans promettre plus que ce que
le corpus et les méthodes pourront permettre.]
```

---

# 8. Bibliographie initiale

La bibliographie initiale contient les références ayant servi à définir
le phénomène, le domaine, le genre, le corpus ou la méthode.

Fichiers associés :

```text
bibliographie_initiale.bib
bibliographie_initiale.md
```

## Structure de `bibliographie_initiale.md`

```markdown
# Bibliographie initiale commentée

## Références théoriques

- [Référence]
  - Utilité : [définition du concept ou cadre théorique]

## Références sur le domaine spécialisé

- [Référence]
  - Utilité : [contexte du domaine, pratiques ou enjeux]

## Références sur le genre ou le discours étudié

- [Référence]
  - Utilité : [fonction, structure ou public du genre]

## Références méthodologiques

- [Référence]
  - Utilité : [corpus, annotation, TAL, statistique, validation]

## Références empiriques comparables

- [Référence]
  - Utilité : [étude voisine ou résultat auquel le projet pourra être comparé]
```

## Références méthodologiques communes

Selon les besoins du projet, les étudiants peuvent consulter les
références communes du cours, notamment :

- Suppe (1998), pour la structure argumentative d’un article scientifique ;
- Swales (1990), pour l’article comme genre et la construction d’une
  introduction ;
- Sollaci et Pereira (2004), pour la structure IMRAD ;
- Mensh et Kording (2017), pour l’organisation argumentative d’un article ;
- Wilson et al. (2017), pour la documentation computationnelle ;
- Arvan, Pina et Parde (2022), pour les limites du partage du code seul ;
- ACL Rolling Review, pour la documentation responsable en TAL.

Ces références ne doivent pas être citées automatiquement dans chaque
article : elles doivent soutenir une proposition ou un choix effectivement
présent dans le projet.

---

# 9. Exemples préliminaires

Le fichier suivant peut conserver les premiers exemples ayant motivé
l’enquête :

```text
exemples_preliminaires.md
```

Ces exemples servent à :

- préciser le phénomène ;
- repérer les difficultés de catégorisation ;
- identifier des cas typiques ou ambigus ;
- vérifier la plausibilité d’une première opérationnalisation ;
- préparer une collecte pilote.

## Gabarit

```markdown
# Exemples préliminaires

## Exemple E01

### Source

[Référence, URL ou description.]

### Extrait

> [Extrait autorisé ou paraphrase.]

### Phénomène observé

[Décrire le phénomène.]

### Pourquoi cet exemple est-il pertinent ?

[Expliquer le lien avec l’objet.]

### Question ou difficulté soulevée

[Décrire l’ambiguïté, le cas limite ou la décision à prendre.]
```

Les exemples ne doivent pas être sélectionnés uniquement parce qu’ils
confirment une intuition initiale. Les contre-exemples et cas ambiguës
sont également utiles.

---

# 10. Faisabilité initiale

Avant de passer à la conception détaillée du corpus, vérifier la
faisabilité du projet.

| Élément | Questions à se poser | État |
|---|---|---|
| Question | Est-elle suffisamment précise et empirique ? | [À compléter] |
| Corpus | Des documents pertinents sont-ils accessibles ? | [À compléter] |
| Langue | Les ressources linguistiques nécessaires existent-elles ? | [À compléter] |
| Période | La période est-elle réaliste ? | [À compléter] |
| Volume | Le nombre de documents est-il gérable ? | [À compléter] |
| Métadonnées | Les informations nécessaires sont-elles disponibles ? | [À compléter] |
| Données | Les conditions d’accès et de réutilisation sont-elles vérifiées ? | [À compléter] |
| Méthode | Les opérations envisagées sont-elles réalisables ? | [À compléter] |
| Validation | Un contrôle des résultats peut-il être prévu ? | [À compléter] |
| Équipe | Les responsabilités peuvent-elles être réparties ? | [À compléter] |

## Décision de faisabilité

```markdown
## Évaluation initiale de faisabilité

### Projet retenu provisoirement

[Décrire la question et le corpus envisagé.]

### Principaux risques

- [Risque 1]
- [Risque 2]
- [Risque 3]

### Solutions ou plans de secours

- [Solution 1]
- [Solution 2]
- [Solution 3]

### Décision

[Maintenir, réduire, modifier ou abandonner le projet.]
```

Toute révision importante doit être documentée dans :

```text
journal/journal_de_bord.md
```

---

# 11. Articulation avec les étapes suivantes

| Étape suivante | Ce que cette étape doit fournir |
|---|---|
| `02_conception_du_corpus/` | Une question, des unités et des critères susceptibles de guider la sélection |
| `03_acquisition/` | Des sources candidates et des conditions d’accès identifiées |
| `04_preparation/` | Des choix initiaux sur les informations à conserver, segmenter ou annoter |
| `05_analyse/` | Des observables, catégories ou comparaisons à examiner |
| `06_validation/` | Des règles, cas ambigus et contrôles à prévoir |
| `07_interpretation/` | Un cadre permettant de délimiter la portée des conclusions |
| `article/` | Une base pour l’Introduction et les Méthodes |

---

# 12. Journal de recherche associé

Les décisions de cadrage sont consignées dans :

```text
journal/journal_de_bord.md
```

Le journal doit notamment documenter :

- les premiers intérêts ou objets envisagés ;
- les questions abandonnées ou réduites ;
- les difficultés de définition ;
- les changements de périmètre ;
- les choix de concepts ;
- les ambiguïtés de catégorisation ;
- les rétroactions reçues ;
- les tests de faisabilité ;
- les raisons ayant conduit à retenir une question plutôt qu’une autre.

Exemple d’entrée de journal :

```markdown
## YYYY-MM-DD — Révision de la question de recherche

### Observation

La formulation initiale portait sur l’ensemble des documents de santé
en français. Les sources accessibles montrent que ce périmètre est trop
large et mélange plusieurs genres et publics.

### Options envisagées

1. Maintenir un corpus large et hétérogène.
2. Limiter le corpus aux articles scientifiques.
3. Comparer des articles scientifiques et leurs communiqués associés
   dans un sous-domaine précis.

### Décision

Nous retenons l’option 3.

### Justification

Cette comparaison permet d’étudier une transformation discursive
précise tout en gardant une relation documentée entre les textes.

### Conséquences

Le plan de corpus doit maintenant définir les critères d’appariement
entre articles et communiqués.
```

---

# Checklist avant de passer à l’étape 02

- [ ] Le domaine ou l’activité spécialisée est délimité.
- [ ] Le phénomène langagier ou discursif est identifié.
- [ ] La question de recherche est formulée.
- [ ] Les sous-questions ou hypothèses sont indiquées, si nécessaires.
- [ ] Les notions centrales sont définies à partir de sources.
- [ ] Les concepts sont distingués de leurs observables.
- [ ] Une première opérationnalisation est proposée.
- [ ] Les unités d’analyse possibles sont identifiées.
- [ ] Les genres documentaires pertinents sont envisagés.
- [ ] Les sources potentielles sont repérées.
- [ ] Les contraintes d’accès, de temps et de compétences sont considérées.
- [ ] Les principaux risques et plans de secours sont documentés.
- [ ] Les décisions importantes sont consignées dans le journal.
- [ ] Le projet peut maintenant passer à la conception détaillée du corpus.