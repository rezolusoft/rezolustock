import flet as ft
from themes import light_theme, dark_theme, font_loader
from components import pager, onboarder
from extras.routes import routes
from importlib import import_module
from models.db_initializer import db_initializer
from extras.store import RStockStore


def main(page: ft.Page):

    db_initializer()

    # Maximiser la fenetre
    page.window.maximized = True
    # Definir Titre
    page.title = "RezoluStock"


    # Charger les police personnalisé 
    font_loader(page=page)

    # Charger le theme
    page.theme = light_theme
    page.theme_mode = ft.ThemeMode.LIGHT
    page.dark_theme = dark_theme
    page.bgcolor = None
    page.padding = 0
    page.spacing = 0


    # Initialiser une instance du store
    store = RStockStore(page)
    # Récupérer les données du store lier a l'oboarding
    onboarded = store.get("onboarded")
    onboarding_step = store.get("onboarding_step")


    # Recuperer les infos de l'onboarding
    
    # initialiser le contenu a vide
    content_container = ft.Container(expand=True)

    # initialisation de l'echaffaudage
    layout = pager(page=page, content=content_container)

    def router(e: ft.RouteChangeEvent):
        # charger dynamiquement le contenu
        # adequat en fonction de la route
        route = page.route

        if route in routes:
            route = route.lstrip("/")
            # recuperation conditionnel des pages en fonction des routes et 
            # de l'onboarding
            if onboarded:
                content = import_module(f"pages.{route}")
                content_container.content = getattr(content, route)()
            else:
                content = import_module(f"pages.onboarding.{route}")
                content_container.content = getattr(content, route)(page)
        else:
            content_container.content = ft.Text("Page introuvable")
        # reconstruire l'echaffaudage au changement de route 
        if onboarded:
            layout.content = pager(page=page, content=content_container)
        else:
            layout.content = onboarder(content=content_container, illustration=route.lstrip('/'))
        page.update()
        


    # ajout de l'echaffaudage a la page
    page.add(layout)

    page.on_route_change = router

    # Controle de la page par défaut
    # redirection conditionnel vers la page initiale 
    if page.route == "/":
        if onboarded:
            page.go('/dashboard')
        else:
            page.go('/on_shop_register')
        
    else:
        page.go(page.route)


ft.app(main)
