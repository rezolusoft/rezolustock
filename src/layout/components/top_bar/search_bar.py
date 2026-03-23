import flet as ft


def search_bar() -> ft.Control:

    search_bar = ft.Container(ft.TextField(
        hint_text="Rechercher quelque chose...", prefix_icon=ft.Icons.SEARCH_ROUNDED))
    search_bar.margin = ft.Margin.symmetric(horizontal=10)

    return search_bar
