# Préparation des données

Ce dossier documente les transformations qui rendent les documents acquis
exploitables pour l’analyse.

La préparation ne transforme pas seulement des fichiers techniques.
Elle détermine aussi ce qui sera conservé, supprimé, segmenté, annoté ou
représenté dans le corpus.

```text
documents sources
    ↓
extraction du contenu et des métadonnées
    ↓
nettoyage et normalisation
    ↓
segmentation en unités d’analyse
    ↓
annotation ou représentation
    ↓
corpus préparé pour l’analyse
```

L’objectif est de répondre aux questions suivantes :

> **Comment les documents sources ont-ils été transformés en données analysables ?**

> **Quelles informations ont été conservées, séparées, normalisées ou supprimées ?**

> **Quelles transformations peuvent affecter les résultats ou leur interprétation ?**

> **Comment les opérations ont-elles été contrôlées ?**

> **Principe :** le prétraitement n’est pas une opération neutre.  
> Toute transformation peut modifier les données disponibles pour l’analyse
> et doit être justifiée par la question de recherche.

---

## Relation avec les autres étapes

Cette étape reçoit les documents acquis dans :

```text
../03_acquisition/
../../donnees/sources/
```

Elle met en œuvre les besoins identifiés dans :

```text
../01_question_et_cadre/
../02_conception_du_corpus/
```

Elle produit des données nécessaires à :

```text
../05_analyse/
```

Les résultats préparés ou annotés sont stockés, selon les droits
applicables, dans :

```text
../../donnees/intermediaires/
../../donnees/preparees/
```

Les décisions, problèmes, erreurs et révisions importantes sont
consignés dans :

```text
../../journal/journal_de_bord.md
```

---

## Structure du dossier

```text
04_preparation/
├── README.md
├── protocole_preparation.md
├── registre_transformations.csv
│
├── 01_extraction/
│   ├── README.md
│   ├── protocole_extraction.md
│   ├── code/
│   │   └── README.md
│   └── controles/
│       └── README.md
│
├── 02_nettoyage/
│   ├── README.md
│   ├── protocole_nettoyage.md
│   ├── regles_nettoyage.md
│   ├── code/
│   │   └── README.md
│   └── controles/
│       └── README.md
│
├── 03_segmentation/
│   ├── README.md
│   ├── protocole_segmentation.md
│   ├── code/
│   │   └── README.md
│   └── controles/
│       └── README.md
│
└── 04_annotation_ou_representation/
    ├── README.md
    ├── guide_annotation.md
    ├── protocole_representation.md
    ├── code/
    │   └── README.md
    └── controles/
        └── README.md
```

| Élément | Fonction | Versionné dans Git ? |
|---|---|:---:|
| `README.md` | Explique la chaîne générale de préparation | Oui |
| `protocole_preparation.md` | Décrit l’ensemble des transformations | Oui |
| `registre_transformations.csv` | Retrace les versions et sorties de chaque opération | Oui |
| `01_extraction/` | Extrait textes et métadonnées depuis les formats sources | Oui |
| `02_nettoyage/` | Corrige, retire ou sépare des éléments selon des règles explicites | Oui |
| `03_segmentation/` | Définit et produit les unités d’analyse | Oui |
| `04_annotation_ou_representation/` | Ajoute des informations ou produit des caractéristiques analytiques | Oui |
| Données intermédiaires | Fichiers temporaires ou extraits | Selon les droits et le volume |
| Données préparées | Corpus prêt pour l’analyse | Selon les droits et le volume |

---

# 1. Principes de préparation

## 1.1 Préserver les données sources

Les documents sources ne doivent jamais être modifiés directement.

```text
donnees/sources/
    ↓
donnees/intermediaires/
    ↓
donnees/preparees/
```

| Version | Fonction |
|---|---|
| Source | Copie acquise ou téléchargée, préservée dans son état initial |
| Intermédiaire | Sortie d’extraction, conversion ou traitement temporaire |
| Préparée | Données retenues pour l’analyse ou l’annotation |
| Résultat | Tableaux, figures, extraits ou sorties finales dans `resultats/` |

> Toute transformation doit produire une nouvelle version identifiable,
> plutôt qu’écraser silencieusement un fichier source.

---

## 1.2 Préparer selon la question

Les transformations dépendent de la question de recherche.

Exemples :

