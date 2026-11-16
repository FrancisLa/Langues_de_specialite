# Séance 5 — Préparation du corpus : textes, métadonnées, annotation et représentation vectorielle

Cours : Langues de spécialité — Enseignant : Francis Lareau

Ce cinquième travail comporte quatre étapes : extraire les textes de vos fichiers HTML, extraire les métadonnées nécessaires à votre question, annoter les textes sur le plan morpho-syntaxique pour choisir vos unités d’observation, puis construire une représentation vectorielle de vos domaines d’information.

Vous partez des sources et de l’inventaire de la séance 4. Le notebook du professeur est une démonstration : vous écrivez votre propre code, adapté à votre source, à votre question et à votre plan de corpus.

Échéance : prochain cours (séance 6).

## 1. Préparer votre travail

### Matériel de départ

- Le dossier `chaine/04_preparation/` et son `README.md`.
- Vos fichiers de `chaine/01_question_et_cadre/` et de `chaine/02_conception_du_corpus/`, notamment la question, le plan de corpus et le plan de métadonnées.
- Votre inventaire `donnees/inventaire.csv` et vos sources de `donnees/sources/`.
- Le notebook de démonstration `preparation_exemple.ipynb`.
- L’exemple de production `preparation_corpus_exemple.md` : un exemple construit à ne pas présenter comme votre propre recherche.

### Productions attendues

| Élément | Travail demandé |
|---|---|
| `chaine/04_preparation/protocole_preparation.md` | Décrire l’ensemble des transformations, leurs entrées, leurs sorties, leurs décisions et leurs limites |
| `chaine/04_preparation/01_extraction/` | Documenter l’extraction des textes et des métadonnées : protocole, code et contrôle |
| `chaine/04_preparation/02_nettoyage/regles_nettoyage.md` | Consigner les règles de nettoyage minimales effectivement appliquées |
| `chaine/04_preparation/03_segmentation/protocole_segmentation.md` | Justifier le choix des domaines d’information |
| `chaine/04_preparation/04_annotation_ou_representation/` | Documenter l’annotation, le choix des unités d’information, la vectorisation, le code et les contrôles |
| `chaine/04_preparation/registre_transformations.csv` | Retracer les opérations et leurs sorties |
| `donnees/intermediaires/` et `donnees/preparees/` | Conserver les versions extraites, nettoyées, annotées et vectorisées, dans un stockage autorisé |
| `donnees/dictionnaire_metadonnees.md` | Définir les métadonnées ajoutées et leurs valeurs |
| `journal/journal_de_bord.md` | Expliquer les décisions importantes et leurs conséquences |

Les noms de colonnes, de fichiers et de dossiers du notebook ne sont pas imposés. Documentez ceux que vous choisissez et ne multipliez pas les exports sans utilité.

Les sources ne sont jamais modifiées. Chaque transformation produit une nouvelle version identifiable, reliée au document d’origine par son identifiant stable.

## 2. Travailler d’abord sur un pilote

Commencez par un petit ensemble de documents de votre corpus. Choisissez-le pour tester vos règles, pas seulement pour qu’elles réussissent : incluez au moins un cas court, un cas long et un document dont la structure diffère des autres, si vous en avez repéré à la séance 3.

Le pilote permet de corriger vos sélecteurs, vos règles et vos paramètres avant de traiter tout le corpus acquis. Il ne démontre pas que votre code fonctionnera sur tous les numéros, genres ou années. Après un pilote concluant, appliquez la procédure à l’ensemble des documents prévus par votre plan et disponibles dans votre inventaire.

Une pondération TF-IDF et un vocabulaire dépendent du corpus. Si vous passez du pilote au corpus complet, recalculez la représentation et créez une nouvelle version : ne mélangez pas des lignes ou des colonnes issues de deux calculs différents.

## 3. Extraire les textes des fichiers HTML

### Ce qu’il faut faire

1. Ouvrez deux ou trois pages sources dans le navigateur et dans l’inspecteur. Repérez les éléments qui contiennent le texte que vous voulez étudier.
2. Décidez de ce qui appartient au texte principal. Notez le sort des titres de section, citations, listes, tableaux, légendes, notes, références, résumés et éléments de navigation.
3. Écrivez votre code sur un seul document. Affichez le nombre d’éléments trouvés, le début du texte et sa fin.
4. Traitez les éléments qui perturbent le texte, par exemple numéros de paragraphes ou appels de notes. Vérifiez que les mots qui les suivent sont conservés.
5. Répétez les mêmes opérations sur tous les documents du pilote, puis sur l’ensemble du corpus. Conservez une ligne pour chaque document, même lorsque l’extraction échoue.
6. Enregistrez le texte brut extrait dans une version intermédiaire, avec l’identifiant stable du document.

