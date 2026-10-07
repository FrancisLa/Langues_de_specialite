# Acquisition des données

Ce dossier documente l’acquisition des documents et métadonnées qui
composeront le corpus.

L’acquisition est l’étape où le plan de corpus devient un ensemble de
données effectivement disponibles pour l’enquête.

```text
plan de corpus
    ↓
sources retenues
    ↓
acquisition des documents et métadonnées
    ↓
inventaire des documents obtenus
    ↓
contrôle initial
    ↓
données sources prêtes pour la préparation
```

L’objectif est de répondre aux questions suivantes :

> **Comment les documents et métadonnées ont-ils été obtenus ?**

> **De quelles sources proviennent-ils, à quelle date et selon quelles conditions ?**

> **Quels documents prévus ont effectivement été récupérés, lesquels ont été exclus et lesquels sont restés inaccessibles ?**

> **Quelles traces permettent de vérifier la provenance des données ?**

> **Principe :** l’acquisition ne consiste pas seulement à télécharger
> des fichiers. Elle doit préserver la provenance, les conditions d’accès,
> l’identification des documents et les décisions ayant conduit à leur
> inclusion ou exclusion.

---

## Relation avec les autres étapes

Cette étape met en œuvre les décisions prises dans :

```text
../01_question_et_cadre/
../02_conception_du_corpus/
```

Elle fournit les données sources nécessaires à :

```text
../04_preparation/
```

Les documents et métadonnées effectivement acquis sont inventoriés dans :

```text
../../donnees/inventaire.csv
../../donnees/exclusions.csv
../../donnees/dictionnaire_metadonnees.md
```

Les décisions, difficultés et révisions importantes sont consignées dans :

```text
../../journal/journal_de_bord.md
```

---

## Structure du dossier

```text
03_acquisition/
├── README.md
├── protocole_acquisition.md
├── journal_acquisition.csv
├── sources_consultees.csv
├── code/
│   ├── README.md
│   ├── telecharger_documents.py
│   ├── extraire_metadonnees.py
│   └── verifier_telechargements.py
├── controles/
│   ├── README.md
│   ├── controle_acquisition.md
│   └── controle_echantillon.csv
└── logs/
    ├── README.md
    └── acquisition_YYYY-MM-DD.log
```

| Élément | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique l’étape d’acquisition | Oui |
| `protocole_acquisition.md` | Décrit les sources, procédures et conditions d’accès | Oui |
| `journal_acquisition.csv` | Consigne les exécutions ou sessions de collecte | Oui |
| `sources_consultees.csv` | Recense les sources consultées et leur statut | Oui |
| `code/` | Scripts d’acquisition ou d’extraction de métadonnées | Oui |
| `controles/` | Vérifications et contrôles d’un échantillon | Oui |
| `logs/` | Journaux techniques de collecte | Selon leur taille et sensibilité |
| Documents sources | Données brutes acquises | Selon les droits et la taille |

Les documents sources eux-mêmes sont généralement stockés dans :

```text
../../donnees/sources/
```

Ce dossier est souvent exclu de Git avec `.gitignore`, notamment lorsque
les documents sont volumineux, sous droits, soumis à abonnement ou non
redistribuables.

---

# 1. Modes d’acquisition

Les documents peuvent être obtenus de différentes manières.

| Mode | Description | Exemple | Documentation requise |
|---|---|---|---|
| Collecte manuelle | Téléchargement ou copie contrôlée par une personne | Télécharger un rapport institutionnel | Date, URL, personne, statut |
| Export | Téléchargement structuré depuis une plateforme | Export CSV depuis une base | Requête, filtres, date, format |
| API | Récupération automatisée via une interface de programmation | Requête vers une base bibliographique | Endpoint, paramètres, date, code |
| Moissonnage | Collecte automatisée de pages accessibles | Extraction de pages institutionnelles | URL de départ, règles, code, rythme |
| Corpus existant | Réutilisation d’un corpus déjà constitué | Corpus ouvert documenté | Version, licence, provenance |
| Numérisation | Transformation de documents physiques ou images | OCR de documents numérisés | Source, outil, paramètres, qualité |
| Transcription | Création de texte à partir d’audio, vidéo ou image | Transcription d’entretiens | Procédure, outil, révision, droits |

