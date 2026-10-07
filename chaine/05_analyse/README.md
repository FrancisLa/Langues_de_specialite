# Analyse

Ce dossier contient les méthodes, scripts, protocoles et sorties
intermédiaires utilisés pour produire les observations empiriques du
projet.

L’analyse constitue le passage entre les données préparées et les résultats
qui permettront de répondre à la question de recherche.

```text
question de recherche
    ↓
données préparées
    ↓
méthode d’analyse
    ↓
paramètres et procédures
    ↓
sorties intermédiaires
    ↓
résultats documentés
    ↓
validation et interprétation
```

L’objectif est de répondre aux questions suivantes :

> **Quelle méthode permet de répondre à la question de recherche ?**

> **Quelles données et unités d’analyse sont utilisées ?**

> **Quels paramètres, règles ou modèles ont été retenus ?**

> **Quelles sorties sont produites et comment sont-elles reliées aux résultats finaux ?**

> **Quels résultats sont principaux, secondaires, exploratoires ou diagnostiques ?**

> **Principe :** une méthode n’est pas choisie parce qu’elle est disponible
> dans un logiciel. Elle est choisie parce qu’elle permet de produire des
> observations pertinentes au regard de la question de recherche.

---

## Relation avec les autres étapes

L’analyse reçoit des données préparées provenant de :

```text
../04_preparation/
../../donnees/preparees/
```

Elle met en œuvre les choix formulés dans :

```text
../01_question_et_cadre/
../02_conception_du_corpus/
../../configuration/
../../environnement/
```

Elle produit des sorties qui seront contrôlées dans :

```text
../06_validation/
```

Les tableaux, figures et extraits finaux sont ensuite conservés dans :

```text
../../resultats/
```

Les décisions, essais, résultats inattendus et modifications importantes
sont consignés dans :

```text
../../journal/journal_de_bord.md
```

---

## Structure du dossier

```text
05_analyse/
├── README.md
├── plan_analyse.md
├── produire_resultats_principaux.py
├── produire_resultats_principaux.R
├── code/
│   ├── README.md
│   ├── 01_description_corpus.py
│   ├── 02_analyse_principale.py
│   ├── 03_analyse_secondaire.py
│   └── 04_produire_figures.py
│
├── configurations/
│   ├── README.md
│   ├── analyse_principale.yml
│   ├── analyse_exploratoire.yml
│   └── parametres_modele.yml
│
├── sorties_intermediaires/
│   ├── README.md
│   ├── description_corpus.csv
│   ├── resultats_bruts.csv
│   ├── resultats_annotes.csv
│   └── journal_execution.csv
│
└── notebooks/
    ├── README.md
    └── analyse_exploratoire.ipynb
```

Tous les éléments ne sont pas obligatoires.

| Élément | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique l’analyse dans son ensemble | Oui |
| `plan_analyse.md` | Justifie les analyses retenues | Oui |
| `code/` | Scripts, fonctions ou procédures analytiques | Oui |
| `configurations/` | Paramètres analytiques versionnés | Oui |
| `sorties_intermediaires/` | Résultats intermédiaires utiles à la traçabilité | Selon le volume |
| `notebooks/` | Exploration documentée ou démonstration | Oui, si lisible et pertinent |
| Résultats finaux | Tableaux, figures et extraits retenus | Dans `resultats/` |

> Les notebooks exploratoires peuvent être conservés, mais ils ne doivent
> pas être l’unique moyen de reproduire un résultat principal. Une
> procédure claire doit permettre de produire les résultats finaux.

---

# 1. Plan d’analyse

Le fichier principal de cette étape est :

```text
plan_analyse.md
```

Le plan d’analyse doit être rédigé avant, ou au plus tard pendant les
premiers essais sur le corpus préparé. Il peut être révisé, mais les
révisions importantes doivent être consignées dans le journal.

## Gabarit