Inspirez-vous des opérations de la démonstration : lire le HTML avec `lxml`, chercher des éléments, tester leurs attributs, retirer certains éléments en mémoire, récupérer leur texte et rassembler les paragraphes. Vérifiez vos sélecteurs sur votre source. Un texte extrait avec succès pour une page peut échouer sur une autre structure.

### Cas à ne pas confondre

- Un HTML absent n’est pas un article sans texte.
- Zéro paragraphe retrouvé n’est pas un texte vide valide : cela peut signaler un mauvais sélecteur ou une page d’erreur.
- Les notes et références peuvent être exclues du texte principal, conservées dans un champ distinct ou étudiées séparément. Justifiez votre choix par la question.
- Ne prenez pas tout le texte de la page par défaut : vous ajouteriez menus et boutons au corpus.

Si votre corpus n’est pas en HTML, ne reprenez pas cette étape telle quelle. Décrivez le format traité et choisissez une procédure adaptée. Un PDF, par exemple, peut avoir une couche de texte imparfaite, un ordre de lecture ambigu ou aucun texte exploitable ; consultez l’enseignant si la source principale est un PDF ou une image.

### Contrôle

Comparez un échantillon de textes extraits avec la page d’origine. Regardez le début, la fin, les citations, les listes, les accents, les passages situés après une note et les cas atypiques. Inscrivez l’échantillon, les critères et les résultats dans `controles/controle_extraction.md`.

## 4. Extraire les métadonnées nécessaires à votre question

### Partir de la question

Ne cherchez pas toutes les informations disponibles. Préparez un tableau qui relie votre question, vos comparaisons et vos métadonnées.

| Besoin de l’enquête | Métadonnée possible | Source probable |
|---|---|---|
| Comparer des numéros ou des périodes | Numéro, date brute, année | Balises `meta` ou éléments visibles de la page |
| Identifier un article | Titre, auteurs, identifiant, DOI | Balises `meta`, adresse ou page |
| Comparer des parties d’un article | Résumé, mots-clés, section | Champs distincts de la page |
| Délimiter le corpus | Langue, genre ou type de document | Métadonnées ou règles du plan |

Ce tableau est un exemple : utilisez les besoins de votre propre projet. Renvoyez à votre plan de métadonnées de l’étape 02 plutôt que de le recopier.

### Ce qu’il faut faire

1. Cherchez chaque métadonnée dans le HTML d’un document : balises `meta` (`name` et `content`), éléments de la page, adresse ou autre repère.
2. Testez votre code sur ce document et affichez le résultat brut.
3. Prévoyez les cas où l’information manque, apparaît plusieurs fois ou est écrite dans plusieurs langues.
4. Répétez l’extraction sur le pilote, puis sur l’ensemble du corpus.
5. Définissez chaque colonne et ses valeurs dans `dictionnaire_metadonnees.md`.
6. Associez les métadonnées au document par son identifiant stable.

Gardez la valeur brute lorsque vous en tirez une version dérivée. Par exemple, conservez la date trouvée dans la page avant d’en extraire l’année. Ne remplacez jamais une date de publication manquante par la date de collecte. Si vous réunissez plusieurs auteurs dans une seule cellule, choisissez un séparateur qui ne dépend pas des virgules d’un nom.

### Contrôle

Comparez plusieurs documents aux pages d’origine : titre complet, auteurs dans le bon ordre, numéro, année, langue, résumé et mots-clés. Vérifiez aussi les documents dont une métadonnée est absente. Une cellule vide signifie « non récupérée par votre code », pas nécessairement « information inexistante ».

## 5. Nettoyer le texte minimalement avant l’annotation

Le nettoyage reste limité à cette séance. Il prépare le texte pour les outils linguistiques sans retirer ce qui pourrait servir à la question.

Les opérations montrées dans la démonstration sont : uniformiser Unicode, remplacer les apostrophes courbes, remplacer les espaces insécables et réduire les espaces horizontaux répétés. Vous pouvez en retenir moins ou plus, mais chaque règle doit être testée sur des exemples et consignée dans `regles_nettoyage.md`.

- Conservez le texte brut extrait et créez une nouvelle version nettoyée.
- Comparez des passages avant et après.
- Évitez de supprimer des majuscules, des accents, des chiffres, des parenthèses ou de la ponctuation sans justification liée à la question.
- Signalez les textes identiques ou presque identiques, les encodages suspects et les caractères de remplacement ; ne les corrigez pas automatiquement.

