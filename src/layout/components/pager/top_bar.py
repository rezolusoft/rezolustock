import flet as ft
from core.state import RstockState

def search_bar() -> ft.Control:

    search_bar = ft.Container(ft.TextField(hint_text="Rechercher...", prefix_icon=ft.Icons.SEARCH_OUTLINED, dense=True, text_size=14, width=220,))
    search_bar.margin = ft.Margin.symmetric(horizontal=10)

    return search_bar


def new_button() -> ft.Control:
    
    new_button = ft.TextButton(content="Nouveau", 
                               
                               style=ft.ButtonStyle(bgcolor=ft.Colors.SECONDARY,
                                                    color=ft.Colors.WHITE,
                                                    shape=ft.RoundedRectangleBorder(radius=5),
                                                    text_style=ft.TextStyle(font_family="PoppinsSemiBold")
                                                    ),
                                icon=ft.Icons.ADD_CIRCLE_OUTLINE_OUTLINED
                            )

    return new_button

def pos_button(page) -> ft.Control:
    state = RstockState(page)
    user = state.get_user()
    shop = user["shop"]

    async def push(e):
        await e.page.push_route('/dashboard')

    pos_button = ft.Container(
    content=ft.Row([
        ft.Container(
            content=ft.Image(f"{shop['logo']}", width=16, height=16),
            bgcolor=ft.Colors.WHITE,
            padding=2,
            border_radius=5,
        ),
        ft.Text(shop["name"], color=ft.Colors.WHITE, font_family="PoppinsSemiBold")
    ]),
    bgcolor=ft.Colors.PRIMARY,
    padding=5,
    border_radius=5,
    on_click= push
    )

    return pos_button

def calc_button() -> ft.Control:

    calc_button = ft.Container(
                content=ft.Icon(ft.Icons.CALCULATE_OUTLINED, size=22, color=ft.Colors.PRIMARY),
                bgcolor=ft.Colors.GREY_100,
                padding=5,
                border_radius=5,
            )

    return calc_button


def fulscreen_button() -> ft.Control:

    fulscreen_button = ft.Container(
                content=ft.Icon(ft.Icons.FULLSCREEN_OUTLINED, size=22, color=ft.Colors.PRIMARY),
                bgcolor=ft.Colors.GREY_100,
                padding=5,
                border_radius=5,
            )

    return fulscreen_button


def cashier_button() -> ft.Control:

    cashier_button = ft.Container(
                content=ft.Icon(ft.Icons.POINT_OF_SALE_OUTLINED, size=22, color=ft.Colors.PRIMARY),
                bgcolor=ft.Colors.GREY_100,
                padding=5,
                border_radius=5,
            )

    return cashier_button


def daily_sales_button() -> ft.Control:

    daily_sales_button = ft.Container(
                content=ft.Icon(ft.Icons.MONETIZATION_ON, size=22, color=ft.Colors.PRIMARY),
                bgcolor=ft.Colors.GREY_100,
                padding=5,
                border_radius=5,
            )

    return daily_sales_button



def settings_button() -> ft.Control:

    settings_button = ft.Container(
                content=ft.Icon(ft.Icons.SETTINGS_OUTLINED, size=22, color=ft.Colors.PRIMARY),
                bgcolor=ft.Colors.GREY_100,
                padding=5,
                border_radius=5,
            )

    return settings_button



def profile_button(page) -> ft.Control:
    state = RstockState(page)
    user = state.get_user()
    avatar = user["avatar"]

    if avatar is None:
        avatar = "/img/user.png"
    profile_button = ft.Container(
                content=ft.Row([ft.Image(f"{avatar}", width=22)]),
                bgcolor=ft.Colors.GREY_100,
                padding=5,
                border_radius=5,
            )
    
    return profile_button


def top_bar(page)->ft.Control:
    top_bar = ft.Container(
    bgcolor=ft.Colors.SURFACE,

    content=ft.Row(controls=[
        
        
        search_bar(),
        
        ft.Row(
            controls=[
                pos_button(page),
                new_button(),
                calc_button(),
                fulscreen_button(),
                cashier_button(),
                daily_sales_button(),
                settings_button(),
                profile_button(page)
            ]
        )


    ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

)

    top_bar.border_radius = ft.BorderRadius.all(5)
    top_bar.padding = ft.Padding.all(10)
    
    return top_bar


