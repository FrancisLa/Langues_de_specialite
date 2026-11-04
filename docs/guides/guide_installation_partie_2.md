# Partie 2 — Ajouter les fichiers du cours et commencer le projet

## GitHub Desktop, Markdown et Google Colab — Windows et macOS

Cours : Langues de spécialité — Enseignant : Francis Lareau

Cette deuxième partie explique comment :

1. télécharger les fichiers de départ du professeur ;
2. les copier dans votre dépôt personnel ou d’équipe ;
3. enregistrer et synchroniser les versions avec GitHub Desktop ;
4. lire et modifier les documents Markdown dans VS Code ;
5. créer et exécuter un notebook dans Colab, puis en enregistrer une copie directement sur GitHub.

> L’installation locale de Python n’est pas nécessaire pour suivre cette partie. Colab fournit l’environnement d’exécution. La partie 3, facultative, explique comment exécuter le code sur votre ordinateur.

## Avant de commencer

La partie 1 doit être terminée :

- votre dépôt privé personnel ou d’équipe existe sur GitHub ;
- il est cloné dans `Mon Drive/GitHub/<nom_du_projet>` ;
- Google Drive pour ordinateur est configuré et synchronisé ;
- GitHub Desktop utilise le bon compte et le bon dépôt ;
- VS Code est installé pour modifier les fichiers texte.

Dans ce guide, `LSP_nom_prenom` est un exemple : remplacez-le par le nom de votre dépôt.

En équipe, une seule personne réalise l’ajout initial du gabarit. Elle envoie ensuite les commits ; les autres récupèrent les changements avec Pull.

## 1. Comprendre les espaces de travail

| Espace | Rôle |
|---|---|
| Dépôt public du professeur | Fournir les consignes, guides et exemples de départ. |
| Dépôt privé de l’étudiant ou de l’équipe | Conserver votre travail et son historique sur GitHub. |
| Copie locale dans Drive | Modifier les fichiers sur l’ordinateur et utiliser GitHub Desktop. |
| Copie de travail Colab | Exécuter et modifier un notebook dans le navigateur. |

La synchronisation Drive et les échanges Git sont différents :

```text
Drive synchronise des fichiers entre votre ordinateur et le nuage.
GitHub Desktop échange des commits entre le dépôt local et GitHub.
Colab peut créer directement un commit sur GitHub lors d’un enregistrement explicite.
```

Pour les notebooks de ce guide, l’enregistrement vers GitHub se fait depuis Colab. Desktop sert ensuite à récupérer ce commit dans la copie locale.

## 2. Télécharger les fichiers du professeur