| Question | Éléments à conserver ou contrôler |
|---|---|
| Étudier les citations | Références, appels de citation, notes et contextes de citation |
| Étudier la structure IMRAD | Titres, sections, sous-sections et ordre des passages |
| Étudier les recommandations | Modalité, verbes, sujets, destinataires et contextes |
| Étudier les termes | Groupes nominaux, lemmes, catégories grammaticales et contextes |
| Étudier la vulgarisation | Reformulations, définitions, analogies et explications |
| Étudier les notes de bas de page | Notes, liens avec le texte principal et emplacement |
| Étudier des genres comparés | Métadonnées de genre, public, source, période et taille |

Une transformation telle que la suppression des références, des tableaux,
des notes ou de la mise en page doit donc être justifiée, car elle peut
supprimer une partie pertinente du phénomène étudié.

---

## 1.3 Documenter les transformations

Chaque opération doit indiquer :

- son objectif ;
- les fichiers d’entrée ;
- les fichiers de sortie ;
- les paramètres ou règles appliqués ;
- la version de code ou de protocole ;
- les contrôles effectués ;
- les erreurs ou limitations connues.

Les transformations sont consignées dans :

```text
registre_transformations.csv
```

### Structure recommandée

```csv
id_transformation;date;etape;entree;sortie;procedure;version_code;parametres;responsable;controle;statut;commentaire
T001;YYYY-MM-DD;extraction;donnees/sources/D0001_source.html;donnees/intermediaires/D0001_extrait.txt;chaine/04_preparation/01_extraction/code/extraction_html.py;abc123;xpath_v1;Nom;controle_10_documents;valide;
T002;YYYY-MM-DD;nettoyage;donnees/intermediaires/D0001_extrait.txt;donnees/preparees/D0001_nettoye.txt;chaine/04_preparation/02_nettoyage/code/nettoyage.py;abc123;regles_v2;Nom;lecture_manuelle;valide;
```

| Colonne | Description |
|---|---|
| `id_transformation` | Identifiant stable de l’opération |
| `date` | Date de l’exécution |
| `etape` | Extraction, nettoyage, segmentation, annotation ou représentation |
| `entree` | Fichier ou jeu de données utilisé |
| `sortie` | Fichier ou jeu de données produit |
| `procedure` | Script, notebook ou protocole appliqué |
| `version_code` | Hash Git, tag ou version de la procédure |
| `parametres` | Fichier de configuration ou résumé des paramètres |
| `responsable` | Personne ou système ayant exécuté l’opération |
| `controle` | Procédure de vérification |
| `statut` | Valide, à vérifier, rejeté, provisoire |
| `commentaire` | Informations complémentaires |

---

# 2. Protocole général de préparation

Le fichier principal de cette étape est :

```text
protocole_preparation.md
```

## Gabarit

```markdown
# Protocole général de préparation

## Version

- Version : [v0.1]
- Date : [YYYY-MM-DD]
- Personnes responsables : [Nom(s)]

## Objectif

[Décrire les données à produire et leur rôle dans l’analyse.]

## Relation avec la question

[Expliquer pourquoi ces transformations sont nécessaires.]

## Données d’entrée

| Jeu de données | Emplacement | Version | Description |
|---|---|---|---|
| [Nom] | [Chemin] | [Version] | [Description] |

## Données de sortie

| Jeu de données | Emplacement | Format | Description |
|---|---|---|---|
| [Nom] | [Chemin] | [Format] | [Description] |

## Étapes réalisées

1. Extraction.
2. Nettoyage.
3. Segmentation.
4. Annotation ou représentation.
5. Contrôle final.

## Décisions importantes

- [Décision de conservation ou suppression]
- [Décision d’unité d’analyse]
- [Décision de modèle ou de représentation]
- [Décision de contrôle]

## Contrôles

[Décrire les contrôles transversaux.]

## Limites

[Décrire les erreurs ou pertes connues.]
```

---

# 3. Extraction

Sous-dossier :

```text
01_extraction/
```

L’extraction transforme des documents sources — HTML, XML, PDF, DOCX,
CSV, JSON, image ou autre format — en contenus structurés ou textuels
exploitables.

```text
HTML / PDF / XML / image / export
    ↓
texte et métadonnées extraits
    ↓
données intermédiaires
```

## Objectifs possibles

- extraire le texte principal ;
- extraire les titres, auteurs, dates et sources ;
- séparer les sections ;
- extraire les références bibliographiques ;
- extraire les notes de bas de page ;
- extraire les tableaux ou légendes ;
- récupérer les métadonnées intégrées à une page ;
- convertir un PDF ou une image en texte ;
- associer un document à un identifiant stable.

