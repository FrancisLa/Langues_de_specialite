# Configuration du projet

Ce dossier contient les paramètres nécessaires à l’exécution de la chaîne de recherche.

La configuration permet de séparer :

1. les **paramètres partageables**, qui décrivent le projet et doivent être versionnés ;
2. les **paramètres locaux**, qui dépendent de l’ordinateur ou du compte d’un membre de l’équipe ;
3. les **secrets**, qui ne doivent jamais être déposés dans Git.

> **Règle générale :** le code ne doit pas contenir directement de chemins personnels, mots de passe, clés API, jetons d’accès ou identifiants privés.

---

## Structure attendue

```text
configuration/
├── README.md
├── config.example.yml
├── sources.example.yml
├── categories.yml
└── config.yml                 # Local et ignoré par Git
```

| Fichier | Rôle | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique la configuration du projet | Oui |
| `config.example.yml` | Modèle public à copier et adapter | Oui |
| `sources.example.yml` | Exemple de description des sources | Oui |
| `categories.yml` | Catégories, règles ou paramètres analytiques partagés | Oui |
| `config.yml` | Configuration locale de chaque poste | Non |
| `.env` | Variables sensibles ou identifiants d’accès | Non |

Les fichiers locaux ou sensibles doivent apparaître dans le fichier `.gitignore` à la racine du projet :

```gitignore
/configuration/config.yml
.env
.env.*
!.env.example
```

---

## Mise en route

Chaque membre de l’équipe doit créer sa propre configuration locale à partir du modèle :

```bash
cp configuration/config.example.yml configuration/config.yml
```

Sous Windows PowerShell :

```powershell
Copy-Item configuration/config.example.yml configuration/config.yml
```

Ensuite, modifier `configuration/config.yml` pour indiquer les chemins locaux et, si nécessaire, les paramètres propres au poste de travail.

> Ne jamais modifier directement `config.example.yml` avec des informations personnelles ou sensibles.

---

## Exemple de configuration

### `config.example.yml`

```yaml
# ============================================================
# Configuration locale — modèle à copier vers config.yml
# ============================================================

projet:
  nom: "titre_provisoire_du_projet"
  version_corpus: "v0.1"
  langue_principale: "fr"

chemins:
  # Remplacer ces chemins par ceux de votre ordinateur.
  donnees_sources: "donnees/sources"
  donnees_intermediaires: "donnees/intermediaires"
  donnees_preparees: "donnees/preparees"
  resultats_tableaux: "resultats/tableaux"
  resultats_figures: "resultats/figures"
  resultats_extraits: "resultats/extraits"

corpus:
  inventaire: "donnees/inventaire.csv"
  dictionnaire_metadonnees: "donnees/dictionnaire_metadonnees.md"
  encodage: "utf-8"

preparation:
  supprimer_doublons: true
  conserver_metadonnees: true
  conserver_references: false
  conserver_notes: false
  segmenter_par: "phrase"

annotation:
  activee: false
  guide: "configuration/categories.yml"
  unite: "phrase"

analyse:
  methode: "a_preciser"
  graine_aleatoire: 42
  seuil_minimal: null

reproductibilite:
  version_depot: "a_preciser"
  date_execution: "a_preciser"
```

---

## Paramètres analytiques partagés

Les choix qui ont une incidence sur les résultats doivent être documentés dans des fichiers versionnés.

Par exemple, si le projet comporte une annotation manuelle ou automatique, les catégories peuvent être définies dans `categories.yml`.

### `categories.yml`

```yaml
# ============================================================
# Catégories analytiques du projet
# ============================================================

unite_analyse: "phrase"

categories:
  - id: correlation
    libelle: "Relation corrélationnelle"
    definition: >
      Énoncé qui décrit une association entre deux variables
      sans affirmer explicitement une relation causale.
    exemple: >
      Une association a été observée entre X et Y.
    contre_exemple: >
      X entraîne une augmentation de Y.

  - id: causalite_conditionnelle
    libelle: "Relation causale conditionnelle"
    definition: >
      Énoncé qui formule une relation causale avec une réserve,
      une hypothèse ou une condition explicite.
    exemple: >
      X pourrait contribuer à une augmentation de Y.
    contre_exemple: >
      X entraîne Y.

  - id: causalite_directe
    libelle: "Relation causale directe"
    definition: >
      Énoncé qui affirme qu’un facteur produit, cause ou entraîne
      directement un effet.
    exemple: >
      X entraîne une augmentation de Y.
    contre_exemple: >
      X est associé à Y.

  - id: hors_categorie
    libelle: "Hors catégorie"
    definition: >
      Aucun énoncé pertinent pour la question de recherche
      n’est repéré dans l’unité analysée.
```

Toute modification de ces catégories doit être :

