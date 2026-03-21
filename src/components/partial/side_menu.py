import flet as ft
from .side_menu_button import side_menu_button


def menu_title(_title: str) -> ft.Control:

    title = ft.Container(ft.Text(value=_title, color=ft.Colors.ON_SURFACE, style=ft.TextStyle(size=12, font_family="PoppinsBold")))
    title.margin = ft.margin.only(top=10)
    return title


logo = ft.Container(ft.Image(src="img/logo.png"), height=50)



spacer = ft.Container()

spacer.margin = ft.margin.symmetric(vertical=10)

def side_menu(page)->ft.Control:
    
    side_menu = ft.Container(
    # bgcolor=ft.Colors.SURFACE,

    content=ft.Column(
        expand=True,
        controls=[
            logo,
            ft.Column(
                controls=[
            menu_title('Inventaire'),
            side_menu_button(title="Produits", icon="INVENTORY_2_OUTLINED", destination="/product", page=page),
            side_menu_button(title="Catégories", icon="CATEGORY_OUTLINED", destination="/category", page=page),
            side_menu_button(title="Gestion de stock", icon="INVENTORY_OUTLINED", destination="/inventory", page=page),
            side_menu_button(title="Devise", icon="CURRENCY_EXCHANGE_OUTLINED", destination="/currency", page=page),
            side_menu_button(title="Unités de mesure", icon="SQUARE_FOOT_OUTLINED", destination="/units", page=page),

            menu_title("Ventes & Finances"),
            side_menu_button(title="Transactions", icon="POINT_OF_SALE_OUTLINED", destination="/transactions", page=page),
            side_menu_button(title="Facturation", icon="RECEIPT_LONG_OUTLINED", destination="/invoices", page=page),
            side_menu_button(title="Dépense", icon="MONEY_OFF_OUTLINED", destination="/expenses", page=page),


            menu_title("Satistiques & Raports"),
            side_menu_button(title="Rapports de ventes", icon="DATA_EXPLORATION_OUTLINED", destination="/sale_report", page=page),
            side_menu_button(title="Rapports d'inventaire", icon="TABLE_CHART_OUTLINED", destination="/inventory_report", page=page),
            side_menu_button(title="Bénéfices et Pertes", icon="BUBBLE_CHART_OUTLINED", destination="/profit_loss", page=page),

            menu_title("Utilisateurs & Permissions"),
            side_menu_button(title="Utilisateurs", icon="PERSON_4_OUTLINED", destination="/feedback", page=page),
            side_menu_button(title="Permissions", icon="SUPERVISED_USER_CIRCLE_OUTLINED", destination="/support", page=page),


            menu_title("Centre d'aide"),
            side_menu_button(title="Documentation", icon="MENU_BOOK_OUTLINED", destination="/feedback", page=page),
            side_menu_button(title="Support Client", icon="SUPPORT_AGENT_ROUNDED", destination="/support", page=page),

                ],
                
            )
        ],
            scroll=ft.ScrollMode.AUTO
        ),

)


    side_menu.border_radius = ft.border_radius.all(7)
    side_menu.padding = ft.padding.all(10)

    return side_menu
