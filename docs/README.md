# Documentation du cours

Ce dossier contient les documents communs du cours :

> **Langues de spécialité**

Il rassemble les documents nécessaires à l’enseignement, à l’encadrement des projets et à l’utilisation du dépôt-gabarit :

- syllabus ;
- guides de séance ;
- présentations ;
- fiches d’activités ;
- guides méthodologiques ;
- références communes ;
- conventions de nommage ;
- documents administratifs ou pédagogiques pertinents.

> **Ce dossier ne contient pas les données, journaux, résultats ou articles produits par les équipes étudiantes.**  
> Ces éléments doivent être conservés dans le dépôt propre à chaque équipe, créé à partir du [gabarit de projet](../gabarit_projet/).

---

## Fonction du dossier `docs/`

Le dossier `docs/` répond à la question suivante :

> **Quels documents communs permettent aux étudiants de comprendre le cours, de réaliser leur enquête et d’utiliser le gabarit de dépôt de manière cohérente ?**

Il constitue la documentation pédagogique du dépôt central. Il ne remplace pas :

| Élément | Emplacement approprié |
|---|---|
| Code et gabarits des projets étudiants | [`../gabarit_projet/`](../gabarit_projet/) |
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
├── activites/
│   ├── README.md
│   ├── exemples_commentes/
│   ├── etudes_de_cas/
│   └── corriges_enseignant/
│
└── modeles/
    ├── README.md
    ├── modele_question_recherche.md
    ├── modele_plan_corpus.md
    ├── modele_inventaire.csv
    ├── modele_journal_recherche.md
    ├── modele_protocole_annotation.md
    └── modele_article_imrad.md
```

Les dossiers de séance sont numérotés avec deux chiffres afin de préserver l’ordre alphabétique :

```text
seance_01/
seance_02/
...
seance_12/
```

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

Le fichier `README.md` du dossier doit notamment préciser :

- la date de dernière mise à jour ;
- la version du syllabus ;
- les informations institutionnelles ;
- les changements apportés depuis la version précédente.

Exemple :

```markdown
# Syllabus du cours

## Statut

- Version : `v0.3`
- Date : `2026-10-07`

## Changements récents

- Ajout des trois livrables : journal, dépôt et article IMRAD.
- Révision de la progression pédagogique.
- Clarification des modalités de travail en équipe.

## Informations à compléter

- Code du cours.
- Crédits.
- Session.
- Horaires.
- Coordonnées institutionnelles.
- Dates de remise.
- Règles institutionnelles applicables.
```

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

Les guides ne doivent pas présumer qu’un étudiant utilise nécessairement Python, R, GitHub public, une base de données payante ou des méthodes d’apprentissage automatique.

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

Ces modèles sont volontairement plus légers que les README du dossier `gabarit_projet/`.

| Modèle | Utilité |
|---|---|
| `modele_question_recherche.md` | Définir objet, question, sous-questions, périmètre et hors-périmètre |
| `modele_plan_corpus.md` | Décrire sources, genres, critères et unités d’analyse |
| `modele_inventaire.csv` | Créer un registre de documents et métadonnées |
| `modele_journal_recherche.md` | Documenter décisions, alternatives, contrôles et conséquences |
| `modele_protocole_annotation.md` | Définir catégories, exemples, contre-exemples et procédures |
| `modele_article_imrad.md` | Structurer le texte final |

---

### `archives/`

Le dossier `archives/` conserve les documents retirés de l’usage courant, mais potentiellement utiles pour comprendre l’évolution du cours.

```text
docs/archives/
├── README.md
├── syllabus_v0.1_2026-09-30.docx
└── seance_01_version_precedente.pdf
```

Ne pas utiliser `archives/` pour les fichiers temporaires, les copies inutiles ou les données brutes. Son rôle est de préserver des versions pédagogiquement ou historiquement pertinentes.

Exemple de `archives/README.md` :

```markdown
# Archives

Ce dossier contient des versions remplacées, mais conservées pour
documenter l’évolution du cours.

Les documents archivés ne constituent pas nécessairement les versions
à utiliser en classe.