## Fichiers attendus

```text
01_extraction/
├── README.md
├── protocole_extraction.md
├── code/
│   ├── README.md
│   └── extraction_[format].[py|R|ipynb]
└── controles/
    ├── README.md
    └── controle_extraction.md
```

## Questions à documenter

- Quel format source est traité ?
- Quel contenu est recherché ?
- Quels éléments sont volontairement exclus ?
- Quel outil ou bibliothèque est utilisé ?
- Quelle règle permet d’identifier le texte principal ?
- Les notes, références, tableaux ou figures sont-ils conservés ?
- Comment les métadonnées sont-elles reliées au texte ?
- Comment l’extraction est-elle contrôlée ?

## Exemple de décision

```markdown
Les titres, auteurs, dates et références sont extraits dans des champs
distincts. Le texte principal est conservé dans un fichier séparé.

Les menus de navigation, publicités et boutons de partage sont retirés,
car ils ne font pas partie du document étudié.

Les notes de bas de page sont conservées dans un champ distinct, car
elles peuvent contenir des justifications ou des sources pertinentes.
```

---

# 4. Nettoyage et normalisation

Sous-dossier :

```text
02_nettoyage/
```

Le nettoyage transforme les données extraites en une forme adaptée à
l’analyse, sans effacer silencieusement des informations pertinentes.

Le nettoyage peut concerner deux niveaux :

| Type de nettoyage | Question | Exemples |
|---|---|---|
| Nettoyage interprétatif | Que considère-t-on comme faisant partie du document ? | Retirer menus, conserver notes, séparer références |
| Nettoyage technique | Que faut-il normaliser pour que les outils fonctionnent ? | UTF-8, espaces, caractères, balises résiduelles |

## Transformations possibles

| Transformation | Exemple | Risque ou précaution |
|---|---|---|
| Encodage | Conversion vers UTF-8 | Vérifier les accents et caractères spéciaux |
| Espaces | Réduire les espaces multiples | Ne pas fusionner des mots ou segments |
| Balises HTML/XML | Retirer les balises résiduelles | Ne pas perdre les sections pertinentes |
| Menus et navigation | Retirer les éléments hors texte | Vérifier que le contenu principal est intact |
| En-têtes et pieds de page | Retirer les répétitions | Vérifier qu’ils ne contiennent pas de métadonnées utiles |
| Doublons | Détecter les documents répétés | Conserver une trace du document original |
| OCR | Corriger les erreurs manifestes | Conserver le texte source et documenter les corrections |
| Casse | Convertir en minuscules | Éviter si la casse a une valeur analytique |
| Ponctuation | Retirer ou normaliser | Éviter si elle sert à la segmentation ou à l’analyse |
| Références | Retirer, conserver ou séparer | Dépend de la question |
| Notes | Retirer, conserver ou séparer | Dépend de la question |
| Tableaux | Retirer, conserver ou extraire | Dépend de la question |

## Règle fondamentale

> Ne supprimer un élément que si la question de recherche, le protocole
> ou une contrainte technique justifie explicitement cette suppression.

## Exemple de règle de nettoyage

```markdown
# Règle N04 — Références bibliographiques

## Décision

Les références bibliographiques sont extraites dans un champ distinct,
mais ne sont pas intégrées au texte principal analysé.

## Justification

La question porte sur les formulations de recommandation dans le corps
des documents. Les références pourraient modifier les fréquences lexicales
sans répondre directement à la question.

## Limite

Cette décision empêche l’étude des fonctions de citation. Si la question
est modifiée pour inclure ces fonctions, les références devront être
réintégrées ou analysées séparément.

## Contrôle

Vérification manuelle de dix documents pour confirmer que les sections de
références sont correctement identifiées et séparées.
```

---

# 5. Segmentation

Sous-dossier :

```text
03_segmentation/
```

La segmentation détermine les unités sur lesquelles l’analyse sera menée.

```text
document
    ↓
section
    ↓
paragraphe
    ↓
phrase
    ↓
token ou groupe de mots
```

L’unité d’analyse doit correspondre à la question.

| Question | Unité d’analyse possible |
|---|---|
| Étudier les genres | Document ou section |
| Étudier la structure IMRAD | Section ou sous-section |
| Étudier les citations | Contexte de citation, phrase ou paragraphe |
| Étudier les recommandations | Phrase ou proposition |
| Étudier des termes | Token, lemme, groupe nominal ou syntagme |
| Étudier l’argumentation | Passage, paragraphe ou séquence argumentative |
| Étudier des paires de documents | Paire article–communiqué ou autre relation documentée |

