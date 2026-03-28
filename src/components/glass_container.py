import flet as ft

class GlassContainer(ft.Container):
    def __init__(self, content=None, **kwargs):
        super().__init__(
            content=content,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#26FFFFFF", "#0DFFFFFF"],
            ),
            blur=ft.Blur(50, 50, ft.BlurTileMode.MIRROR),
            border=ft.border.all(1, "#40FFFFFF"),
            border_radius=10,
            padding=20,
            **kwargs
        )
