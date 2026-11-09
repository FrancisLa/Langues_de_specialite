# Acquisition des données

Ce dossier documente la récupération effective des documents et métadonnées nécessaires à l’enquête.

L’étape `02_conception_du_corpus/` précise **quels documents viser et pourquoi**. L’acquisition explique **comment les obtenir, ce qui a effectivement été récupéré et comment le vérifier**.

```text
plan de corpus et critères définis à l’étape 02
    ↓
choix et configuration de la procédure d’acquisition
    ↓
test sur un corpus pilote
    ↓
récupération des documents et métadonnées
    ↓
inventaire, échecs et exclusions documentés
    ↓
contrôle des fichiers sources
    ↓
passage à la préparation
```

Les questions centrales sont :

- Comment les documents et métadonnées ont-ils été obtenus ?
- Quelles versions des procédures, quels paramètres et quelles conditions d’accès ont été utilisés ?
- Quels documents ont été récupérés, exclus ou laissés inaccessibles ?
- Quelles traces permettent de vérifier la provenance et de reprendre la collecte ?

> L’acquisition ne redéfinit pas le corpus : elle met le plan à l’épreuve. Si elle impose de modifier une source, un critère ou le périmètre, le plan de corpus est révisé et la décision est justifiée dans le journal de recherche.

## 1. Réutiliser les décisions de conception

Les documents suivants font référence. Ne recopiez pas leur contenu dans ce dossier :

| Document de l’étape 02 | Utilisation pendant l’acquisition |
|---|---|
| `../02_conception_du_corpus/plan_corpus.md` | Périmètre, population documentaire, langues, périodes et unités |
| `../02_conception_du_corpus/protocole_selection.md` | Repérage et sélection des documents |
| `../02_conception_du_corpus/criteres_inclusion_exclusion.md` | Décisions d’éligibilité |
| `../02_conception_du_corpus/sources_candidates.csv` | Répertoire de référence des sources et de leurs identifiants |
| `../02_conception_du_corpus/plan_echantillonnage.md` | Sélection exhaustive ou échantillonnage prévu |
| `../02_conception_du_corpus/plan_metadonnees.md` | Informations recherchées et premiers repères dans les pages |

Les noms, adresses principales et descriptions des sources sont maintenus dans `sources_candidates.csv`. Les vérifications et opérations effectivement réalisées sont consignées ici, avec les mêmes `id_source`.

Lors d’une révision importante, indiquez dans le protocole la version du plan appliquée : date, numéro de version ou identifiant du commit.

## 2. Organisation du dossier

```text
03_acquisition/
├── README.md
├── protocole_acquisition.md
├── journal_acquisition.csv
├── acces_sources.csv
├── code/
│   └── [script ou notebook effectivement utilisé]
├── controles/
│   └── controle_acquisition.md
└── logs/
    └── [journaux techniques, si nécessaires]
```

Cette structure est indicative. Créez seulement les fichiers utiles à votre projet. Un protocole manuel explicite est recevable ; les scripts et notebooks ne sont pas obligatoires pour toutes les enquêtes.

| Élément | Fonction |
|---|---|
| `protocole_acquisition.md` | Explique comment effectuer et reprendre la collecte |
| `acces_sources.csv` | Conserve les vérifications pratiques des conditions d’accès |
| `journal_acquisition.csv` | Résume les sessions de collecte et leurs résultats |
| `code/` | Contient le script ou notebook utilisé, s’il y en a un |
| `controles/controle_acquisition.md` | Décrit le contrôle des fichiers effectivement acquis |
| `logs/` | Conserve les événements détaillés produits par le programme, si utiles |

Les fichiers partagés dans Git doivent être inspectés avant l’envoi : aucun secret, contenu non partageable ou renseignement personnel inutile ne doit y figurer. Les journaux techniques peuvent rester hors de Git selon leur contenu, leur taille et les règles du projet. Vérifiez les règles de `.gitignore`, notamment pour les fichiers `.log`.

### Emplacements communs au projet

