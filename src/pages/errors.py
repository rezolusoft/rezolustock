import flet as ft
import flet_lottie as ftl

 
def notFoundError():

    async def go_home(e):
        await e.page.push_route('/dashboard')

    return ft.Container(
        ft.Column(
            [
                ft.Container(ftl.Lottie(src="lotties/404.json", reverse=False, animate=True, error_content=ft.Text("Erreur")), width=380),
                ft.Text("Oups ! La ressource demandée n'a pas été retrouvée", font_family='PoppinsMedium', size=16, color=ft.Colors.PRIMARY, text_align=ft.TextAlign.CENTER),
                ft.Container(
                    ft.Row(
                            [
                                ft.Text("Retour à l'accueil", text_align=ft.TextAlign.CENTER, color=ft.Colors.PRIMARY, font_family="PoppinsBold", style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color=ft.Colors.PRIMARY)),
                                ft.Icon(ft.Icons.HOME_OUTLINED, color=ft.Colors.PRIMARY),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        on_click=go_home
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        expand=1,
        align=ft.Alignment.CENTER
    )


def emptyError():

    return  ft.Container(
        ft.Column(
                [
                    ft.Container(ftl.Lottie(src="lotties/404.json", reverse=False, animate=True, error_content=ft.Text("Erreur")), width=148, align=ft.Alignment.CENTER),
                    ft.Text("Oups ! Il semble que tout est vide ici... Commencez par créer en cliquant sur nouveau !", font_family='PoppinsMedium', size=16, color=ft.Colors.PRIMARY, text_align=ft.TextAlign.CENTER, align=ft.Alignment.CENTER),
                   
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment = ft.Alignment.CENTER

    )