## Informations à conserver

Chaque unité produite doit pouvoir être reliée :

- au document source ;
- à sa position dans le document ;
- aux métadonnées du document ;
- à une version de préparation ;
- à une éventuelle unité associée.

### Exemple de fichier segmenté

```csv
id_segment;id_document;type_segment;ordre;texte;section;position_debut;position_fin
S0001;D0001;phrase;1;Texte de la première phrase.;introduction;0;35
S0002;D0001;phrase;2;Texte de la deuxième phrase.;introduction;36;87
```

## Contrôles possibles

- vérifier les abréviations ;
- vérifier les titres et listes ;
- vérifier les dates et nombres ;
- vérifier les références ;
- vérifier les citations entre guillemets ;
- vérifier les frontières de phrases ;
- vérifier la conservation des identifiants ;
- comparer un échantillon aux documents sources.

---

# 6. Annotation ou représentation

Sous-dossier :

```text
04_annotation_ou_representation/
```

Cette étape est conditionnelle. Elle dépend de la question et de la
méthode retenues.

Les projets peuvent réaliser :

- une annotation linguistique ;
- une annotation analytique manuelle ;
- une annotation automatique ;
- une représentation lexicale ;
- une représentation vectorielle ;
- une sélection de variables descriptives ;
- une combinaison de plusieurs approches.

> L’annotation et la vectorisation ne sont pas obligatoires pour tous les
> projets. Elles sont retenues seulement lorsqu’elles contribuent à
> répondre à la question.

---

## 6.1 Annotation

L’annotation ajoute des informations aux unités textuelles.

### Types d’annotation possibles

| Type | Exemples |
|---|---|
| Morphologique | Lemme, catégorie grammaticale, traits morphologiques |
| Syntaxique | Dépendances, groupes nominaux, fonctions grammaticales |
| Entités nommées | Personnes, institutions, lieux, dates, organisations |
| Discursive | Section, mouvement rhétorique, fonction de citation |
| Argumentative | Thèse, raison, preuve, objection, conclusion |
| Sémantique | Relation causale, incertitude, recommandation, définition |
| Terminologique | Terme, candidat-terme, variante, relation conceptuelle |
| Métadonnée | Genre, public, institution, période, langue |

### Guide d’annotation

Lorsqu’une annotation analytique est utilisée, créer :

```text
guide_annotation.md
```

Le guide doit contenir :

- les catégories ;
- les définitions ;
- les critères d’inclusion ;
- les critères d’exclusion ;
- les exemples ;
- les contre-exemples ;
- les cas ambigus ;
- les règles de résolution des désaccords ;
- les personnes ou outils responsables ;
- les versions du guide.

### Exemple de structure

```markdown
# Guide d’annotation

## Unité annotée

[Phrase / paragraphe / contexte de citation / autre.]

## Catégories

| Code | Catégorie | Définition | Exemple | Contre-exemple |
|---|---|---|---|---|
| CORR | Corrélation | [Définition] | [Exemple] | [Contre-exemple] |
| CAUS_COND | Causalité conditionnelle | [Définition] | [Exemple] | [Contre-exemple] |
| CAUS_DIR | Causalité directe | [Définition] | [Exemple] | [Contre-exemple] |

## Cas ambigus

[Décrire les cas qui demandent une décision interprétative.]

## Contrôle

[Décrire le double codage, l’analyse d’erreurs ou la validation.]
```

---

## 6.2 Représentation

La représentation transforme les unités textuelles en caractéristiques
exploitables par une analyse.

### Représentations possibles

| Représentation | Description | Usage possible |
|---|---|---|
| Formes | Mots tels qu’ils apparaissent | Fréquences, concordances |
| Lemmatisation | Formes ramenées à un lemme | Réduire la variation flexionnelle |
| Catégories grammaticales | Noms, verbes, adjectifs, etc. | Analyse morphosyntaxique |
| N-grammes | Séquences de mots ou caractères | Phraséologie, classification |
| Groupes nominaux | Syntagmes nominaux | Terminologie, concepts |
| Matrice document-terme | Occurrences par document | Comparaison, clustering |
| TF-IDF | Pondération des formes selon leur distribution | Similarité, classification |
| Embeddings | Vecteurs denses représentant des unités textuelles | Similarité sémantique, regroupement |
| Variables métadonnées | Genre, période, source, langue | Comparaison et contrôle |