```markdown
# Plan d’analyse

## Version

- Version : [v0.1]
- Date : [YYYY-MM-DD]
- Personnes responsables : [Nom(s)]

## Question principale

> [Question de recherche.]

## Sous-questions

1. [Sous-question 1]
2. [Sous-question 2]
3. [Sous-question 3, si nécessaire]

## Données utilisées

| Jeu de données | Emplacement | Version | Description |
|---|---|---|---|
| [Nom] | [Chemin] | [Version] | [Description] |

## Unité d’analyse

[Document, section, paragraphe, phrase, contexte de citation, paire
de documents, token, lemme, groupe nominal, etc.]

## Méthodes prévues

| ID | Méthode | Question associée | Type | Statut |
|---|---|---|---|---|
| A01 | [Méthode] | [Question] | Descriptive | Principale |
| A02 | [Méthode] | [Question] | Comparative | Principale |
| A03 | [Méthode] | [Question] | Qualitative | Secondaire |
| A04 | [Méthode] | [Question] | Exploration | Exploratoire |

## Sorties attendues

| ID | Sortie | Format | Emplacement |
|---|---|---|---|
| R01 | Description du corpus | CSV / tableau | `resultats/tableaux/` |
| R02 | Résultat principal | CSV / figure | `resultats/` |
| R03 | Extraits contextualisés | Markdown | `resultats/extraits/` |

## Contrôles prévus

[Décrire les contrôles qui seront réalisés à l’étape 06.]

## Limites attendues

[Décrire les limites de la méthode ou des données.]
```

---

# 2. Statut des analyses

Chaque sortie doit être identifiée selon son rôle dans l’enquête.

| Statut | Définition | Usage dans l’article |
|---|---|---|
| Principale | Répond directement à la question principale | Résultats et Discussion |
| Secondaire | Éclaire une sous-question ou contextualise le résultat principal | Résultats, annexe ou Discussion |
| Descriptive | Décrit le corpus ou les données | Méthodes ou Résultats |
| Diagnostique | Vérifie un problème technique ou méthodologique | Méthodes, validation ou annexe |
| Exploratoire | Génère des hypothèses ou explore des régularités inattendues | À identifier explicitement comme exploratoire |
| Provisoire | Essai non retenu ou sortie temporaire | Journal, annexe ou non conservé |

> Un résultat exploratoire peut être utile et intéressant. Il doit
> toutefois être distingué d’un résultat produit selon une procédure
> définie à l’avance pour répondre à la question principale.

---

# 3. Choisir une méthode d’analyse

Le choix de méthode doit découler de la question, du corpus, de l’unité
d’analyse et des observables retenus.

## Méthodes descriptives

| Question | Méthode possible | Sortie |
|---|---|---|
| Quels documents composent le corpus ? | Description des métadonnées | Tableau descriptif |
| Quelles unités sont présentes ? | Comptage de documents, mots, segments ou catégories | Tableau de distribution |
| Comment se répartissent les genres ? | Fréquences, proportions, visualisation | Tableau ou figure |
| Quels termes apparaissent le plus souvent ? | Liste de fréquences, dispersion | Tableau ou concordances |
| Comment les catégories sont-elles distribuées ? | Comptage par sous-corpus | Tableau comparatif |

## Méthodes contextuelles

| Question | Méthode possible | Sortie |
|---|---|---|
| Comment une forme est-elle utilisée ? | Concordances | Lignes de contexte |
| Avec quelles unités une forme apparaît-elle ? | Cooccurrences ou collocations | Liste pondérée ou tableau |
| Dans quels passages apparaît un phénomène ? | Recherche structurée et retour au texte | Extraits contextualisés |
| Comment les auteurs formulent-ils une recommandation ? | Annotation qualitative, lecture des contextes | Catégories et extraits |
| Comment les citations sont-elles mobilisées ? | Analyse des contextes de citation | Extraits et catégories |

## Méthodes comparatives

| Question | Méthode possible | Sortie |
|---|---|---|
| Qu’est-ce qui distingue deux sous-corpus ? | Comparaison de fréquences ou spécificités | Tableau comparatif |
| Une catégorie varie-t-elle selon le genre ? | Proportions, tableau croisé, test adapté | Tableau et figure |
| Une forme est-elle spécifique à une période ? | Comparaison temporelle | Série ou tableau |
| Les documents diffèrent-ils selon la langue ? | Comparaison multilingue contrôlée | Tableau, figure, extraits |
| Les paires de documents sont-elles reformulées ? | Alignement et comparaison intra-paire | Tableau de transformations |

## Méthodes de classification ou de prédiction

| Objectif | Méthode possible | Contrôles nécessaires |
|---|---|---|
| Catégoriser des segments | Règles, modèle supervisé, LLM, classifieur | Jeu de validation, erreurs, métriques |
| Identifier des documents pertinents | Recherche, score, classifieur | Précision, rappel ou contrôle humain |
| Détecter une section | Règles structurelles ou classification | Échantillon annoté et erreurs |
| Identifier une thèse principale | Annotation, modèle ou règles | Référence annotée, analyse qualitative |
| Pré-annoter des données | Modèle linguistique ou LLM | Vérification humaine et correction |

