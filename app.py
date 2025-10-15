# frontend/app.py

import flet as ft
from pages.signup import signup_view
from pages.login import login_view
from pages.home import home_view

def main(page: ft.Page):
    page.title = "SWIFTBANK APP"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.auto_scroll = True

    def route_change(route):
        page.views.clear()

        if page.route == "/signup":
            page.views.append(signup_view(page))
        elif page.route == "/login":
            page.views.append(login_view(page))
        elif page.route == "/home":
            page.views.append(home_view(page))
        else:
            page.go("/login")

        page.update()

    page.on_route_change = route_change
    page.go("/home")

ft.app(target=main)
