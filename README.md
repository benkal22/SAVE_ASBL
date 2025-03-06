# SAVE_ASBL Project

## Description

SAVE_ASBL est un projet basé sur Django CMS 4.1.4 et Django 5.1.6, conçu pour gérer le contenu d'une organisation à but non lucratif. Le projet utilise une variété de plugins et de fonctionnalités pour offrir une expérience utilisateur riche et dynamique.

## Fonctionnalités principales

- **Gestion de contenu dynamique** : Utilisation de Django CMS pour créer et gérer des pages de contenu de manière intuitive.
- **Support multilingue** : Le site prend en charge plusieurs langues, notamment l'anglais et le français.
- **Plugins personnalisés** : Intégration de plugins personnalisés pour des fonctionnalités spécifiques telles que les carousels d'images, les vidéos d'introduction, les témoignages, et plus encore.
- **Design réactif** : Utilisation de Tailwind CSS et Flowbite pour un design moderne et réactif.
- **Gestion des médias** : Utilisation de django-filer pour gérer les fichiers et les images de manière efficace.
- **Sécurité et permissions** : Mise en place de permissions pour contrôler l'accès et les actions des utilisateurs.

## Technologies utilisées

- **Django CMS** : Pour la gestion de contenu.
- **Django** : Framework web principal.
- **Tailwind CSS** : Pour le design et la mise en page.
- **Flowbite** : Composants UI pour Tailwind CSS.
- **Alpine.js** : Pour les interactions JavaScript légères.
- **django-filer** : Pour la gestion des fichiers et des images.
- **easy-thumbnails** : Pour la génération de vignettes d'images.
- **django-compressor** : Pour la compression des fichiers CSS et JavaScript.

## Installation et exécution

1. Cloner le dépôt du projet :
    ```sh
    git clone <URL_DU_DEPOT>
    cd SAVE_ASBL
    ```

2. Créer et activer un environnement virtuel :
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # Sur Windows
    source .venv/bin/activate  # Sur macOS/Linux
    ```

3. Installer les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

4. Appliquer les migrations de la base de données :
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Démarrer le serveur de développement :
    ```sh
    python manage.py runserver
    ```

## Configuration

### Base de données

Le projet utilise SQLite par défaut. Vous pouvez configurer d'autres bases de données dans le fichier `settings.py`.

### Fichiers statiques et médias

Les fichiers statiques et les médias sont configurés pour être servis correctement. Assurez-vous que les répertoires `static` et `media` existent dans votre projet.

### Internationalisation

Le projet prend en charge plusieurs langues. Vous pouvez ajouter des langues supplémentaires dans le fichier `settings.py`.

## Structure du projet

- **settings.py** : Configuration principale du projet.
- **urls.py** : Configuration des routes URL.
- **templates** : Répertoire contenant les templates HTML.
- **static** : Répertoire contenant les fichiers statiques (CSS, JS, images).
- **cms_plugins** : Répertoire contenant les plugins personnalisés.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre des pull requests ou ouvrir des issues pour signaler des bugs ou proposer des améliorations.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
