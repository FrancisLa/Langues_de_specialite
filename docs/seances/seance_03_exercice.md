# Séance 3 — Conception du corpus et inspection du HTML

Cours : Langues de spécialité — Enseignant : Francis Lareau

Ce troisième travail comporte deux volets : documenter l'étape *conception du corpus* de la chaîne de traitement, puis parcourir votre corpus et inspecter le code HTML de ses pages pour repérer des informations qui ne sont pas visibles à l'écran.

Le but n'est pas de collecter votre corpus. Il s'agit de décider précisément quels documents vous allez collecter, pourquoi, et quelles informations vous pourrez en extraire. Ces décisions guideront la séance 4 (acquisition).

Échéance : prochain cours (séance 4).

## 1. Documenter l'étape « conception du corpus »

### Matériel de départ

- Le dossier `chaine/02_conception_du_corpus/` de votre dépôt et son `README.md`, qui contient les gabarits.
- Le document `conception_corpus_exemple.md`. C'est un exemple construit : il montre le niveau de détail attendu, mais il ne doit pas être copié. Ses résultats de pilote sont fictifs.
- Vos fichiers de la séance 2 dans `chaine/01_question_et_cadre/`, en particulier `question_recherche.md`.

> Principe du README : un corpus n'est pas une collection de textes disponibles. C'est un échantillon construit pour rendre une question de recherche observable.

### Fichiers à produire

Dans `chaine/02_conception_du_corpus/`, créez ou complétez les fichiers suivants avec VS Code :

| Fichier | Contenu attendu |
|---|---|
| `plan_corpus.md` | Le corpus visé, sa relation à la question, la population documentaire, les genres, les langues, la période, l'unité documentaire et l'unité d'analyse, les limites |
| `protocole_selection.md` | La procédure, en étapes, pour repérer et choisir les documents |
| `criteres_inclusion_exclusion.md` | Les règles d'inclusion et d'exclusion, les cas limites et la procédure en cas de doute |
| `sources_candidates.csv` | Les sources examinées, avec leur statut |
| `plan_echantillonnage.md` | La stratégie d'échantillonnage (voir les consignes plus bas) |
| `plan_metadonnees.md` | Les informations à conserver pour chaque document (liste de départ) et les observations de l'inspection du HTML (voir la section 2) |

Les fichiers `corpus_pilote.md` et `evaluation_faisabilite.md` **ne sont pas à produire maintenant**. Ils feront l'objet des démonstrations d'acquisition et de préparation, aux prochaines séances.

Utilisez les gabarits du `README.md` du dossier. Supprimez les crochets et les consignes une fois chaque rubrique remplie. Si une rubrique ne s'applique pas à votre projet, écrivez-le et expliquez pourquoi dans votre journal de recherche.

### Ce qu'on attend de chaque fichier

**`plan_corpus.md`**