1. Ouvrez le dépôt de départ :
   [FrancisLa/Langues_de_specialite](https://github.com/FrancisLa/Langues_de_specialite).
2. Cliquez sur le bouton `Code`.
3. Choisissez `Download ZIP`.
4. Enregistrez l’archive dans Téléchargements ou un autre emplacement temporaire.
5. Décompressez-la :
   - Windows : clic droit sur le ZIP → `Extraire tout…` ;
   - macOS : double-cliquez sur le ZIP.
6. Ouvrez le dossier extrait.

Vous devez y retrouver le README et les dossiers du cours.

Le ZIP est une copie des fichiers à ce moment précis. Il ne contient pas l’historique complet et n’établit pas de lien de synchronisation avec votre dépôt. Les prochaines mises à jour du professeur ne seront pas automatiquement intégrées à votre travail.

## 3. Copier le gabarit dans votre dépôt

### 3.1 Vérifier la destination avant de copier

1. Dans GitHub Desktop, sélectionnez votre dépôt personnel ou d’équipe.
2. Faites `Fetch origin`, puis `Pull origin` si proposé.
4. Utilisez `Repository` → `Show in Explorer` sous Windows ou `Show in Finder` sous macOS.

La destination doit être votre dossier cloné dans Drive, pas Téléchargements ni le dossier extrait du ZIP.

### 3.2 Copier le contenu, pas le dossier extérieur

1. Ouvrez côte à côte le dossier extrait du cours et votre dépôt local.
2. Copiez tout le contenu du dossier extrait dans la racine de votre dépôt, incluant les fichiers commençant par un point, notamment `.gitignore`.
3. Conservez le dossier `.git` de votre dépôt. Ne le supprimez pas et ne le remplacez pas.
4. Conservez les fichiers de licence et les mentions d’auteur des contenus réutilisés.

Sous macOS, `Cmd + Maj + .` permet d’afficher les fichiers masqués. Sous Windows, utilisez l’option d’affichage des éléments masqués si nécessaire.

Pour le README initial de votre dépôt, vous pouvez l'écraser avec celui du gabarit. Si vous avez déjà rédigé du contenu personnel, comparez les deux fichiers au lieu d’accepter un remplacement aveugle.

Les dossiers doivent se trouver directement à la racine, par exemple :

```text
LSP_nom_prenom/
├── .git/                     # Déjà présent : à conserver
├── .gitignore
├── README.md
├── LICENSE                  # Si fourni dans le gabarit
├── LICENSE-DOCS.md           # Si fourni dans le gabarit
├── article/
├── chaine/
├── configuration/
├── docs/
├── donnees/
├── environnement/
├── journal/
└── resultats/
```

Cette arborescence est indicative : vérifiez les fichiers effectivement téléchargés et lisez leurs README.

N’obtenez pas cette structure imbriquée :

```text
LSP_nom_prenom/
└── Langues_de_specialite-main/
    └── chaine/
```

### 3.3 Enregistrer l’ajout initial sur GitHub

1. Revenez dans Desktop, onglet `Changes`.
2. Examinez les fichiers ajoutés et modifiés.
3. Vérifiez la présence de `.gitignore` avant de sélectionner les fichiers.
4. Sélectionnez les éléments utiles et autorisés, pas un environnement installé ou des données privées.
5. Dans `Summary`, écrivez :

```text
Ajoute le gabarit de départ du cours
```

6. Cliquez sur `Commit … to main`.
7. Cliquez sur `Push origin`.
8. Ouvrez votre dépôt dans le navigateur et vérifiez les dossiers.

## 4. Synchroniser avec GitHub Desktop

### 4.1 Six actions à distinguer

| Action | Effet |
|---|---|
| Enregistrer dans l’éditeur | Écrire les changements dans le fichier de travail. |
| Synchronisation Drive | Répliquer les fichiers avec Drive, sans créer de commit. |
| Fetch origin | Vérifier les nouveaux commits disponibles sur GitHub. |
| Pull origin | Intégrer ces commits dans la copie locale. |
| Commit to main | Enregistrer localement une version des changements sélectionnés. |
| Push origin | Envoyer les commits locaux sur GitHub. |

### 4.2 Avant de commencer une séance

1. Vérifiez qu’aucune autre session ne modifie cette copie du projet.
2. Dans Desktop, sélectionnez le bon dépôt.
3. Examinez les changements restés en cours.
4. Faites `Fetch origin`, puis `Pull origin` si proposé et sans conflit.

Fetch seul ne met pas les fichiers de travail à jour : Pull réalise cette intégration.

### 4.3 Après une modification locale

1. Enregistrez les fichiers modifiés localement dans VS Code.
2. Dans Desktop, examinez `Changes` et les différences.
3. Écrivez un message commit précis.
4. Créez le commit, puis faites `Push origin`.
5. Vérifiez le résultat dans le navigateur.

Exemples de messages :

```text
Précise les critères de sélection du corpus
Documente la décision de limiter la période étudiée
Corrige le chemin du fichier de métadonnées
```

### 4.4 Recevoir de nouvelles consignes du professeur

Pull récupère les changements de votre dépôt, pas automatiquement ceux du professeur. Lisez les annonces et intégrez uniquement les fichiers ou corrections demandés. Ne recopiez pas ultérieurement tout le gabarit sur votre projet sans comparaison : cela pourrait écraser votre travail.

## 5. Lire et modifier les fichiers Markdown

### 5.1 Ouvrir le projet et les fichiers

1. Ouvrez VS Code.
2. Utilisez `File` → `Open Folder…`, ou `Open…` selon le système.
3. Sélectionnez la racine de votre dépôt local.
4. Dans l’explorateur latéral, ouvrez un fichier `.md`, par exemple un README ou le journal.

Un fichier Markdown est un fichier texte. Ne l’enregistrez pas comme document Word et vérifiez qu’il ne s’appelle pas `README.md.txt`.

### 5.2 Voir le rendu

Depuis le fichier Markdown, lancez `Markdown: Open Preview` dans la palette de commandes :

| Action | Windows | macOS |
|---|---|---|
| Palette de commandes | `Ctrl + Maj + P` | `Cmd + Maj + P` |
| Aperçu Markdown | `Ctrl + Maj + V` | `Cmd + Maj + V` |
| Enregistrer | `Ctrl + S` | `Cmd + S` |

Pour conserver texte et aperçu côte à côte, utilisez `Markdown: Open Preview to the Side`. Aucune extension supplémentaire n’est nécessaire pour cet aperçu.

### 5.3 Syntaxe minimale

````markdown
# Titre principal

## Sous-titre

Un paragraphe séparé du suivant par une ligne vide.

**Texte important** et *texte en italique*.

- Premier élément
- Deuxième élément

1. Première étape
2. Deuxième étape

- [ ] Élément à vérifier
- [x] Élément vérifié

[Inventaire du corpus](../donnees/inventaire.csv)

```python
print("Exemple de code présenté dans un document")
```
````

Les blocs de code dans un fichier `.md` présentent du code mais ne l’exécutent pas. Dans un lien, `../` signifie « remonter d’un dossier » ; adaptez-le à l’emplacement du fichier.

### 5.4 Premier exercice : une entrée dans le journal

1. Lisez `journal/README.md`.
2. Ouvrez ou créez `journal/journal_de_bord.md`, selon les consignes.
3. Ajoutez une entrée réelle, par exemple avec cette structure :

```markdown
## AAAA-MM-JJ — Prise en main du projet

Personnes concernées : [noms]

Objectif : [objectif de la séance]
Opérations réalisées : [ce qui a effectivement été fait]
Difficultés : [problèmes rencontrés, ou aucune difficulté particulière]
Décision et justification : [si une décision a été prise]
Vérification : [ce qui a été contrôlé]
Prochaine étape : [suite prévue]
```

4. Remplacez les indications par votre contenu, puis enregistrez.
5. Dans Desktop, vérifiez le fichier, créez un commit et faites un push.

Le journal explique la démarche et les décisions. Le message de commit décrit les changements des fichiers. Documentez les usages substantiels d’IA et leurs vérifications selon les consignes du cours.

## 6. Créer et exécuter un notebook dans Colab

### 6.1 Créer le fichier

1. Ouvrez [Google Colab](https://colab.research.google.com/).
2. Connectez-vous avec le compte Google contenant les fichiers du projet.
3. Choisissez `Fichier` → `Nouveau notebook`.
4. Renommez-le `test_environnement.ipynb`.

Un notebook contient notamment :

- des cellules texte, qui utilisent Markdown pour expliquer la démarche ;
- des cellules de code, qui exécutent les opérations Python.

### 6.2 Ajouter une cellule texte

Cliquez sur `+ Texte` et ajoutez :

```markdown
# Vérification de l’environnement

Projet : [nom du projet]
Auteur ou équipe : [noms]

Objectif : identifier l’environnement Python utilisé dans Colab.
```

Remplacez les indications entre crochets. Une cellule texte ne s’exécute pas comme du code Python : elle documente l’opération.

### 6.3 Ajouter une cellule de code

Cliquez sur `+ Code`, puis ajoutez :

```python
import platform
import sys

print("Version de Python :", platform.python_version())
print("Exécutable :", sys.executable)
```

Cliquez sur ▶ ou utilisez `Maj + Entrée`. Attendez la fin de l’exécution avant de continuer.

Le résultat décrit l’ordinateur distant de Colab, pas votre ordinateur personnel. La version n’a pas à être celle de l’installation locale facultative.

Exécutez les cellules dans l’ordre. En cas de nouvelle session, les variables précédentes peuvent ne plus exister : il faut réexécuter les cellules qui les définissent.

## 7. Enregistrer le notebook directement dans GitHub

### 7.1 Premier enregistrement

1. Inspectez le notebook et ses sorties : aucun mot de passe, token ou contenu non autorisé ne doit être envoyé.
2. Choisissez `Fichier` → `Enregistrer une copie dans GitHub` (`Save a copy in GitHub`).
3. Si demandé, connectez-vous à GitHub et autorisez Colab à accéder aux dépôts nécessaires. Vérifiez le compte utilisé.
4. Dans la fenêtre, choisissez votre dépôt privé personnel ou d’équipe.
5. Sélectionnez la branche `main`.
6. Dans le chemin du fichier, indiquez :

```text
test/test_environnement.ipynb
```

Ce chemin crée un fichier dans `test/` à la racine. Il n’est pas nécessaire de créer le dossier séparément sur GitHub.

7. Écrivez le message de commit :

```text
Ajoute un notebook de vérification de l’environnement Colab
```

8. Activer l’option d’inclusion d’un lien vers Colaboratory si elle est proposée.
9. Confirmez avec `OK` ou le bouton d’enregistrement.
10. Dans le navigateur, vérifiez le fichier dans votre dépôt GitHub.

Cette action crée directement un commit sur GitHub. Vous n’avez pas à refaire un commit local et un push pour ce même enregistrement.

### 7.2 Si le dépôt privé n’est pas proposé

1. Vérifiez le compte GitHub connecté et votre accès au dépôt.
2. Dans Colab : `Fichier` → `Ouvrir un notebook` → onglet `GitHub`.
3. Activez `Include private repos` si proposé et suivez l’autorisation.
4. Revenez à l’enregistrement dans GitHub.

Un compte institutionnel ou une organisation peut limiter les applications autorisées. Demandez de l’aide si l’accès reste refusé. Ne rendez pas le dépôt public pour contourner le problème.

### 7.3 Récupérer le commit dans le dépôt local

1. Assurez-vous que le même notebook n’est pas modifié dans votre clone local.
2. Dans Desktop, sélectionnez le bon dépôt.
3. Cliquez sur `Fetch origin`, puis `Pull origin`.
4. Vérifiez la présence de `test/test_environnement.ipynb` dans le dépôt local.

Le parcours est :

```text
Colab → enregistrement explicite dans GitHub → commit distant
→ Fetch/Pull sur l’ordinateur → copie locale dans Drive
```

N’ajoutez pas un deuxième commit pour un fichier identique déjà récupéré par Pull.

### 7.4 Continuer un notebook existant

1. Au début de la séance, ouvrez la dernière version du notebook maintenant disponible depuis GitHub en cliquant le lien `Open in Colab`.
2. Effectuez les modifications et les vérifications.
3. Le notebook ouvert à partir de GitHub s'enregistre dans GitHub lorsque `Fichier -> Enregistrer`.
4. Récupérez ensuite le fichier modifié sur l’ordinateur avec Fetch et Pull dans Desktop.

En équipe, convenez d’une personne responsable du fichier pendant la séance. Avant l’enregistrement vers GitHub, vérifiez que personne n’a envoyé une version plus récente. Ne remplacez pas silencieusement le travail d’un équipier.

## 8. Accéder aux données Drive depuis Colab

Un notebook ouvert depuis GitHub n’emporte pas les fichiers de données du projet. Pour accéder aux fichiers Drive autorisés, adaptez ce guide de démarrage : [Démarrage — notebook du cours](https://github.com/FrancisLa/Langues_de_specialite/blob/main/docs/demarrage.ipynb).


La définition des chemins ne crée pas les dossiers. Vérifiez leur présence et suivez les consignes de l’activité pour les entrées et les sorties.

Après montage, le code du notebook peut accéder aux fichiers Drive.

Si des bibliothèques manquent, installez-les dans la session Colab selon les instructions du notebook. La partie 3 du guide d'installation et l’environnement local ne sont pas nécessaires ici.

Les fichiers temporaires de Colab et les variables en mémoire ne sont pas sauvegardés dans Drive automatiquement. Enregistrez explicitement les données et sorties durables dans les emplacements autorisés.

## 9. Ranger et protéger les fichiers

Lisez les README avant de créer les documents et choisissez le dossier correspondant à l’opération.

| Contenu | Emplacement indicatif |
|---|---|
| Question, corpus et protocoles | Sous-dossier approprié de `chaine/` |
| Notebooks des activités | Sous-dossier correspondant de `chaine/` |
| Inventaire et documentation des données | `donnees/` |
| Décisions et usages substantiels d’IA | `journal/` |
| Résultats partageables retenus | `resultats/` |
| Article et bibliographie | `article/` |
| Dépendances et versions | `environnement/` |

### Comprendre .gitignore

Consultez le `.gitignore` copié depuis le gabarit. Il définit les fichiers non suivis que Git doit ignorer. Ne modifiez pas ses règles pour publier des données sans autorisation.

- Un fichier ignoré peut rester dans Drive sans être envoyé à GitHub.
- `.gitignore` n’empêche pas la synchronisation Drive et ne sécurise pas les données.
- Il ne retire pas les fichiers déjà suivis de l’historique.
- L’enregistrement direct de Colab vers GitHub ne doit pas être considéré comme protégé par les règles d’exclusion de votre copie locale : vérifiez le fichier et le chemin choisis.
- Les sorties d’un notebook peuvent contenir des données non partageables même si le code est partageable.

N’envoyez aucun secret. Si une clé a été exposée, révoquez-la et contactez l’enseignant. Pour les données interdites, demandez immédiatement de l’aide : une suppression visible ne suffit pas nécessairement à traiter l’historique.

## 10. Routines à retenir

### Document Markdown modifié localement

```text
Fetch → Pull si nécessaire → modifier dans VS Code → enregistrer
→ examiner Changes → Commit → Push → vérifier dans GitHub
```

### Notebook exécuté dans Colab

```text
Ouvrir la dernière version GitHub dans Colab → travailler et vérifier
→ Enregistrer une copie dans GitHub avec le même chemin
→ vérifier le commit distant → Fetch/Pull sur l’ordinateur
```

### Checklist de fin de séance

- [ ] J’ai travaillé dans le bon dépôt et la bonne version du fichier.
- [ ] Je n’ai pas modifié simultanément des copies concurrentes.
- [ ] Mes décisions et contrôles sont documentés.
- [ ] Les fichiers envoyés ne contiennent aucun secret ou contenu interdit.
- [ ] Les Markdown locaux ont été committés puis envoyés.
- [ ] Les notebooks Colab ont été enregistrés explicitement dans GitHub.
- [ ] Le dépôt local a récupéré les commits créés en ligne.
- [ ] Les données non versionnées sont conservées dans l’espace autorisé.

Vous pouvez maintenant suivre les activités du cours dans Colab. La partie 3 reste facultative et concerne uniquement l’exécution locale de Python.

## Documentation utile

- [Dépôt du cours](https://github.com/FrancisLa/Langues_de_specialite)
- [Télécharger une archive GitHub](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)
- [Commits et examen des changements dans Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
- [Markdown dans VS Code](https://code.visualstudio.com/docs/languages/markdown)
- [Exemple officiel Colab et GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Questions fréquentes sur Colab](https://research.google.com/colaboratory/faq.html)
