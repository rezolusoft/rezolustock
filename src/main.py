import flet as ft
from themes import light_theme, dark_theme, font_loader
from layout import pager, onboarder
from extras.routes import routes
from importlib import import_module
from models.db_initializer import db_initializer
from extras.store import RStockStore


async def main(page: ft.Page):

    db_initializer()

    
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
    store = RStockStore()
    # Récupérer les données du store lier a l'oboarding
    onboarded = await store.check("onboarded")
    onboarding_step = await store.get("onboarding_step")

    # Maximiser la fenetre
    page.window.maximized = True

    # Recuperer les infos de l'onboarding

    # initialiser le contenu a vide
    content_container = ft.Container(expand=True)

    # initialisation de l'echaffaudage
    layout = pager(page=page, content=content_container)

    async def router(e: ft.RouteChangeEvent):
        # charger dynamiquement le contenu
        # adequat en fonction de la route
        route = page.route
        onboarded = await store.check("onboarded")

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
            await page.push_route('/dashboard')
        else:
            if onboarding_step:
                await page.push_route(f"/{onboarding_step}")
            else:
                await page.push_route('/on_welcome')

    else:
        await page.push_route(page.route)


ft.run(main)
