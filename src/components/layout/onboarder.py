import flet as ft
from components.partial import side_menu, top_bar


def onboarder(content, illustration=None) -> ft.Control:

    onborder = ft.Container(

        content=ft.Container(

            content=ft.Row(
                controls=[
                    content,
                    ft.Stack(
                        controls=[
                            ft.Container(
                                bgcolor="#FFF5E5",
                                border_radius=ft.border_radius.all(10),
                                
                            ),
                            ft.Container(
                                content=ft.Image(
                                f"illustration/{illustration}.png"),
                                padding=50,
                               
                            )
                        ],


                        expand=True,
                       
                    )
                ]
            ),

            bgcolor=ft.Colors.SURFACE,
            border_radius=ft.border_radius.all(10),
            padding=ft.padding.all(50)

        ),



        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=["#F7A31C", "#033C59"],
        ),

        expand=True,
        margin=ft.margin.all(0),
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.symmetric(horizontal=200, vertical=50)

    )
    return onborder
