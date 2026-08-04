from .routes import routes

class RouterEngine():
    
    def __init__(self, page, store, state):

        self.page = page
        self.store = store
        self.state = state

    async def resolve(self, path: str)->dict:
        route = routes.get(path)
        
        if not route:
            return {"type":"error", "content": "Page introuvable"}
        

        # S'assurer du fait que l'utilisateur a fait le onboarding
        onbaording_step = await self.store.get_onboarding_step()
        

        if onbaording_step != "completed" and route.layout != "onboarding":
            return {"redirect":f"/{onbaording_step or "on_welcome"}"}
        
        
        # Verifier l'authentification
        if route.requires_auth and not self.state.is_authenticated():
            return {"redirect": "/login"}
            

        # Chargement de la view...
        view = route.get_view()

        

        if route.requires_page:
            if route.is_async:
                content = await view(page=self.page)
            else:
                content = view(page=self.page)

        else:
            if route.is_async:
                content = await view(self.page)
            else:
                content = view(self.page)

        return {
            "type" : "view",
            "layout" : route.layout,
            "content" : content
        }



async def push(page, destination):
    await page.push_route(destination)

