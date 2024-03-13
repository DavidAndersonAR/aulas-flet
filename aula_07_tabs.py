import flet as ft
import datetime

def main(page: ft.Page):
    t = ft.Tabs(
        tabs=[
            ft.Tab(
                text='Tab1',
                content=ft.Container(
                    content=ft.Text('Conteudo da tab1')
                ),
            ),
            ft.Tab(             
                icon=ft.icons.SETTINGS,
                content=ft.Text('conteudo da tab2'),
            ),
            
            
        ],
        selected_index=1,
        animation_duration=300,
        divider_color=ft.colors.AMBER,
        indicator_border_radius=ft.border_radius.all(10),
        indicator_color=ft.colors.RED,
        indicator_padding=ft.padding.all(5),
        indicator_tab_size=True,
        label_color=ft.colors.GREEN,
        unselected_label_color=ft.colors.BLUE,
        overlay_color={
            ft.MaterialState.HOVERED:ft.colors.PINK
        },
        scrollable=False,
    )
    

    page.add(t)
   
if __name__==('__main__'):
    ft.app(target=main)