Le nettoyage des doublons, de l’encodage et des erreurs d’extraction sera approfondi à la séance suivante.

## 6. Analyser les textes sur le plan morpho-syntaxique

### Choisir et documenter l’outil

La démonstration utilise un modèle français de spaCy. Vous pouvez l’utiliser si votre corpus est en français et si ses limites vous conviennent. Un autre outil ou une autre langue exigent un modèle adapté et documenté.

Dans votre protocole, indiquez le nom du modèle, sa version, la langue traitée et les composants utilisés. Le modèle est un outil probabiliste : ses annotations sont des prédictions à contrôler, pas une vérité.

### Observer d’abord un exemple

Choisissez un court passage de votre corpus qui contient des termes spécialisés, une élision, un nom propre ou une construction difficile. Appliquez le modèle et affichez dans un tableau les informations utiles :

- forme du token et lemme ;
- catégorie grammaticale ;
- traits morphologiques ;
- relation syntaxique et token gouverneur ;
- positions de début et de fin dans le texte ;
- indicateurs : alphabétique, ponctuation, espace, mot-outil.

Lisez ce tableau avant d’automatiser le traitement. Quels lemmes sont plausibles ? Quels termes spécialisés ou noms propres sont mal analysés ? Quelles informations seront utiles à votre question ?

### Appliquer à votre pilote

Répétez l’analyse sur les textes du pilote. Décidez ce que vous conservez :

- seulement une version lemmatisée du texte ;
- ou une table d’annotations avec une ligne par token, reliée à l’identifiant du document.

Si vous voulez filtrer par catégorie grammaticale, étudier des constructions, retrouver des contextes ou changer de domaine d’information, une table de tokens est préférable. Elle augmente toutefois le volume des données et peut contenir des extraits protégés : vérifiez le stockage et le partage.

### Contrôle

Lisez un échantillon de phrases choisi et justifié, avec des cas ordinaires et des cas difficiles. Relevez des erreurs de lemmatisation, de catégorie ou de découpage, expliquez leur effet possible sur vos observations et décidez de les accepter, corriger ou documenter. Une annotation automatique ne se valide pas parce que le programme s’est exécuté.

## 7. Choisir vos unités d’observation

Cette décision relie la question à la représentation. Elle comprend deux choix.

| Choix | Question à poser | Exemples |
|---|---|---|
| Domaine d’information (DOMIF) | Que représentera chaque ligne de la matrice ? | Article, section, paragraphe, phrase, passage contenant un terme |
| Unité d’information (UNIF) | Que représentera chaque colonne ? | Forme, lemme, lemme avec catégorie, n-gramme |

### Choisir le domaine d’information

| Si votre question porte sur... | Domaine à envisager | Conséquence à examiner |
|---|---|---|
| La comparaison de documents, de numéros ou de genres | Document | La structure interne du texte disparaît |
| Une idée ou un passage autonome | Paragraphe | Les paragraphes sont courts et plus nombreux |
| Une formulation, une définition ou une recommandation | Phrase | Peu de mots par ligne et dépendance au découpage en phrases |
| Un terme précis dans son contexte | Passages contenant ce terme | La sélection modifie le corpus étudié |

La démonstration représente un article par ligne. Ce n’est pas toujours le bon choix. Si votre question exige un paragraphe ou une phrase, adaptez votre code pour conserver leurs identifiants pendant l’annotation. Chaque unité doit pouvoir être reliée au document, à sa position et à ses métadonnées. Si cette adaptation est trop difficile, demandez de l’aide ; un choix de document est admissible lorsqu’il est justifié.

### Choisir les unités d’information

Décidez quelles formes seront comptées :

- formes originales ou lemmes ;
- minuscules ou casse conservée ;
- tous les tokens alphabétiques ou certaines catégories grammaticales ;
- mots-outils conservés ou retirés ;
- unigrammes ou séquences contiguës de plusieurs unités ;
- seuils de fréquence, seulement s’ils sont justifiés.

Un filtre n’est pas appliqué par défaut. Retirer les mots-outils peut éliminer des négations, des connecteurs ou des marqueurs argumentatifs. Conserver tous les mots peut laisser dominer des termes presque présents dans tous les documents. Si vous construisez des n-grammes, ne rapprochez pas des unités qui n’étaient pas voisines avant filtrage.

### Comparer au moins deux options sur le pilote

