import flet as ft

def main(page: ft.Page):
    def show_sb(e):
        page.snack_bar.open=True
        page.update()

    page.snack_bar = ft.SnackBar(
        content=ft.Text(value='Não foi possivel processar os dados ness momento'),
        bgcolor=ft.colors.RED_100,
        show_close_icon=True,
        close_icon_color=ft.colors.BLACK,
        padding=ft.padding.all(30),
        duration=10000,

        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.margin.all(50),
        dismiss_direction=ft.DismissDirection.START_TO_END,

        action='OK',
        action_color=ft.colors.GREEN,
        on_action=lambda _: print('Ação selecionada'),
    )
    btn = ft.ElevatedButton('Abrir', on_click=show_sb)
    page.add(btn)

   

   
if __name__==('__main__'):
    ft.app(target=main)