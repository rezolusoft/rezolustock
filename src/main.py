import flet as ft
from themes import light_theme, dark_theme, font_loader
from models.db_initializer import db_initializer
from core.store import RStockStore
from core.state import RstockState
from core.router.engine import RouterEngine
from core.layout import build_layout


async def main(page: ft.Page):

  
    # Initialiser une instance du store
    store = RStockStore()
    
    # Initialiser une instance du state
    state = RstockState(page)
    
    # Initialiser une instance du routeur
    onboarding_step = await store.get_onboarding_step()
    print(f"step------>{onboarding_step}")
    print(f"route----->{page.route}")
    router_engine = RouterEngine(page, store, state)

    

    db_initializer()


    # Definir Titre
    page.title = "RezoluStock"


    # Charger les police personnalisé 
    font_loader(page=page)
    # Maximiser la fenetre
    page.window.maximized = True
    # Charger le theme
    page.theme = light_theme
    page.theme_mode = ft.ThemeMode.LIGHT
    page.dark_theme = dark_theme
   


    # Recuperer les infos de l'onboarding

    # initialiser le contenu et de l'echaffaudage
    layout = ft.Container(expand=True)
    content_container = ft.Container(expand=True)


    async def router(e: ft.RouteChangeEvent):
        route = page.route
        router_engine = RouterEngine(page, store, state)
        result = await router_engine.resolve(route)

        if "redirect" in result:
            print(f"redirect----->{result["redirect"]}")
            await page.push_route(result["redirect"])
            return

        content = build_layout(page, result, content_container)
        layout.content = content
        page.update()

        print("content---->", content)
        print(f"route----->{page.route}")
        
        


    # ajout de l'echaffaudage a la page
    page.add(layout)

    page.on_route_change = router

    page.update()

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
