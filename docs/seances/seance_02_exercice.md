# Séance 2 — Question, cadre et vérification du carnet de démarrage

Cours : Langues de spécialité — Enseignant : Francis Lareau

Ce deuxième travail comporte trois volets : documenter l'étape *question et cadre*, explorer le corpus envisagé, puis vérifier que l'environnement de calcul fonctionne pour les opérations des prochaines séances.

Le but n'est pas de figer votre sujet. Il s'agit de produire une première version solide, vérifiable et révisable, et de vous familiariser avec VS Code, avec l'écriture en Markdown et avec le corpus.

Échéance : prochain cours (seance 3).

## 1. Documenter l'étape « question et cadre »

### Matériel de départ

- Le dossier `chaine/01_question_et_cadre/` de votre dépôt et son `README.md`.
- Le document `question_et_cadre_exemple.md`. C'est un exemple construit : il montre le niveau de détail attendu, mais il ne doit pas être copié.
- Votre travail de la séance 1 (`pistes_recherche.md`) et son entrée de journal.

### Fichiers à produire

Dans `chaine/01_question_et_cadre/`, créez ou complétez les fichiers suivants avec VS Code :

| Fichier | Contenu attendu |
|---|---|
| `question_recherche.md` | Objet d'étude, problème, question principale, sous-questions, corpus et unité envisagés, faisabilité, hors périmètre |
| `cadre_conceptuel.md` | Les notions nécessaires, définies à partir de sources |
| `operationnalisation.md` | Le passage des concepts à des observables, avec des règles de décision |
| `bibliographie_initiale.md` | Les références commentées |
| `exemples_preliminaires.md` | Les extraits qui ont orienté le projet (voir la section 2) |

Utilisez les gabarits du `README.md` du dossier. Supprimez les crochets et les consignes une fois chaque rubrique remplie. Si une rubrique ne s'applique pas, écrivez-le et expliquez pourquoi dans votre journal de recherche.

### Ce qu'on attend de chaque fichier

**`question_recherche.md`**

- Une seule question principale, formulée sans outil ni méthode.
- De deux à trois sous-questions.
- Le lien avec les langues et discours de spécialité : domaine, communauté, genre, phénomène.
- Une phrase qui indique si le projet est exploratoire ou s'il teste une hypothèse.
- Une section *Faisabilité* qui reprend la grille du README : corpus, accès, volume, métadonnées, conditions d'utilisation, méthode, validation, équipe.
- Une section *Hors périmètre*.

**`cadre_conceptuel.md`**

- Deux à six concepts, pas plus.
- Pour chacun : une définition de travail, au moins une source réellement consultée, sa pertinence pour la question et ses ambiguïtés.
- Les concepts voisins sont distingués. Par exemple, un thème n'est pas un mot-clé et un mot-clé n'est pas un terme.

**`operationnalisation.md`**

- Un tableau avec les colonnes : concept, définition de travail, observable, unité d'analyse, règle de décision, exemple, cas limite.
- Au moins deux lignes.
- Les règles doivent pouvoir être appliquées par une autre personne sur un petit échantillon.

**`bibliographie_initiale.md`**

- Cinq références pertinentes au minimum, dont au moins une sur le phénomène, une sur le domaine ou le genre étudié et une sur la méthode.
- Chaque entrée du fichier `.md` indique son utilité pour le projet.
- Ne complétez jamais une référence de mémoire : vérifiez l'auteur, l'année, le titre et la source.

### Principes d'écriture

- Titres hiérarchisés avec `#`, `##`, `###`.
- Listes avec `-` et listes numérotées avec `1.`.
- Tableaux Markdown pour l'opérationnalisation.
- Citations avec `>`.
- Fichiers enregistrés en texte brut avec l'extension `.md`. Vérifiez qu'un fichier ne s'appelle pas `.md.txt`.
- Utilisez l'aperçu Markdown de VS Code (`Ctrl + Maj + V`) pour relire le rendu.

> Un fichier plus long n'est pas un meilleur fichier. Visez des textes précis, qu'un lecteur extérieur pourrait suivre.

## 2. Explorer le corpus envisagé

Avant de décider quoi collecter, regardez attentivement ce que vous allez collecter. Cette exploration est manuelle. Elle ne remplace pas la conception du corpus de la séance 3.

### Ce qu'il faut faire