```text
donnees/sources/                       fichiers sources non modifiés
donnees/inventaire.csv                 registre des documents repérés
donnees/exclusions.csv                 précisions sur les exclusions, si nécessaires
donnees/dictionnaire_metadonnees.md    définition des champs et valeurs
journal/journal_de_bord.md             décisions et justifications
```

Ces chemins partent de la racine du projet. Depuis ce dossier, on y accède avec `../../donnees/` et `../../journal/`.

Les données sources sont conservées dans un espace autorisé et ne sont pas automatiquement déposées dans Git. Le projet indique leur emplacement et les modalités d’accès ou de vérification permises.

## 3. Choisir une procédure d’acquisition

| Mode | Ce qu’il faut documenter |
|---|---|
| Collecte manuelle | Parcours suivi, adresses, dates, fichiers enregistrés et personne responsable |
| Export | Requête, filtres, date, format et éventuelles limites de l’export |
| API | Documentation, paramètres, pagination, quotas et version de l’interface si disponible |
| Moissonnage | Page de départ, parcours, règles vérifiées, identification du programme, temporisation et gestion des erreurs |
| Corpus existant | Version ou édition, provenance, licence, fichiers récupérés et modalités d’accès |
| Numérisation ou enregistrement | Origine des documents, dispositif, format et conditions d’acquisition |

Privilégiez une API ou un export documenté lorsque cette voie répond aux besoins et est autorisée. Le moissonnage n’est pas obligatoire.

L’OCR, la transcription, l’extraction du texte des HTML ou PDF et le nettoyage relèvent normalement de `04_preparation/`. Si une source fournit directement un texte transcrit ou un export textuel, conservez ce fichier comme source reçue et documentez sa provenance.

## 4. Vérifier les conditions pratiques d’accès

Avant le pilote puis avant la collecte complète, consultez les conditions applicables : accès, licence, téléchargement, réutilisation, redistribution, quotas et transmission éventuelle à un service externe. Enregistrez la date et un lien vers les informations consultées.

Pour le Web automatisé, examinez aussi le fichier `robots.txt` à la racine du domaine lorsque pertinent. Ce fichier indique les règles destinées aux agents automatisés ; il ne remplace pas une autorisation d’accès ni les droits de réutilisation.

### Règles du cours

- Ne contournez pas les restrictions techniques ou les conditions d’accès.
- Si les règles du site interdisent le parcours automatisé, n’effectuez pas ce parcours sans autorisation explicite appropriée.
- L’absence de `robots.txt` n’équivaut pas à une autorisation.
- Un résultat technique autorisant le parcours ne prouve pas que les contenus sont redistribuables.
- La collecte manuelle n’exonère pas du respect des droits et conditions.
- En cas de doute, demandez une clarification à l’enseignant, utilisez une autre voie autorisée ou réduisez le corpus. Ne lancez pas une collecte pour tester les limites du site.

### `acces_sources.csv`

Ce fichier complète le répertoire des sources de l’étape 02 : il ne le remplace pas. Il peut contenir plusieurs vérifications datées pour une même source.

```csv
id_source;date_verification;mode_acquisition;reference_conditions;conclusion_conditions;robots_examen;conclusion_parcours;limites_techniques;responsable;commentaire
S001;YYYY-MM-DD;moissonnage;URL_DES_CONDITIONS;a_verifier;a_verifier;a_verifier;a_verifier;Nom;Collecte non lancée
```

- `conclusion_conditions` : résumé des conditions applicables ou `a_verifier` ; distinguer collecte et redistribution.
- `robots_examen` : `consulte`, `absent`, `inaccessible`, `a_verifier` ou `non_applicable`.
- `conclusion_parcours` : `compatible_avec_regles_consultees`, `interdit`, `incertain` ou `non_applicable` ; préciser dans le commentaire l’agent et les chemins examinés.
- `limites_techniques` : temporisation, quota ou autre contrainte effectivement retenue.

N’indiquez une vérification comme réalisée que si vous l’avez effectuée. Ne déposez aucun identifiant de connexion dans ce tableau.

## 5. Décrire le protocole d’acquisition

Le fichier principal est `protocole_acquisition.md`. Utilisez le gabarit suivant en supprimant les rubriques non pertinentes.

