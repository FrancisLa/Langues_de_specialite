# Interprétation et discussion

Ce dossier contient les documents permettant de transformer les résultats
validés en une réponse scientifique prudente à la question de recherche.

L’interprétation ne consiste pas à répéter les résultats. Elle consiste à
expliquer leur signification au regard :

- de la question de recherche ;
- du cadre conceptuel ;
- du corpus effectivement étudié ;
- des méthodes employées ;
- des contrôles réalisés ;
- des travaux antérieurs ;
- des limites reconnues.

```text
question de recherche
    ↓
résultats validés
    ↓
retour aux textes et aux contextes
    ↓
interprétations possibles
    ↓
explications concurrentes
    ↓
limites
    ↓
réponse prudente
    ↓
discussion dans l’article
```

L’objectif est de répondre aux questions suivantes :

> **Que montrent les résultats au sujet de la question de recherche ?**

> **Quelles interprétations sont soutenues par les données ?**

> **Quelles interprétations dépasseraient les données disponibles ?**

> **Quels contre-exemples, limites ou explications concurrentes doivent être pris en compte ?**

> **Quelle est la portée réelle de la conclusion ?**

> **Principe :** les données établissent ce qui a été observé dans un
> corpus et selon une méthode donnée. L’interprétation explique ce que ces
> observations peuvent raisonnablement signifier, sans attribuer aux
> données une portée qu’elles ne possèdent pas.

---

## Relation avec les autres étapes

Cette étape interprète les résultats produits dans :

```text
../05_analyse/
```

et contrôlés dans :

```text
../06_validation/
```

Elle s’appuie sur :

```text
../01_question_et_cadre/
../../resultats/
../../donnees/
```

Elle fournit les éléments nécessaires à :

```text
../../article/article_imrad.md
```

Les hésitations, alternatives, révisions de conclusions et décisions
importantes sont consignées dans :

```text
../../journal/journal_de_bord.md
```

---

## Structure du dossier

```text
07_interpretation/
├── README.md
├── synthese_resultats.md
├── interpretation_principale.md
├── contre_exemples.md
├── explications_concurrentes.md
├── limites.md
├── implications.md
├── perspectives.md
├── discussion_preliminaire.md
└── tableau_inferences.md
```

| Fichier | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique l’étape d’interprétation | Oui |
| `synthese_resultats.md` | Rassemble les résultats nécessaires à la réponse | Oui |
| `interpretation_principale.md` | Formule et justifie l’interprétation centrale | Oui |
| `contre_exemples.md` | Documente les cas qui résistent à l’interprétation initiale | Oui |
| `explications_concurrentes.md` | Examine les autres explications possibles | Oui |
| `limites.md` | Décrit les limites du corpus, de la méthode et de la portée | Oui |
| `implications.md` | Discute les conséquences théoriques, pratiques ou méthodologiques | Oui |
| `perspectives.md` | Identifie les travaux ou données nécessaires à la suite | Oui |
| `discussion_preliminaire.md` | Sert de brouillon pour la Discussion de l’article | Oui |
| `tableau_inferences.md` | Distingue observations, interprétations et conclusions | Oui |

Tous les fichiers ne sont pas obligatoires dans chaque projet. Toutefois,
les contre-exemples, explications concurrentes et limites doivent être
pris en compte, même si leur discussion est intégrée à un fichier unique.

---

# 1. Distinguer les niveaux d’inférence

L’interprétation exige de distinguer ce qui est observé de ce qui est
inféré.

| Niveau | Question | Exemple |
|---|---|---|
| Donnée | Qu’est-ce qui est présent dans le corpus ? | Une phrase contient l’expression « pourrait contribuer à » |
| Résultat | Qu’a produit l’analyse ? | Cette expression est plus fréquente dans un sous-corpus |
| Interprétation | Que peut signifier ce résultat ? | Le sous-corpus semble privilégier une formulation plus prudente |
| Conclusion | Quelle réponse peut être donnée à la question ? | Dans le corpus étudié, ce genre emploie plus souvent des formulations prudentes |
| Généralisation | À quoi ce résultat peut-il être étendu ? | Peut-être à une population plus large, sous réserve de nouvelles données |

> Une conclusion peut être soutenue par les résultats sans justifier une
> généralisation à l’ensemble d’un domaine, d’une institution ou d’une
> langue.

## Exemple de surinterprétation

