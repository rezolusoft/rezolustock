import flet as ft

def on_welcome()->ft.Control:
    on_welcome = ft.Container(ft.Row(
    expand=True,
    controls=[
        ft.Text("👋🏾", size=40)
    ],
    ),
    
    )
    
    return on_welcome