- La question principale, recopiée de l'étape 01, pour que le plan reste relié à elle.
- Une distinction claire entre la **population documentaire visée** (tous les documents auxquels vous voulez vous rapporter) et le **corpus effectivement visé** (ceux que vous allez réellement collecter).
- Le ou les genres, la langue, la période et la source.
- L'unité documentaire (l'article, le rapport, la page Web…) et l'unité d'analyse (le document entier, une section, un paragraphe…).
- Une taille visée indicative, avec un raisonnement simple (par exemple le nombre de numéros multiplié par le nombre moyen d'articles par numéro, estimé sur quelques numéros).
- Les limites anticipées. Évitez d'écrire que votre corpus est « représentatif » d'un domaine entier. Décrivez plutôt ce qu'il permet de dire, et ce qu'il ne permet pas de dire.

**`protocole_selection.md`**

- Une liste numérotée d'étapes qu'une autre personne pourrait suivre pour retrouver exactement les mêmes documents.
- Pour chaque étape : où aller, quoi relever, quel statut attribuer (`retenu`, `exclu`, `a_verifier`).

**`criteres_inclusion_exclusion.md`**

- Un tableau de critères d'inclusion, chacun justifié par un lien avec la question.
- Un tableau de critères d'exclusion, avec un exemple et la conséquence.
- Exemple de cas limites concrets, observés pendant votre exploration.
- La procédure en cas de doute (statut `a_verifier`, discussion, journal).

**`sources_candidates.csv`**

- Au minimum la source retenue et une source écartée, avec la raison de la décision.
- Les colonnes du `README.md`, séparées par des points-virgules. Écrivez les adresses en texte brut, sans lien Markdown.
- Une date de consultation.
- Dans la colonne `conditions_utilisation`, résumez ce que vous avez lu. Si vous n'avez pas encore vérifié, écrivez `a_verifier`.

**`plan_echantillonnage.md`**

- Ce fichier peut être très simple lorsque le corpus visé est une **population complète** (par exemple tous les articles d'une revue).
- Dans ce cas, cochez « Exhaustif dans une population délimitée », justifiez en deux ou trois phrases, et précisez s'il y a des sous-corpus à comparer (des périodes, des genres).
- Si vous ne visez pas la population entière, indiquez comment vous choisirez les documents (au hasard, par strates, par sélection raisonnée) et pourquoi.
- Surveillez ce qui pourrait fausser une comparaison : taille des documents, répartition par numéro, langue.

**`plan_metadonnees.md`**

- Une liste de départ, non exhaustive. Elle sera complétée plus tard.
- Retenez seulement les informations dont vous avez besoin pour répondre à la question et que vous serez capable d'extraire : identifiant, adresse (URL), titre, numéro ou date, langue, type de document, statut.
- Pour chaque champ : une description courte et la mention « oui / non / si disponible ».
- Quelques règles : format des dates (`AAAA-MM-JJ`), codage des valeurs inconnues (`non_disponible`), identifiants stables.
- Évitez de collecter des données personnelles qui ne sont pas nécessaires à l'étude.

### Principes d'écriture

- Une décision = une justification. Écrivez le « pourquoi » à côté de chaque règle.
- Les fichiers restent révisables. Datez les changements importants dans le journal.
- Ne présentez pas un nombre ou une propriété de votre corpus que vous n'avez pas vérifié. Écrivez `à vérifier`.

> Un plan de corpus n'a pas besoin d'être long. Il doit permettre à un lecteur extérieur de comprendre, et de refaire, la sélection.

## 2. Parcourir le corpus et inspecter le HTML

Les pages Web contiennent plus d'informations que ce qui s'affiche à l'écran. Certaines sont utiles pour votre projet : date exacte, langue, identifiants, mots-clés, adresse du PDF. D'autres perturbent l'extraction : menus, bandeaux, notes. Cette partie vous apprend à les repérer avant d'écrire un seul programme.

### Ce qu'il faut faire

1. Ouvrez la page principale de votre source. Notez comment les numéros, les rubriques ou les listes sont organisés.
2. Ouvrez la page d'un numéro, puis celle d'un article. Repérez la forme des adresses (URL) : les identifiants se répètent-ils ? Peut-on en déduire une structure ?
3. Dans votre navigateur, ouvrez les outils de développement :
   - clic droit sur un élément de la page, puis **Inspecter** ;
   - ou `F12`, ou `Ctrl + Maj + I` (macOS : `Cmd + Option + I`).
4. Dans l'onglet **Éléments** (ou *Inspecteur*), survolez les lignes de code. Le navigateur surligne la partie correspondante de la page. Dépliez les balises avec la flèche.
5. Pour voir le code de la page tel que le serveur l'envoie, ouvrez le code source avec `Ctrl + U`. Comparez-le avec ce que l'inspecteur affiche.
6. Dans la zone de recherche de l'inspecteur (`Ctrl + F`), cherchez des mots que vous voyez à l'écran (le titre, un mot-clé, le nom d'un auteur) pour retrouver où ils sont stockés.
7. Faites l'inverse : cherchez dans le code des informations que vous **ne voyez pas** à l'écran.
8. Notez les observations dans `plan_metadonnees.md` (voir le gabarit plus bas).

### Où regarder

| Endroit | Ce qu'on peut y trouver |
|---|---|
| Début du document (`<head>`) | Titre, langue, balises `<meta>` (auteur, date, mots-clés, résumé, identifiant du document), liens vers d'autres versions |
| Attributs (`id`, `class`, `lang`, `href`) | Zones de la page (titre, résumé, texte, notes), langue d'un passage, adresse d'un PDF |
| Corps du texte | Paragraphes, intertitres, notes de bas de page, références, légendes |
| Éléments masqués | Texte présent dans le code mais non affiché (menus repliés, blocs cachés) |
| Données structurées | Informations encodées dans des blocs de script (par exemple des données bibliographiques) |
| Commentaires | Notes du développeur dans le code (`<!-- ... -->`) |
| Pied de page et menus | Éléments répétés sur toutes les pages, à exclure du texte analysé |

Le nom exact des balises varie d'une source à l'autre. Ne supposez pas qu'une balise vue dans un exemple du cours existe dans votre source : vérifiez-la.

### Quoi comparer

Inspectez au moins **cinq pages** de votre source, de nature différente :

- la page principale ;
- la page d'un numéro ou d'une liste ;
- un article typique ;
- un article avec une version PDF, si la source en propose ;
- un document atypique : article sans résumé, sans mot-clé, dans une autre langue, très court ou très long, ou encore un compte rendu.

Pour chaque page, observez ce qui change dans la structure. Les différences sont des risques pour l'extraction automatique de la séance suivante.

### Précautions

- **Inspecter ne modifie pas le site.** Si vous changez du texte dans l'inspecteur, vous ne modifiez que l'affichage dans votre navigateur, et le changement disparaît au rechargement.
- Ne copiez pas des contenus entiers dans votre dépôt. Notez des repères, des noms de balises et de courts extraits.
- Ne tentez pas de contourner un accès restreint (connexion, abonnement).
- N'automatisez aucune collecte pour le moment. La séance 4 expliquera comment procéder de manière respectueuse (identification, délai entre les requêtes, règles du site).
- Ne copiez ni mot de passe ni information personnelle dans vos notes.

### Gabarit à ajouter à `plan_metadonnees.md`

```markdown
## Informations repérées dans le HTML

### Pages inspectées

| Page | Adresse | Type | Remarque |
|---|---|---|---|
| P1 | [URL] | Page principale | [Remarque] |
| P2 | [URL] | Numéro | [Remarque] |
| P3 | [URL] | Article typique | [Remarque] |
| P4 | [URL] | Article avec PDF | [Remarque] |
| P5 | [URL] | Document atypique | [Remarque] |

### Informations repérées

| Information | Visible à l'écran ? | Présente dans le HTML ? | Où ? (balise, attribut, zone) | Utile pour le projet ? |
|---|---|---|---|---|
| Titre | [oui/non] | [oui/non] | [Repère] | [oui/non, pourquoi] |
| Auteur·es | | | | |
| Date | | | | |
| Numéro | | | | |
| Langue | | | | |
| Résumé | | | | |
| Mots-clés | | | | |
| Adresse du PDF | | | | |
| Identifiant (DOI ou autre) | | | | |
| Notes de bas de page | | | | |
| Autres informations cachées | | | | |

### Éléments à exclure du texte analysé

[Menus, bandeaux, pieds de page, notes, légendes… avec leur repère dans le code.]

### Différences entre les pages

[Ce qui varie d'un type de page à l'autre, et ce que cela implique pour l'extraction.]

### Difficultés et questions

[Ce qui est ambigu, incohérent ou manquant.]
```

### Pour votre corpus : un résumé chiffré

À la fin de votre exploration, ajoutez dans `plan_corpus.md`, section *Taille visée*, un court bilan :

```markdown
- Nombre de numéros ou de listes consultés : [n]
- Nombre d'articles ou de documents estimé par numéro (sur [k] numéros) : [intervalle]
- Taille totale estimée : [n], à recompter lors de la collecte
- Date de la consultation : [AAAA-MM-JJ]
```

## 3. Mettre à jour le dépôt et le journal

### Dépôt

1. Faites un *Fetch origin*, puis un *Pull origin* si nécessaire.
2. Enregistrez tous les fichiers de `chaine/02_conception_du_corpus/`.
3. Dans GitHub Desktop, vérifiez la liste des fichiers modifiés.
4. Faites un commit avec un message précis, par exemple :

```text
Précise le plan de corpus, les critères et les informations repérées dans le HTML
```

5. Faites un *Push origin*.
6. Vérifiez sur GitHub que les fichiers sont présents.

Vous pouvez séparer le travail en plusieurs commits (par exemple un pour les critères, un pour les sources, un pour l'inspection) si chaque message décrit bien ce qui a été fait. N'en créez pas artificiellement.

### Journal

Ajoutez dans `journal/journal_de_bord.md` au moins **une entrée** pour cette séance et une entrée de plus pour chaque décision importante (changement de source, réduction du périmètre, ajout d'un critère, exclusion d'un genre). Chaque entrée contient :

- la date et l'étape ;
- l'observation ou la difficulté rencontrée, avec un exemple si possible ;
- les options envisagées ;
- la décision et sa justification ;
- la vérification effectuée ;
- la conséquence pour la suite ;
- un lien vers la trace : fichier ou commit.

Si vous avez utilisé un outil d'IA de manière substantielle, indiquez l'outil, la fonction, les parties concernées et ce que vous avez vérifié. Une proposition générée n'est pas une observation sur votre corpus tant qu'elle n'a pas été contrôlée.

## 4. Checklist

- [ ] J'ai relu `conception_corpus_exemple.md` sans le copier.
- [ ] `plan_corpus.md` distingue la population visée du corpus effectivement visé et reprend la question principale.
- [ ] L'unité documentaire et l'unité d'analyse sont précisées.
- [ ] `protocole_selection.md` décrit des étapes qu'une autre personne pourrait suivre.
- [ ] `criteres_inclusion_exclusion.md` contient des critères justifiés et au moins deux cas limites.
- [ ] `sources_candidates.csv` contient la source retenue et au moins une source écartée, avec une date de consultation.
- [ ] `plan_echantillonnage.md` justifie l'approche choisie, même si elle est simple.
- [ ] `plan_metadonnees.md` contient une liste de départ de champs réalistes.
- [ ] J'ai inspecté au moins cinq pages de natures différentes.
- [ ] J'ai noté au moins une information visible dans le code mais absente de l'écran, ou j'ai expliqué qu'il n'y en avait pas.
- [ ] J'ai noté les éléments à exclure du texte analysé.
- [ ] J'ai fait un commit et un push, puis vérifié le résultat sur GitHub.
- [ ] J'ai ajouté au moins une entrée au journal de bord.

## 5. Pour la séance 4

La séance 4 porte sur l'acquisition. Apportez :

- votre `plan_corpus.md` et vos critères d'inclusion et d'exclusion ;
- vos notes d'inspection du HTML, notamment les différences entre pages ;
- vos questions sur les conditions d'accès et d'utilisation de votre source ;
- votre carnet `demarrage.ipynb` fonctionnel.

Les fichiers `corpus_pilote.md` et `evaluation_faisabilite.md` seront abordés à partir des démonstrations d'acquisition et de préparation. Vos plans peuvent encore être modifiés après ces démonstrations, à condition que les révisions soient datées et justifiées dans le journal.
