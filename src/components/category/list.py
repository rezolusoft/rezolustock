import flet as ft
import flet_datatable2 as fdt
from pages.errors import emptyError

from models.category import Category


def category_list(page):




    # bar de recherche
    search_bar = ft.Container(ft.TextField(hint_text="Rechercher...", suffix_icon=ft.Icons.SEARCH_OUTLINED, dense=True, text_size=14, width=220, border_radius=10))

    # Récupération en bd
    categories = Category.select() #ToDo: rajouter pagination 

    category_colums = [
            fdt.DataColumn2(label="Code",size=fdt.DataColumnSize.M),
            fdt.DataColumn2(label="Nom", size=fdt.DataColumnSize.L),
            fdt.DataColumn2(label="Description", size=fdt.DataColumnSize.L),
            fdt.DataColumn2(label="Actions", size=fdt.DataColumnSize.S),

    ]

    empty_control = emptyError()

    category_rows = [
            
            fdt.DataRow2([ft.DataCell(ft.Text(category.code)), ft.DataCell(ft.Text(category.name)), ft.DataCell(ft.Text(category.description)), ft.DataCell(ft.Text("-")), ]) for category in categories
    ]
    category_list = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        search_bar,
                    ],
                    expand=1,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                        fdt.DataTable2(
                            columns=category_colums,
                            rows=category_rows,
                            show_checkbox_column=True,
                            empty=empty_control,
                            expand=True,
                            border_radius=10,
                            heading_row_color=ft.Colors.GREY_100,
                            border=ft.Border.all(1, ft.Colors.PRIMARY)
                            
                        )
                
            ],
            expand=1
        ),
        bgcolor=ft.Colors.SURFACE,
        border_radius=10,
        padding=10
    )

    return category_list      