```markdown
# Protocole d’acquisition

## Version et responsables

- Version du protocole : [v0.1]
- Date : [YYYY-MM-DD]
- Responsables : [noms]
- Version du plan de corpus appliquée : [date, version ou commit]

## Entrées

- Plan : [lien vers ../02_conception_du_corpus/plan_corpus.md]
- Critères : [lien vers les critères d’inclusion et d’exclusion]
- Sources utilisées : [id_source du registre des sources de l’étape 02]
- Métadonnées prévues : [lien vers plan_metadonnees.md]

## Mode et paramètres

- Mode d’acquisition : [manuel, export, API, moissonnage, corpus existant]
- Point de départ : [adresse, requête ou référence]
- Paramètres : [filtres, pagination, périmètre technique]
- Conditions vérifiées : [renvoi à acces_sources.csv]
- Code ou outil : [chemin et version, si applicable]
- Environnement requis : [renvoi vers environnement/]

## Procédure reproductible

1. [Ouvrir la source ou lancer la requête prévue.]
2. [Repérer les documents selon le protocole de sélection de l’étape 02.]
3. [Appliquer les critères, sans les redéfinir ici.]
4. [Attribuer ou retrouver l’identifiant stable.]
5. [Récupérer les documents et les métadonnées accessibles.]
6. [Enregistrer les fichiers sources sans les modifier.]
7. [Mettre à jour inventaire.csv et le journal d’acquisition.]
8. [Effectuer le contrôle initial.]

## Erreurs et reprise

[Comment sont signalés les échecs ? Que sauvegarde-t-on ?
Comment reprendre sans tout télécharger de nouveau ?]

## Sorties et stockage

[Emplacement des fichiers sources, inventaire, dictionnaire,
rapport de contrôle et journaux. Distinguer stockage local et Git.]

## Bilan et écarts au plan

[Documents prévus, récupérés, exclus ou inaccessibles ; champs manquants ;
limites. Renvoyer aux traces plutôt que recopier tous les tableaux.]

## Révisions nécessaires

[Liens vers les modifications du plan et les décisions du journal.]
```

### Précisions pour le moissonnage et les API

Selon le cas, indiquez :

- l’identification du programme et les pages ou chemins visés ;
- la temporisation ou les quotas ;
- la pagination et les limites de résultats ;
- les délais d’attente, les conditions d’arrêt et la gestion des échecs ;
- le contrôle du format reçu : une réponse réussie peut être une page d’erreur ou de connexion plutôt que le document attendu ;
- la sauvegarde des résultats et le mécanisme de reprise.

Ne déposez jamais les clés d’API, jetons ou mots de passe dans Git. Utilisez un fichier local ignoré ou un dispositif de secrets adapté. Si vous utilisez `.env` ou une configuration privée, vérifiez leur exclusion dans `.gitignore`. Un fichier d’exemple partageable ne contient que les noms de paramètres et des valeurs fictives ou vides.

## 6. Réaliser le pilote avant la collecte complète

Le pilote teste la procédure sur un petit ensemble choisi pour révéler les difficultés : structure des pages, accès, formats et disponibilité des métadonnées. Il ne démontre pas à lui seul que le corpus final sera complet ou représentatif.

Dans le parcours du cours, `corpus_pilote.md` et `evaluation_faisabilite.md` ont été laissés en attente à la séance de conception. Ils sont renseignés progressivement à partir des démonstrations et essais d’acquisition et de préparation.

Pour éviter de multiplier les comptes rendus :

- décrivez le pilote dans `../02_conception_du_corpus/corpus_pilote.md` ;
- consignez ici les exécutions et leurs résultats dans `journal_acquisition.csv` ;
- mettez à jour `../02_conception_du_corpus/evaluation_faisabilite.md` à partir des constats ;
- réservez le contrôle détaillé de l’extraction du texte aux opérations correspondantes de `04_preparation/`.

Si le pilote impose un changement, mettez à jour le plan ou les critères avant de poursuivre. Ne présentez pas une collecte complète comme validée tant que des conditions essentielles restent non vérifiées.