Le choix du mode dépend :

- de la question de recherche ;
- des conditions d’accès ;
- des droits de réutilisation ;
- de la structure des données disponibles ;
- du volume de documents ;
- des métadonnées nécessaires ;
- des ressources techniques et temporelles du projet.

> Une méthode techniquement possible n’est pas nécessairement autorisée,
> appropriée ou proportionnée au projet.

---

# 2. Protocole d’acquisition

Le fichier principal de cette étape est :

```text
protocole_acquisition.md
```

## Gabarit

```markdown
# Protocole d’acquisition

## Version

- Version du protocole : [v0.1]
- Date : [YYYY-MM-DD]
- Personnes responsables : [Nom(s)]

## Objectif

[Décrire les documents et métadonnées à acquérir.]

## Relation avec la question de recherche

[Expliquer pourquoi ces sources et documents sont nécessaires.]

## Sources retenues

| ID source | Nom | Type | URL ou référence | Mode d’accès | Statut |
|---|---|---|---|---|---|
| S001 | [Nom] | [Base / site / archive] | [URL] | [Ouvert / institutionnel] | [Retenue] |
| S002 | [Nom] | [Base / site / archive] | [URL] | [Ouvert / institutionnel] | [Retenue] |

## Documents recherchés

[Décrire les documents attendus selon le plan de corpus.]

## Métadonnées à collecter

- Identifiant stable ;
- Titre ;
- Source ;
- URL ou référence ;
- Date de publication ;
- Date de collecte ;
- Langue ;
- Genre ;
- Producteur ou institution ;
- Sous-corpus ;
- Conditions d’accès ;
- Relation avec un autre document, si pertinente.

## Procédure

### Étape 1 — Recherche ou repérage

[Décrire la requête, les filtres, mots-clés, catégories ou pages de départ.]

### Étape 2 — Vérification de l’éligibilité

[Décrire comment les critères d’inclusion et d’exclusion sont appliqués.]

### Étape 3 — Acquisition

[Décrire le téléchargement, export, API, moissonnage ou autre procédure.]

### Étape 4 — Attribution d’un identifiant

[Décrire le format des identifiants, par exemple `D0001`, `D0002`, etc.]

### Étape 5 — Enregistrement des métadonnées

[Décrire comment `inventaire.csv` est complété.]

### Étape 6 — Contrôle initial

[Décrire les vérifications : fichiers présents, encodage, format,
doublons, métadonnées, taille, relation entre documents.]

## Fichiers produits

| Fichier | Emplacement | Description |
|---|---|---|
| Documents sources | `donnees/sources/` | Fichiers bruts acquis |
| Inventaire | `donnees/inventaire.csv` | Registre des documents |
| Exclusions | `donnees/exclusions.csv` | Documents non retenus |
| Journal technique | `chaine/03_acquisition/logs/` | Traces automatisées, si pertinent |
| Journal de recherche | `journal/journal_de_bord.md` | Décisions méthodologiques |

## Limites connues

[Décrire les documents manquants, sources restreintes, métadonnées
incomplètes, erreurs de téléchargement ou limites de couverture.]
```

---

# 3. Sources et conditions d’accès

Les sources retenues doivent être documentées dans :

```text
sources_consultees.csv
```

## Structure recommandée

