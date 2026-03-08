import flet as ft
from .side_menu_button import side_menu_button


def menu_title(_title: str) -> ft.Control:

    title = ft.Container(ft.Text(value=_title))
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
            menu_title('Menu Principal'),
            side_menu_button(title="Tableau de bord", icon="DASHBOARD_ROUNDED", destination="/dashboard", page=page),
            side_menu_button(title="Mon Stock", icon="WAREHOUSE_ROUNDED", destination="/stock", page=page),
            side_menu_button(title="Mes Produits", icon="INVENTORY_ROUNDED", destination="/product", page=page),
            side_menu_button(title="Ma Caisse", icon="WALLET_ROUNDED", destination="/cashier", page=page),
            side_menu_button(title="Mes statistiques", icon="BAR_CHART_ROUNDED", destination="/datas", page=page),
            spacer,
            menu_title("Centre d'aide"),
            side_menu_button(title="Donner un avis", icon="MODE_COMMENT", destination="/feedback", page=page),
            side_menu_button(title="Support Client", icon="SUPPORT_AGENT_ROUNDED", destination="/support", page=page),

        ]),

)


    side_menu.border_radius = ft.border_radius.all(7)
    side_menu.padding = ft.padding.all(10)

    return side_menu