## Méthodes exploratoires

| Objectif | Méthode possible | Prudence requise |
|---|---|---|
| Regrouper des segments | Clustering | Retour aux textes, stabilité, choix du nombre de groupes |
| Explorer des thèmes | Modélisation thématique | Interprétation des thèmes, paramètres, stabilité |
| Visualiser des similarités | Réduction dimensionnelle | Ne pas interpréter une projection comme une preuve complète |
| Mesurer une proximité sémantique | Embeddings et similarité | Contrôle des voisins et limites du modèle |
| Identifier des réseaux | Cooccurrences ou graphes | Justifier les seuils et éviter les causalités implicites |

Les listes de fréquences, concordances, collocations et mots-clés sont
des techniques classiques de la linguistique de corpus. Elles gagnent à
être articulées : une fréquence ou une association statistique oriente
l’attention, mais l’examen des contextes permet de comprendre les usages
effectifs. [369][378]

---

# 4. Description obligatoire des analyses

Chaque méthode retenue doit comporter une documentation spécifique.

Créer, selon les besoins :

```text
code/01_description_corpus.py
code/02_analyse_principale.py
code/03_analyse_secondaire.py
configurations/analyse_principale.yml
```

Chaque script ou protocole important doit préciser :

| Élément | Question à laquelle répondre |
|---|---|
| Objectif | À quelle question ou sous-question répond l’analyse ? |
| Données | Quel fichier, version ou sous-corpus est utilisé ? |
| Unité | Quel est l’objet analysé : document, phrase, segment, paire ? |
| Méthode | Quel calcul, règle, modèle ou procédure est appliqué ? |
| Paramètres | Quels seuils, filtres, fenêtres, graines ou options sont retenus ? |
| Sortie | Quel fichier, tableau, figure ou extrait est produit ? |
| Contrôle | Comment le résultat sera-t-il vérifié ? |
| Limite | Que la méthode ne permet-elle pas de conclure ? |

## Gabarit de README pour une analyse

```markdown
# Analyse [ID] — [Titre]

## Statut

- [ ] Principale
- [ ] Secondaire
- [ ] Descriptive
- [ ] Diagnostique
- [ ] Exploratoire

## Question associée

> [Question ou sous-question.]

## Objectif

[Décrire l’objectif de l’analyse.]

## Données utilisées

| Fichier | Version | Description |
|---|---|---|
| [Chemin] | [Version] | [Description] |

## Unité d’analyse

[Document / phrase / paragraphe / paire / token / autre.]

## Méthode

[Décrire la procédure, le calcul, la règle ou le modèle.]

## Paramètres

| Paramètre | Valeur | Justification |
|---|---|---|
| [Nom] | [Valeur] | [Justification] |

## Commande ou procédure

```bash
[Commande d’exécution.]
```

## Sorties

| Fichier | Description |
|---|---|
| [Chemin] | [Description] |

## Contrôles prévus

[Décrire les vérifications prévues.]

## Limites

[Décrire les limites d’interprétation.]

## Journal associé

- [Lien vers une entrée de journal.]
```

---

# 5. Paramètres et configurations

Les paramètres qui influencent les résultats doivent être versionnés.

Les fichiers de configuration sont stockés dans :

```text
configurations/
```

## Exemple : `analyse_principale.yml`

```yaml
analyse:
  id: "A02"
  nom: "Comparaison_des_categories_par_genre"
  statut: "principale"

donnees:
  fichier_entree: "../../donnees/preparees/segments_annotes.csv"
  version_corpus: "v0.3"
  unite_analyse: "phrase"

variables:
  variable_groupe: "genre"
  variable_analysee: "categorie"

filtres:
  langues:
    - "fr"
  statuts_documents:
    - "retenu"
  categories_exclues:
    - "hors_categorie"

parametres:
  seuil_minimal_effectif: 5
  inclure_cas_ambigus: false
  graine_aleatoire: 42

sorties:
  tableau: "../../resultats/tableaux/tableau_02_categories_par_genre.csv"
  figure: "../../resultats/figures/figure_02_categories_par_genre.png"
```

## Règles

- Ne pas laisser les paramètres uniquement dans le code.
- Ne pas modifier silencieusement un seuil ou un filtre.
- Ne pas écraser une configuration ayant produit un résultat cité.
- Associer chaque résultat final à une version identifiable des paramètres.
- Documenter les changements de paramètres dans le journal.
- Séparer les paramètres partagés des secrets ou chemins personnels.

