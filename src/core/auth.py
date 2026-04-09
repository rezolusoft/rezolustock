import flet as ft
from argon2 import PasswordHasher
from models.user import User
from utils.types import UserType
from datetime import datetime
from components.notification import rstocknotif



class RstockAuthentication():

    
    def __init__(self, state, store):
        self.state = state
        self.store = store
    


    def _make_password(self, password:str)->str:
        # create and return a password
        hasher = PasswordHasher()
        
        return hasher.hash(password)



    def _check_password(self, hash, password)->bool:
        # check a password 
        return PasswordHasher().verify(hash, password)
    

    
    def _user_exist(self, email):
        
        try:
            user = User.get(User.email==email)
            
            return user
        
        except Exception as e:

            print("Utilisateur introuvable")
            return False



    def create_user(self, first_name:str|None, last_name:str|None, email:str, phone:str, password:str, account_type:str, avatar:str|None=None,):
        # create and return a new user

        if self._user_exist(email):

            return False
        
        else :

            password = self._make_password(password)
            try:
                user = User(
                    avatar = avatar,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    phone = phone,
                    password = password,
                    account_type = account_type
                )
                user.save()

            except Exception as e:
                print(e)
                return False
            
            return user


    async def login(self, login, password, persist=False) -> bool:
        
        user = self._user_exist(login)

        try:
            
            if self._check_password(user.password, password):
                user.last_seen = datetime.now()
                user.save()

                shop  = await self.store.get_shop()

                user_data = {
                    "id" : user.id,
                    "avatar": user.avatar,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "phone": user.phone,
                    "account_type": user.account_type,
                    "last_seen": user.last_seen,
                    "shop": shop
                }

                self.state.set_user(user_data)

                if persist:
                    await self.store.set_user(user_data)

                
                
                return True

            else:
                print("Email ou mot de passe invalide.")
                return False
                
        
        except Exception as e:
            print(e)
            return False


    async def auto_login(self):
        saved_user = await self.store.get_user()
        self.state.set_user(saved_user)


    async def refresh(self):
        pass


    async def logout(self):
        self.state.clear_user()
        await self.store.clear_user()

    