```text
Résultat :
Les communiqués du corpus contiennent plus de formulations causales
directes que les articles associés.

Interprétation défendable :
Dans le corpus étudié, les communiqués reformulent plus souvent les
relations observées sous une forme causale directe.

Interprétation non établie :
Les institutions exagèrent volontairement les résultats scientifiques.

Pourquoi ?
Les données analysent des formulations textuelles, non les intentions
des rédacteurs, les motivations institutionnelles ou la validité
scientifique de chaque affirmation.
```

---

# 2. Synthèse des résultats

Le fichier suivant rassemble les résultats pertinents :

```text
synthese_resultats.md
```

Il ne doit pas répéter tous les fichiers de `resultats/`. Il sélectionne
les observations nécessaires pour répondre à la question principale.

## Gabarit

```markdown
# Synthèse des résultats

## Question principale

> [Question de recherche.]

## Résultats principaux

| ID | Résultat | Fichier associé | Rôle dans la réponse |
|---|---|---|---|
| R01 | [Résultat] | [Chemin] | [Rôle] |
| R02 | [Résultat] | [Chemin] | [Rôle] |
| R03 | [Résultat de validation] | [Chemin] | [Rôle] |

## Résultats secondaires utiles

| ID | Résultat | Fichier associé | Utilité |
|---|---|---|---|
| R04 | [Résultat] | [Chemin] | [Utilité] |

## Résultats exploratoires

| ID | Résultat | Fichier associé | Précaution |
|---|---|---|---|
| R05 | [Résultat] | [Chemin] | [Précaution] |

## Résultats non retenus

[Décrire les analyses abandonnées ou non retenues, si leur omission
risquerait de tromper le lecteur sur la démarche.]
```

---

# 3. Tableau des inférences

Le fichier suivant est particulièrement recommandé :

```text
tableau_inferences.md
```

Il aide à éviter qu’une interprétation soit formulée comme un fait
directement observé.

## Gabarit

```markdown
# Tableau des inférences

| Observation ou résultat | Interprétation proposée | Éléments de soutien | Limites ou explications concurrentes | Formulation retenue |
|---|---|---|---|---|
| [Résultat R01] | [Interprétation] | [Tableau, figure, extrait] | [Limite] | [Phrase prudente] |
| [Résultat R02] | [Interprétation] | [Éléments] | [Limite] | [Phrase prudente] |
```

## Exemple

| Observation ou résultat | Interprétation proposée | Éléments de soutien | Limites ou explications concurrentes | Formulation retenue |
|---|---|---|---|---|
| Les communiqués contiennent une proportion plus élevée de causalité directe | Les communiqués du corpus reformulent plus directement les relations étudiées | Tableau 2, extraits E01–E06 | Différences de genre, de public, de sélection des études ou d’extraction | « Dans le corpus étudié, les communiqués emploient plus souvent des formulations causales directes » |
| Les formulations prudentes sont concentrées dans quelques sources | La tendance globale peut dépendre d’institutions particulières | Distribution par source | Taille inégale des sous-corpus | « La distribution observée varie selon les sources et doit être interprétée avec prudence » |

---

# 4. Interprétation principale

Le fichier suivant formule l’interprétation centrale :

```text
interpretation_principale.md
```

## Gabarit

```markdown
# Interprétation principale

## Question de recherche

> [Question.]

## Réponse synthétique

[Formuler une réponse provisoire, précise et prudente.]

## Résultats soutenant cette réponse

| Résultat | Contribution à la réponse |
|---|---|
| [R01] | [Contribution] |
| [R02] | [Contribution] |
| [R03] | [Contribution] |

## Retour aux textes

[Présenter les extraits, contextes ou exemples nécessaires pour
interpréter les résultats.]

## Articulation avec le cadre conceptuel

[Expliquer comment les résultats éclairent les concepts définis dans
`01_question_et_cadre/`.]

## Limites immédiates

[Préciser les limites qui affectent directement cette interprétation.]

## Formulation retenue pour l’article

[Écrire la formulation qui sera reprise ou adaptée dans la Discussion.]
```

## Règles de formulation

Préférer :

```text
Dans le corpus étudié, les résultats indiquent que…
```

```text
Les données suggèrent une association entre…
```

```text
Cette tendance peut être liée à…
```

```text
L’interprétation demeure limitée par…
```

```text
Les résultats ne permettent pas d’établir…
```

Éviter :

```text
Les auteurs veulent…
```

```text
Le domaine fonctionne toujours ainsi…
```

```text
Cette différence prouve que…
```

```text
Le modèle a découvert que…
```

```text
Les textes sont objectivement plus…
```

---

# 5. Retour aux textes et contextualisation

Les résultats de corpus doivent être replacés dans leurs contextes.