Les paramètres locaux ou sensibles restent dans :

```text
../../configuration/config.yml
../../configuration/.env
```

et ne doivent pas être ajoutés à Git.

---

# 6. Scripts, notebooks et procédures manuelles

## Scripts

Les scripts doivent, lorsque possible :

- utiliser des chemins relatifs ;
- lire les paramètres depuis un fichier de configuration ;
- produire des sorties dans un emplacement prévisible ;
- indiquer clairement les entrées et sorties ;
- éviter les valeurs cachées directement dans le code ;
- conserver les identifiants de documents et de segments ;
- permettre de relancer l’analyse sans intervention manuelle non documentée.

## Notebooks

Les notebooks sont utiles pour :

- explorer les données ;
- expliquer une procédure ;
- tester une hypothèse ;
- présenter une démonstration ;
- conserver une analyse qualitative guidée.

Cependant, un notebook ne doit pas être la seule documentation d’un
résultat principal s’il dépend :

- d’un ordre caché d’exécution ;
- de variables créées dans des cellules précédentes ;
- de fichiers locaux non documentés ;
- d’interventions manuelles non consignées.

Pour chaque notebook retenu, indiquer :

```markdown
- Les données d’entrée.
- L’ordre d’exécution.
- Les cellules importantes.
- Les fichiers produits.
- Les sorties qui sont finales ou exploratoires.
- Les limites connues.
```

## Procédures manuelles

Une analyse manuelle est admissible lorsqu’elle est documentée.

Exemples :

- lecture de concordances ;
- codage qualitatif ;
- examen de citations ;
- comparaison de paires de documents ;
- sélection d’extraits ;
- interprétation de groupes ;
- vérification de résultats automatiques.

Documenter au minimum :

```markdown
- La personne responsable.
- Les unités examinées.
- Les règles ou questions de lecture.
- Les décisions prises.
- Les résultats produits.
- Les cas ambigus.
- Les contrôles ou discussions réalisés.
```

---

# 7. Statistiques, fréquences et comparaisons

Les statistiques descriptives doivent toujours préciser :

- l’unité d’analyse ;
- le nombre de documents ou segments ;
- le dénominateur ;
- la période ;
- le sous-corpus ;
- les filtres appliqués ;
- les valeurs manquantes ou exclusions ;
- la mesure utilisée : nombre brut, proportion, taux, moyenne, médiane,
  score ou autre.

## Exemple de formulation insuffisante

```text
Les communiqués utilisent plus de formulations causales.
```

## Formulation améliorée

```text
Dans le corpus retenu, les formulations classées comme causales directes
représentent [x %] des [n] phrases analysées dans les communiqués,
contre [y %] des [m] phrases dans les articles. Cette différence décrit
le corpus étudié ; elle ne permet pas, à elle seule, d’attribuer une
intention aux producteurs des documents.
```

## Comparaison de sous-corpus

Avant de comparer des sous-corpus, vérifier :

- les unités sont-elles comparables ?
- les documents appartiennent-ils aux mêmes périodes ?
- les corpus ont-ils des tailles très différentes ?
- les genres, sources ou publics constituent-ils des variables
  confondantes ?
- les documents sont-ils indépendants ?
- une paire documentaire doit-elle être analysée comme telle ?
- la différence observée est-elle répartie dans le corpus ou concentrée
  dans quelques documents ?
- les contextes confirment-ils l’interprétation proposée ?

---

# 8. Concordances, cooccurrences et retour aux textes

Les analyses automatiques ou quantitatives doivent être confrontées aux
contextes textuels.

```text
fréquence ou score
    ↓
candidats ou régularités
    ↓
concordances et contextes
    ↓
lecture des segments
    ↓
interprétation prudente
```

Une concordance permet de récupérer les occurrences d’une forme, d’une
expression ou d’une annotation avec leur contexte immédiat. Elle est
particulièrement utile pour vérifier qu’une fréquence, une cooccurrence
ou une catégorie correspond réellement au phénomène interprété.

## Exemple de procédure

```markdown
1. Identifier une forme ou une catégorie saillante.
2. Extraire les occurrences avec leur contexte.
3. Trier les contextes selon une propriété pertinente.
4. Lire un échantillon ou l’ensemble des occurrences, selon le volume.
5. Identifier les usages, ambiguïtés et contre-exemples.
6. Conserver les extraits pertinents dans `resultats/extraits/`.
7. Documenter les limites de l’interprétation.
```