### Règles de documentation

Toute représentation doit préciser :

- l’unité représentée ;
- les éléments retenus ;
- les éléments filtrés ;
- les règles de normalisation ;
- les paramètres ;
- le logiciel ou modèle ;
- la version du modèle ;
- le format de sortie ;
- les contrôles ;
- les limites d’interprétation.

---

# 7. Lemmatisation, racinisation et filtrage

Ces opérations peuvent être utiles, mais ne sont jamais automatiques.

## Lemmatisation

La lemmatisation ramène une forme fléchie à une forme canonique.

Exemple :

```text
analysent
analysait
analyseront
    ↓
analyser
```

Elle peut réduire la variation flexionnelle, mais dépend du modèle
linguistique utilisé et peut produire des erreurs.

## Racinisation

La racinisation réduit les mots à une racine approximative.

Exemple :

```text
analyse
analyser
analysant
    ↓
analys
```

Elle peut être utile dans certains traitements statistiques, mais produit
souvent des formes moins interprétables que les lemmes.

## Filtrage

Le filtrage sélectionne ou retire certaines unités.

Exemples :

- conserver seulement les noms et adjectifs ;
- retirer les mots-outils ;
- conserver les phrases contenant une citation ;
- retirer les unités trop courtes ;
- retirer les mots très rares ;
- conserver uniquement les documents en français ;
- exclure les références bibliographiques.

> Un filtre ne doit pas être appliqué par défaut.  
> Il doit être justifié par la question et documenté, car il modifie ce
> qui pourra être observé dans le corpus.

---

# 8. LLM et IA dans la préparation

Les usages de LLM ou d’outils d’IA pendant la préparation doivent être
documentés dans :

```text
../../journal/journal_de_bord.md
```

Ils doivent également être documentés dans :

```text
../../configuration/
```

lorsqu’ils impliquent des paramètres, prompts, modèles ou procédures
partageables.

## Exemples d’usages à documenter

- proposition d’un script d’extraction ;
- génération d’expressions régulières ;
- correction ou normalisation de texte ;
- OCR ou post-correction d’OCR ;
- classification de documents ;
- préannotation de segments ;
- génération d’embeddings ;
- extraction de relations ;
- détection de catégories discursives ;
- résumé ou transformation de données textuelles.

## Documentation minimale

| Élément | Information attendue |
|---|---|
| Outil ou modèle | Nom, fournisseur, version ou date d’accès |
| Tâche | Extraction, correction, annotation, représentation, etc. |
| Données transmises | Description des données ou segments envoyés |
| Prompt ou règle | Prompt complet, gabarit ou description détaillée |
| Sortie | Format et contenu de la sortie produite |
| Vérification | Contrôle humain, échantillon, analyse d’erreurs |
| Décision | Utilisation, correction ou rejet de la sortie |
| Limites | Biais, confidentialité, coût, variabilité ou couverture |

> Ne jamais transmettre à un service externe des documents confidentiels,
> des données personnelles non autorisées ou des contenus sous licence
> restrictive sans avoir vérifié que cet usage est permis.

---

# 9. Contrôle de la préparation

Le contrôle de la préparation porte sur les transformations elles-mêmes,
pas seulement sur les résultats finaux.

## Contrôles minimaux

| Étape | Contrôle recommandé |
|---|---|
| Extraction | Comparer un échantillon au document source |
| Nettoyage | Vérifier les éléments supprimés et conservés |
| Normalisation | Vérifier encodage, accents et caractères spéciaux |
| Déduplication | Vérifier les documents regroupés ou retirés |
| Segmentation | Vérifier les frontières d’unités |
| Annotation manuelle | Double annotation ou discussion des cas ambigus |
| Annotation automatique | Analyse d’erreurs sur un échantillon |
| Lemmatisation | Vérifier les lemmes problématiques |
| Représentation | Vérifier les filtres, dimensions et unités |
| IA ou LLM | Vérifier les sorties et documenter les paramètres |

## Gabarit de contrôle

```markdown
# Contrôle de préparation

## Étape contrôlée

[Extraction / nettoyage / segmentation / annotation / représentation.]

## Version concernée

[Version des données et du code.]

## Échantillon contrôlé

- Nombre de documents : [n]
- Nombre d’unités : [n]
- Méthode d’échantillonnage : [description]

## Critères de contrôle

[Décrire les éléments vérifiés.]

## Résultats

| Élément vérifié | Résultat | Erreur ou limite | Action |
|---|---|---|---|
| [Élément] | [Résultat] | [Problème] | [Correction] |

## Conclusion

[Valider, corriger, reprendre ou limiter l’usage de cette préparation.]
```