## 7. Identifier les documents et tenir l’inventaire

### Identifiants stables

Chaque document repéré doit pouvoir être suivi indépendamment de son statut ou de ses différents fichiers. Utilisez un identifiant stable issu de la source ou défini par le projet, par exemple :

```text
D0001
D0002
```

Pour un identifiant issu d’une plateforme, ajoutez un préfixe de source si nécessaire afin d’éviter les collisions. Ne réattribuez pas les identifiants à chaque reprise de collecte.

Les versions HTML et PDF d’un même article partagent l’identifiant du document : elles ne constituent pas deux articles.

```text
D0001_source.html
D0001_source.pdf
```

Si la question exige des paires de documents, ajoutez un `id_paire`. Sinon, ce champ n’est pas nécessaire.

### Inventaire commun

Le registre de référence est `../../donnees/inventaire.csv`. La structure exacte et le sens des champs sont documentés dans `../../donnees/dictionnaire_metadonnees.md`.

Ne recopiez pas la liste des documents dans plusieurs fichiers. Si un registre d’exclusions distinct est utile, reliez-le à l’inventaire par `id_document`.

Exemple minimal de structure — en-tête à adapter :

```csv
id_document;id_source;url;date_collecte;fichier_source;statut_selection;raison_selection;statut_acquisition;conditions_acces;redistribution
```

Les colonnes analytiques prévues à l’étape 02 (titre, langue, numéro, date de publication, genre, etc.) sont ajoutées selon les besoins et les informations effectivement disponibles.

### Distinguer les dimensions de statut

Un document peut être sélectionné, téléchargé, mais non redistribuable. Une seule colonne `statut` ne rend pas ces dimensions clairement. Vous pouvez donc les séparer :

| Dimension | Exemple de colonne | Valeurs possibles |
|---|---|---|
| Éligibilité | `statut_selection` | `retenu`, `exclu`, `a_verifier` |
| Récupération | `statut_acquisition` | `non_tente`, `recupere`, `echec`, `inaccessible` |
| Contrôle du fichier | `statut_controle` | `non_controle`, `conforme`, `incomplet`, `format_inattendu`, `a_verifier` |
| Droit de partage | `redistribution` | `autorisee`, `non_autorisee`, `a_verifier` |
| Usage | `role_corpus` | `pilote`, `principal` |

Ce tableau est un vocabulaire de départ, pas une obligation d’ajouter toutes les colonnes. Ne supprimez pas silencieusement les échecs, les doublons ou les exclusions : conservez une raison et, pour un doublon, le lien vers le document de référence.

Distinguez aussi :

- `date_publication` : date indiquée par la source ;
- `date_collecte` : date de la récupération ;
- les dates inconnues, sans leur substituer la date de consultation.

## 8. Conserver les traces de collecte

### `journal_acquisition.csv`

Ce fichier résume les sessions d’acquisition. L’inventaire contient le détail par document ; il n’est pas recopié dans le journal des sessions.

```csv
id_session;date_heure;id_source;operation;point_depart;nombre_cibles;nombre_recupere;nombre_echec;sortie;version_code_ou_protocole;responsable;commentaire
```

Définissez l’unité des comptes dans le protocole : documents, pages ou fichiers. Ne mélangez pas, dans un même bilan, le nombre d’articles avec le nombre de fichiers HTML et PDF. Si nécessaire, ajoutez des colonnes distinctes.

Pour une collecte manuelle, indiquez la version du protocole à la place de celle du code. Si une source doit être décrite en détail, utilisez son `id_source` plutôt que répéter son nom et son adresse dans tous les tableaux.

### Journaux techniques détaillés

Les programmes peuvent produire des traces plus fines : URL appelée, heure, format reçu, code de réponse, erreur ou nouvelle tentative. Ces traces complètent le bilan des sessions lorsqu’elles sont utiles. Elles ne sont pas obligatoires pour une petite collecte manuelle.

### Journal de recherche

`../../journal/journal_de_bord.md` explique les raisons des décisions, pas la succession de toutes les requêtes.

Exemple construit :

