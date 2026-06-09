from .routes import routes

class RouterEngine():
    
    def __init__(self, page, store, state):

        self.page = page
        self.store = store
        self.state = state

    async def resolve(self, path: str)->dict:
        route = routes.get(path)
        onbaording_step = await self.store.get_onboarding_step()
        

        if path == "/":
            if onbaording_step == "completed":
                authenticated = await self.state.is_authenticated()
                if authenticated :
                    return {"redirect": "/dashboard"}
                else:
                    saved_session = await self.store.remember_me()
                    if saved_session:
                        from core.auth import RstockAuthentication
                        auth = RstockAuthentication(self.state, self.store)
                        await auth.auto_login()
                        return {"redirect": "/dashboard"}
                    else:
                        return {"redirect": "/login"}

            else:
                return {"redirect": f"/{onbaording_step or 'on_welcome'}"}

        else:
            
            if route :
                # Chargement de la view...
                view = route.get_view()
    
                content = view()
    
                if route.requires_root:
                    content = view(page=self.page)
    
            
                return {
                    "type" : "view",
                    "layout" : route.layout,
                    "content" : content
                }

