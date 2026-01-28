import flet as ft
from extras.store import RStockStore



def on_done(page) -> ft.Control:
    
    def start(e):
        store = RStockStore(page)
        store.destroy("onboarded")
        store.set("onboarded", True)
        page.go("/dashboard")

    welcome_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("🎉", size=40),
            ft.Text("Bravo ! Vous êtes prêt à tirer le meilleur de RezoluStock", size=25, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text("Votre espace est maintenant prêt. Il ne vous reste plus qu’à explorer et profiter des fonctionnalités.", size=20, font_family="Poppins", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                    content = ft.Text("Démarrer"),                              
            
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(10),
                          padding=15,
                          bgcolor=ft.Colors.SECONDARY,
                          text_style=ft.TextStyle(
                              font_family="PoppinsMedium",
                              size=18
                          )
                          ),
                          color=ft.Colors.ON_SURFACE,
                        
                        on_click=start,
                        
                    )
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return welcome_container
