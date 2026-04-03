# RezoluStock Inventory 📦

**Le système de gestion de stock pensé et conçu pour optimiser vos activités commerciales.**

---

## 📋 À propos

RezoluStock est une application desktop de gestion d'inventaire complète et intuitive. Elle permet aux entrepreneurs et aux petites entreprises de gérer efficacement leurs stocks, produits, clients et ventes en un seul endroit.

**Développé par** [Rezolusoft](https://rezolusoft.com) ❤️ Ajdarra, Bénin 🇧🇯

---

## 🚀 Démarrage rapide

### Prérequis

* **Python** 3.10 ou supérieur
* **pip** (gestionnaire de paquets Python)

---

### Installation

1. **Clonez le repository** :

```bash
git clone https://github.com/rezolusoft/akonta.git
cd akonta
```

2. **Préparez votre environnement et installez les dépendances** :

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. **Lancez l'application** :

```bash
flet run
```

---

## 📦 Dépendances

* **flet** 0.82.2 — Framework UI multiplateforme
* **peewee** 3.18.2 — ORM léger pour SQLite
* **peewee-migrate** 1.13.0 — Gestion des migrations
* **argon2-cffi** ≥ 25.1.0 — Hash sécurisé des mots de passe

---

## 📂 Structure du projet

```
akonta/
├── src/
│   ├── main.py                 # Point d'entrée de l'application
│   ├── components/             # Composants UI réutilisables
│   ├── layout/                 # Layouts (pager, onboarder)
│   ├── pages/                  # Pages de l'application
│   ├── models/                 # Modèles ORM (Peewee)
│   ├── themes/                 # Thèmes (dark/light)
│   ├── core/                   # Logique centrale de l'application
│   ├── utils/                  # Utilitaires et helpers
│   ├── assets/                 # Ressources (images, polices)
│   └── db/                     # Base de données & schéma
├── storage/                    # Stockage local (fichiers, uploads)
├── pyproject.toml              # Configuration du projet
├── requirements.txt            # Dépendances Python
└── README.md                   # Documentation
```

---

## 🧩 Détail des répertoires

### `/src/core` — Cœur de l’application

Contient toute la logique métier et les mécanismes globaux :

* **`auth.py`** — Gestion de l’authentification (login, logout, auto-login)
* **`state.py`** — Gestion de l’état runtime (session utilisateur)
* **`store.py`** — Persistance locale (SharedPreferences)
* **`routes.py`** — Définition des routes de navigation
* **`serializer.py`** — Sérialisation des données (JSON, Peewee → dict)

---

### `/src/utils` — Utilitaires

Fonctions et structures réutilisables :

* **`tools.py`** — Helpers (validation, upload, etc.)
* **`enums.py`** — Énumérations (roles, types, statuts)
* **`types.py`** — Types personnalisés (TypedDict, etc.)

---

### `/src/components` — Composants UI

Contient les éléments réutilisables de l’interface :

* `glass_container.py` — Effets visuels
* `rstocknotif.py` — Système de notifications

---

### `/src/layout` — Layouts

Structure globale de l’application :

* **Pager** — Interface principale (menu + top bar)
* **Onboarder** — Flux d’accueil utilisateur

---

### `/src/pages` — Pages

Chaque page correspond à une route définie dans `core/routes.py`.

**Exemple :**

```python
# core/routes.py
routes = [..., "dashboard"]

# pages/dashboard.py
def dashboard() -> ft.Control:
    return ft.Container(...)
```

---

### `/src/models` — Modèles de données

Modèles Peewee + migrations :

* `user.py` — Utilisateurs
* `shop.py` — Boutiques
* `product.py` — Produits
* `category.py` — Catégories
* `stock.py` — Inventaire
* `sale.py` — Ventes
* `invoice.py` — Factures
* `customer.py` — Clients

---

### `/src/themes` — Thèmes

* `dark.py` — Mode sombre
* `light.py` — Mode clair
* `fonts.py` — Typographie

---

### `/src/assets` — Ressources

* `img/` — Images
* `fonts/` — Polices
* `illustration/` — Illustrations

---

### `/src/db` — Base de données

* `rstock.db.schema` — Schéma de la base

---


## 🤝 Contribution

Les contributions sont les bienvenues !

1. Créez une branche depuis un issue
2. Commitez vos changements
3. Ouvrez une Pull Request

---


## 📧 Contact

* **Email** : [info@rezolusoft.com](mailto:info@rezolusoft.com)
* **Auteurs** : Rezolusoft HQ, Abiodoun Paraiso

---


## 📄 Licence

© 2025 Rezolusoft — Tous droits réservés

---
