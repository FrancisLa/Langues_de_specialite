# Exemple de question et cadre
## De trois pistes à un corpus pour le moissonnage

> **Statut :** exemple construit pour les étudiant.es. Il ne présente aucune observation réelle et ne doit pas être copié.

Équipe : [Prénom Nom, Prénom Nom]
Date : [AAAA-MM-JJ]
Dossier : `chaine/01_question_et_cadre/`

Cet exemple montre la trace que produirait une équipe à la fin de la séance 2. Il part des trois pistes de la séance 1 et conduit à un choix argumenté de corpus, donc à une revue à moissonner. Le choix reste provisoire : le plan de corpus et le pilote de moissonnage le valident ou le révisent.

---

## Partie A — `question_recherche.md`

### Titre provisoire

Évolution des thèmes d'une revue de spécialité : que montre le vocabulaire d'une discipline en train de se structurer ?

### Intérêt général

Les études sur l'argumentation et le discours forment un champ interdisciplinaire (linguistique, rhétorique, philosophie, communication). On ne sait pas quels thèmes y dominent, ni comment ils changent d'un numéro à l'autre.

### Objet d'étude

Les thèmes et les motifs récurrents dans les articles d'une revue spécialisée, et leur évolution au fil des numéros.

### Problème de recherche

[Les sommaires donnent une impression d'évolution, mais cette impression n'a pas été confrontée à une lecture systématique des textes. Un thème peut changer de nom sans changer d'objet, ou rester le même sous des mots différents.]

### Question principale

> Quels thèmes structurent les articles de la revue retenue, et comment la présence de ces thèmes varie-t-elle d'un numéro à l'autre ?

### Sous-questions

1. Quels thèmes apparaissent de façon récurrente dans le texte intégral ?
2. Ces thèmes que l'on retrouve dans le texte intégral, se retrouvent-ils également dans les titres, résumés et mots-clés ?
3. Quels thèmes apparaissent, disparaissent ou se transforment entre les numéros ?

### Hypothèses ou attentes initiales

Projet **exploratoire**. Attente provisoire : les mots-clés donnent une première cartographie, mais ils ne suffisent pas à rendre compte des thèmes présents dans le texte intégral.

### Corpus envisagé

Les articles d'une seule revue d'OpenEdition Journals (voir la Partie C), avec leurs métadonnées (titre, auteurs, date ou numéro, résumé, mots-clés, langue, DOI).

### Unité d'analyse envisagée

L'article, pour l'inventaire et la comparaison entre numéros. Le paragraphe est envisagé à titre exploratoire.

### Méthodes envisagées

Analyse thématique, dont la méthode sera présentée plus tard. Au stade actuel : lecture d'un échantillon, repérage manuel de thèmes, puis comparaison avec ce qu'un traitement automatique pourrait proposer.

### Faisabilité

Textes en accès ouvert sur OpenEdition, métadonnées structurées, numéros bien délimités. Voir la Partie C.

### Hors périmètre

Le projet ne cherche pas à établir l'influence d'un thème, la qualité des articles, ni l'évolution de tout le champ de l'argumentation.

---

## Partie B — `operationnalisation.md` (première version)

| Concept | Définition de travail | Observable | Unité | Règle de décision | Cas limite |
|---|---|---|---|---|---|
| Thème | Sujet récurrent traité dans plusieurs articles | Mots-clés, termes du titre et du résumé, termes répétés dans le texte | Article | Un thème est retenu s'il apparaît dans au moins [N] articles | Même thème, termes différents |
| Évolution thématique | Variation de la présence d'un thème selon les numéros | Nombre d'articles par thème et par numéro | Numéro | Comparer des numéros de taille comparable | Numéros de taille très inégale |
| Thème explicite | Thème nommé dans les métadonnées | Mot-clé ou terme du titre | Article | Présence du terme | Terme polysémique |
| Thème implicite | Thème traité par un ensemble de termes, avec ou sans terme canonique | Formulations proches dans le texte | Article | Décision par lecture, avec double codage, ou encore apprentissage automatique | Désaccord entre codeurs, ou encore détection automatique de chose qui ne sont pas des thèmes (une autre langue par exemple) |

**À contrôler :** deux équipiers codent indépendamment 10 articles, puis comparent leurs décisions.

---

## Partie C — Choix du corpus : comparaison des trois pistes

Les trois pistes de la séance 1 sont évaluées avec les mêmes critères. Les notes vont de 0 (très défavorable) à 2 (favorable). Chaque note doit être justifiée par une vérification réelle, pas par une impression.

| Critère | Piste 1 : *Argumentation et Analyse du Discours* | Piste 2 : *Revue d'Anthropologie des Connaissances* | Piste 3 : [revue à choisir] |
|---|---|---|---|
| Lien avec la question | 2 | 1 | [ ] |
| Phénomène visible dans les textes consultés | 2 | 1 | [ ] |
| Accès au texte intégral | 2 | [2] | [ ] |
| Structure des numéros et articles | 2 | 2 | [ ] |
| Métadonnées disponibles | 2 | 2 | [ ] |
| Volume gérable | 2 | 1 | [ ] |
| Autorisation de moissonner (`robots.txt`, conditions) | [2] | [2] | [ ] |
| Soutien du matériel du cours | 2 | 2 | [ ] |
| **Total provisoire** | **[ ]** | **[ ]** | **[ ]** |

**Éléments vérifiés pour la piste 1 :**

- La page de la revue présente la liste des numéros, lesquels donnent accès aux articles.
- Le notebook de démonstration du cours a déjà inventorié cette revue : environ 37 numéros et 457 articles à la date d'exécution du notebook (08/10/2026). Ces valeurs seront recontrôlées au moment de la collecte.
- La structure HTML des pages (numéros, articles, liens PDF) est connue.

### Décision

Nous retenons provisoirement la **piste 1** comme corpus de départ.

### Justification

1. La question porte sur les thèmes d'une revue : une revue avec de nombreux numéros permet une comparaison.
2. Les métadonnées et les textes sont accessibles de manière structurée.
3. Le volume est suffisant pour une analyse, sans être démesuré.
4. Un pilote est réalisable en quelques jours avec le matériel du cours.

### Risques

- Les numéros thématiques peuvent produire des variations qui reflètent les choix éditoriaux, non les tendances du champ.
- Les mots-clés peuvent manquer ou varier d'un numéro à l'autre.
- Le nombre d'articles par numéro est possiblement inégal.
- Les conditions de moissonnage sont à confirmer avant la collecte.

### Plan de secours

Si le moissonnage échoue ou si les conditions d'accès changent : utiliser un corpus de secours fourni par le cours, ou réduire la collecte à quelques numéros téléchargés manuellement.

---

## Partie D — `exemples_preliminaires.md` (gabarit rempli de manière fictive)

### Exemple E01

- **Source :** [Article de la revue, titre, lien, numéro]
- **Extrait :** > [Court extrait exact du résumé ou du texte]
- **Phénomène observé :** [Thème repéré]
- **Pourquoi pertinent :** [Lien avec la question]
- **Difficulté soulevée :** [Le thème est-il explicite ou implicite ?]

### Exemple E02 (contre-exemple)

- **Source :** [Article]
- **Extrait :** > [Court extrait]
- **Phénomène observé :** [Article qui ne s'inscrit dans aucun thème prévu]
- **Difficulté soulevée :** [Faut-il créer un thème ou garder l'article hors classement ?]

> Consigne : au moins cinq exemples, dont un contre-exemple et un cas ambigu, tous tirés d'articles réellement lus.

---

## Partie E — Entrée de journal

### AAAA-MM-JJ — Choix d'un corpus

**Étape :** question et cadre, vers la conception du corpus.

**Objectif :** choisir une revue pour tester la collecte.

**Observation :** les trois pistes reposaient sur des phénomènes différents. Seule la piste 1 était reliée à une question qui exige plusieurs numéros comparables.

**Options envisagées :**

1. Garder les trois revues.
2. Choisir la revue la plus proche de nos intérêts.
3. Choisir la revue qui permet de répondre à une question testable dans le temps disponible.

**Décision :** option 3 ; la piste 1 est retenue.

**Justification :** l'option 1 aurait dispersé le travail, l'option 2 n'aurait pas garanti la faisabilité.

**Vérification prévue :** recueillir les articles d'un numéro et vérifier les métadonnées disponibles.

**Conséquence :** la prochaine étape est le plan de corpus.

**Trace :** `chaine/01_question_et_cadre/question_recherche.md`

---

## Partie F — Passage à la séance 3

Cette production fournit à la conception du corpus :

- une question principale ;
- une première unité d'analyse (l'article) ;
- une revue candidate et ses critères de choix ;
- des risques et un plan de secours ;
- des premiers exemples à vérifier ;
- une règle de contrôle à tester sur un échantillon.

### Checklist de sortie

- [ ] La question ne mentionne aucun outil.
- [ ] La revue est choisie par des critères explicites.
- [ ] Les exemples proviennent de textes réellement lus.
- [ ] Les conditions d'accès sont notées comme à vérifier ou vérifiées.
- [ ] Un plan de secours est prévu.
- [ ] Le journal explique le choix.
