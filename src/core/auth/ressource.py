from core.auth.BasePermission import Permission


class Resource():
    """
    Représente une ressource dans le du système
    Par défaut sur une ressource on peut effectuer 
    quatre actions principale qui correspondent
    chacunes à des objets permission. On peut créer
    des ressource personnalisé pour prendre en compte
    des actions supplémentaire.
    """


    def __init__(self, name):
        self.name = name


    @property
    def add(self):
        return Permission(self.name, 'add')

    @property
    def view(self):
        return Permission(self.name, 'view')


    @property
    def change(self):
        return Permission(self.name, 'change')


    @property
    def delete(self):
        return Permission(self.name, 'delete')



class CategoryResource(Resource):
    pass
CATEGORY = CategoryResource("category")



class ProductResource(Resource):
    @property
    def archive(self):
        return Permission(self.name, 'archive')
    
PRODUCT = ProductResource("product")



class UserResource(Resource):
    @property
    def block(self):
        return Permission(self.name, 'block')
    
USER = UserResource("user")


class CustomerResource(Resource):
    pass
CUSTOMER = Resource("customer")



class SaleResource(Resource):
    @property
    def refund(self):
        return Permission(self.name, 'refund')

    @property
    def export(self):
        return Permission(self.name, 'export')
    
SALE = SaleResource("sale")



