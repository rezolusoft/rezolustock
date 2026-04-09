import flet as ft
from utils.types import ShopType, UserType
import json
from core.serializers import rstore_serializer




class RStockStore():
    """
    
    ##################################################################
    ############################## STORE #############################
    ##################################################################
    #                                                                #
    #     Couche de persistance responsable du stockage et de la     #
    #      récupération des données locales (SharedPreferences).     #
    #                                                                #
    ##################################################################
    ############################## CORE ##############################
    ##################################################################
    """
    prefix = "rstore"

    def _get_key(self, key):
        return f"{self.prefix}_{key}"
    

    async def _set(self, key, data):
        key = self._get_key(key)
        if isinstance(data, (dict, list)):
            data = json.dumps(data, default=rstore_serializer)
        set = await ft.SharedPreferences().set(key, data)
        return set

    
    async def _get(self, key, default=None):
        key = self._get_key(key)
        data = await ft.SharedPreferences().get(key)

        if data is None:
            return default

        try:
            return json.loads(data)
        except Exception:
            return data
        

    async def _destroy(self, key):
        key = self._get_key(key)
        await ft.SharedPreferences().remove(key)
        return False


    ##################################################################
    ############################# STORE ##############################
    ##################################################################

    ##### SHOP #####
    
    async def set_shop(self, shop: ShopType):
        await self._set("shop", shop)
    
    async def get_shop(self) -> ShopType | None:
        return await self._get("shop")
    
    async def clear_shop(self):
        await self._destroy("shop")
    


    ##### ONBOARDING #####

    async def set_onboarding_step(self, step):
        await self._set("o_step", step)
    
    async def get_onboarding_step(self) -> str | None:
        return await self._get("o_step")
    
    async def clear_onboarding(self):
        await self._destroy("o_step")
    


    ##### USER #####

    async def get_user(self) -> UserType | None:
        return await self._get("user")
    
    async def set_user(self, user:UserType):
        await self._set("user", user)
    
    async def remember_me(self):
        return await self.get_user() is not None
    
    async def clear_user(self):
        await self._destroy("user")


    ##### GENERAL #####

    async def clear_all_data(self):
        print("### EREASE STORE ###")
        await self.clear_shop()
        await self.clear_onboarding()
        await self.clear_user()
        print("##### DONE ######")
    