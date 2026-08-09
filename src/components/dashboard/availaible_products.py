import flet as ft



def available_products():
    return ft.Container(
        
            ft.Row(
                [
                    
                    
                    ft.Column(
                    [
                        ft.Text("1322", color=ft.Colors.WHITE, font_family="PoppinsExtraBold", size=20),
                        ft.Text("Produits disponible", color=ft.Colors.WHITE),
                        


                    ],
                ),

                ft.Container(
                    ft.Image(
                        "img/product.png",
                        width=80,
                        height=80
                    )
                ),
                
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                
            ),
       
       bgcolor=ft.Colors.PRIMARY,
       expand=2,
        padding=ft.Padding.all(15),
       border_radius=ft.BorderRadius.all(10)
       
    )
