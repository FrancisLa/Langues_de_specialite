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
│   └── syllabus_cours.md
│
├── guides/
│   ├── README.md
│   ├── guide_installation_partie_1.md
│   ├── guide_installation_partie_2.md
│   ├── guide_installation_partie_3_facultative.md
│   └── demarrage.ipynb
│
├── references/
│   ├── README.md
│   └── references.bib
│
└── seances/
    ├── README.md
    ├── seance_01_exercice.md
    ├── seance_01_powerpoint.pdf
    ...

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
| `syllabus_cours.md` | Version stable distribuée aux étudiants |
| `README.md` | Date, version, statut et changements importants |

---

### `guides/`

Ce dossier contient les guides permanents utiles pendant tout le semestre.

```text
docs/guides/
├── guide_installation_partie_1.md
├── guide_installation_partie_2.md
├── guide_installation_partie_3_facultative.md
└── demarrage.ipynb
```

| Guide | Contenu attendu |
|---|---|
| `guide_installation_partie_1.md` | Création d’un dépôt, première structure, installation des outils |
| `guide_installation_partie_2.md` | Clonage du gabarit, `.gitignore` |
| `guide_installation_partie_3_facultative.md` | Python en local |
| `demarrage.ipynb` | Code de demarrage |

---

### `references/`

Ce dossier contient les références communes du cours.

```text
docs/references/
└── references.bib
```

---

### `seances/`

Ce dossier contient les exercices et les powerpoints des seances.

```text
docs/seances/
├── seance_01_exercice.md
├── seance_01_powerpoint.pdf
└...
```

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
