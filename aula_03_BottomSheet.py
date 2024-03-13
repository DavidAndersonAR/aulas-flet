import flet as ft

def main(page: ft.Page):
    def show_bottom(e):
        bs.open = True
        bs.bgcolor=ft.colors.BLUE_200
        bs.elevation = 8.0
        page.update()
        
    def close_bottom(e):
        bs.open = False
        page.update()

    bs=ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(value='Titulo', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value='Conteudo do bottomsheet', style=ft.TextThemeStyle.LABEL_SMALL),
                    ft.FilledButton(text='Fechar', on_click=close_bottom)
                ]
            ),
            padding=20,
        ),
        dismissible=False, # nao permiti fechar clicando fora
        enable_drag=True, # habilita arrastar o conteudo
        is_scroll_controlled=False,
        maintain_bottom_view_insets_padding=False,
        show_drag_handle=True
    )

    page.overlay.append(bs)

    btn = ft.ElevatedButton(text="Abrir", on_click=show_bottom)
    page.add(btn)
   

   
if __name__==('__main__'):
    ft.app(target=main)