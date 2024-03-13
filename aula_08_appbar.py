import flet as ft
import datetime

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text(value='App Fit'),
        bgcolor=ft.colors.BLACK,
        center_title=True,
        toolbar_height=100,
        color=ft.colors.AMBER,
        leading=ft.Icon(name=ft.icons.HOME),
        leading_width=100,
        actions=[
            ft.IconButton(icon=ft.icons.SUNNY),
            ft.IconButton(icon=ft.icons.NOTIFICATIONS),
            ft.CircleAvatar(content=ft.Text(value='DA')),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='Meus dados'),
                    ft.PopupMenuItem(text='Configurações'),
                    ft.PopupMenuItem(text='Sair')
                    ,
                ]
            )
        ],
    )

    page.update()
   
if __name__==('__main__'):
    ft.app(target=main)