1. expliquée dans le journal de recherche ;
2. enregistrée dans Git ;
3. prise en compte dans la section Méthodes de l’article IMRAD ;
4. accompagnée, si nécessaire, d’une reprise de l’analyse.

---

## Description des sources

Le fichier `sources.example.yml` décrit les sources potentielles et les modalités d’acquisition. Il ne doit pas contenir de mot de passe, de jeton ou de clé API.

```yaml
# ============================================================
# Sources documentaires — modèle
# ============================================================

sources:
  - id: source_01
    nom: "Nom de la plateforme ou de l’institution"
    type: "site_web | base_de_donnees | archive | export_manuel"
    url: "[https://exemple.org](https://exemple.org)"
    documents_recherches: "Articles scientifiques"
    acces: "ouvert | institutionnel | manuel"
    conditions_utilisation: "À vérifier"
    methode_acquisition: "Téléchargement manuel"
    date_consultation: "YYYY-MM-DD"
    remarques: "Aucun secret ou identifiant dans ce fichier."

  - id: source_02
    nom: "Nom de la seconde source"
    type: "base_de_donnees"
    url: "[https://exemple.org](https://exemple.org)"
    documents_recherches: "Communiqués institutionnels"
    acces: "ouvert"
    conditions_utilisation: "À vérifier"
    methode_acquisition: "Export CSV"
    date_consultation: "YYYY-MM-DD"
    remarques: ""
```

Les informations détaillées sur chaque document effectivement retenu figurent dans :

```text
donnees/inventaire.csv
```

---

## Variables sensibles

Les secrets doivent être stockés hors du dépôt, par exemple dans un fichier `.env` ignoré par Git.

### Exemple de `.env.example`

```bash
# Copier ce fichier vers .env, puis compléter les valeurs localement.
# Ne jamais ajouter .env au dépôt.

API_KEY=
API_TOKEN=
DATABASE_PASSWORD=
```

Le fichier `.env.example` peut être versionné, car il ne contient aucune valeur secrète. Le fichier `.env`, lui, doit être ignoré.

Si une clé ou un jeton a été commité par erreur :

1. le considérer comme compromis ;
2. le révoquer ou le renouveler auprès du service concerné ;
3. le retirer du dépôt et de son historique selon les procédures appropriées ;
4. documenter l’incident de manière proportionnée, sans republier le secret.

---

## Chemins locaux

Les chemins doivent être relatifs au dépôt lorsque possible :

```yaml
donnees_sources: "donnees/sources"
```

Préférer ce format à un chemin absolu propre à un ordinateur :

```yaml
# À éviter
donnees_sources: "/Users/nom_utilisateur/Documents/projet/donnees/sources"
```

Les chemins relatifs facilitent la reprise du projet par une autre personne et évitent d’exposer des informations personnelles dans le dépôt.

---

## Paramètres de reproductibilité

Tout paramètre susceptible de modifier les résultats doit être documenté.

Exemples :

| Type de choix | Exemple |
|---|---|
| Sélection du corpus | Période, langue, genre, critères d’inclusion |
| Nettoyage | Suppression des doublons, références, tableaux ou notes |
| Segmentation | Document, section, paragraphe, phrase ou autre unité |
| Annotation | Jeu de catégories, guide, modèle linguistique utilisé |
| Analyse statistique | Seuil, mesure, normalisation, unité de comparaison |
| Apprentissage automatique | Modèle, version, paramètres, graine aléatoire |
| Résultats | Version du corpus et version du dépôt |

Les paramètres ne doivent pas être modifiés silencieusement après l’analyse. Toute modification importante doit être inscrite :

- dans le [journal de recherche](../journal/journal_de_bord.md) ;
- dans le message de commit ;
- dans le protocole de la sous-tâche concernée ;
- dans l’article, si elle affecte les résultats ou leur interprétation.

---

## Vérification avant exécution

Avant de lancer une étape de traitement ou d’analyse :

- [ ] Le fichier `configuration/config.yml` existe localement.
- [ ] Les chemins indiqués existent ou peuvent être créés.
- [ ] Le fichier d’inventaire du corpus est disponible.
- [ ] Les paramètres analytiques correspondent à la version du projet.
- [ ] Les fichiers sensibles sont exclus par `.gitignore`.
- [ ] La version du code utilisée est identifiable avec Git.
- [ ] Les conditions d’accès aux données ont été vérifiées.

---

## Responsabilités

La configuration ne remplace pas le protocole scientifique.

- Le fichier de configuration indique **comment** une opération est exécutée.
- Le journal explique **pourquoi** certains paramètres ont été choisis ou modifiés.
- Le dépôt documente **où** retrouver les données, le code et les sorties.
- L’article IMRAD explique **en quoi** ces choix affectent l’interprétation des résultats.