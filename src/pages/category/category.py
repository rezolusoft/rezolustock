import flet as ft
from components.category import category_list 
from components.shared import new_button, export_to_pdf, export_to_xls
from core.context.state import RstockState
from core.auth.permissions import ADD_CATEGORY

def category(page)->ft.Control :


    # load context
    
    state = RstockState(page)

    # new category add button
    add = new_button()
    add.visible = state.can(ADD_CATEGORY)

    # boutton d'actiong généraux
    pdf = export_to_pdf()
    xls = export_to_xls()

    category = ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            expand=1,
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text("Catégories", color=ft.Colors.PRIMARY, font_family="PoppinsBold"),
                                        ft.Text("Gérez vos catégories ici", color=ft.Colors.PRIMARY, font_family="PoppinsMedium")
                                    ]
                                ),
                                ft.Row(
                                        [
                                            add,
                                            pdf,
                                            xls
                                        ]
                                    )
                            ]
                        ),
                        padding=10
                    ),
                    category_list(page),
                ]
            )
        )
    
    return category