```csv
id_source;nom;type_source;url;date_consultation;mode_acces;conditions_utilisation;robots_verifie;mode_acquisition;statut;responsable;commentaire
S001;Nom de la source;base_de_donnees;[https://exemple.org;YYYY-MM-DD;ouvert;a_verifier;non_applicable;export_csv;retenue;Nom;Source](https://exemple.org;YYYY-MM-DD;ouvert;a_verifier;non_applicable;export_csv;retenue;Nom;Source) principale
S002;Nom de la source;site_institutionnel;[https://exemple.org;YYYY-MM-DD;ouvert;a_verifier;oui;telechargement_manuel;retenue;Nom;Communiques](https://exemple.org;YYYY-MM-DD;ouvert;a_verifier;oui;telechargement_manuel;retenue;Nom;Communiques)
S003;Nom de la source;site_web;[https://exemple.org;YYYY-MM-DD;restreint;non_autorise;oui;non_effectue;ecartee;Nom;Acces](https://exemple.org;YYYY-MM-DD;restreint;non_autorise;oui;non_effectue;ecartee;Nom;Acces) insuffisant
```

## Champs recommandés

| Colonne | Description |
|---|---|
| `id_source` | Identifiant stable de la source |
| `nom` | Nom de la plateforme, institution ou base |
| `type_source` | Base, site, archive, API, export, collection, etc. |
| `url` | URL de la source ou de la documentation |
| `date_consultation` | Date de consultation au format `YYYY-MM-DD` |
| `mode_acces` | Ouvert, institutionnel, restreint, manuel, API, etc. |
| `conditions_utilisation` | Licence, conditions, restrictions ou statut à vérifier |
| `robots_verifie` | Oui, non, non applicable ou inconnu |
| `mode_acquisition` | Téléchargement, API, export, moissonnage, etc. |
| `statut` | Candidate, retenue, écartée, inaccessible, à vérifier |
| `responsable` | Personne ayant vérifié ou acquis la source |
| `commentaire` | Remarques, problèmes ou justifications |

---

# 4. Conditions d’utilisation, robots.txt et autorisation

Avant toute acquisition, vérifier :

- les conditions d’utilisation de la source ;
- les licences applicables ;
- les conditions d’accès institutionnel ;
- les restrictions de téléchargement ou de redistribution ;
- la présence de données personnelles ;
- les règles propres aux API ;
- les limitations de fréquence ;
- les modalités de citation ou d’attribution ;
- la possibilité de transmettre ou non les données à des services externes.

## Robots Exclusion Protocol

Lorsqu’un projet utilise une collecte automatisée sur le Web, le fichier :

```text
https://[domaine]/robots.txt
```

doit être examiné et documenté, lorsque pertinent.

Le protocole `robots.txt` indique les chemins qu’un opérateur de site
demande aux agents automatisés d’éviter ou peut autoriser à parcourir.
Cependant, il ne constitue pas une autorisation juridique d’accès,
d’extraction, de réutilisation ou de redistribution des contenus. Le RFC
9309 précise explicitement que ces règles ne constituent pas une forme
d’autorisation d’accès. [338]

Par conséquent :

| Situation | Interprétation |
|---|---|
| `robots.txt` autorise un chemin | Cela ne garantit pas que les données peuvent être réutilisées ou redistribuées |
| `robots.txt` interdit un chemin | Ne pas collecter automatiquement sans autorisation explicite ou procédure institutionnelle appropriée |
| Aucun fichier `robots.txt` | Cela ne constitue pas une autorisation implicite |
| Site public | L’accès public ne garantit pas les droits de réutilisation |
| Accès institutionnel | L’accès par abonnement ne garantit pas le droit de redistribuer les documents |

## Règle du cours

En cas de doute :

1. privilégier une API, un export ou une source ouverte ;
2. privilégier la collecte manuelle d’un corpus réduit ;
3. demander une autorisation ou consulter la documentation institutionnelle ;
4. ne pas contourner les restrictions techniques ;
5. ne pas utiliser de compte, clé, identifiant ou jeton dans le code versionné ;
6. documenter la limitation dans le journal ;
7. réduire ou modifier le corpus si nécessaire.

