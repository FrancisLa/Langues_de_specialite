# Documentation du cours

Ce dossier contient les documents communs du cours :

> **Langues de spécialité**

Il rassemble les documents nécessaires à l’enseignement, à l’encadrement des projets et à l’utilisation du dépôt-gabarit :

- syllabus ;
- guides de séance ;
- références communes ;
- conventions de nommage ;
- documents administratifs ou pédagogiques pertinents.

> **Ce dossier ne contient pas les données, journaux, résultats ou articles produits par les équipes étudiantes.**  

---

## Fonction du dossier `docs/`

Le dossier `docs/` répond à la question suivante :

> **Quels documents communs permettent aux étudiants de comprendre le cours, de réaliser leur enquête et d’utiliser le gabarit de dépôt de manière cohérente ?**

Il constitue la documentation pédagogique du dépôt central. Il ne remplace pas :

| Élément | Emplacement approprié |
|---|---|
| Corpus d’une équipe | Dépôt privé de l’équipe, dossier `donnees/` |
| Journal de recherche d’une équipe | Dépôt privé de l’équipe, dossier `journal/` |
| Résultats d’une équipe | Dépôt privé de l’équipe, dossier `resultats/` |
| Article IMRAD d’une équipe | Dépôt privé de l’équipe, dossier `article/` |
| Supports et consignes communs | Ce dossier `docs/` |

---

## Structure du dossier

```text
docs/
├── README.md
│
├── syllabus/
│   ├── README.md
│   ├── syllabus_cours.pdf
│   └── syllabus_cours.docx
│
├── guides/
│   ├── README.md
│   ├── demarrer_un_projet.md
│   ├── utiliser_git_github.md
│   ├── choisir_une_licence.md
│   ├── conventions_nommage.md
│   ├── rediger_un_article_imrad.md
│   └── gerer_donnees_et_acces.md
│
├── references/
│   ├── README.md
│   └── references.bib
│
└── modeles/
    ├── README.md
    ├── modele_question_recherche.md
    ├── modele_plan_corpus.md
    ├── modele_inventaire.csv
    ├── modele_journal_recherche.md
    ├── modele_protocole_annotation.md
    └── modele_article_imrad.md

---

## Contenu des sous-dossiers

### `syllabus/`

Ce dossier contient la version officielle ou de travail du syllabus du cours.

```text
docs/syllabus/
├── README.md
├── syllabus_cours.pdf
└── syllabus_cours.docx
```

| Fichier | Fonction |
|---|---|
| `syllabus_cours.pdf` | Version stable distribuée aux étudiants |
| `syllabus_cours.docx` | Version éditable destinée à l’enseignant |
| `README.md` | Date, version, statut et changements importants |

---

### `guides/`

Ce dossier contient les guides permanents utiles pendant tout le semestre.

```text
docs/guides/
├── demarrer_un_projet.md
├── utiliser_git_github.md
├── choisir_une_licence.md
├── conventions_nommage.md
├── rediger_un_article_imrad.md
└── gerer_donnees_et_acces.md
```

| Guide | Contenu attendu |
|---|---|
| `demarrer_un_projet.md` | Création d’un dépôt, clonage du gabarit, première structure |
| `utiliser_git_github.md` | Commits, branches, dépôts privés, collaborateurs, `.gitignore` |
| `choisir_une_licence.md` | Différence entre code, documentation et données ; choix de licence |
| `conventions_nommage.md` | Noms de fichiers, versions, identifiants de documents et de résultats |
| `rediger_un_article_imrad.md` | Attentes pour Introduction, Méthodes, Résultats et Discussion |
| `gerer_donnees_et_acces.md` | Provenance, licences, conditions d’accès, données sensibles et partage |

---

### `references/`

Ce dossier contient les références communes du cours.

```text
docs/references/
└── references.bib
```

---

### `modeles/`

Ce dossier contient des fichiers que les étudiants peuvent copier et adapter dans leur dépôt privé.

```text
docs/modeles/
├── modele_question_recherche.md
├── modele_plan_corpus.md
├── modele_inventaire.csv
├── modele_journal_recherche.md
├── modele_protocole_annotation.md
└── modele_article_imrad.md
```

| Modèle | Utilité |
|---|---|
| `modele_question_recherche.md` | Définir objet, question, sous-questions, périmètre et hors-périmètre |
| `modele_plan_corpus.md` | Décrire sources, genres, critères et unités d’analyse |
| `modele_inventaire.csv` | Créer un registre de documents et métadonnées |
| `modele_journal_recherche.md` | Documenter décisions, alternatives, contrôles et conséquences |
| `modele_protocole_annotation.md` | Définir catégories, exemples, contre-exemples et procédures |
| `modele_article_imrad.md` | Structurer le texte final |


## Licence et réutilisation

### Code et gabarits techniques

Les scripts et gabarits techniques sont distribués sous licence MIT. Voir :

```text
../LICENSE
```

### Documents pédagogiques originaux

Les README, guides, fiches, présentations et documents pédagogiques originaux sont distribués sous licence CC BY 4.0. Voir :

```text
../LICENSE-DOCS.md
```

- [ ] Le document ne contient pas d’information privée ou sensible.
- [ ] La version PDF est présente si le document doit être distribué.
- [ ] Le fichier est référencé dans le README pertinent.
- [ ] Les documents remplacés sont archivés ou supprimés de manière justifiée.
- [ ] Le commit décrit clairement la modification.
