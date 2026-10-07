# Conception du corpus

Ce dossier documente la conception du corpus avant l’acquisition complète
des documents.

Il traduit la question de recherche en décisions explicites sur :

```text
question de recherche
    ↓
population documentaire visée
    ↓
genres, sources et périodes pertinents
    ↓
critères d’inclusion et d’exclusion
    ↓
stratégie d’échantillonnage
    ↓
métadonnées à conserver
    ↓
corpus pilote
    ↓
corpus final envisagé
```

L’objectif est de répondre aux questions suivantes :

> **Quels documents doivent être étudiés pour répondre à la question de recherche ?**

> **Quelle population documentaire le corpus cherche-t-il à représenter ou à décrire ?**

> **Quels critères permettent d’inclure ou d’exclure un document ?**

> **Quelles comparaisons le corpus doit-il rendre possibles ?**

> **Quelles limites de couverture, d’accès ou de représentativité doivent être reconnues avant l’analyse ?**

> **Principe :** un corpus n’est pas une collection de textes disponibles.  
> Il est un échantillon construit pour rendre une question de recherche observable.

---

## Structure du dossier

```text
02_conception_du_corpus/
├── README.md
├── plan_corpus.md
├── protocole_selection.md
├── criteres_inclusion_exclusion.md
├── sources_candidates.csv
├── plan_echantillonnage.md
├── plan_metadonnees.md
├── corpus_pilote.md
└── evaluation_faisabilite.md
```

| Fichier | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique la logique de conception du corpus | Oui |
| `plan_corpus.md` | Décrit le corpus visé et sa relation à la question | Oui |
| `protocole_selection.md` | Décrit la procédure de sélection des documents | Oui |
| `criteres_inclusion_exclusion.md` | Définit les règles d’inclusion et d’exclusion | Oui |
| `sources_candidates.csv` | Répertorie les sources documentaires examinées | Oui |
| `plan_echantillonnage.md` | Documente les groupes, comparaisons et tailles visées | Oui |
| `plan_metadonnees.md` | Définit les métadonnées nécessaires | Oui |
| `corpus_pilote.md` | Documente la collecte et l’examen d’un premier échantillon | Oui |
| `evaluation_faisabilite.md` | Évalue les accès, limites et plans de secours | Oui |

Tous les fichiers ne doivent pas être remplis intégralement dès le début.
Leur contenu évolue après le corpus pilote et avant l’acquisition
définitive.

---

# 1. Relation avec la question de recherche

La conception du corpus dépend de la question formulée dans :

```text
../01_question_et_cadre/question_recherche.md
```

Avant de sélectionner des documents, rappeler :

| Élément | Décision issue de l’étape 01 |
|---|---|
| Objet d’étude | [Phénomène langagier ou discursif étudié] |
| Question principale | [Question de recherche] |
| Sous-questions | [Sous-questions éventuelles] |
| Concepts centraux | [Concepts à opérationnaliser] |
| Unité d’analyse | [Document, section, paragraphe, phrase, paire, etc.] |
| Comparaison envisagée | [Genres, périodes, langues, publics ou institutions] |
| Hors périmètre | [Ce que le projet ne cherche pas à établir] |

> Le corpus n’a pas à représenter « tout le domaine » ou « toute la
> langue ». Il doit être adéquat à une population documentaire et à une
> question explicitement définies.

---

# 2. Population documentaire visée

La population documentaire désigne l’ensemble théorique des documents
auxquels le projet cherche à se rapporter.

Elle est différente du corpus effectivement constitué.

```text
Population visée
    ↓
Documents accessibles ou repérés
    ↓
Documents éligibles
    ↓
Corpus pilote
    ↓
Corpus final
```

## Exemple

```markdown
### Population documentaire visée

Les communiqués institutionnels en français publiés entre 2020 et 2025
par des universités ou organismes de recherche et associés à des articles
scientifiques portant sur [sous-domaine].

### Corpus effectivement observé

Les paires article–communiqué pour lesquelles :

- un lien explicite est disponible ;
- les deux documents sont accessibles ;
- la langue est le français ;
- le texte est suffisamment extractible ;
- les métadonnées nécessaires peuvent être récupérées.
```

## Délimitation de la population

Pour définir une population documentaire, préciser :