```text
fréquence / score / catégorie
    ↓
document et segment identifiés
    ↓
contexte immédiat
    ↓
contexte du document
    ↓
genre, source, période et public
    ↓
interprétation
```

L’examen des concordances, extraits, unités atypiques et contre-exemples
réduit le risque d’interpréter une forme ou un score hors contexte. Les
méthodes de corpus gagnent ainsi à articuler procédures quantitatives et
lecture qualitative plutôt qu’à opposer ces deux approches. [395][404]

## Questions de contextualisation

Pour chaque résultat important, demander :

- Dans quels documents le résultat apparaît-il ?
- Est-il réparti dans le corpus ou concentré dans quelques textes ?
- À quels genres, sources, périodes ou publics est-il associé ?
- Quelle est la fonction du passage dans son document ?
- Le contexte confirme-t-il l’interprétation ?
- Le phénomène peut-il avoir plusieurs sens ou fonctions ?
- Les extraits sélectionnés sont-ils typiques, atypiques ou ambigus ?
- Les exemples contraires ont-ils été examinés ?

## Gabarit pour les extraits interprétés

```markdown
## Extrait interprété [ID]

### Résultat associé

[Nom du tableau, figure, catégorie ou score.]

### Provenance

| Champ | Valeur |
|---|---|
| Document | [ID] |
| Segment | [ID] |
| Source | [Source] |
| Genre | [Genre] |
| Date | [Date] |
| Sous-corpus | [Sous-corpus] |

### Extrait

> [Extrait autorisé ou paraphrase.]

### Contexte

[Décrire le rôle du passage dans le document.]

### Interprétation

[Expliquer ce que l’extrait soutient ou nuance.]

### Limite

[Indiquer toute ambiguïté ou réserve.]
```

---

# 6. Contre-exemples et résultats inattendus

Le fichier suivant documente les cas qui résistent à l’interprétation
initiale :

```text
contre_exemples.md
```

Les contre-exemples ne sont pas des échecs à cacher. Ils peuvent :

- montrer que la tendance est limitée ;
- révéler une variation selon une source ou un genre ;
- indiquer une catégorie insuffisante ;
- suggérer une variable non contrôlée ;
- exiger une révision de l’interprétation ;
- ouvrir une nouvelle question de recherche.

## Gabarit

```markdown
# Contre-exemples et résultats inattendus

## Interprétation initiale concernée

[Décrire l’interprétation.]

## Contre-exemple [ID]

### Provenance

[Document, segment, source, genre, période.]

### Observation

[Décrire le cas.]

### Pourquoi est-ce un contre-exemple ?

[Expliquer en quoi il résiste à l’interprétation initiale.]

### Explications possibles

1. [Explication]
2. [Explication]
3. [Explication]

### Conséquence

- [ ] Ne modifie pas l’interprétation principale.
- [ ] Limite la portée de l’interprétation.
- [ ] Exige une révision des catégories.
- [ ] Exige une analyse complémentaire.
- [ ] Ouvre une nouvelle sous-question.
```

> Une analyse crédible ne sélectionne pas seulement les exemples qui
> confirment l’hypothèse initiale. Elle examine également les cas qui la
> compliquent ou la limitent.

---

# 7. Explications concurrentes

Le fichier suivant permet de distinguer l’interprétation retenue des
autres interprétations plausibles :

```text
explications_concurrentes.md
```

## Gabarit

```markdown
# Explications concurrentes

## Résultat concerné

[Décrire le résultat.]

## Interprétation principale

[Décrire l’interprétation privilégiée.]

## Explications concurrentes

| Hypothèse concurrente | Éléments qui la rendent plausible | Éléments qui la limitent | Décision |
|---|---|---|---|
| [Hypothèse 1] | [Éléments] | [Limites] | [Retenue / écartée / à discuter] |
| [Hypothèse 2] | [Éléments] | [Limites] | [Retenue / écartée / à discuter] |
| [Hypothèse 3] | [Éléments] | [Limites] | [Retenue / écartée / à discuter] |
```

## Exemples d’explications concurrentes

| Résultat observé | Interprétation trop rapide | Explications concurrentes à examiner |
|---|---|---|
| Une expression est plus fréquente dans un sous-corpus | Le public est plus prudent | Différence de genre, période, source, taille ou auteur |
| Une catégorie est plus présente dans des communiqués | Les institutions exagèrent | Différence de fonction communicative, sélection des études, contexte éditorial |
| Un terme est rare dans un corpus | Le concept est absent | Synonymie, périphrase, termes concurrents, limitation du corpus |
| Un cluster semble thématique | Le corpus contient ce thème | Effet de source, de longueur ou de représentation vectorielle |
| Un modèle classe un segment | Le segment appartient réellement à la catégorie | Erreur de modèle, ambiguïté, problème d’annotation ou contexte absent |