Choisissez deux options plausibles, par exemple article ou paragraphe, lemmes de toutes les catégories ou lemmes de noms, adjectifs et verbes. Comparez les dimensions de la matrice, les termes les plus fréquents, les lignes vides et les risques d’interprétation. Retenez ensuite l’option la plus adaptée à votre question et expliquez pourquoi.

Les paramètres choisis sont décrits dans `protocole_segmentation.md` pour les domaines et dans `protocole_representation.md` pour les unités d’information.

## 8. Représenter vos domaines d’information par des vecteurs

### Matrice de comptage

Construisez une matrice dont les lignes sont vos domaines d’information et les colonnes vos unités d’information. Chaque cellule contient le nombre d’occurrences de l’unité dans le domaine.

Vérifiez les règles de découpage appliquées par l’outil de vectorisation. Par exemple, la configuration par défaut de `CountVectorizer` ignore les mots d’un seul caractère. Documentez cet effet si les abréviations, symboles ou lemmes courts peuvent être pertinents.

### Au moins une variante justifiée

Ajoutez une représentation dérivée si elle répond à un besoin de la question :

| Représentation | Utilité possible | Précaution |
|---|---|---|
| Présence ou absence | Mesurer la diffusion d’une unité | Perd le nombre d’occurrences |
| Fréquence normalisée | Comparer des domaines de longueurs différentes | Ne pondère pas les unités rares |
| TF-IDF | Favoriser les unités plus caractéristiques de certains domaines | Dépend du corpus et du domaine choisi |

Un poids élevé ne définit pas un thème, un terme important ou un résultat. Il s’agit d’une représentation numérique. Conservez aussi la matrice de comptage : certaines analyses ultérieures en auront besoin.

Les matrices sont de grande taille. Utilisez un format creux pour les sauvegarder et n’affichez que de petits extraits lisibles. Évitez de convertir toute la matrice en tableau complet.

### Conserver les index

Une matrice sauvegardée ne contient pas automatiquement les noms de ses lignes et de ses colonnes. Enregistrez séparément :

- l’ordre des lignes avec l’identifiant du document ou de l’unité ;
- l’ordre des colonnes dans un fichier de vocabulaire ;
- les occurrences, les fréquences documentaires ou les poids utiles au contrôle ;
- les paramètres de la vectorisation.

Le vocabulaire doit rester dans l’ordre des colonnes, et non trié par fréquence.

### Contrôle

| Contrôle | Question à poser |
|---|---|
| Lignes | Combien de domaines sont représentés et pourquoi ? |
| Colonnes | Le vocabulaire contient-il des résidus de menus, de numéros ou de formes mal découpées ? |
| Alignement | Un domaine retrouvé dans la matrice correspond-il au bon texte ? |
| Lignes vides | Quels domaines n’ont aucune unité retenue et pourquoi ? |
| Termes fréquents | Les termes dominants sont-ils interprétables et attendus ? |
| Lemmes | Des erreurs de lemmatisation modifient-elles les colonnes ? |
| Sauvegarde | Les fichiers relus ont-ils les mêmes dimensions et le même ordre ? |

Pour un domaine, regardez ses unités non nulles et comparez-les au texte. Une matrice qui s’exécute n’est pas une matrice correcte.

## 9. Documenter, contrôler et décider

### Protocoles et dictionnaire

Complétez les protocoles sans recopier leur contenu entre eux.

- `protocole_preparation.md` : objectif, relation avec la question, entrées, sorties, étapes, décisions importantes, contrôles et limites.
- `protocole_extraction.md` : format traité, éléments retenus ou exclus, métadonnées recherchées et règles pour les valeurs absentes.
- `regles_nettoyage.md` : règles effectivement appliquées, risques et contrôles.
- `protocole_segmentation.md` : domaines d’information choisis, justification, identifiants et conséquences.
- `protocole_representation.md` : modèle, unités, filtres, paramètres, pondérations, format et limites d’interprétation.
- `dictionnaire_metadonnees.md` : champs, définitions, valeurs et provenance.

### Registre des transformations

Ajoutez au `registre_transformations.csv` une ligne par opération importante : extraction, nettoyage, annotation, sélection des unités et représentation. Indiquez l’entrée, la sortie, la procédure, la version du code, les paramètres, le contrôle et le statut. Utilisez `a_verifier` ou `provisoire` tant que le contrôle humain n’est pas terminé.

### Rapports de contrôle