| Dimension | Questions à traiter |
|---|---|
| Domaine | Quel domaine ou sous-domaine est étudié ? |
| Activité ou pratique | Quelle activité spécialisée est concernée ? |
| Producteurs | Quelles personnes, institutions ou communautés produisent les documents ? |
| Destinataires | Quels publics sont visés ou présupposés ? |
| Genres | Quels types de documents sont retenus ? |
| Langue(s) | Quelles langues sont étudiées ? |
| Période | Quelle période est couverte ? |
| Espace ou institution | Quels pays, organisations ou plateformes sont concernés ? |
| Support | Documents écrits, pages Web, PDF, transcriptions, données structurées ? |
| Relations documentaires | Les documents doivent-ils être associés en paires, réseaux ou séries ? |

---

# 3. Plan de corpus

Le fichier principal de cette étape est :

```text
plan_corpus.md
```

## Gabarit

```markdown
# Plan de corpus

## Titre provisoire du corpus

[Nom descriptif du corpus.]

## Version

[Ex. : plan_v0.1]

## Question de recherche associée

> [Question principale.]

## Population documentaire visée

[Description de la population.]

## Corpus effectivement visé

[Description précise des documents à collecter.]

## Domaine ou activité spécialisée

[Description.]

## Langue(s)

[Description.]

## Période

[Date de début et date de fin.]

## Genres documentaires

| Genre | Producteur | Destinataire présumé | Fonction principale | Rôle dans le projet |
|---|---|---|---|---|
| [Genre A] | [Producteur] | [Public] | [Fonction] | [Sous-corpus ou comparaison] |
| [Genre B] | [Producteur] | [Public] | [Fonction] | [Sous-corpus ou comparaison] |

## Unité documentaire

[Article, rapport, note, décision, communiqué, page Web, etc.]

## Unité d’analyse

[Document, section, phrase, paragraphe, paire de documents, contexte de citation, etc.]

## Comparaisons prévues

[Décrire les comparaisons nécessaires pour répondre à la question.]

## Taille visée

[Nombre indicatif de documents, paires, mots, phrases ou segments.]

## Justification de la taille

[Justifier la taille en fonction de la question, de l’unité d’analyse,
de la diversité des documents, du temps disponible et de la méthode.]

## Limites anticipées

[Décrire les limites de couverture, de disponibilité, de langue,
de genre, de période ou de métadonnées.]
```

---

# 4. Critères d’inclusion et d’exclusion

Les critères doivent être définis avant la collecte complète, puis
révisés de manière transparente après le pilote si nécessaire.

Le fichier correspondant est :

```text
criteres_inclusion_exclusion.md
```

## Gabarit

```markdown
# Critères d’inclusion et d’exclusion

## Critères d’inclusion

Un document est retenu s’il respecte tous les critères obligatoires :

| Critère | Règle | Justification |
|---|---|---|
| Domaine | [Règle] | [Lien avec la question] |
| Langue | [Règle] | [Lien avec la question] |
| Période | [Règle] | [Lien avec la question] |
| Genre | [Règle] | [Lien avec la comparaison] |
| Source | [Règle] | [Fiabilité ou accès] |
| Texte exploitable | [Règle] | [Nécessité méthodologique] |
| Métadonnées | [Règle] | [Nécessité analytique] |
| Relation documentaire | [Règle] | [Si documents appariés] |

## Critères d’exclusion

Un document est exclu lorsqu’il :

| Critère | Exemple | Conséquence |
|---|---|---|
| Hors domaine | [Exemple] | Exclure |
| Hors période | [Exemple] | Exclure |
| Doublon | [Exemple] | Conserver une version documentée |
| Texte incomplet | [Exemple] | Exclure ou signaler |
| Langue non étudiée | [Exemple] | Exclure |
| Métadonnées insuffisantes | [Exemple] | Exclure ou classer à vérifier |
| Accès non autorisé | [Exemple] | Ne pas collecter ou redistribuer |
| Relation incertaine | [Exemple] | Exclure de l’analyse appariée |

## Cas limites

[Décrire les cas nécessitant une décision humaine.]

## Procédure en cas de doute

1. Attribuer le statut `a_verifier` dans l’inventaire.
2. Documenter la difficulté dans `donnees/exclusions.csv` ou
   `donnees/inventaire.csv`.
3. Discuter la décision avec l’équipe.
4. Consigner une modification importante dans le journal.
5. Mettre à jour les critères si la règle générale doit changer.
```

---

# 5. Échantillonnage et comparaisons

Le corpus ne doit pas être équilibré en général ; il doit être équilibré
ou contrasté **par rapport à la question de recherche**.

Par exemple :

- un corpus de normes techniques n’a pas nécessairement besoin de
  documents de vulgarisation ;
- une étude de médiation des savoirs doit souvent comparer plusieurs
  genres ou publics ;