---

# 5. Journal d’acquisition

Le journal technique de collecte est distinct du journal de recherche.

```text
journal_acquisition.csv
```

consigne les opérations de récupération, notamment lorsqu’elles sont
répétables ou automatisées.

## Structure recommandée

```csv
date_heure;id_source;operation;requete_ou_page_depart;nombre_repere;nombre_telecharge;nombre_echec;sortie;version_code;responsable;commentaire
YYYY-MM-DDTHH:MM:SS;S001;export;requete_exemple;100;95;5;donnees/sources/export_YYYY-MM-DD.csv;abc123;Nom;Cinq documents inaccessibles
```

| Colonne | Description |
|---|---|
| `date_heure` | Date et heure de l’opération |
| `id_source` | Source concernée |
| `operation` | Export, téléchargement, API, moissonnage, vérification, etc. |
| `requete_ou_page_depart` | Requête, URL de départ ou description de l’action |
| `nombre_repere` | Nombre de documents identifiés |
| `nombre_telecharge` | Nombre de documents récupérés |
| `nombre_echec` | Nombre d’échecs rencontrés |
| `sortie` | Fichier ou dossier produit |
| `version_code` | Hash de commit ou version du script |
| `responsable` | Personne ou système ayant exécuté l’opération |
| `commentaire` | Détails nécessaires à l’interprétation |

> Le journal technique décrit les opérations.  
> Le journal de recherche explique les raisons méthodologiques des choix,
> difficultés ou révisions importantes.

---

# 6. Attribution d’identifiants

Chaque document acquis doit recevoir un identifiant stable.

## Format recommandé

```text
D0001
D0002
D0003
```

Pour des paires documentaires :

```text
P0001
P0002
```

Exemple :

| `id_document` | `id_paire` | Genre | Description |
|---|---|---|---|
| `D0001` | `P0001` | Article | Article scientifique |
| `D0002` | `P0001` | Communiqué | Communiqué associé |
| `D0003` | `P0002` | Article | Deuxième article scientifique |
| `D0004` | `P0002` | Communiqué | Deuxième communiqué associé |

Les identifiants doivent être attribués au moment de l’acquisition ou
aussitôt après. Ils ne doivent pas changer après le début de la
préparation et de l’analyse.

## Nom de fichier suggéré

```text
D0001_source.pdf
D0001_source.html
D0001_source.xml
D0001_metadonnees.json
D0002_source.html
```

Après préparation :

```text
D0001_prepare.txt
D0001_segments.csv
D0001_annote.csv
```

> Ne pas utiliser le titre intégral du document comme seul nom de fichier :
> il peut être long, contenir des caractères spéciaux, varier dans le
> temps ou révéler inutilement des informations.

---

# 7. Inventaire des documents

L’inventaire principal est stocké dans :

```text
../../donnees/inventaire.csv
```

Chaque document repéré doit recevoir un statut.

| Statut | Signification |
|---|---|
| `retenu` | Document intégré au corpus |
| `a_verifier` | Document nécessitant une vérification |
| `exclu` | Document écarté selon un critère documenté |
| `doublon` | Document dupliquant une autre version |
| `inaccessible` | Document non récupéré ou non accessible |
| `incomplet` | Document récupéré mais insuffisant pour l’analyse |
| `hors_perimetre` | Document hors domaine, période, langue ou genre |
| `non_redistribuable` | Document utilisable sous conditions, mais non partageable |
| `pilote` | Document retenu seulement pour tester le protocole |

Exemple :

