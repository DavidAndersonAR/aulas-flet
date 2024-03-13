import flet as ft

def main(page: ft.Page):
    def close_banner(e):
        page.banner.open=False
        page.update()

    def ope_banner(e):
        page.banner= bn1
        bn1.open= True
        page.update()
    
    bn1 = ft.Banner(
        actions=[
            ft.TextButton(text="Cancelar", style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_banner),
            ft.ElevatedButton(text='Salvar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE))# botão elevado

        ],
        content=ft.Text(value="Deu ruim em meu nobre"),
        leading=ft.Icon(name=ft.icons.WARNING_AMBER),
        force_actions_below= True,
        bgcolor=ft.colors.BLACK
    )

    btn01 = ft.ElevatedButton(text='Abrir', on_click=ope_banner)
    page.add(btn01)

if __name__==('__main__'):
    ft.app(target=main)