- une étude diachronique doit documenter les périodes comparées ;
- une étude multilingue doit définir les unités comparables entre langues ;
- une étude de citation peut nécessiter des documents contenant des
  références exploitables.

La représentativité n’est pas une propriété binaire. Elle dépend de la
population définie, des variations pertinentes pour la question et des
procédures de sélection. Elle peut être améliorée par une définition
explicite de la population, un échantillonnage raisonné, des strates
documentaires et un pilote permettant de réviser le plan. [324][330]

Le fichier correspondant est :

```text
plan_echantillonnage.md
```

## Gabarit

```markdown
# Plan d’échantillonnage

## Type d’échantillonnage

- [ ] Exhaustif dans une population délimitée
- [ ] Aléatoire
- [ ] Stratifié
- [ ] Raisonné
- [ ] Par quotas
- [ ] Par paires documentaires
- [ ] Par disponibilité documentée
- [ ] Autre : [préciser]

## Justification

[Expliquer pourquoi cette stratégie est appropriée à la question.]

## Strates ou sous-corpus

| Sous-corpus | Critère de définition | Taille visée | Rôle analytique |
|---|---|---:|---|
| [A] | [Critère] | [n] | [Comparaison] |
| [B] | [Critère] | [n] | [Comparaison] |
| [C] | [Critère] | [n] | [Comparaison] |

## Unités comparées

[Préciser si la comparaison porte sur documents, phrases, paires,
institutions, périodes, langues ou autres unités.]

## Règles d’équilibre ou de contrôle

[Décrire les dimensions dont la répartition doit être surveillée :
genre, source, période, taille des documents, langue, institution, etc.]

## Limites

[Décrire les dimensions qui ne peuvent pas être équilibrées ou
contrôlées.]
```

---

# 6. Sources candidates

Le fichier suivant recense les sources évaluées avant la collecte :

```text
sources_candidates.csv
```

## Structure minimale

```csv
id_source;nom;type_source;url;documents_disponibles;langues;periode;mode_acces;conditions_utilisation;metadonnees_disponibles;statut;raison_decision;date_consultation
S001;Nom de la source;base_de_donnees;[https://exemple.org;articles](https://exemple.org;articles) scientifiques;fr;2020-2025;ouvert;a_verifier;titre_date_auteur;candidate;source pertinente;YYYY-MM-DD
S002;Nom de la source;site_institutionnel;[https://exemple.org;communiques;fr;2020-2025;ouvert;a_verifier;titre_date_url;candidate;source](https://exemple.org;communiques;fr;2020-2025;ouvert;a_verifier;titre_date_url;candidate;source) à tester;YYYY-MM-DD
```

## Statuts possibles

| Statut | Signification |
|---|---|
| `candidate` | Source repérée, mais non encore testée |
| `pilote_en_cours` | Source utilisée pour le corpus pilote |
| `retenue` | Source retenue pour la collecte |
| `ecartee` | Source non retenue |
| `a_verifier` | Source ou condition d’accès incertaine |
| `inaccessible` | Source non accessible ou non utilisable |
| `restreinte` | Source accessible sous conditions particulières |

> Les informations d’accès, licences et conditions de réutilisation
> doivent être vérifiées avant la collecte complète. Une URL publique ne
> signifie pas automatiquement que les documents peuvent être moissonnés,
> redistribués ou transmis à un service externe.

---

# 7. Plan de métadonnées

Les métadonnées sont les informations nécessaires pour comprendre,
retrouver, sélectionner, comparer et interpréter les documents.

Le fichier correspondant est :

```text
plan_metadonnees.md
```

## Métadonnées minimales recommandées

| Champ | Description | Nécessaire ? |
|---|---|:---:|
| `id_document` | Identifiant stable du document | Oui |
| `id_source` | Identifiant de la source | Oui |
| `titre` | Titre du document | Oui |
| `url` ou référence | Localisation ou référence stable | Oui |
| `date_publication` | Date attribuée par la source | Oui, si période pertinente |
| `date_collecte` | Date de récupération | Oui |
| `langue` | Langue du document | Oui |
| `genre` | Type de document | Oui |
| `producteur` | Auteur, institution ou organisme | Selon la question |
| `destinataire_presume` | Public visé ou présupposé | Selon la question |
| `sous_corpus` | Groupe comparatif | Oui si comparaison |
| `id_paire` | Relation entre documents associés | Si appariement |
| `conditions_acces` | Droit, licence ou restriction | Oui |
| `statut` | Retenu, exclu, à vérifier, doublon | Oui |
| `fichier_source` | Nom du fichier brut ou source | Oui si fichier local |
| `fichier_prepare` | Nom du fichier préparé | Oui après préparation |