> La procédure repère un lien HTML et un lien PDF pour chaque article. Nous conservons un identifiant d’article unique et distinguons les deux fichiers dans l’inventaire. Cette décision évite de compter deux fois un même article. Nous vérifierons la correspondance sur un petit échantillon.

Un changement de source, de période, de genre ou de critères est expliqué dans le journal et reporté dans le plan de corpus. Les usages substantiels d’outils d’assistance et leurs vérifications y sont également documentés.

## 9. Contrôler l’acquisition avant la préparation

Le contrôle initial porte sur les sources effectivement obtenues. Il est distinct :

- du pilote, qui teste la procédure sur un petit ensemble avant extension ;
- du contrôle d’extraction et de nettoyage, réalisé dans `04_preparation/`.

| Contrôle | Question |
|---|---|
| Concordance | Les fichiers présents correspondent-ils aux entrées de l’inventaire ? |
| Complétude de la collecte | Parmi les documents ciblés, lesquels ont été récupérés et lesquels manquent ? |
| Format | Le fichier annoncé comme PDF ou HTML est-il bien dans ce format ? |
| Intégrité | Le fichier est-il non vide et peut-il être ouvert ? |
| Doublons | Deux URL ou deux fichiers désignent-ils le même document ? |
| Métadonnées | Les champs essentiels ont-ils été obtenus ? Quelles valeurs restent inconnues ? |
| Éligibilité | L’application des critères a-t-elle été respectée ? |
| Provenance | Source, adresse, date de collecte, identifiant et fichier sont-ils reliés ? |
| Stockage | Les originaux sont-ils conservés sans modification dans l’espace prévu ? |

Pour les HTML et PDF, la présence d’un fichier ne garantit pas que le texte pourra être correctement extrait. Cette vérification sera approfondie pendant la préparation.

### Rapport : `controles/controle_acquisition.md`

```markdown
# Contrôle de l’acquisition

## Date et état contrôlé

- Date : [YYYY-MM-DD]
- Version du protocole ou du code : [version ou commit]
- Version ou état de l’inventaire : [référence]

## Périmètre du contrôle

[Nombre de documents ou fichiers contrôlés, ensemble de référence,
mode de choix de l’échantillon, formats et cas particuliers.]

## Vérifications

| Contrôle | Procédure | Résultat observé | Action |
|---|---|---|---|
| [Contrôle] | [Comment vérifier] | [Constat réel] | [Action ou aucune] |

## Bilan

[Échecs, fichiers manquants, doublons, métadonnées absentes.
Renvoyer aux identifiants de l’inventaire.]

## Décision

[Passer à la préparation, compléter la collecte, corriger la procédure
ou réviser le plan de corpus.]
```

Ne remplacez pas un résultat non vérifié par une case cochée. Si un contrôle est reporté, indiquez-le et expliquez sa conséquence.

## 10. Passage à la préparation

Avant de commencer `../04_preparation/`, vérifiez :

- [ ] Le protocole renvoie au plan et aux critères de l’étape 02, sans les recopier.
- [ ] Les conditions d’accès et les usages permis ont été examinés et datés.
- [ ] Le pilote a été documenté, et les révisions nécessaires ont été apportées.
- [ ] Les documents ont des identifiants stables ; les variantes HTML/PDF sont reliées.
- [ ] L’inventaire décrit les documents obtenus, les échecs et les exclusions.
- [ ] Les champs et valeurs de l’inventaire sont définis dans le dictionnaire.
- [ ] Les sources reçues sont conservées sans modification, séparées des données préparées.
- [ ] Un contrôle initial a été réalisé et les anomalies sont documentées.
- [ ] La collecte peut être comprise et reprise à partir du protocole et des traces.
- [ ] Aucun secret ou contenu non partageable n’est envoyé dans Git.
- [ ] Les décisions importantes sont justifiées dans le journal de recherche.

Les traitements d’extraction, d’OCR, de nettoyage, de segmentation et d’annotation sont documentés dans les sous-dossiers pertinents de `04_preparation/`. La provenance des fichiers y est conservée à partir des identifiants définis ici.