```csv
id_document;id_paire;id_source;titre;url;date_publication;date_collecte;langue;genre;statut;raison_statut;fichier_source;conditions_acces
D0001;P0001;S001;Titre de l'article;[https://exemple.org/article;2024-01-15;2026-10-07;fr;article;retenu;respecte](https://exemple.org/article;2024-01-15;2026-10-07;fr;article;retenu;respecte) les criteres;D0001_source.pdf;ouvert
D0002;P0001;S002;Titre du communique;[https://exemple.org/communique;2024-02-02;2026-10-07;fr;communique;retenu;paire](https://exemple.org/communique;2024-02-02;2026-10-07;fr;communique;retenu;paire) documentee;D0002_source.html;ouvert
D0003;;S001;Titre d'un document;[https://exemple.org/document;2023-01-01;2026-10-07;en;article;exclu;langue](https://exemple.org/document;2023-01-01;2026-10-07;en;article;exclu;langue) hors perimetre;D0003_source.pdf;ouvert
```

Les exclusions importantes doivent être détaillées dans :

```text
../../donnees/exclusions.csv
```

---

# 8. Acquisition manuelle

Une collecte manuelle peut être méthodologiquement préférable lorsqu’un
corpus est petit, lorsqu’un accès automatisé est inapproprié, ou lorsque
la relation entre documents exige une vérification interprétative.

## Procédure minimale

```markdown
1. Ouvrir la source documentée.
2. Vérifier que le document répond aux critères.
3. Vérifier les conditions d’accès et de réutilisation.
4. Télécharger ou enregistrer le document, si autorisé.
5. Attribuer un identifiant stable.
6. Enregistrer le fichier dans `donnees/sources/`.
7. Ajouter les métadonnées à `donnees/inventaire.csv`.
8. Consigner les exclusions ou ambiguïtés.
9. Vérifier que le fichier est lisible et non vide.
```

## Informations à enregistrer

- URL ou référence complète ;
- date de consultation ;
- date de téléchargement ;
- nom de fichier ;
- format du document ;
- taille approximative ;
- statut d’accès ;
- relation avec d’autres documents ;
- personne responsable ;
- difficultés rencontrées.

---

# 9. Acquisition par API ou export

Lorsqu’une API ou une fonction d’export est disponible, elle doit être
privilégiée par rapport à une extraction non structurée, si elle répond
aux besoins du projet.

## Documentation minimale

```markdown
## API ou export utilisé

### Source

[Nom de la plateforme.]

### Documentation

[URL de la documentation officielle.]

### Date d’accès

[YYYY-MM-DD]

### Requête ou paramètres

[Décrire les filtres, période, langue, genres, pages ou limites.]

### Pagination ou limites

[Décrire la gestion des résultats multiples.]

### Champs récupérés

[Décrire les métadonnées et contenus récupérés.]

### Fichier de sortie

[Indiquer le fichier ou dossier produit.]

### Conditions d’utilisation

[Décrire les limites de l’API, licences, quotas et restrictions.]

### Reproduction

[Indiquer le script, les variables d’environnement nécessaires et la
commande d’exécution.]
```

## Secrets et clés d’API

Les clés, jetons et mots de passe ne doivent jamais être déposés dans Git.

Utiliser :

```text
.env
configuration/config.yml
```

Ces fichiers doivent être ignorés par Git.

Conserver plutôt :

```text
configuration/.env.example
configuration/config.example.yml
```

Exemple :

```bash
# .env.example
API_KEY=
API_TOKEN=
```

---

# 10. Acquisition par moissonnage

Le moissonnage doit être utilisé seulement lorsqu’il est :

- nécessaire ;
- autorisé ;
- proportionné ;
- documenté ;
- techniquement respectueux de la source ;
- compatible avec les règles du cours et de l’établissement.

## Documentation minimale

```markdown
## Moissonnage

### Domaine de départ

[URL de départ.]

### Pages ou chemins visés

[Décrire les parties du site concernées.]

### Pages ou chemins exclus

[Décrire les exclusions.]

### Agent utilisateur

[Nom ou description de l’agent, si applicable.]

### Rythme des requêtes

[Décrire la temporisation ou la limite appliquée.]

### Date de collecte

[YYYY-MM-DD]

### Nombre de pages visitées

[n]

### Nombre de documents retenus

[n]

### Erreurs

[Décrire les erreurs, redirections ou pages inaccessibles.]

### Conditions d’utilisation

[Décrire les règles vérifiées.]

### Code

[Chemin vers le script.]
```