## Règles de métadonnées

- Les identifiants doivent être stables.
- Les dates utilisent le format ISO `YYYY-MM-DD`.
- Les valeurs catégorielles doivent être normalisées.
- Les informations inconnues sont codées explicitement, par exemple
  `inconnu`, `non_disponible` ou cellule vide selon la règle choisie.
- Les décisions de catégorisation doivent être documentées.
- Les métadonnées nécessaires à une comparaison doivent être collectées
  avant l’analyse, lorsque possible.
- Les données personnelles inutiles à l’étude ne doivent pas être
  collectées.

Les définitions exactes des colonnes seront transférées dans :

```text
donnees/dictionnaire_metadonnees.md
```

---

# 8. Corpus pilote

Un corpus pilote est un petit échantillon de documents collecté avant la
constitution complète du corpus.

Il permet de vérifier :

- la disponibilité réelle des documents ;
- l’extraction du texte et des métadonnées ;
- la pertinence des critères ;
- l’existence de variations inattendues ;
- la qualité des métadonnées ;
- la faisabilité de l’appariement ;
- la taille des documents ;
- la pertinence de l’unité d’analyse ;
- les premières difficultés d’annotation ou de traitement.

Le corpus pilote ne doit pas être présenté comme le corpus final.

Le fichier correspondant est :

```text
corpus_pilote.md
```

## Gabarit

```markdown
# Corpus pilote

## Objectif

[Préciser ce que le pilote doit vérifier.]

## Date

[YYYY-MM-DD]

## Documents inclus

| ID | Source | Genre | Langue | Statut | Raison de l’inclusion |
|---|---|---|---|---|---|
| [D001] | [Source] | [Genre] | [Langue] | Pilote | [Raison] |

## Taille

- Nombre de documents : [n]
- Nombre de paires, si pertinent : [n]
- Taille approximative : [nombre de mots ou de segments]

## Vérifications réalisées

| Élément | Procédure | Résultat | Conséquence |
|---|---|---|---|
| Accès | [Procédure] | [Résultat] | [Décision] |
| Extraction | [Procédure] | [Résultat] | [Décision] |
| Métadonnées | [Procédure] | [Résultat] | [Décision] |
| Critères | [Procédure] | [Résultat] | [Décision] |
| Unité d’analyse | [Procédure] | [Résultat] | [Décision] |

## Révisions apportées au plan de corpus

[Décrire les changements décidés après le pilote.]

## Décision

- [ ] Passer à la collecte complète
- [ ] Réviser les critères
- [ ] Changer de source
- [ ] Réduire le périmètre
- [ ] Reformuler la question
- [ ] Abandonner ou remplacer le projet
```

---

# 9. Évaluation de la faisabilité

Le fichier correspondant est :

```text
evaluation_faisabilite.md
```

## Gabarit

```markdown
# Évaluation de la faisabilité

## Accès aux données

| Élément | État | Risque | Solution ou plan de secours |
|---|---|---|---|
| Source A | [État] | [Risque] | [Solution] |
| Source B | [État] | [Risque] | [Solution] |

## Ressources techniques

| Besoin | État | Risque | Solution |
|---|---|---|---|
| Extraction de PDF | [État] | [Risque] | [Solution] |
| Annotation linguistique | [État] | [Risque] | [Solution] |
| Stockage | [État] | [Risque] | [Solution] |
| Logiciel ou bibliothèque | [État] | [Risque] | [Solution] |

## Ressources temporelles

| Étape | Charge estimée | Risque | Solution |
|---|---:|---|---|
| Sélection | [Temps] | [Risque] | [Solution] |
| Acquisition | [Temps] | [Risque] | [Solution] |
| Préparation | [Temps] | [Risque] | [Solution] |
| Annotation | [Temps] | [Risque] | [Solution] |
| Analyse | [Temps] | [Risque] | [Solution] |

## Aspects juridiques et éthiques

- [ ] Les conditions d’accès aux sources ont été consultées.
- [ ] Les droits de réutilisation ou de redistribution ont été examinés.
- [ ] Les données personnelles éventuelles ont été repérées.
- [ ] Les données sensibles sont évitées ou font l’objet d’une procédure autorisée.
- [ ] Les documents ne seront pas transmis à un service externe sans vérification préalable.
- [ ] Les données non partageables seront documentées sans être déposées publiquement.

## Décision de faisabilité

[Décrire la décision : poursuivre, réviser, réduire, changer de source
ou reformuler la question.]
```

