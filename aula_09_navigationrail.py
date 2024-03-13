import flet as ft
import datetime

def main(page: ft.Page):
    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label='Inicio',

            ),
            ft.NavigationRailDestination(
                label='chat',
                icon=ft.icons.CHAT,
            ),
            ft.NavigationRailDestination(
                label='Itens salvos',
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Container(bgcolor='red', height=20, width=20),
                selected_icon_content=ft.Container(bgcolor='green', width=50, height=20),
                label='Configurações',
                padding=ft.padding.all(10)
            ),
        ],
        bgcolor=ft.colors.GREY_900,
        selected_index= 0,
        extended=True,
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text = "Cadastrar novo"),
                ft.PopupMenuItem(text = "Enviar em massa"),
            ]
        ),
        leading=ft.CircleAvatar(content=ft.Text(value='DA')),
        on_change=lambda e: print(e.control.selected_index)
    )
    row = ft.Row(controls=[rail], expand=True)
    page.add(row)
    page.update()
   
if __name__==('__main__'):
    ft.app(target=main)