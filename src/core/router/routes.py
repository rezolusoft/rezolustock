from .base import Route


routes = {

    # Auth
    "/login": Route(path="/login", module="pages.auth.login", view="login", layout="auth", requires_page=True, is_async=True),

    # Main
    "/dashboard": Route(path="/dashboard", module="pages.dashboard", view="dashboard", layout="main"),
    "/inventory": Route(path="/inventory", module="pages.inventory", view="inventory", layout="main"),
    "/product": Route(path="/product", module="pages.product", view="product", layout="main"),

    # Onboarding
    "/on_welcome": Route(path="/on_welcome", module="pages.onboarding.on_welcome", view="on_welcome",  layout="onboarding"),
    "/on_product": Route(path="/on_product", module="pages.onboarding.on_product", view="on_product",  layout="onboarding"),
    "/on_sale": Route(path="/on_sale", module="pages.onboarding.on_sale", view="on_sale",  layout="onboarding"),
    "/on_stats": Route(path="/on_stats", module="pages.onboarding.on_stats", view="on_stats",  layout="onboarding"),
    "/on_start": Route(path="/on_start", module="pages.onboarding.on_start", view="on_start",  layout="onboarding"),
    "/on_shop_register": Route(path="/on_shop_register", module="pages.onboarding.on_shop_register", view="on_shop_register", requires_page=True,  layout="onboarding"),
    "/on_add_password": Route(path="/on_add_password", module="pages.onboarding.on_add_password", view="on_add_password", requires_page=True,  layout="onboarding"),
    "/on_add_category": Route(path="/on_add_category", module="pages.onboarding.on_add_category", view="on_add_category", requires_page=True,  layout="onboarding"),
    "/on_add_product": Route(path="/on_add_product", module="pages.onboarding.on_add_product", view="on_add_product", requires_page=True,  layout="onboarding"),
    "/on_done": Route(path="/on_done", module="pages.onboarding.on_done", view="on_done", requires_page=True,  layout="onboarding"),

}
