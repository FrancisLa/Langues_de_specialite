# Exemple de conception du corpus
## De la question « thèmes d'une revue » au choix du corpus à moissonner

> **Statut :** exemple construit pour les étudiant·es. Il ne présente aucune observation réelle sur une revue et ne doit pas être copié. Les nombres de numéros et d'articles viennent de la sortie du notebook de démonstration du cours (exécuté le 2026-10-08) et sont à recontrôler. Les résultats du pilote de la Partie G sont **fictifs** : ils montrent le niveau de détail attendu, pas ce qu'on trouvera.

Équipe : [Prénom Nom, Prénom Nom]
Date : [AAAA-MM-JJ]
Dossier : `chaine/02_conception_du_corpus/`

Cet exemple prolonge `question_et_cadre_exemple.md`. L'équipe y avait retenu provisoirement la revue *Argumentation et Analyse du Discours* (AAD) pour répondre à la question suivante :

> Quels thèmes structurent les articles de la revue retenue, et comment la présence de ces thèmes varie-t-elle d'un numéro à l'autre ?

La séance 3 transforme ce choix provisoire en **plan de corpus** précis. Chaque décision ci-dessous prépare l'acquisition de la séance 4. Un exemple d'analyse thématique sera présenté plus tard, lors des séances d'analyse : le corpus doit donc seulement rendre cette analyse possible.

---

## Partie A — Rappel de l'étape 01

| Élément | Décision issue de l'étape 01 |
|---|---|
| Objet d'étude | Thèmes et motifs récurrents dans les articles d'une revue spécialisée |
| Question principale | Quels thèmes structurent les articles de la revue, et comment varient-ils d'un numéro à l'autre ? |
| Sous-questions | (1) Quels thèmes dans le texte intégral ? (2) Se retrouvent-ils dans titres, résumés et mots-clés ? (3) Lesquels apparaissent, disparaissent ou se transforment ? |
| Concepts centraux | Thème explicite, thème implicite, évolution thématique |
| Unité d'analyse | L'article (paragraphe envisagé à titre exploratoire) |
| Comparaison envisagée | Entre numéros, regroupés si nécessaire en périodes |
| Hors périmètre | Influence des thèmes, qualité des articles, évolution du champ de l'argumentation en général |

---

## Partie B — `plan_corpus.md`

### Titre provisoire du corpus

Articles de la revue *Argumentation et Analyse du Discours* sur OpenEdition Journals.

### Version

plan_v0.1

### Question de recherche associée

> Quels thèmes structurent les articles de la revue retenue, et comment la présence de ces thèmes varie-t-elle d'un numéro à l'autre ?

### Population documentaire visée

L'ensemble des articles publiés par la revue AAD et accessibles sur sa page OpenEdition Journals, tous numéros confondus.

### Corpus effectivement visé

Les articles de recherche de cette revue pour lesquels le texte intégral (HTML, avec PDF en secours) et les métadonnées essentielles sont accessibles. La liste des numéros et des articles est obtenue à partir de la page de la revue.

### Domaine ou activité spécialisée

Études de l'argumentation et du discours.

### Langue(s)

[À confirmer pendant le pilote. La revue peut contenir des articles dans plusieurs langues ; la langue de chaque article est relevée dans les métadonnées.]

### Période

Du premier au dernier numéro disponible au moment de la collecte : [date du premier numéro] à [date du dernier numéro].

### Genres documentaires

| Genre | Producteur | Destinataire présumé | Fonction principale | Rôle dans le projet |
|---|---|---|---|---|
| Article de recherche | Chercheur·es | Communauté scientifique | Présenter une étude | Cœur du corpus |
| Introduction ou présentation de dossier | Coordinateur·rices de numéro | Lecteurs de la revue | Cadrer un numéro | À examiner au pilote |
| Compte rendu ou note de lecture | [À vérifier] | Lecteurs de la revue | Présenter un ouvrage | À examiner au pilote |

### Unité documentaire

L'article tel que publié sur la page HTML de la revue, avec sa version PDF lorsqu'elle existe.

### Unité d'analyse

L'article entier pour l'inventaire, la comparaison entre numéros et la comparaison entre métadonnées et texte intégral. Le paragraphe est conservé comme unité exploratoire pour l'analyse thématique.

### Comparaisons prévues

- entre numéros ou groupes de numéros ;
- entre les thèmes présents dans les métadonnées et ceux présents dans le texte intégral.

### Taille visée

Environ 37 numéros et 457 articles. À recompter lors de la collecte.

### Justification de la taille

La question porte sur l'évolution entre numéros : une revue complète est plus utile qu'un échantillon de numéros isolés. Le volume reste gérable avec une collecte lente et un contrôle de la qualité. Si le pilote montre qu'il y a trop de variété de genres, la taille sera réduite aux articles de recherche.

