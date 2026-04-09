import flet as ft
from components.dashboard import (top_sales, welcome_bar, profit_by_period, sales_by_period, available_products, top_sales, sales_chart, last_transactions)

def dashboard()->ft.Control:


    dashboard = ft.Container(
        ft.Column(
            [
                welcome_bar(),
                ft.Column(
                            [
                                ft.Row([profit_by_period(), sales_by_period(), available_products()]),
                                ft.Row([top_sales(), sales_chart()]),
                                last_transactions()
                            ],
                            spacing=20,
                            expand=True,
                            scroll=ft.ScrollMode.AUTO
                        )

            ],

        )
    
    )
    dashboard.border_radius = ft.BorderRadius.all(5)
    return dashboard