---

# 8. Limites

Le fichier suivant documente les limites :

```text
limites.md
```

Les limites doivent être précises, reliées à leur effet probable et
distinguées des formules générales telles que « l’étude comporte des
limites ».

## Types de limites

| Type | Exemple | Conséquence possible |
|---|---|---|
| Corpus | Sources limitées à une plateforme | Couverture incomplète de la population visée |
| Genre | Comparaison de genres aux fonctions différentes | Les différences ne peuvent pas être attribuées à un seul facteur |
| Période | Corpus limité à une année | Résultats non nécessairement stables dans le temps |
| Langue | Corpus monolingue | Généralisation limitée à cette langue |
| Métadonnées | Public ou auteur inconnus | Comparaisons restreintes |
| Acquisition | Documents non accessibles | Biais de disponibilité |
| Extraction | Tableaux ou notes mal extraits | Perte possible d’information |
| Annotation | Catégories ambiguës | Incertitude sur certaines unités |
| Modèle | Erreurs ou biais du modèle | Résultats automatiques imparfaits |
| Paramètres | Résultat sensible à un seuil | Robustesse limitée |
| Reproductibilité | Données non redistribuables | Vérification complète limitée |
| Interprétation | Intentions non observées | Conclusion limitée aux formulations textuelles |

## Gabarit

```markdown
# Limites

## Limite [L01] — [Titre bref]

### Description

[Décrire la limite.]

### Étape concernée

[Conception, acquisition, préparation, analyse, validation ou interprétation.]

### Effet possible

[Expliquer comment elle peut affecter les résultats ou leur portée.]

### Éléments de contrôle disponibles

[Indiquer les contrôles qui limitent ou documentent le problème.]

### Conséquence pour la conclusion

[Formuler ce que l’étude peut ou ne peut pas soutenir.]

### Perspective

[Indiquer ce qui permettrait de réduire cette limite dans une étude future.]
```

Les limites doivent être discutées avec honnêteté et précision. La
Discussion sert précisément à interpréter les résultats sans aller au-delà
de ce que les données permettent de soutenir. [397][398]

---

# 9. Implications

Le fichier suivant peut être utilisé lorsque les résultats ont des
conséquences identifiables :

```text
implications.md
```

Les implications peuvent être :

| Type | Question |
|---|---|
| Théorique | Que suggèrent les résultats pour la compréhension du phénomène ? |
| Méthodologique | Que montrent-ils sur la conception de corpus ou les méthodes utilisées ? |
| Discursive | Que révèlent-ils sur les genres, publics ou pratiques étudiés ? |
| Professionnelle | Que pourraient-ils apporter à une pratique de rédaction, traduction, indexation ou communication ? |
| Technique | Que suggèrent-ils pour la conception d’un outil ou d’une ressource ? |
| Pédagogique | Que pourraient-ils apporter à l’enseignement ou à la formation ? |

## Règle de prudence

Une implication doit être reliée à un résultat et ne pas transformer
une observation limitée en recommandation générale.

Préférer :

```text
Ces résultats suggèrent que les outils de [type] pourraient bénéficier
d’une distinction entre [catégories], sous réserve d’une validation sur
un corpus plus large.
```

Éviter :

```text
Les institutions doivent désormais adopter cette méthode.
```

---

# 10. Perspectives

Le fichier suivant conserve les suites raisonnables du projet :

```text
perspectives.md
```

Une perspective utile découle d’une limite, d’un contre-exemple ou d’une
question ouverte identifiée pendant l’enquête.

## Gabarit

```markdown
# Perspectives

| Perspective | Justification | Données ou méthode nécessaires | Priorité |
|---|---|---|---|
| [Perspective 1] | [Lien avec une limite ou un résultat] | [Besoin] | [Haute / moyenne / basse] |
| [Perspective 2] | [Lien] | [Besoin] | [Haute / moyenne / basse] |
```

Exemples :

- élargir le corpus à une autre période ;
- comparer une autre langue ;
- ajouter des métadonnées institutionnelles ;
- tester le guide d’annotation avec davantage d’annotateurs ;
- vérifier les résultats sur un corpus indépendant ;
- étudier les documents exclus ;
- comparer plusieurs représentations textuelles ;
- conduire des entretiens avec les producteurs de documents ;
- analyser la réception effective des textes par leurs destinataires.

---

# 11. Discussion préliminaire

Le fichier suivant sert de brouillon structuré pour la Discussion de
l’article :