### Limites anticipées

- La revue ne représente pas tout le champ de l'argumentation.
- Les numéros thématiques reflètent des choix éditoriaux.
- Le nombre d'articles par numéro peut être inégal.
- Les mots-clés ou résumés peuvent manquer pour certains articles.
- La couverture de l'archive en ligne peut être incomplète.

---

## Partie C — `protocole_selection.md`

1. Ouvrir la page de la revue et noter la liste des numéros.
2. Pour chaque numéro, noter la liste des articles et les liens vers les versions HTML et PDF.
3. Enregistrer l'identifiant, le numéro et les liens dans l'inventaire.
4. Appliquer les critères d'inclusion et d'exclusion (Partie D).
5. Attribuer à chaque document un statut : `retenu`, `exclu` ou `a_verifier`.
6. Consigner les exclusions et les cas incertains dans `donnees/exclusions.csv` et dans le journal.

Ce protocole décrit la sélection. La collecte elle-même (séance 4) suivra le plan d'acquisition et respectera les règles du site.

---

## Partie D — `criteres_inclusion_exclusion.md`

### Critères d'inclusion

Un document est retenu s'il respecte tous les critères obligatoires :

| Critère | Règle | Justification |
|---|---|---|
| Source | Publié dans la revue AAD sur OpenEdition Journals | Population délimitée |
| Genre | Article de recherche | Les thèmes d'un champ se lisent d'abord dans les articles |
| Texte exploitable | Texte intégral disponible en HTML ou en PDF | Sous-question 1 |
| Langue | Langue(s) retenue(s) après le pilote | Comparabilité de l'analyse |
| Métadonnées | Numéro et au moins le titre disponibles | Comparaison entre numéros |

### Critères d'exclusion

| Critère | Exemple | Conséquence |
|---|---|---|
| Hors genre | Compte rendu, éditorial, annonce | Exclure ou signaler |
| Texte incomplet | Page sans corps de texte, PDF vide | Exclure ou signaler |
| Doublon | Même article accessible sous deux liens | Conserver une version documentée |
| Langue non étudiée | Article dans une autre langue | Exclure |
| Accès non autorisé | Contenu à accès restreint | Ne pas collecter |
| Métadonnées insuffisantes | Numéro inconnu | Classer `a_verifier` |

### Cas limites

- Une introduction de dossier qui a la forme d'un article de recherche.
- Un article dont le PDF existe mais dont le texte HTML est incomplet.
- Un article bilingue.

### Procédure en cas de doute

1. Attribuer le statut `a_verifier` dans l'inventaire.
2. Documenter la difficulté dans `donnees/inventaire.csv` ou `donnees/exclusions.csv`.
3. Discuter la décision en équipe.
4. Consigner toute modification importante dans le journal.
5. Mettre à jour les critères si la règle générale change.

---

## Partie E — `sources_candidates.csv`

```csv
id_source;nom;type_source;url;documents_disponibles;langues;periode;mode_acces;conditions_utilisation;metadonnees_disponibles;statut;raison_decision;date_consultation
S001;Argumentation et Analyse du Discours;revue_en_ligne;https://journals.openedition.org/aad;articles scientifiques;a_verifier;tous les numéros;ouvert;a_verifier;titre_auteurs_numero_resume_mots_cles_doi;pilote_en_cours;lien fort avec la question et structure connue par le notebook;AAAA-MM-JJ
S002;Revue d'Anthropologie des Connaissances;revue_en_ligne;https://journals.openedition.org/rac;articles scientifiques;a_verifier;tous les numéros;ouvert;a_verifier;a_verifier;ecartee;lien plus faible avec la question;AAAA-MM-JJ
S003;[Troisième revue de la séance 1];revue_en_ligne;[URL];articles scientifiques;a_verifier;a_verifier;a_verifier;a_verifier;a_verifier;candidate;à examiner si le pilote échoue;AAAA-MM-JJ
```

> Les conditions d'utilisation restent à vérifier. Une adresse publique ne signifie pas automatiquement que les documents peuvent être moissonnés, redistribués ou transmis à un service externe.

---

## Partie F — `plan_echantillonnage.md`

### Type d'échantillonnage

- [x] Exhaustif dans une population délimitée
- [ ] Aléatoire
- [ ] Stratifié
- [ ] Raisonné
- [ ] Par quotas
- [ ] Par paires documentaires
- [ ] Par disponibilité documentée
- [ ] Autre

### Justification

La question porte sur l'évolution de la revue. Un échantillon aléatoire d'articles aurait pu manquer des numéros entiers. La population étant délimitée et de taille raisonnable, nous visons tous les articles retenus.

### Strates ou sous-corpus

