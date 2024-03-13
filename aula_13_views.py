import flet as ft
import datetime

def main(page: ft.Page):

    def change_route(e):
        if e.control.selected_index == 0:
            page.go('/')
        elif e.control.selected_index == 1:
            page.go('/loja')
        elif e.control.selected_index == 2:
            page.go('/app')
    

    def route_changed(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text("meu app"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                controls=[
                    ft.ElevatedButton(
                        text='Ver loja',
                        on_click=lambda _: page.go("/loja")
                    ),
                    ft.ListView(
                        controls = [
                            ft.Text(
                                value=f"item {i}",
                                size=30,
                            ) for i in range(50)
                        ]
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                bgcolor=ft.colors.BLACK,
                drawer=ft.NavigationDrawer(
                    controls=[
                        ft.NavigationDrawerDestination(
                            label='Home',
                            icon=ft.icons.HOME,
                        ),
                        ft.NavigationDrawerDestination(
                            label='Loja',
                            icon=ft.icons.STORE,
                        ),
                        ft.NavigationDrawerDestination(
                            label='App',
                            icon=ft.icons.PHONE_ANDROID,
                        ),
                    ],
                    on_change=change_route
                ),
                floating_action_button=ft.FloatingActionButton(icon=ft.icons.ADD)

            )
        )

        if page.route == '/loja':
            page.views.append(
                ft.View(
                    route='/loja',
                    appbar=ft.AppBar(
                        title=ft.Text('Loja'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para pagina inicial",
                            on_click= lambda _: page.go('/')
                        ), 
                        ft.ElevatedButton(
                            text="Ir para app",
                            on_click= lambda _: page.go('/app')
                        )
                    ],
                    
                    fullscreen_dialog=True,
                    
                )
            )

        if page.route == '/app':
            page.views.append(
                ft.View(
                    route='/app',
                    appbar=ft.AppBar(
                        title=ft.Text('Loja'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para pagina inicial",
                            on_click= lambda _: page.go('/')
                        )
                    ]
                )
            )
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_changed
    page.go(page.route)
    page.on_view_pop = view_pop
    #page.update()

   
        
   
if __name__==('__main__'):
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)