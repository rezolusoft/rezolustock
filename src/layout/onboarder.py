import flet as ft


def onboarder(content, illustration=None) -> ft.Control:

    onboarder = ft.Container(

        content=ft.Container(

            content=ft.Row(
                controls=[
                    ft.Container(content=content, expand=1),
                    ft.Container(
                        expand=1,
                        content=ft.Container(
                                bgcolor="#FFF5E5",
                                
                                border_radius=ft.BorderRadius.all(10),
                                alignment=ft.Alignment.CENTER,
                                content= ft.Image(f"illustration/{illustration}.png"),padding=50),
                                )
                ],
                
            ),

            bgcolor=ft.Colors.SURFACE,
            border_radius=ft.BorderRadius.all(10),
            padding=ft.Padding.all(50),
            

        ),



        gradient=ft.LinearGradient(
            begin=ft.Alignment.BOTTOM_LEFT,
            end=ft.Alignment.TOP_RIGHT,
            colors=["#F7A31C", "#033C59"],
        ),

        expand=True,
        margin=ft.Margin.all(0),
        border_radius=ft.BorderRadius.all(10),
        padding=ft.Padding.symmetric(horizontal=200, vertical=50)

    )
    return onboarder