| Sous-corpus | Critère de définition | Taille visée | Rôle analytique |
|---|---|---:|---|
| Période 1 | Premiers numéros | [n] | Comparaison |
| Période 2 | Numéros intermédiaires | [n] | Comparaison |
| Période 3 | Derniers numéros | [n] | Comparaison |

Les périodes seront fixées après le pilote, à partir des dates et du nombre d'articles par numéro, afin d'obtenir des groupes de taille comparable.

### Unités comparées

Les articles, regroupés par numéro ou par période.

### Règles d'équilibre ou de contrôle

Surveiller la répartition par numéro, la longueur des articles, la langue et la proportion d'articles sans résumé ou sans mots-clés.

### Limites

La revue ne peut pas être équilibrée : le nombre d'articles par numéro dépend des choix éditoriaux. Les comparaisons entre périodes seront donc exprimées en proportions plutôt qu'en nombres bruts.

---

## Partie G — `plan_metadonnees.md` (provisoire)

| Champ | Description | Nécessaire ? |
|---|---|:---:|
| `id_document` | Identifiant stable de l'article | Oui |
| `id_source` | Identifiant de la source (S001) | Oui |
| `num_url` | Adresse de la page du numéro | Oui |
| `titre` | Titre de l'article | Oui |
| `url_html` | Adresse de la version HTML | Oui |
| `url_pdf` | Adresse du PDF | Si disponible |
| `date_publication` | Date de publication ou du numéro | Oui |
| `date_collecte` | Date de récupération | Oui |
| `langue` | Langue de l'article | Oui |
| `genre` | Type de contribution | Oui |
| `resume` | Résumé | Selon disponibilité |
| `mots_cles` | Mots-clés | Oui (sous-question 2) |
| `acces_html` / `acces_pdf` | Réussite ou échec de la collecte | Oui |
| `statut` | Retenu, exclu, à vérifier, doublon | Oui |
| `fichier_source` | Nom du fichier brut | Oui |
| `fichier_prepare` | Nom du fichier préparé | Après préparation |

### Règles

- Les dates utilisent le format `AAAA-MM-JJ`.
- Les valeurs inconnues sont codées `non_disponible`.
- Aucune donnée personnelle inutile n'est collectée.
- Les définitions détaillées seront transférées dans `donnees/dictionnaire_metadonnees.md`.

---

## Partie H — `corpus_pilote.md` (résultats fictifs, sera effectué lors des séances 4 et 5)

### Objectif

Vérifier, sur un seul numéro, l'accès aux articles, l'extraction du texte et des métadonnées, et la pertinence des critères.

### Date

[AAAA-MM-JJ]

### Documents inclus

Les articles d'un seul numéro, par exemple le premier numéro de l'inventaire du notebook (14 articles).

| ID | Source | Genre | Langue | Statut | Raison de l'inclusion |
|---|---|---|---|---|---|
| [D001] | S001 | [Article] | [fr] | Pilote | Premier article du numéro |
| [D002] | S001 | [Article] | [fr] | Pilote | [Raison] |
| ... | ... | ... | ... | ... | ... |

### Taille

- Nombre de documents : 14
- Taille approximative : [nombre de mots]

### Vérifications réalisées (résultats fictifs, sera effectué lors des séances 4 et 5)

| Élément | Procédure | Résultat (fictif) | Conséquence |
|---|---|---|---|
| Accès | Lecture de `robots.txt`, puis accès avec délai | Les 14 pages HTML sont accessibles | Poursuivre |
| Extraction | Comparaison HTML et PDF pour trois articles | Le texte HTML est plus complet que celui du PDF | HTML comme version principale |
| Métadonnées | Relevé du titre, du résumé et des mots-clés | Deux articles sans mots-clés | Coder `non_disponible` |
| Critères | Application des règles aux 14 articles | Un document est un cas limite | Ajouter une règle |
| Unité d'analyse | Lecture de trois articles | L'article entier est une unité utilisable | Maintenir |

### Révisions apportées au plan de corpus

- Ajout d'une règle pour les introductions de dossier.
- Ajout d'une règle pour les articles sans mots-clés.

### Décision

- [x] Passer à la collecte complète
- [ ] Réviser les critères
- [ ] Changer de source
- [ ] Réduire le périmètre
- [ ] Reformuler la question
- [ ] Abandonner ou remplacer le projet

---

## Partie I — `evaluation_faisabilite.md`

### Accès aux données

| Élément | État | Risque | Solution ou plan de secours |
|---|---|---|---|
| Pages de la revue | Accessibles pour le pilote | Modification de la structure du site | Revérifier avant la collecte |
| Texte HTML | Accessible | Texte partiel pour certains articles | Utiliser le PDF en secours |
| PDF | Disponible pour certains articles | Extraction de mauvaise qualité | Garder le HTML comme version principale |

### Ressources techniques

