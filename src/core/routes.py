routes = [
    # Pages
    '/dashboard',
    '/stock',
    '/product',

    # Auth
    '/login',

    # Onboarding Pages
    '/on_welcome',
    '/on_product',
    '/on_sale',
    '/on_stats',
    '/on_start',
    '/on_shop_register',
    '/on_add_password',
    '/on_add_category',
    '/on_add_product',
    '/on_done',
]

async def push(page, destination):
    await page.push_route(destination)
