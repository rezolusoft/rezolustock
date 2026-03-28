# RezoluStock Inventory 📦  
**Le système de gestion de stock pensé et conçu pour optimiser vos activités.**  


## Organisation du Repo

- ```/src/components```  Repertoire principal qui comporte l'ensemble des 
controles presonalisés

- ```/src/layout```  Contient les controles dynamiques de l'echaffaudage de l'application notament
    
    * Un pager qui met en place la structure de base en chargeant en son sein la ```side_menu``` et la ```top_bar```

    * Un Onboarder qui met en place la structure de base de
    l'experience d'accueil du logiciel : de l'ecran de bienvenue a la creation de son premier produit

- ```/src/extras``` Contient l'ensemble des utilitaires du logiciel notament
   
    * un fichier ```enums``` qui liste l'ensemble des collections d'élements Pair = Valeur.

    * un fichier ```routes``` qui liste l'ensemble des routes liés à chaque pages dans src/pages.

    * un fichier ```store``` qui gère les interaction avec le client storage pour la gestion des préférence et donnés produite et utilisé par le fonctionnement de l'appli.

    * un fichier ```tool``` qui contient l'ensemble des petites fonctions utiles au fonctionnement de l'application.

- ```/src/pages```  contient l'ensemble des pages des l'application.
 
    Les pages sont intresquement liées aux routes listé dans ```src/extras/routes```. Chaque route correspond à un fichier dans ```/src/page``` au nom de cette route qui porte en son sein une fonction du meme nom censé retourner un objet flet.Control representant le contenu de la page

```python 
    # Exemple
    # -------

    # src/extras/routes.py
    routes = [..., 'dashboard', '...']


    # src/pages/dashboard.py
    def dashboard()->flet.Control:
        return flet.Container()
    
```

- ```/src/models``` : contient les fichier de gestion des données de la bd

- ```/src/themes``` : contient les fichiers de themes

- ```/src/assets``` : contient les assets

- ```/src/db``` : contient les fichiers de base de données