| Besoin | État | Risque | Solution |
|---|---|---|---|
| Moissonnage lent et poli | Notebook de démonstration | Interdiction ou limite de requêtes | Respecter `robots.txt` et prévoir un délai |
| Stockage | Google Drive | Espace limité | Garder les données hors du dépôt Git |
| Extraction | Bibliothèques du notebook | Erreurs de structure HTML | Journal de collecte et contrôle manuel |

### Ressources temporelles

Estimation de la durée de collecte, avec un délai de 3 secondes entre requêtes, pour 37 pages de numéros et 457 articles en HTML et PDF :

\[ (37 + 457 + 457) \times 3 \text{ s} \approx 2\,853 \text{ s} \approx 48 \text{ min} \]

Cette estimation ne tient pas compte du temps de réponse du serveur. Il est prudent de collecter par blocs de numéros, en sauvegardant l'inventaire régulièrement.

| Étape | Charge estimée | Risque | Solution |
|---|---:|---|---|
| Sélection | [x h] | Cas limites nombreux | Statut `a_verifier` |
| Acquisition | environ 1 h de requêtes | Interruption | Collecte par blocs, reprise à partir de l'inventaire |
| Préparation | [x h] | Texte mal extrait | Contrôle d'un échantillon |
| Analyse | [x h] | Dépend de la méthode | Décidé aux séances suivantes |

### Aspects juridiques et éthiques

- [x] Les conditions d'accès aux sources ont été consultées.
- [ ] Les droits de réutilisation ou de redistribution ont été examinés.
- [x] Les données personnelles éventuelles ont été repérées (noms d'auteurs).
- [x] Les données sensibles sont évitées.
- [ ] Les documents ne seront pas transmis à un service externe sans vérification préalable.
- [x] Les textes collectés ne seront pas déposés publiquement dans le dépôt Git.

### Décision de faisabilité

Poursuivre avec la revue AAD. Réduire au besoin la collecte aux articles de recherche si le pilote montre une trop grande variété de genres.

---

## Partie J — Choix du corpus à moissonner

Cette synthèse relie les décisions de conception à la séance 4 (acquisition).

| Décision de conception | Conséquence pour le moissonnage |
|---|---|
| Population : tous les articles de la revue | Parcourir la page principale, puis chaque numéro |
| Unité documentaire : l'article | Une ligne par article dans l'inventaire |
| Texte principal : HTML | Télécharger d'abord les pages HTML |
| PDF en secours | Télécharger les PDF et vérifier le contenu |
| Métadonnées nécessaires | Extraire titre, date, résumé, mots-clés, langue |
| Accès et conditions | Lire `robots.txt`, s'identifier, ralentir les requêtes |
| Traçabilité | Journal de collecte avec date et statut d'accès |
| Reprise possible | Sauvegarder l'inventaire à intervalle régulier |

**Corpus retenu pour le moissonnage :** la revue *Argumentation et Analyse du Discours*, tous numéros, articles de recherche, avec un pilote préalable sur un numéro.

---

## Partie K — Entrée de journal

### AAAA-MM-JJ — Passage de la revue complète au plan de corpus

**Étape :** conception du corpus.

**Objectif :** décider quelle population documentaire collecter.

**Observation :** la question compare des numéros. Un échantillon aléatoire d'articles risquait de laisser certains numéros sans article.

**Options envisagées :**

1. Collecter un échantillon aléatoire d'articles.
2. Collecter quelques numéros représentatifs.
3. Viser tous les articles de recherche de la revue après un pilote sur un numéro.

**Décision :** option 3.

**Justification :** la population est délimitée et le volume est gérable. Les comparaisons entre périodes demandent tous les numéros.

**Vérification prévue :** collecter les articles d'un numéro, comparer HTML et PDF, relever les métadonnées.

**Conséquence :** la séance 4 préparera la collecte sur la base de ce plan. Les périodes de comparaison seront fixées après le pilote.

**Trace :** `chaine/02_conception_du_corpus/plan_corpus.md`

---

## Checklist avant de passer à l'acquisition

- [ ] La question est stabilisée provisoirement.
- [ ] La population documentaire est distinguée du corpus effectivement visé.
- [ ] Les genres, langues, périodes et sources sont définis.
- [ ] Les critères d'inclusion et d'exclusion sont explicites.
- [ ] Les cas limites et la procédure en cas de doute sont prévus.
- [ ] Les sous-corpus ou comparaisons sont définis.
- [ ] Le plan de métadonnées est établi.
- [ ] Les sources candidates sont documentées avec leur statut.
- [ ] Un corpus pilote est réalisé ou planifié.
- [ ] Les accès, droits et conditions d'utilisation sont examinés.
- [ ] Les limites de couverture sont écrites.
- [ ] Les décisions importantes sont consignées dans le journal.