Les concordances permettent d’articuler l’analyse quantitative à
l’interprétation qualitative. Les listes de fréquences et les mesures
d’association ne remplacent pas le retour aux usages attestés dans les
textes. [369][374][377]

---

# 9. Modèles, apprentissage automatique et LLM

Lorsqu’un modèle est utilisé, documenter la méthode comme une composante
de recherche, et non comme une boîte noire.

## Informations minimales

| Élément | Information attendue |
|---|---|
| Objectif du modèle | Quelle tâche réalise-t-il ? |
| Données d’entrée | Quel corpus, quelles unités et quelles versions ? |
| Variables ou représentations | Formes, lemmes, embeddings, métadonnées, etc. |
| Jeu de référence | Comment les annotations ou labels ont-ils été produits ? |
| Séparation des données | Entraînement, validation, test, ou autre stratégie |
| Modèle | Nom, version, architecture ou algorithme |
| Paramètres | Valeurs et stratégie de sélection |
| Environnement | Bibliothèques, matériel, versions et graines |
| Nombre d’exécutions | Nombre de runs ou répétitions |
| Métriques | Mesures utilisées et définition |
| Erreurs | Analyse qualitative ou quantitative des erreurs |
| Sorties | Prédictions, scores, tableaux et figures |
| Limites | Biais, variabilité, couverture, généralisabilité |

Les checklists de reproductibilité en TAL recommandent notamment de
documenter les détails des données, les séparations entraînement–
validation–test, les paramètres, les dépendances, les métriques, le
nombre d’exécutions et les méthodes de sélection des modèles.
[370][371]

## LLM et IA générative

Lorsqu’un LLM est utilisé pour l’analyse :

- l’usage doit être documenté dans le journal ;
- le modèle, la version ou la date d’accès doivent être indiqués ;
- les prompts ou gabarits de prompts doivent être conservés lorsque
  nécessaire à la reprise ;
- les données transmises doivent être documentées ;
- les sorties doivent être contrôlées ;
- les erreurs doivent être analysées ;
- les limites de confidentialité, de version, de variabilité et de coût
  doivent être discutées ;
- les résultats générés par le modèle ne doivent pas être interprétés
  comme valides sans vérification.

Voir également :

```text
../../journal/README.md
../../configuration/README.md
../../article/README.md
```

---

# 10. Sorties intermédiaires

Les sorties intermédiaires sont stockées dans :

```text
sorties_intermediaires/
```

Elles peuvent inclure :

- listes de fréquence ;
- tables de comptage ;
- prédictions brutes ;
- scores ;
- matrices ;
- sorties de modèles ;
- échantillons annotés ;
- listes de candidats ;
- fichiers de regroupement ;
- tableaux avant mise en forme ;
- données sources de figures.

## Convention de nommage

```text
[analyse]_[identifiant]_[description]_[version].[extension]
```

Exemples :

```text
A01_description_corpus_v01.csv
A02_categories_par_genre_v02.csv
A03_predictions_brutes_v01.csv
A04_clustering_segments_v03.csv
```

Les fichiers finaux retenus doivent être copiés, générés ou référencés
dans :

```text
../../resultats/
```

Ne pas produire directement dans `resultats/` un fichier dont le statut,
la procédure ou les contrôles ne sont pas encore établis.

---

# 11. Journal d’exécution

Le fichier suivant peut consigner les exécutions importantes :

```text
sorties_intermediaires/journal_execution.csv
```

## Structure suggérée

```csv
date_heure;id_analyse;entree;configuration;version_code;sortie;statut;responsable;commentaire
YYYY-MM-DDTHH:MM:SS;A01;donnees/preparees/segments.csv;configurations/analyse_principale.yml;abc123;sorties_intermediaires/A01_description_corpus_v01.csv;valide;Nom;
```

| Colonne | Description |
|---|---|
| `date_heure` | Date et heure de l’exécution |
| `id_analyse` | Identifiant de l’analyse |
| `entree` | Fichier ou version de données utilisée |
| `configuration` | Paramètres utilisés |
| `version_code` | Hash Git ou version du code |
| `sortie` | Fichier produit |
| `statut` | Provisoire, valide, rejeté, à vérifier |
| `responsable` | Personne ou système ayant exécuté la procédure |
| `commentaire` | Erreurs, limites ou décisions pertinentes |

---

# 12. Articulation avec la validation

Les résultats produits ici ne doivent pas être interprétés comme finaux
avant les contrôles de :