1. Ouvrez la revue ou la source que vous envisagez. Notez son adresse, son domaine et son éditeur.
2. Examinez l'organisation : numéros, volumes, dossiers, rubriques, types de contributions, langues.
3. Ouvrez au moins **dix documents** répartis sur plusieurs numéros ou périodes, et au moins un document par genre de contribution si la revue en propose plusieurs.
4. Repérez les métadonnées disponibles : titre, auteurs, date, numéro, résumé, mots-clés, langue, DOI, URL, format HTML ou PDF.
5. Lisez des passages assez longs pour observer le phénomène étudié, pas seulement les titres et les résumés.
6. Cherchez au moins un cas où l'organisation de la source complique votre projet : numéro thématique, article sans résumé, mots-clés absents, plusieurs langues, document de type particulier.
7. Consultez les conditions d'accès et d'utilisation ([celles de journal.openedition.org](https://amubox.univ-amu.fr/s/WsGHWw7xnq9zK8K) par exemple), ainsi que le fichier `robots.txt` du site ([celui de journal.openedition.org](https://journals.openedition.org/robots.txt) par exemple). Notez les règles pertinentes. N'effectuez aucun moissonnage massif à cette étape.

### Ce qu'il faut consigner dans `exemples_preliminaires.md`

Consignez **au moins cinq exemples**, tous tirés de textes que vous avez lus :

- un exemple typique ;
- un contre-exemple (le phénomène est absent ou différent) ;
- un cas ambigu qui oblige à prendre une décision ;
- deux autres exemples, pris de préférence dans des numéros ou périodes différents.

Pour chaque exemple, utilisez le gabarit du `README.md` du dossier :

```markdown
## Exemple E01

### Source

[Référence, numéro, URL]

### Extrait

> [Court extrait exact, ou paraphrase si l'extrait ne peut pas être reproduit]

### Phénomène observé

[Ce que vous observez]

### Pourquoi cet exemple est-il pertinent ?

[Lien avec l'objet de l'enquête]

### Question ou difficulté soulevée

[Ambiguïté, décision à prendre, règle à préciser]
```

Les exemples ne doivent pas être choisis uniquement parce qu'ils confirment votre intuition. Ne présentez pas une régularité comme établie à partir de quelques cas : à ce stade, vous préparez des vérifications.

### Fiche d'exploration

Ajoutez à la fin de `question_recherche.md`, dans la section *Faisabilité*, un bref bilan de cette exploration :

```markdown
## Bilan de l'exploration du corpus

- Source explorée : [nom, adresse]
- Date de consultation : [AAAA-MM-JJ]
- Documents ouverts : [nombre, répartition]
- Genres de contributions rencontrés : [liste]
- Métadonnées disponibles : [liste]
- Formats disponibles : [HTML, PDF, etc.]
- Conditions d'accès et d'utilisation : [résumé et lien]
- Règles du fichier robots.txt pertinentes : [résumé]
- Difficultés repérées : [liste]
- Décision : [maintenir, réduire, modifier]
```

## 3. Ouvrir et vérifier le carnet `demarrage.ipynb`

Le carnet `demarrage.ipynb` sert à vérifier que votre environnement permet d'exécuter les opérations de codage des prochaines séances. Il ne réalise pas encore d'analyse.

### Ce que le carnet vérifie

- **Section 1.1, environnement de travail :** la date, le système, la version de Python, le fait que vous travailliez en local ou dans Google Colab, et l'emplacement de votre Google Drive.
- **Section 1.2, dossiers et chemins :** que le dossier de votre projet et le dossier de l'opération sont accessibles, puis la définition du dossier de travail.

### Étapes

1. Copiez `demarrage.ipynb` dans le dossier de l'opération de votre dépôt (par exemple `chaine/01_question_et_cadre/`, selon les indications du cours).
2. Ouvrez-le dans Google Colab ou dans VS Code. Si vous utilisez Colab, ouvrez-le depuis votre copie dans Google Drive ou depuis GitHub.
3. Dans la cellule de titre, remplissez les champs : projet, étudiant·e ou équipe, notebook, date, objectif.
4. Section 1.1 :
   - Mettez `IS_LOCAL = False` si vous travaillez dans Colab, ou `IS_LOCAL = True` si vous travaillez sur votre ordinateur.
   - En local, indiquez le chemin de votre dossier Google Drive.
   - Dans Colab, autorisez l'accès à Google Drive lorsque la fenêtre le demande.
   - Exécutez la cellule et vérifiez les informations affichées.
5. Section 1.2 :
   - Remplacez les champs vides par le nom du dossier principal de votre projet.
   - Si votre projet est dans un sous-dossier de Drive (par exemple `GitHub`), ajoutez-le au chemin.
   - Indiquez le sous-dossier de l'opération en cours.
   - Exécutez la cellule. Les messages doivent confirmer que les deux dossiers sont accessibles.
6. Exécutez les cellules **dans l'ordre**, de haut en bas, et attendez la fin de chaque exécution.
7. Enregistrez le carnet dans votre dépôt local, puis faites un commit et un push avec GitHub Desktop.
8. Vérifiez sur GitHub que le fichier est présent.

### Résultats attendus

Les deux cellules s'exécutent sans erreur. Elles affichent la date, le système, la version de Python, l'environnement choisi, la racine de Drive, puis deux messages indiquant que les dossiers sont accessibles.

### Si une erreur apparaît

| Message ou symptôme | Vérification |
|---|---|
| Le dossier du projet est introuvable | Le nom du dossier est-il exact, avec la bonne casse et les bons sous-dossiers ? Le dossier est-il bien dans Google Drive ? |
| Le dossier de l'opération est introuvable | Le sous-dossier existe-t-il dans votre dépôt local ? A-t-il été synchronisé par Drive ? |
| `IS_LOCAL` est faux alors que vous êtes en local | Corrigez la valeur et réexécutez la cellule 1.1 avant la cellule 1.2. |
| Le chemin de Drive est vide ou incorrect | En local, indiquez le chemin réel de Google Drive pour votre système (voir les exemples dans la cellule). |
| L'accès à Drive est refusé dans Colab | Relancez la cellule 1.1 et acceptez l'autorisation avec le compte Google que vous utilisez dans Colab. |
| Une cellule semble ne rien faire | Attendez la fin de l'exécution. Un astérisque indique que la cellule est encore en cours. |

En cas de blocage, notez la cellule, le message exact et la capture d'écran de l'erreur. Ne supprimez pas vos fichiers et ne réinstallez pas tout pour tenter de résoudre le problème. Envoyez-moi ces informations.

### Avant le commit

Les sorties du carnet peuvent contenir des informations personnelles, par exemple le nom d'utilisateur de votre ordinateur dans un chemin. Avant de faire le commit, relisez les sorties. Si elles contiennent des informations que vous ne souhaitez pas partager, effacez-les (*Clear outputs*), puis enregistrez de nouveau.

## 4. Mettre à jour le dépôt et le journal

### Dépôt

1. Faites un *Fetch origin*, puis un *Pull origin* si nécessaire.
2. Enregistrez tous les fichiers de `chaine/01_question_et_cadre/`.
3. Dans GitHub Desktop, vérifiez la liste des fichiers modifiés.
4. Faites un commit avec un message précis, par exemple :

```text
Précise la question, le cadre et les premiers exemples
```

5. Faites un *Push origin*.
6. Vérifiez sur GitHub que les fichiers et le carnet sont présents.

Vous pouvez séparer le travail en plusieurs commits (par exemple un pour la question, un pour la bibliographie, un pour le carnet) si chaque message décrit bien ce qui a été fait. N'en créez pas artificiellement.

### Journal

Ajoutez dans `journal/journal_de_bord.md` au moins **une entrée** pour cette séance et une entrée de plus pour chaque décision importante (changement de question, abandon d'une piste, réduction du périmètre). Chaque entrée contient :

- la date et l'étape ;
- l'observation ou la difficulté rencontrée, avec un exemple si possible ;
- les options envisagées ;
- la décision et sa justification ;
- la vérification effectuée ;
- la conséquence pour la suite ;
- un lien vers la trace : fichier ou commit.

Si vous avez utilisé un outil d'IA de manière substantielle, indiquez l'outil, la fonction, les parties concernées et ce que vous avez vérifié. Une proposition générée n'est pas une observation sur le corpus tant qu'elle n'a pas été contrôlée.

## 5. Checklist

- [ ] J'ai relu `question_et_cadre_exemple.md` sans le copier.
- [ ] `question_recherche.md` contient une question principale, des sous-questions, le lien avec les langues de spécialité, la faisabilité et le hors-périmètre.
- [ ] `cadre_conceptuel.md` définit de deux à quatre concepts à partir de sources consultées.
- [ ] `operationnalisation.md` contient un tableau de règles applicables à un petit échantillon.
- [ ] La bibliographie contient au moins cinq références vérifiées.
- [ ] J'ai ouvert au moins dix documents de mon corpus envisagé.
- [ ] `exemples_preliminaires.md` contient cinq exemples, dont un contre-exemple et un cas ambigu.
- [ ] J'ai consulté les conditions d'accès et le fichier `robots.txt`.
- [ ] J'ai noté le bilan de l'exploration dans la section *Faisabilité*.
- [ ] `demarrage.ipynb` s'exécute sans erreur, ou j'ai noté le message d'erreur exact.
- [ ] J'ai relu les sorties du carnet avant le commit.
- [ ] J'ai fait un commit et un push, puis vérifié le résultat sur GitHub.
- [ ] J'ai ajouté au moins une entrée au journal de bord.

## 6. Pour la séance 3

Apportez :

- votre question principale et votre unité d'analyse provisoire ;
- vos exemples préliminaires, notamment les cas ambigus ;
- vos critères d'inclusion et d'exclusion envisagés ;
- vos questions sur l'accès aux données ;
- votre carnet `demarrage.ipynb` fonctionnel.

Ces productions servent de point de départ à la conception du corpus. Elles peuvent encore être modifiées, à condition que les révisions soient datées et justifiées dans le journal.
