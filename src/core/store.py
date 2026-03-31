import flet as ft
from utils.types import Shop, User
import json
from core.serializers import rstore_serializer




class RStockStore():

    ##################################################################
    ############################## STORE #############################
    ##################################################################
    #                                                                #
    # Classe centralisant et gérant l’état global de l’application,  #
    # incluant sa persistance et les règles de modification          #
    #                                                                #
    ##################################################################
    ############################## CORE ##############################
    ##################################################################

    prefix = "rstock"

    # STATE SETTER
    async def _set(self, key, data):
        key = f"{self.prefix}_{key}"

        # Add logic to parse dict and list
        if isinstance(data, (dict, list)):
            data = json.dumps(data, default=rstore_serializer)
        set = await ft.SharedPreferences().set(key, data)
        return set
    
    # STATE GETTER
    async def _get(self, key):
        key = f"{self.prefix}_{key}"
        data = await ft.SharedPreferences().get(key)

        # Add auto parsing for dict and list
        try:
            return json.loads(data)
        except:
            return data
        
    # STATE DESTROYER
    async def _destroy(self, key):
        key = f"{self.prefix}_{key}"
        await ft.SharedPreferences().remove(key)
        return False


    ##################################################################
    ############################# STATE ##############################
    ##################################################################

    # SHOP
    
    async def set_shop(self, shop: Shop):
        await self._set("shop", shop)
    
    async def get_shop(self) -> Shop | None:
        return await self._get("shop")
    
    async def clear_shop(self):
        await self._destroy("shop")
    


    # ONBOARDING

    async def set_onboarding_step(self, step):
        await self._set("o_step", step)
    
    async def get_onboarding_step(self) -> str | None:
        return await self._get("o_step")
    
    async def clear_onboarding(self):
        await self._destroy("o_step")
    


    # USER

    async def user_is_authenticated(self) -> User | None:
        return await self._get("user")
    
    async def set_user_data(self, user):
        await self._set("user", user)
    
    async def clear_user(self):
        await self._destroy("user")


    # GENERAL

    async def clear_all_data(self):
        print("### EREASE STORE ###")
        await self.clear_shop()
        await self.clear_onboarding()
        await self.clear_user()
        print("##### DONE ######")
    