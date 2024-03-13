import flet as ft
import datetime

def main(page: ft.Page):
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME,
                label='Inicio',
            ),
            ft.NavigationDestination(label='chat'),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Configurações',
                
            ),
        ],
        indicator_color=ft.colors.PINK,
    )
    page.update()
   
if __name__==('__main__'):
    ft.app(target=main)