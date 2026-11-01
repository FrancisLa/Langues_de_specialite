# Préparer son projet — GitHub, Google Drive, Desktop et VS Code

Cours : Langues de spécialité — Enseignant : Francis Lareau

Cette première partie vous accompagne dans la création de votre dépôt
personnel sur GitHub, l’installation de sa copie locale dans Google Drive
et la préparation de VS Code pour modifier les documents du projet,
notamment les fichiers Markdown.

À cette étape, vous mettez en place l’espace qui accueillera votre travail.
Les fichiers et gabarits fournis par le professeur y seront ajoutés dans
la partie 2, qui expliquera également comment utiliser les notebooks dans
Google Colab et enregistrer votre travail sur GitHub.

La partie 3, **facultative**, présente l’installation de Python pour exécuter
le code sur votre propre ordinateur. Elle n’est pas nécessaire si vous
choisissez de travailler dans Colab.

Parcours :

```text
Compte GitHub → dépôt privé → Google Drive → GitHub Desktop
→ clonage dans Drive → VS Code
```

## 1. Créer votre compte GitHub et le dépôt du cours

### 1.1 Créer un compte, si nécessaire

1. Ouvrez [github.com/signup](https://github.com/signup).
2. Créez un compte personnel ou connectez-vous à votre compte existant.
3. Choisissez un nom d’utilisateur que vous pourrez communiquer à l’enseignant.
4. Vérifiez votre adresse courriel lorsque GitHub le demande.
5. Activez l’authentification à deux facteurs et conservez les moyens de récupération dans un endroit sûr.

Chaque personne utilise son propre compte. Ne partagez pas votre mot de passe.

### 1.2 Créer le dépôt privé

1. Sur GitHub, cliquez sur `+` → `New repository`.
2. Dans `Owner`, sélectionnez votre compte.
3. Dans `Repository name`, inscrivez par exemple `LSP_nom_prenom`.
4. Ajoutez une description : `Projet du cours Langues de spécialité`.
5. Choisissez `Private`.
6. Activez l’ajout d’un `README` : il initialise le dépôt avec un premier fichier et un premier commit.
7. N’ajoutez pas de licence ou de modèle `.gitignore` à cette étape.
8. Cliquez sur `Create repository`.
9. Vérifiez la mention `Private` et notez l’adresse de votre dépôt.

Exemple :

```text
https://github.com/VotreCompte/LSP_nom_prenom
```

Conservez le même nom de dépôt dans la suite du guide. Si le dépôt existe déjà, réutilisez-le plutôt que d’en créer un deuxième.

### 1.3 Cas d’un travail en équipe et accès de l’enseignant

Une seule personne crée le dépôt commun. Sur ce dépôt, ouvrez `Settings` → `Collaborators`, ou la rubrique de gestion des accès, puis invitez les équipiers et `FrancisLa` selon les consignes.

Chaque personne doit accepter l’invitation. Les équipiers cloneront ensuite ce même dépôt dans leur propre Drive personnel ; ils ne créeront pas un deuxième dépôt d’équipe.

## 2. Installer Google Drive pour ordinateur

### 2.1 Préparer le compte Google

1. Connectez-vous à [Google Drive](https://drive.google.com/).
2. Si nécessaire, [créez un compte Google](https://accounts.google.com/signup).
3. Utilisez le compte que vous utiliserez aussi dans Colab.
4. Vérifiez l’espace disponible et les éventuelles restrictions du compte institutionnel.

### 2.2 Installer et configurer Drive

1. Téléchargez [Google Drive pour ordinateur](https://www.google.com/drive/download/).
2. Installez la version pour Windows ou macOS et connectez-vous.
3. Ouvrez les préférences depuis l’icône Drive : zone de notification sous Windows, barre des menus sous macOS.
4. Dans les options de synchronisation de Mon Drive, choisissez la duplication des fichiers (`Mirror files`).
5. Relevez le chemin du dossier local et attendez la fin de la synchronisation.

La duplication conserve les fichiers de Mon Drive sur l’ordinateur et dans le nuage. Vérifiez que le disque dispose de suffisamment d’espace : cette option concerne Mon Drive, pas seulement le projet du cours.

Si l’espace manque ou si l’installation est bloquée, demandez un parcours adapté avant de poursuivre.

### 2.3 Créer le dossier parent GitHub

Dans Mon Drive, créez seulement le dossier :

```text
GitHub
```

Le clonage créera ensuite le dossier `LSP_nom_prenom` à l’intérieur. Ne le créez pas à l’avance avec des fichiers.

Relevez le vrai chemin de Mon Drive : il varie selon l’installation et la langue.

- Windows : ouvrez le dossier dans l’Explorateur et copiez son chemin depuis la barre d’adresse.
- macOS : utilisez le Finder et sa barre du chemin ; l’option de copie du chemin est également accessible dans le menu contextuel avec la touche Option, selon la version du système.

Ne supposez pas une lettre de lecteur ou un nom de dossier universel.

## 3. Installer GitHub Desktop et cloner votre dépôt dans Drive

### 3.1 Installer et connecter GitHub Desktop

1. Installez [GitHub Desktop](https://desktop.github.com/) pour Windows ou macOS.
2. Ouvrez l’application.
3. Choisissez `Sign in to GitHub.com` et terminez la connexion dans le navigateur.
4. Si demandé, configurez votre nom et l’adresse associés aux commits. Vous pouvez utiliser l’adresse de confidentialité `noreply` fournie par GitHub.

GitHub Desktop dispose de Git pour ses propres opérations. Il n’est normalement pas nécessaire de générer un token ou une clé SSH pour suivre ce parcours : utilisez sa connexion au compte.

### 3.2 Cloner le dépôt personnel

Cloner signifie créer une copie locale déjà liée à votre dépôt en ligne. Il ne faut pas créer un nouveau dépôt local indépendant ni changer son adresse distante.

1. Dans Desktop : `File` → `Clone repository`.
2. Dans l’onglet GitHub.com, choisissez votre dépôt. Vous pouvez aussi utiliser l’onglet `URL` et son adresse HTTPS.
3. Réglez `Local Path` pour que le chemin final soit :

```text
<chemin réel de Mon Drive>/GitHub/LSP_nom_prenom
```

4. Vérifiez qu’il n’y a pas de dossier `LSP_nom_prenom` imbriqué dans un autre dossier du même nom.
5. Cliquez sur `Clone` et attendez la fin.
6. Vérifiez le nom de `Current Repository`.
7. Choisissez `Repository` → `Show in Explorer` sous Windows ou `Show in Finder` sous macOS.

Le dossier doit contenir votre `README.md` et le dossier technique `.git`, parfois masqué. Ne supprimez pas `.git`.

Si le projet est déjà cloné au bon emplacement, ajoutez-le au besoin avec `File` → `Add local repository`, plutôt que de le cloner de nouveau.

### 3.3 Comprendre les deux synchronisations

| Échange | Ce qui se passe |
|---|---|
| Dossier local ↔ Google Drive | L’application Drive synchronise les fichiers. |
| Dépôt local ↔ GitHub | Git échange les commits avec Fetch, Pull et Push. |

Drive ne fait ni commit ni push. Une modification visible dans Drive n’est pas nécessairement présente sur GitHub.

> Un dépôt dans un dossier synchronisé demande des précautions. Le mode miroir ne garantit pas l’absence de conflits. Travaillez sur un seul ordinateur ou environnement à la fois pour cette copie et attendez la synchronisation avant de changer d’environnement. Ne partagez pas un dossier Drive contenant `.git` comme espace collectif de modification.

## 4. Installer VS Code et Git pour le terminal

### 4.1 VS Code et les extensions

1. Installez [Visual Studio Code](https://code.visualstudio.com/).
2. Sous macOS, placez l’application dans Applications ; sous Windows, suivez l’installateur.
3. Ouvrez les Extensions et installez `Python` et `Jupyter`, publiées par Microsoft.
4. Utilisez `File` → `Open Folder…`, ou `Open…` selon le système, pour ouvrir la racine de votre dépôt dans Drive.

| Action | Windows | macOS |
|---|---|---|
| Palette de commandes | `Ctrl + Maj + P` | `Cmd + Maj + P` |
| Extensions | `Ctrl + Maj + X` | `Cmd + Maj + X` |
| Enregistrer | `Ctrl + S` | `Cmd + S` |

L’aperçu Markdown est intégré : depuis un fichier `.md`, lancez `Markdown: Open Preview` dans la palette. Pour les opérations Git de ce guide, continuez à utiliser Desktop : cela évite de mélanger deux interfaces.

### 4.2 Git dans VS Code et le terminal

Desktop gère déjà ses opérations Git. Pour que Git soit aussi disponible indépendamment dans VS Code ou le terminal, vérifiez :

```bash
git --version
```

Si la commande n’est pas reconnue :

- Windows : installez [Git pour Windows](https://git-scm.com/downloads/win), en conservant l’accès depuis la ligne de commande et les autres logiciels.
- macOS : lancez `git --version` dans le Terminal et acceptez les outils de ligne de commande si proposés. Vous pouvez aussi lancer `xcode-select --install`.

Rouvrez VS Code après installation. Si vous utilisez Git directement, vérifiez l’identité des commits et configurez-la si nécessaire :

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "votre.adresse@example.com"
```

Remplacez les valeurs et respectez vos préférences de confidentialité. Ce n’est pas une connexion à GitHub.

## Documentation officielle

- [Créer un compte GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
- [Créer un dépôt](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Cloner avec GitHub Desktop](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
- [Google Drive pour ordinateur](https://www.google.com/drive/download/)
- [Git](https://git-scm.com/downloads)
- [VS Code et Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
