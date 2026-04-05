import flet as ft
from themes import light_theme, dark_theme, font_loader
from layout import pager, onboarder
from pages.auth.login import login
from core.routes import routes
from importlib import import_module
from models.db_initializer import db_initializer
from core.store import RStockStore
from core.state import RstockState


async def main(page: ft.Page):

  
    # Initialiser une instance du store
    store = RStockStore()
    # Initialiser une instance du state
    state = RstockState(page)
    # Récupérer les données du store lier a l'oboarding
    onboarding_step = await store.get_onboarding_step()


    # fetch connected user at the top level to avoid coroutine error


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




    # Maximiser la fenetre
    page.window.maximized = True

    # Recuperer les infos de l'onboarding

    # initialiser le contenu a vide
    content_container = ft.Container(expand=True)
    # initialisation de l'echaffaudage
    layout = ft.Container(expand=True)

    async def router(e: ft.RouteChangeEvent):
        # charger dynamiquement le contenu
        # adequat en fonction de la route
        route = page.route
        onboarding_step = await store.get_onboarding_step()

        if route in routes:
            route = route.lstrip("/")
            # recuperation conditionnel des pages en fonction des routes et 
            # de l'onboarding
            if onboarding_step=="completed":
                if route=="login":
                    layout.content = await login(page)
                else:
                    content = import_module(f"pages.{route}")
                    content_container.content = getattr(content, route)()
                    # reconstruction de l'echaffaudage au changement de route 
                    layout.content = pager(page=page, content=content_container)
            else:
                content = import_module(f"pages.onboarding.{route}")
                content_container.content = getattr(content, route)(page)

                # reconstruction de l'echaffaudage au changement de route 
                layout.content = onboarder(content=content_container, illustration=route.lstrip('/'))
        else:
            layout.content = ft.Text("Page introuvable")
        
        page.update()
        


    # ajout de l'echaffaudage a la page
    page.add(layout)

    page.on_route_change = router
    
    # Controle de la page par défaut
    # redirection conditionnel vers la page initiale 
    if page.route == "/":
        if onboarding_step=="completed":
            # add auth verification
            if state.is_authenticated():
                await page.push_route('/dashboard')
            else:
                saved_session = await store.remember_me()
                if saved_session:
                    from core.auth import RstockAuthentication
                    auth = RstockAuthentication(state, store)
                    await auth.auto_login()
                    await page.push_route('/dashboard')
                else:
                    await page.push_route('/login')
        else:
            if onboarding_step:
                await page.push_route(f"/{onboarding_step}")
            else:
                await page.push_route('/on_welcome')

    else:
        await page.push_route(page.route)


ft.run(main)