```text
discussion_preliminaire.md
```

## Gabarit

```markdown
# Discussion préliminaire

## Rappel de la question

> [Question de recherche.]

## Réponse principale

[Réponse synthétique et prudente.]

## Résultat principal et interprétation

[Présenter le résultat principal, son sens et ses limites.]

## Résultat secondaire ou complémentaire

[Présenter le résultat secondaire, son sens et ses limites.]

## Comparaison avec les travaux antérieurs

[Indiquer les convergences, divergences ou compléments.]

## Contre-exemples et explications concurrentes

[Présenter les éléments qui limitent l’interprétation.]

## Limites principales

[Présenter les limites ayant les conséquences les plus importantes.]

## Implications

[Décrire les implications théoriques, méthodologiques ou pratiques.]

## Perspectives

[Décrire les suites raisonnables de l’étude.]

## Formulation finale

[Formuler une conclusion correspondant exactement à la portée des données.]
```

La Discussion ne doit pas seulement résumer les résultats. Elle doit
expliquer ce qu’ils signifient, les situer par rapport aux travaux
antérieurs, reconnaître les limites et préciser les implications ou
perspectives. [397][398]

---

# 12. Articulation avec l’article IMRAD

| Élément du présent dossier | Section correspondante de l’article |
|---|---|
| `synthese_resultats.md` | Résultats et début de Discussion |
| `interpretation_principale.md` | Discussion |
| `contre_exemples.md` | Résultats ou Discussion |
| `explications_concurrentes.md` | Discussion |
| `limites.md` | Discussion |
| `implications.md` | Discussion ou conclusion |
| `perspectives.md` | Fin de Discussion |
| `discussion_preliminaire.md` | Brouillon de la Discussion |
| `tableau_inferences.md` | Outil interne de contrôle de l’argumentation |

L’article final est rédigé dans :

```text
../../article/article_imrad.md
```

Les fichiers de ce dossier peuvent être plus détaillés que l’article.
L’article doit sélectionner les éléments nécessaires pour répondre à la
question de manière claire, cohérente et proportionnée.

---

# 13. Journal de recherche associé

Les décisions interprétatives importantes doivent être documentées dans :

```text
../../journal/journal_de_bord.md
```

Le journal doit notamment consigner :

- les premières interprétations envisagées ;
- les résultats qui surprennent l’équipe ;
- les contre-exemples ;
- les changements de conclusion ;
- les explications concurrentes discutées ;
- les limites nouvellement reconnues ;
- les retours au texte ;
- les rétroactions de pairs ou de l’enseignant ;
- les raisons d’écarter une interprétation ;
- les usages de LLM ou d’IA ayant influencé l’interprétation.

## Exemple d’entrée de journal

```markdown
## YYYY-MM-DD — Révision de l’interprétation principale

### Résultat concerné

Les documents du sous-corpus A présentent une proportion plus élevée de
formulations causales directes que ceux du sous-corpus B.

### Interprétation initiale

Le sous-corpus A simplifie ou renforce les relations scientifiques.

### Contre-exemple ou limite

Les documents du sous-corpus A sont aussi plus courts et appartiennent
à un genre ayant une fonction de synthèse. Une partie de la différence
pourrait donc être liée au genre ou à la longueur, et non uniquement à
la reformulation.

### Décision

Nous révisons la formulation : le sous-corpus A emploie plus souvent des
formulations causales directes dans le corpus étudié. Nous ne concluons
pas que les auteurs cherchent intentionnellement à simplifier ou
exagérer les résultats.

### Conséquence

La Discussion traite la fonction du genre comme une explication
concurrente et présente cette limite explicitement.
```

---

# Checklist avant la rédaction finale

- [ ] La réponse à la question est formulée clairement.
- [ ] Les résultats soutenant cette réponse sont identifiés.
- [ ] Les interprétations sont distinguées des observations.
- [ ] Les unités, contextes et extraits ont été examinés.
- [ ] Les contre-exemples sont documentés.
- [ ] Les explications concurrentes sont considérées.
- [ ] Les limites sont précises et reliées à leurs conséquences.
- [ ] Les implications ne dépassent pas les résultats.
- [ ] Les perspectives découlent des limites ou questions ouvertes.
- [ ] Les formulations évitent d’attribuer des intentions non observées.
- [ ] Les généralisations sont proportionnées au corpus.
- [ ] Les conclusions sont cohérentes avec les contrôles réalisés.
- [ ] Les décisions interprétatives sont consignées dans le journal.
- [ ] La Discussion préliminaire peut être transférée vers l’article IMRAD.