## Bonnes pratiques minimales

- Préférer les fichiers directement fournis au téléchargement.
- Respecter les limites documentées des API.
- Utiliser des requêtes espacées.
- Éviter les collectes massives non nécessaires.
- Conserver les URL et dates de collecte.
- Ne pas contourner les pages nécessitant une authentification.
- Ne pas tenter de contourner les restrictions d’accès.
- Ne pas collecter de données personnelles non nécessaires.
- Interrompre la collecte si le comportement de la source devient
  incertain ou problématique.
- Documenter les échecs et exclusions.

---

# 11. Contrôle initial de l’acquisition

Avant de préparer les textes, contrôler l’intégrité du corpus source.

Le dossier correspondant est :

```text
controles/
```

## Vérifications minimales

| Contrôle | Question | Exemple de procédure |
|---|---|---|
| Présence | Les fichiers attendus sont-ils présents ? | Comparer inventaire et dossier source |
| Lisibilité | Les fichiers peuvent-ils être ouverts ? | Ouvrir ou lire un échantillon |
| Taille | Des fichiers sont-ils vides ou anormalement petits ? | Vérifier taille et longueur du texte |
| Doublons | Le même document est-il présent plusieurs fois ? | Comparer URL, titre, DOI ou hash |
| Métadonnées | Les champs essentiels sont-ils présents ? | Contrôler l’inventaire |
| Langue | Le document correspond-il à la langue prévue ? | Vérification manuelle ou automatique |
| Genre | Le document correspond-il au genre déclaré ? | Vérification manuelle |
| Appariement | Les documents d’une paire sont-ils réellement associés ? | Vérifier référence, DOI, titre ou lien |
| Encodage | Les caractères sont-ils correctement récupérés ? | Vérifier accents et caractères spéciaux |
| Droits | Le statut d’accès est-il enregistré ? | Vérifier la colonne `conditions_acces` |

## Gabarit de contrôle

```markdown
# Contrôle de l’acquisition

## Date

[YYYY-MM-DD]

## Version du corpus contrôlée

[Version ou identifiant.]

## Taille de l’échantillon contrôlé

[n] documents sur [N] documents.

## Vérifications

| Élément | Procédure | Résultat | Action requise |
|---|---|---|---|
| Fichiers présents | [Procédure] | [Résultat] | [Action] |
| Métadonnées | [Procédure] | [Résultat] | [Action] |
| Doublons | [Procédure] | [Résultat] | [Action] |
| Appariement | [Procédure] | [Résultat] | [Action] |
| Encodage | [Procédure] | [Résultat] | [Action] |

## Problèmes détectés

[Décrire les problèmes.]

## Décision

[Passer à la préparation / corriger / compléter / revoir la source.]
```

---

# 12. Provenance et traçabilité

La provenance comprend l’origine des données, leur mode d’acquisition,
leur date, les personnes ou systèmes impliqués et les transformations
subies.

Les métadonnées de provenance permettent de comprendre pourquoi et
comment les données ont été produites, où et quand elles ont été
collectées, et par qui. Elles contribuent à la vérification, à la
réutilisation et à la reproductibilité des données de recherche.
[340][341]

Pour chaque fichier source, conserver autant que possible :