Dans chaque dossier `controles/`, consignez l’étape contrôlée, la version, l’échantillon, les critères, les résultats, les erreurs, les actions et la conclusion. Distinguez les vérifications automatiques de la lecture d’exemples. N’inscrivez pas de nombre ou de résultat avant d’avoir exécuté le contrôle.

## 10. Mettre à jour le dépôt et le journal

### Dépôt

1. Au début du travail, vérifiez le bon dépôt dans GitHub Desktop, puis faites *Fetch origin* et *Pull origin* si nécessaire.
2. Enregistrez votre code, vos protocoles, vos contrôles et vos fichiers partageables dans votre copie locale.
3. Avant chaque commit, examinez les fichiers et les sorties de notebook. Les affichages peuvent contenir des textes complets, des chemins personnels ou du contenu non partageable.
4. Faites un commit avec un message précis, par exemple :

```text
Ajoute l’extraction des textes et des métadonnées du pilote
```

Puis, après la représentation :

```text
Documente les unités d’observation et les matrices du corpus préparé
```

5. Faites *Push origin*, puis vérifiez les fichiers sur GitHub.

Les textes, tokens annotés et vecteurs dérivés peuvent exposer le contenu des sources. Ne les versez pas dans Git sans avoir vérifié le droit de redistribution ; documentez leur emplacement et les contrôles effectués.

### Journal de recherche

Ajoutez une entrée pour les décisions importantes, notamment :

- le périmètre du texte extrait et le sort des notes, références, titres et tableaux ;
- le choix des métadonnées nécessaires à la question ;
- une règle de nettoyage retenue, rejetée ou révisée ;
- le choix de l’outil et des paramètres d’annotation ;
- le choix du domaine d’information et des unités d’information ;
- la décision d’étendre ou de reprendre la préparation après le pilote ;
- les limites découvertes pendant le contrôle.

Décrivez l’observation, les options, la décision, sa justification, le contrôle et la conséquence. Liez l’entrée au protocole, au fichier ou à la version du code.

Si vous utilisez une IA de façon substantielle, indiquez l’outil, la tâche, les données transmises, la sortie conservée ou rejetée et vos vérifications. N’envoyez pas à un service externe des textes dont l’usage n’est pas autorisé. Vous devez pouvoir expliquer chaque ligne de code retenue.

## 11. Checklist

- [ ] J’ai relu le README de préparation, mon plan de corpus et mon plan de métadonnées.
- [ ] J’ai vérifié le format de mes sources avant d’appliquer une procédure d’extraction.
- [ ] Mes textes sont extraits par des repères vérifiés sur ma source, sans prendre toute la page par défaut.
- [ ] Les documents sans HTML, sans texte ou avec une extraction douteuse restent identifiables.
- [ ] Je n’extrais que les métadonnées utiles à ma question, avec leurs valeurs brutes et leur dictionnaire.
- [ ] Je n’ai pas remplacé une date de publication absente par une date de collecte.
- [ ] Mon nettoyage est limité, testé et justifié.
- [ ] J’ai observé les annotations morpho-syntaxiques sur un exemple avant de traiter le corpus.
- [ ] J’ai documenté l’outil linguistique, sa version et ses erreurs repérées.
- [ ] J’ai choisi mon domaine d’information et mes unités d’information en fonction de ma question.
- [ ] J’ai comparé au moins deux options sur le pilote.
- [ ] Ma matrice de comptage et ma variante éventuelle sont accompagnées de l’ordre des lignes, du vocabulaire et des paramètres.
- [ ] J’ai contrôlé l’alignement entre un domaine, son texte et ses valeurs dans la matrice.
- [ ] Après un pilote concluant, j’ai appliqué la procédure au corpus prévu, ou documenté ce qui manque et pourquoi.
- [ ] Le registre des transformations et les contrôles n’affirment pas une validation non réalisée.
- [ ] Les décisions importantes et les usages substantiels d’IA sont consignés dans le journal.
- [ ] Les fichiers partageables sont envoyés sur GitHub ; les données non redistribuables restent dans l’espace autorisé.

## 12. Pour la séance 6

Apportez votre code, vos données extraites, votre corpus préparé, vos matrices et leurs index, ainsi que vos rapports de contrôle. Préparez trois ou quatre exemples de problèmes : texte mal extrait, métadonnée absente, caractère suspect, doublon possible, lemme erroné, domaine vide ou terme étrange dans le vocabulaire.

La séance suivante portera sur le nettoyage, les doublons, l’encodage et les erreurs d’extraction. Si une étape reste bloquée, apportez le message exact, l’identifiant du document concerné et les vérifications déjà faites.
