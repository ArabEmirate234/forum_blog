DIY Forum

DIY Forum est une plateforme web conçue pour permettre aux utilisateurs de partager des idées de bricolage (DIY), de discuter dans des fils de discussion, et de contribuer via des commentaires et des publications.

---

Caractéristiques

- **Gestion des Catégories** : Permet de créer et gérer des catégories pour organiser les threads.
- **Fils de Discussion** : Création de threads associés aux catégories.
- **Système de Publications** : Les utilisateurs peuvent publier des réponses/commentaires dans les threads.
- **Likes & Commentaires** : Fonctionnalité pour liker et commenter les publications.
- **Authentification** : Connexion, déconnexion, et gestion des utilisateurs.
- **API REST** : Accès aux catégories, threads et publications via une API REST utilisant Django REST Framework.
- **Test Automatisé** :
  - Tests unitaires et d'intégration avec `unittest`.
  - Tests de performance avec `locust`.

---

Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés :

- Python 3.7 ou plus récent
- Django 3.2 ou plus récent
- Un serveur de base de données SQLite (préconfiguré pour ce projet)
- `pip` pour installer les dépendances Python
- `locust` pour les tests de performance
- `flake8` pour l'analyse de code

---

## **Installation**

1. Clonez le dépôt Git :
   ```bash
   git clone https://github.com/ArabEmirate234/forum_blog.git
   cd forum_blog
   ```

2. Configurez un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate  # Pour Linux/Mac
   env\Scripts\activate     # Pour Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

Accédez au site web à [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

API REST

Les API REST sont accessibles via les endpoints suivants :

- Catégories : `/api/categories/`
- Threads : `/api/threads/`
- Posts : `/api/posts/`

Vous pouvez tester ces API avec des outils comme Postman ou cURL.

---

Tests

Tests unitaires et d'intégration
1. Lancez les tests avec :
   ```bash
   python manage.py test
   ```

Tests de performance
1. Lancez les tests Locust :
   ```bash
   locust
   ```
2. Accédez à l'interface Locust à [http://127.0.0.1:8089](http://127.0.0.1:8089).

---

Outils et Technologies

- Backend : Django, Django REST Framework
- Frontend : Bootstrap
- Base de Données : SQLite
- Tests : `unittest`, `locust`, `flake8`
- Linting : `flake8`, `black`, `isort`

---

Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

Auteurs

- Nom : [ArabEmirate234](https://github.com/ArabEmirate234)
- Projet : Forum DIY

N'hésitez pas à poser vos questions ou à suggérer des améliorations ! 🎉

--- 
