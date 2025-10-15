import flet as ft
import requests

API_BASE = "http://127.0.0.1:8000"

def signup_view(page):
    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, width=300, can_reveal_password=True)
    status = ft.Text("")

    def handle_signup(e):
        data = {"username": username.value, "password": password.value}
        try:
            r = requests.post(f"{API_BASE}/signup", json=data)
            if r.status_code == 200:
                page.client_storage.set("signup_success", "Account created successfully!")
                page.go("/login")
            else:
                status.value = r.json()["detail"]
                status.color = ft.Colors.RED
        except Exception as err:
            status.value = f"Error: {err}"
            status.color = ft.Colors.RED
        page.update()

    return ft.View(
        "/signup",
        controls=[
            ft.AppBar(title=ft.Text("SWIFTBANK APP"), center_title=True, bgcolor=ft.Colors.RED, color=ft.Colors.ON_PRIMARY, surface_tint_color=ft.Colors.ON_SURFACE_VARIANT),
            ft.Text("Sign Up", size=30,color=ft.Colors.RED, weight=ft.FontWeight.W_500),
            username,
            password,
            ft.ElevatedButton("Create Account",width=300 ,on_click=handle_signup),
            status,
            ft.TextButton("Already have an account? Login", on_click=lambda e: page.go("/login"))
        ],
        vertical_alignment="center",
        horizontal_alignment="center"
    )