| Fichier | Statut | Remplacé par |
|---|---|---|
| `syllabus_v0.1_2026-09-30.docx` | Archive | `../syllabus/syllabus_cours.docx` |
| `seance_01_version_precedente.pdf` | Archive | `../seances/seance_01/guide_enseignant.pdf` |
```

---

## Conventions de nommage

Utiliser des noms de fichiers descriptifs, stables et sans espaces ni accents.

### Format conseillé

```text
[type_document]_[sujet]_[version_ou_date].[extension]
```

Exemples :

```text
syllabus_cours_v1.0.pdf
guide_enseignant_seance_01.docx
presentation_seance_01.pptx
fiches_etudiantes_seance_01.pdf
modele_plan_corpus.md
references_reproductibilite.bib
```

Éviter :

```text
nouveau_syllabus_final_v7_bon.pdf
presentation_corrigee_2.pptx
documentFrancisfinal.docx
test.docx
```

### Dates

Utiliser le format ISO :

```text
YYYY-MM-DD
```

Exemples :

```text
2026-10-07
syllabus_2026-10-07.docx
```

---

## Versions éditables et versions distribuables

Lorsqu’un document existe en plusieurs formats :

| Usage | Format conseillé |
|---|---|
| Version modifiable par l’enseignant | `.docx`, `.pptx`, `.md`, `.qmd` |
| Version stable distribuée aux étudiants | `.pdf` |
| Version accessible en ligne | `.md` ou `.html`, selon les besoins |
| Références | `.bib`, `.ris` ou `.csv` |

Exemple :

```text
docs/seances/seance_01/
├── guide_enseignant.docx
├── guide_enseignant.pdf
├── presentation_seance_01.pptx
└── fiches_etudiantes.pdf
```

La version PDF sert de référence pour la diffusion. La version éditable facilite la révision. Si les deux divergent, indiquer explicitement laquelle est à utiliser en classe.

---

## Licence et réutilisation

### Code et gabarits techniques

Les scripts, gabarits techniques et fichiers de configuration du dépôt sont distribués sous licence MIT. Voir :

```text
../LICENSE
```

### Documents pédagogiques originaux

Les README, guides, fiches, présentations et documents pédagogiques originaux sont distribués sous licence CC BY 4.0. Voir :

```text
../LICENSE-DOCS.md
```

### Ressources tierces

Les licences du dépôt ne s’appliquent pas automatiquement :

- aux articles scientifiques ;
- aux extraits de publications ;
- aux corpus ;
- aux données ;
- aux images ;
- aux logos ;
- aux textes fournis par des institutions ou des tiers ;
- aux travaux des étudiants.

Avant d’ajouter une ressource externe à `docs/`, vérifier :

1. sa licence ;
2. les conditions de citation ;
3. les limites de reproduction ou de redistribution ;
4. la possibilité de fournir un lien plutôt qu’une copie ;
5. les règles institutionnelles applicables.

Pour les ressources sous droits, privilégier :

```markdown
- Une référence complète ;
- Un lien stable ;
- Un court extrait justifié, si autorisé ;
- Une synthèse rédigée par l’enseignant ;
- Des exemples construits explicitement identifiés comme tels.
```

---

## Contribution et mise à jour

### Ajout d’un document

Avant d’ajouter un nouveau fichier :

- [ ] Déterminer son public : enseignant, étudiant ou les deux.
- [ ] Choisir le sous-dossier approprié.
- [ ] Utiliser un nom descriptif.
- [ ] Vérifier les droits de diffusion.
- [ ] Ajouter ou mettre à jour le README du sous-dossier.
- [ ] Ajouter une date ou version si nécessaire.
- [ ] Vérifier que le document ne contient pas de données personnelles ou confidentielles.
- [ ] Produire un PDF stable si le document est destiné aux étudiants.
- [ ] Utiliser un message de commit clair.

### Exemples de messages de commit

```text
Ajoute le syllabus de la session
```

```text
Met à jour le guide enseignant de la séance 1
```

```text
Ajoute un modèle de plan de corpus
```

```text
Archive la version précédente du syllabus
```

```text
Corrige les références méthodologiques
```

### Documents réservés à l’enseignant

Les corrections détaillées, notes personnelles et documents non destinés aux étudiants doivent être séparés clairement :

```text
docs/activites/corriges_enseignant/
```

Si les étudiants disposent d’un accès en écriture au dépôt central, il est préférable de conserver ces documents dans un dépôt privé distinct ou dans un espace institutionnel réservé à l’enseignant.

---

## Rapport avec le gabarit étudiant

Le dossier `docs/` donne les consignes et ressources communes. Le dossier [`../gabarit_projet/`](../gabarit_projet/) fournit la structure que les étudiants doivent copier pour leur propre enquête.

```text
docs/
    ↓
consignes, modèles et ressources pédagogiques
    ↓
gabarit_projet/
    ↓
dépôt privé de chaque équipe
    ↓
journal + données + chaîne + résultats + article
```

Les étudiants ne doivent pas déposer leur corpus, leur journal personnel ou leur article final dans ce dossier central, sauf si l’enseignant met explicitement en place un espace de remise distinct.

---

## Checklist avant la diffusion d’un document

- [ ] Le document porte un titre, une date et une version appropriés.
- [ ] Son public est clairement identifiable.
- [ ] Les consignes sont cohérentes avec le syllabus.
- [ ] Les liens, références et citations ont été vérifiés.
- [ ] Les droits de diffusion ont été examinés.
- [ ] Le document ne contient pas d’information privée ou sensible.
- [ ] La version PDF est présente si le document doit être distribué.
- [ ] Le fichier est référencé dans le README pertinent.
- [ ] Les documents remplacés sont archivés ou supprimés de manière justifiée.
- [ ] Le commit décrit clairement la modification.