| Information | Exemple |
|---|---|
| Identifiant de document | `D0001` |
| Source | Nom de l’institution ou de la base |
| URL ou référence | URL stable, DOI ou référence complète |
| Date de publication | `2024-01-15` |
| Date de collecte | `2026-10-07` |
| Mode d’acquisition | Export, téléchargement manuel, API, etc. |
| Fichier source | `D0001_source.pdf` |
| Format source | PDF, HTML, XML, CSV, JSON, TXT |
| Conditions d’accès | Ouvert, institutionnel, restreint |
| Version du script | Hash de commit ou tag |
| Responsable | Personne ou système ayant effectué l’opération |
| Transformations ultérieures | Liens vers les étapes de préparation |

> La provenance doit être enregistrée pendant l’acquisition, et non
> reconstituée uniquement à la fin du projet.

---

# 13. Articulation avec les autres dossiers

| Dossier | Rôle par rapport à l’acquisition |
|---|---|
| `01_question_et_cadre/` | Définit le phénomène et les observables à étudier |
| `02_conception_du_corpus/` | Définit les sources, critères et comparaisons |
| `04_preparation/` | Extrait, nettoie, segmente ou annote les données acquises |
| `donnees/` | Conserve l’inventaire, les métadonnées et les fichiers sources |
| `configuration/` | Contient les paramètres partageables de collecte |
| `environnement/` | Décrit les logiciels nécessaires aux scripts d’acquisition |
| `06_validation/` | Vérifie la qualité des données et de leur provenance |
| `journal/` | Documente les décisions, problèmes et révisions |
| `article/` | Présente l’acquisition et le corpus dans les Méthodes |

---

# 14. Journal de recherche associé

Les décisions méthodologiques importantes doivent être consignées dans :

```text
../../journal/journal_de_bord.md
```

Exemples de décisions à documenter :

- changement de source ;
- source inaccessible ;
- modification de requête ;
- réduction du corpus ;
- exclusion d’un genre ;
- difficulté d’appariement ;
- changement de période ;
- condition d’utilisation limitant la redistribution ;
- décision de passer d’un moissonnage à une collecte manuelle ;
- erreur de téléchargement ou métadonnée manquante ;
- problème d’encodage ;
- transmission ou non de données à un service externe.

Exemple :

```markdown
## YYYY-MM-DD — Abandon d’une source automatisée

### Observation

La source envisagée ne fournit pas d’export structuré et ses conditions
d’utilisation ne permettent pas clairement une collecte automatisée.

### Options envisagées

1. Mettre en place un moissonnage à grande échelle.
2. Demander une autorisation ou un accès institutionnel.
3. Utiliser une source ouverte alternative.
4. Réduire le corpus à une collecte manuelle documentée.

### Décision

Nous retenons l’option 3.

### Justification

La source alternative fournit des métadonnées structurées et des
conditions d’accès plus compatibles avec le projet. Elle permet de
conserver la comparaison nécessaire à la question.

### Conséquences

La population documentaire est modifiée. Cette limite est ajoutée au
plan de corpus et devra être discutée dans l’article.
```

---

# Checklist avant de passer à la préparation

- [ ] Les sources retenues sont documentées.
- [ ] Les conditions d’accès et de réutilisation ont été examinées.
- [ ] Les documents acquis ont reçu des identifiants stables.
- [ ] L’inventaire du corpus est à jour.
- [ ] Les exclusions et documents inaccessibles sont documentés.
- [ ] Les fichiers sources sont séparés des fichiers préparés.
- [ ] Les documents sources ne sont pas modifiés directement.
- [ ] Les métadonnées essentielles ont été récupérées.
- [ ] Les doublons ont été contrôlés.
- [ ] Les fichiers vides, illisibles ou incomplets ont été repérés.
- [ ] Les relations entre documents appariés ont été vérifiées.
- [ ] Les règles de stockage et de partage sont respectées.
- [ ] Les secrets et données sensibles ne sont pas présents dans Git.
- [ ] Les scripts ou protocoles d’acquisition sont documentés.
- [ ] Un contrôle initial a été effectué.
- [ ] Les problèmes importants sont consignés dans le journal.
- [ ] Les données sont prêtes pour `04_preparation/`.