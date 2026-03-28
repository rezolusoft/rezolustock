import flet as ft



def rstocknotif(title:str, content:str, actions:list):
    return ft.AlertDialog(
        modal=True, title=ft.Text(title),
        content=ft.Text(content),
        actions=actions,
        actions_alignment=ft.MainAxisAlignment.END
    )
