import flet as ft



def profit_by_period(period=None):
    return ft.Container(
        
            ft.Row(
                [ft.Column(
                    [
                        ft.Text("Bénéfice Hebdomadaire", color=ft.Colors.SECONDARY, font_family="PoppinsSemiBold"),
                        ft.Text("7.500 XOF", color=ft.Colors.PRIMARY, font_family="PoppinsExtraBold", size=20),
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.ARROW_DROP_UP, color=ft.Colors.GREEN_300),
                                ft.Text("48%", color=ft.Colors.GREEN_300),
                                ft.Text("de plus que la semaine dernière", color=ft.Colors.PRIMARY),
                            ]
                        )

                    ]
                ),
                
                ft.Container(
                    ft.Image(
                        "img/profit.png",
                        width=80,
                        height=80
                    )
                )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
       
       bgcolor=ft.Colors.WHITE,
       expand=3,
       padding=ft.Padding.all(10),
       border_radius=ft.BorderRadius.all(5)
       
    )