---

# 10. Articulation avec les résultats

Les données préparées doivent conserver les informations nécessaires pour
relier un résultat à son origine.

Chaque résultat doit pouvoir être relié :

```text
résultat
    ↓
script ou protocole d’analyse
    ↓
données préparées
    ↓
transformation documentée
    ↓
document source et métadonnées
```

Exemple :

```text
resultats/extraits/extrait_01.md
    ↓
id_segment = S023
    ↓
donnees/preparees/segments.csv
    ↓
chaine/04_preparation/03_segmentation/
    ↓
id_document = D0007
    ↓
donnees/inventaire.csv
    ↓
donnees/sources/D0007_source.pdf
```

---

# 11. Articulation avec les autres dossiers

| Dossier | Relation avec la préparation |
|---|---|
| `01_question_et_cadre/` | Définit les concepts et observables guidant les transformations |
| `02_conception_du_corpus/` | Définit les documents, genres, métadonnées et comparaisons |
| `03_acquisition/` | Fournit les documents sources et leur provenance |
| `05_analyse/` | Utilise les données préparées |
| `06_validation/` | Vérifie la qualité des transformations et leurs effets |
| `07_interpretation/` | Discute les limites liées à la préparation |
| `donnees/` | Conserve les versions sources, intermédiaires et préparées |
| `configuration/` | Conserve les paramètres et règles partageables |
| `environnement/` | Documente les logiciels, bibliothèques et modèles |
| `resultats/` | Conserve les sorties analytiques finales |
| `journal/` | Explique les décisions et révisions de préparation |
| `article/` | Décrit les transformations pertinentes dans les Méthodes |

---

# 12. Journal de recherche associé

Les décisions importantes doivent être consignées dans :

```text
../../journal/journal_de_bord.md
```

Exemples de décisions à documenter :

- conservation ou suppression des notes ;
- conservation ou suppression des références ;
- retrait de menus, publicités ou métadonnées ;
- changement d’encodage ;
- correction d’erreurs OCR ;
- modification de l’unité de segmentation ;
- choix de lemmatisation ou de formes originales ;
- choix d’un modèle linguistique ;
- modification d’un guide d’annotation ;
- changement de filtre lexical ;
- recours à un outil d’IA ;
- erreur d’extraction ;
- reprise d’une transformation après un contrôle.

## Exemple d’entrée de journal

```markdown
## YYYY-MM-DD — Révision des règles de nettoyage

### Observation

Le nettoyage initial supprimait les notes de bas de page avec les
éléments de mise en page. La vérification de cinq documents montre que
certaines notes contiennent des justifications et des références utiles
pour la question de recherche.

### Options envisagées

1. Supprimer toutes les notes.
2. Intégrer toutes les notes au texte principal.
3. Extraire les notes dans un champ distinct lié au document et à la
   section concernée.

### Décision

Nous retenons l’option 3.

### Justification

Cette solution conserve l’information pertinente sans modifier
artificiellement le texte principal. Elle permet une analyse distincte
des notes si cela devient nécessaire.

### Contrôle

Nous vérifions l’extraction des notes dans dix documents sources.

### Conséquences

Le protocole d’extraction et le dictionnaire de métadonnées sont
modifiés. Les limites de l’extraction seront mentionnées dans l’article.
```

---

# Checklist avant de passer à l’analyse

- [ ] Les documents sources sont préservés sans modification directe.
- [ ] Les versions intermédiaires et préparées sont séparées.
- [ ] Les transformations sont consignées dans le registre.
- [ ] Les éléments supprimés ou conservés sont justifiés.
- [ ] L’encodage et la lisibilité des textes ont été vérifiés.
- [ ] Les métadonnées restent liées aux documents préparés.
- [ ] Les unités d’analyse sont définies et identifiables.
- [ ] Les règles de segmentation sont documentées.
- [ ] Les annotations ou représentations sont justifiées.
- [ ] Les modèles linguistiques et paramètres sont documentés.
- [ ] Les usages de LLM ou d’IA sont documentés dans le journal.
- [ ] Les contrôles de préparation ont été réalisés.
- [ ] Les erreurs et limites connues sont documentées.
- [ ] Les données préparées sont prêtes pour `05_analyse/`.