```text
../06_validation/
```

La validation peut porter sur :

- les données d’entrée ;
- les filtres appliqués ;
- les catégories ;
- les annotations ;
- les unités d’analyse ;
- les métriques ;
- les paramètres ;
- les erreurs du modèle ;
- les cas ambigus ;
- les contre-exemples ;
- les dénominateurs ;
- la stabilité d’un résultat ;
- la cohérence entre tableau, figure et texte source.

## Questions de validation à prévoir

- Le résultat peut-il être reproduit avec la même configuration ?
- Les documents ou unités analysés sont-ils les bons ?
- Les exclusions sont-elles documentées ?
- Une erreur de préparation pourrait-elle expliquer le résultat ?
- Le résultat dépend-il fortement d’un seuil ou paramètre particulier ?
- Quelques documents dominent-ils la tendance observée ?
- Les contextes textuels confirment-ils l’interprétation ?
- Les contre-exemples modifient-ils la conclusion ?
- La méthode répond-elle réellement à la question ?

---

# 13. Articulation avec les résultats et l’article

| Élément | Emplacement |
|---|---|
| Sortie intermédiaire | `chaine/05_analyse/sorties_intermediaires/` |
| Contrôle de sortie | `chaine/06_validation/` |
| Tableau final | `resultats/tableaux/` |
| Figure finale | `resultats/figures/` |
| Extraits contextualisés | `resultats/extraits/` |
| Description dans l’article | `article/article_imrad.md` |
| Réflexion sur une décision | `journal/journal_de_bord.md` |

Chaque résultat présenté dans l’article doit pouvoir être retracé :

```text
article
    ↓
résultat final
    ↓
sortie intermédiaire
    ↓
script ou protocole
    ↓
configuration
    ↓
données préparées
    ↓
transformations documentées
    ↓
documents sources
```

---

# 14. Journal de recherche associé

Les décisions importantes doivent être consignées dans :

```text
../../journal/journal_de_bord.md
```

Documenter notamment :

- les méthodes envisagées puis rejetées ;
- les paramètres modifiés ;
- les résultats inattendus ;
- les analyses exploratoires ;
- les erreurs de code ou de données ;
- les changements de question ;
- les problèmes de comparaison ;
- les retours au texte ;
- les contre-exemples ;
- les changements de modèle ;
- les usages de LLM ou d’IA ;
- les raisons de conserver ou d’abandonner une analyse.

## Exemple d’entrée de journal

```markdown
## YYYY-MM-DD — Révision de l’analyse principale

### Observation

La première analyse comparait les fréquences brutes des catégories entre
deux sous-corpus de tailles très différentes.

### Problème

Les fréquences brutes ne permettent pas de comparer directement les deux
groupes, car le nombre de phrases analysées varie fortement.

### Options envisagées

1. Conserver les fréquences brutes.
2. Comparer des proportions par sous-corpus.
3. Réduire les sous-corpus à une taille identique.
4. Comparer les paires de documents plutôt que les sous-corpus agrégés.

### Décision

Nous retenons l’option 2 pour l’analyse descriptive principale et
l’option 4 comme analyse secondaire lorsque des paires sont disponibles.

### Justification

Les proportions permettent une première comparaison des distributions,
tandis que l’analyse par paires respecte la relation entre documents
associés.

### Contrôle prévu

Vérifier les dénominateurs, examiner les distributions par document et
contrôler des extraits contextualisés.

### Conséquences

Le plan d’analyse et les sorties attendues sont révisés. Les limites de
comparaison seront discutées dans l’article.
```

---

# Checklist avant de passer à la validation

- [ ] Chaque analyse est reliée à une question ou sous-question.
- [ ] Les données, unités et versions utilisées sont documentées.
- [ ] Les méthodes sont justifiées.
- [ ] Les paramètres importants sont versionnés.
- [ ] Les scripts ou procédures sont identifiables.
- [ ] Les sorties intermédiaires sont nommées clairement.
- [ ] Les résultats principaux, secondaires et exploratoires sont distingués.
- [ ] Les dénominateurs, unités et filtres sont connus.
- [ ] Les tableaux et figures peuvent être reliés à leurs données sources.
- [ ] Les usages de LLM ou d’IA sont documentés.
- [ ] Les contrôles nécessaires sont planifiés.
- [ ] Les limites de méthode sont explicitées.
- [ ] Les décisions et résultats inattendus sont consignés dans le journal.
- [ ] Les sorties sont prêtes pour `06_validation/`.