---

# 10. Représentativité, équilibre et portée

Le corpus doit être décrit avec prudence.

Éviter :

```text
Ce corpus est représentatif de la communication scientifique.
```

Préférer :

```text
Ce corpus est conçu pour décrire [phénomène] dans [population
documentaire délimitée], selon les critères de sélection explicités.
```

ou :

```text
Le corpus permet une comparaison exploratoire entre [sous-corpus A]
et [sous-corpus B], mais ne représente pas l’ensemble des documents
produits dans ce domaine.
```

La taille seule ne rend pas un corpus représentatif. La définition de la
population, les catégories documentaires, la stratégie de sélection, les
métadonnées et les variations pertinentes pour la question doivent être
considérées avant le nombre de mots ou de documents. [324][328]

## Questions de contrôle

- Quelle population le corpus cherche-t-il à décrire ?
- Quels documents restent hors du corpus ?
- Pourquoi les genres retenus sont-ils pertinents ?
- Quelles variations sont importantes pour la question ?
- Quelles variations ne sont pas couvertes ?
- Les sous-corpus sont-ils comparables ?
- Les différences observées pourraient-elles s’expliquer par une
  variable non contrôlée ?
- Quelle généralisation le corpus permet-il raisonnablement ?
- Quelle généralisation doit être évitée ?

---

# 11. Articulation avec les autres dossiers

| Dossier | Rôle par rapport à la conception du corpus |
|---|---|
| `01_question_et_cadre/` | Définit la question et les concepts guidant la sélection |
| `03_acquisition/` | Met en œuvre la collecte selon le plan de corpus |
| `04_preparation/` | Transforme les documents retenus en données analysables |
| `donnees/` | Conserve l’inventaire, les métadonnées et les versions du corpus |
| `configuration/` | Documente les paramètres et sources partageables |
| `06_validation/` | Vérifie les données, métadonnées et choix de corpus |
| `journal/` | Conserve les décisions, révisions et difficultés de conception |
| `article/` | Présente le corpus et ses limites dans les Méthodes |

---

# 12. Journal de recherche associé

Les décisions prises ici doivent être consignées dans :

```text
journal/journal_de_bord.md
```

Le journal doit notamment documenter :

- les sources examinées ;
- les difficultés d’accès ;
- les modifications de période ou de langue ;
- les changements de genre retenu ;
- les documents inattendus ;
- les critères ajoutés ou retirés ;
- les exclusions importantes ;
- les problèmes d’appariement ;
- les modifications du plan après le pilote ;
- les limites reconnues avant l’analyse.

Exemple :

```markdown
## YYYY-MM-DD — Révision du plan de corpus après le pilote

### Observation

Le pilote montre que plusieurs communiqués identifiés ne sont pas liés
de manière suffisamment fiable à un article précis.

### Options envisagées

1. Conserver ces communiqués dans une analyse non appariée.
2. Les inclure dans les paires selon une correspondance thématique.
3. Les exclure de l’analyse appariée et conserver seulement les liens
   explicitement documentés.

### Décision

Nous retenons l’option 3.

### Justification

La question compare des documents associés. Une correspondance seulement
thématique risquerait d’attribuer à une transformation discursive des
différences qui proviennent de recherches distinctes.

### Conséquences

La taille du corpus diminue, mais la validité de la comparaison entre
paires augmente. Le critère d’appariement est ajouté au protocole.
```

---

# Checklist avant de passer à l’acquisition

- [ ] La question de recherche est stabilisée provisoirement.
- [ ] La population documentaire visée est définie.
- [ ] Le corpus effectivement visé est distingué de cette population.
- [ ] Les genres documentaires sont justifiés.
- [ ] Les langues, périodes et sources sont définies.
- [ ] Les unités documentaires et unités d’analyse sont précisées.
- [ ] Les critères d’inclusion sont explicites.
- [ ] Les critères d’exclusion sont explicites.
- [ ] Les cas limites sont identifiés.
- [ ] Les comparaisons ou sous-corpus sont définis.
- [ ] Les métadonnées nécessaires sont prévues.
- [ ] Les sources candidates sont documentées.
- [ ] Un corpus pilote a été réalisé ou planifié.
- [ ] Les accès, droits et conditions d’utilisation ont été examinés.
- [ ] Les limites de couverture sont explicitées.
- [ ] Les principales décisions sont consignées dans le journal.
- [ ] Le plan peut maintenant guider l’étape `03_acquisition/`.