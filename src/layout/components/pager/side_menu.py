import flet as ft
from core.router.engine import push



def side_menu_button(title, icon, page=None, destination=None)->ft.Control:

    # Déterminer si ce bouton est actif
    is_active = (page.route == destination)

    # Couleurs
    default_color = ft.Colors.PRIMARY
    active_color = ft.Colors.SECONDARY

    # On part avec la couleur active ou par défaut
    color = active_color if is_active else default_color

    button = ft.Container(
                ft.Row(
                    controls=[
                        ft.Icon(icon=getattr(ft.Icons, icon), color=color, size=20),
                        ft.Text(title, color=color),
                    
                    ],
                  expand=True,  
                ),
                padding=ft.Padding.all(2),
                margin=ft.Margin.only(left=8),
                on_click= lambda e : e.page.run_task(push, e.page, destination),
                border_radius=ft.BorderRadius.all(10),

                
            )
    

    
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
     bgcolor=ft.Colors.SURFACE,
     width=240,
     padding=10,
     border_radius=ft.BorderRadius.all(10),
     content= ft.Column(
         controls=[
            ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                                    logo,
                                
                                    menu_title('Catalogue'),
                                    side_menu_button(title="Produits", icon="INVENTORY_2_OUTLINED", destination="/product", page=page),
                                    side_menu_button(title="Catégories", icon="CATEGORY_OUTLINED", destination="/category", page=page),

                                    menu_title('Stock'),
                                    side_menu_button(title="Mon stock", icon="INVENTORY_OUTLINED", destination="/inventory", page=page),
                                    
                                    menu_title("Ventes & Finances"),
                                    side_menu_button(title="Transactions", icon="POINT_OF_SALE_OUTLINED", destination="/transactions", page=page),
                                    side_menu_button(title="Facturation", icon="RECEIPT_LONG_OUTLINED", destination="/invoices", page=page),
                                    side_menu_button(title="Dépenses", icon="MONEY_OFF_OUTLINED", destination="/expenses", page=page),

                                    menu_title("Rapports"),
                                    side_menu_button(title="Ventes", icon="DATA_EXPLORATION_OUTLINED", destination="/sale_report", page=page),
                                    side_menu_button(title="Inventaire", icon="TABLE_CHART_OUTLINED", destination="/inventory_report", page=page),
                                    side_menu_button(title="Bénéfices & Pertes", icon="BUBBLE_CHART_OUTLINED", destination="/profit_loss", page=page),

                                    menu_title("Paramètres"),
                                    side_menu_button(title="Devise", icon="CURRENCY_EXCHANGE_OUTLINED", destination="/currency", page=page),
                                    side_menu_button(title="Unités de mesure", icon="SQUARE_FOOT_OUTLINED", destination="/units", page=page),
                                    side_menu_button(title="Utilisateurs", icon="PERSON_4_OUTLINED", destination="/feedback", page=page),
                                    side_menu_button(title="Permissions", icon="SUPERVISED_USER_CIRCLE_OUTLINED", destination="/support", page=page),

                                    menu_title("Centre d'aide"),
                                    side_menu_button(title="Documentation", icon="MENU_BOOK_OUTLINED", destination="/feedback", page=page),
                                    side_menu_button(title="Support Client", icon="SUPPORT_AGENT_ROUNDED", destination="/support", page=page),
                                ],
                    ),

         ft.Container(ft.Text("Built With ❤️ By Rezolusoft", color=ft.Colors.PRIMARY, font_family="PoppinsSemiBold", text_align=ft.TextAlign.CENTER), width=float("inf"), alignment=ft.Alignment.CENTER, padding=ft.Padding.symmetric(vertical=20, horizontal=10), bgcolor=ft.Colors.GREY_100, border_radius=10)

         ]
     )

)


    return side_menu
