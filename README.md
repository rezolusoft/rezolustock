# RezoluStock Inventory 📦

**Le système de gestion de stock pensé et conçu pour optimiser vos activités commerciales.**

---

## 📋 À propos

RezoluStock est une application desktop de gestion d'inventaire complète et intuitive. Elle permet aux entrepreneurs et aux petites entreprises de gérer efficacement leurs stocks, produits, clients et ventes en un seul endroit.

**Développé  par** [Rezolusoft](https://rezolusoft.com) ❤️ Ajdarra, Bénin 🇧🇯

---

## 🚀 Démarrage rapide

### Prérequis

- **Python** 3.10 ou supérieur
- **pip** (gestionnaire de paquets Python)

### Installation

1. **Clonez le repository** :
```bash
git clone https://github.com/rezolusoft/akonta.git
cd akonta
```

2. **Préparez votre environnement et installez les dépendances** :
```bash
virtualenv venv -p3
source venv/bin/actvivate
pip install -r requirements.txt
```

3. **Lancez l'application** :
```bash
flet run
```

---

## 📦 Dépendances

- **flet** 0.82.2 - Framework UI multiplateforme
- **peewee** 3.18.2 - ORM léger pour base de données SQLite
- **peewee-migrate** 1.13.0 - Système de migration pour Peewee
- **argon2-cffi** ≥ 25.1.0 - Chiffrement sécurisé des mots de passe

---

## 📂 Structure du projet

```
akonta/
├── src/
│   ├── main.py                 # Point d'entrée de l'application
│   ├── components/             # Composants réutilisables (UI)
│   ├── layout/                 # Mise en page principale (pager, onboarder)
│   ├── pages/                  # Pages de l'application
│   ├── models/                 # Modèles de données
│   ├── themes/                 # Thèmes de l'application
│   ├── extras/                 # Utilitaires et configurations
│   ├── assets/                 # Ressources (images, polices)
│   └── db/                     # Schéma et fichiers de base de données
├── storage/                    # Stockage des données locales
├── pyproject.toml              # Configuration du projet
├── requirements.txt            # Dépendances Python
└── README.md                   # Ce fichier
```

### Détail des répertoires

#### `/src/components` - Composants personnalisés
Contient tous les contrôles UI réutilisables de l'application.
- `glass_container.py` - Conteneurs avec effet de verre
- `rstocknotif.py` - Système de notifications

#### `/src/layout` - Mise en page principale
Gère la structure générale de l'application :
- **Pager** - Structure de base avec `side_menu` et `top_bar`
- **Onboarder** - Expérience d'accueil du nouveau utilisateur (du bienvenue à la création du premier produit)

#### `/src/pages` - Pages de l'application
Chaque page correspond à une route dans `src/extras/routes.py`. Chaque fichier contient une fonction du même nom qui retourne un objet `flet.Control`.

**Exemple de structure** :
```python
# src/extras/routes.py
routes = [..., 'dashboard', ...]

# src/pages/dashboard.py
def dashboard() -> flet.Control:
    """Retourne le contenu de la page tableau de bord"""
    return flet.Container(...)
```

**Pages actuelles** :
- `dashboard.py` - Tableau de bord principal
- `product.py` - Gestion des produits
- `stock.py` - Gestion du stock

#### `/src/extras` - Utilitaires et configurations
- **`enums.py`** - Collections d'énumérations (paires clé-valeur)
- **`routes.py`** - Définition de toutes les routes de l'application
- **`store.py`** - Gestion du localStorage pour les préférences utilisateur
- **`tools.py`** - Fonctions utilitaires réutilisables

#### `/src/models` - Modèles de données
- Modèles ORM Peewee pour la base de données
- Fichiers de migration pour versionner le schéma
- `db_initializer.py` - Initialisation de la base de données

Modèles principaux :
- `user.py` - Utilisateurs
- `shop.py` - Magasins
- `product.py` - Produits
- `category.py` - Catégories de produits
- `stock.py` - Inventaire
- `sale.py` - Ventes
- `invoice.py` - Factures
- `customer.py` - Clients

#### `/src/themes` - Thèmes
- `dark.py` - Thème sombre
- `light.py` - Thème clair
- `fonts.py` - Configurations typographiques

#### `/src/assets` - Ressources
- `img/` - Images de l'application
- `fonts/` - Polices de caractères
- `illustration/` - Illustrations

#### `/src/db` - Base de données
- `rstock.db.schema` - Schéma de la base de données

---

## 🏗️ Architecture

L'application suit une architecture **modulaire et basée sur les composants** :

1. **Pages** (`/pages`) - Écrans principaux liées aux routes
2. **Layout** (`/layout`) - Structure de mise en page (navigation, accueil)
3. **Components** (`/components`) - Composants réutilisables
4. **Models** (`/models`) - Couche données (ORM Peewee)
5. **Extras** (`/extras`) - Logique métier et utilitaires

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour contribuer :

1. Créez une branche pour votre fonctionnalité à partir d'un issue qui détails vos modifications
2. Commitez vos changements
3. Ouvrez une Pull Request

---

## 📄 Licence

© 2025 Rezolusoft - Tous droits réservés

---

## 📧 Contact

- **Email** : info@rezolusoft.com
- **Auteurs** : Rezolusoft HQ, Abiodoun Paraiso





