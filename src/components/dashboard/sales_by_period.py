import flet as ft

def sales_by_period():
    return ft.Container(
        
            ft.Row(
                [
                    ft.Container(
                    ft.Image(
                        "img/sale.png",
                        width=80,
                        height=80
                    )
                ),
                    
                    ft.Column(
                    [
                        ft.Text("521", color=ft.Colors.WHITE, font_family="PoppinsExtraBold", size=20, text_align=ft.TextAlign.RIGHT),
                        ft.Text("Produits vendus au total", color=ft.Colors.WHITE),
                        
                

                    ],
                    expand=True,
                    

                ),
                
                ],

               
                
            ),
       
       bgcolor=ft.Colors.SECONDARY,
       expand=2,
        padding=ft.Padding.all(15),
       border_radius=ft.BorderRadius.all(10)
       
    )
