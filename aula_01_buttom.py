import flet as ft
def main(page: ft.Page):
    #Função para alterar a propriedade {open} para False, para fechar o alerta
    def fechar_message(e):
        page.dialog=ad1
        ad1.open = False
        page.update()

    # Iniciando a criação do alerta
    ad1 = ft.AlertDialog(
        title=ft.Text(value="Aviso importante"),
        content=ft.Text(value="Tem certeza meu nobre?????"),
        content_padding=ft.padding.all(30),
        inset_padding=ft.padding.all(10),
        modal=True,
        on_dismiss= lambda _: print("Fechei"),

        # incluido ação de butões
        actions=[
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=fechar_message), # botão comun
            ft.ElevatedButton(text='Salvar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE))# botão elevado
        ]
    )
    # função que chama o alerta
    def message(e):
        page.dialog=ad1
        ad1.open = True
        page.update()

    
    # butão para chamar chamar o alerta
    btn1 = ft.ElevatedButton(text="Abrir", on_click=message)
    page.add(btn1)# adicioanando o butão ao projeto

if __name__=='__main__':
    ft.app(target=main)