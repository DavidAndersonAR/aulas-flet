import flet as ft
import datetime

def main(page: ft.Page):
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label='Item 1',
                icon = ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.NavigationDrawerDestination(
                label='Item 2',
                icon_content=ft.FilledButton(text='Botão')
            )
        ],
        bgcolor=ft.colors.GREY_100,
        indicator_color=ft.colors.DEEP_ORANGE,
        indicator_shape=ft.RoundedRectangleBorder(radius=10),

        on_change=lambda e: print(e.control.selected_index)
    )
    def show_drawer(e):
        page.drawer.open = True
        page.update()
        
    btn = ft.IconButton(icon=ft.icons.MENU, on_click=show_drawer)
    page.add(btn)
   
   
if __name__==('__main__'):
    ft.app(target=main)