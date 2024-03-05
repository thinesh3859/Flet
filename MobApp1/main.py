import flet as ft
from views import views_handler

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet Inspirisys!")))
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
    
    page.on_route_change = route_change
    page.go('/welcome')


ft.app(target=main,assets_dir="assets",view=ft.WEB_BROWSER)
