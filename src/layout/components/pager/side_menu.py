import flet as ft
from core.routes import push



def side_menu_button(title, icon, page=None, destination=None)->ft.Control:

    # Déterminer si ce bouton est actif
    is_active = (page.route == destination)

    # Couleurs
    default_bg = ft.Colors.TRANSPARENT
    hover_bg = ft.Colors.ORANGE_50
    active_bg = ft.Colors.ORANGE_100

    # On part avec la couleur active ou par défaut
    bg_color = active_bg if is_active else default_bg

    button = ft.Container(
                ft.Row(
                    controls=[
                        ft.Icon(icon=getattr(ft.Icons, icon), color=ft.Colors.PRIMARY, size=20),
                        ft.Text(title, color=ft.Colors.ON_SURFACE),
                    
                    ],
                  expand=True,  
                ),
                padding=ft.Padding.all(3),
                margin=ft.Margin.only(left=7),
                bgcolor=bg_color,
                on_click= lambda e : e.page.run_task(push, e.page, destination),
                border_radius=ft.BorderRadius.all(5),

                
            )
    
    def on_hover(e: ft.HoverEvent):
        if not is_active:  # On ne change pas si déjà actif
            button.bgcolor = hover_bg if e.data == "true" else default_bg
            button.update()

    button.on_hover = on_hover
    
    return button



def menu_title(_title: str) -> ft.Control:

    title = ft.Container(ft.Text(value=_title, color=ft.Colors.ON_SURFACE, style=ft.TextStyle(size=12, font_family="PoppinsBold")))
    title.margin = ft.Margin.only(top=10)
    return title


logo = ft.Container(ft.Image(src="img/logo.png"), height=48,)



spacer = ft.Container()


spacer.margin = ft.Margin.symmetric(vertical=10)

def side_menu(page)->ft.Control:
    
    side_menu = ft.Container(
     # bgcolor=ft.Colors.SURFACE,
     width=240,
     padding=10,
     border_radius=ft.BorderRadius.all(7),
    content=ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        controls=[
            logo,
           
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
        

        ),

        

)


    return side_menu
