import flet as ft
import requests

API_BASE = "http://127.0.0.1:8000"
#define the login view (holding what should be in the login view)
def login_view(page):
    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, width=300, can_reveal_password=True)
    status = ft.Text(color="red")
    loading = ft.Text(value="", color="blue")
    success_message = ft.Text(value="", color=ft.Colors.GREEN)

    login_button = ft.ElevatedButton(
        "Log In",
        width=300,
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE,
        on_click=lambda e: None,
        disabled=True  # Initially disabled
    )
#this tells the button that nothing was in the input fields
    def check_fields(e):
        login_button.disabled = not (username.value and password.value)
        page.update()
#handles the event of redirecting when the login button is clicked
    def handle_login(e):
        status.value = ""
        loading.value = "Please wait..."
        login_button.disabled = True
        page.update()

        data = {
            "username": username.value,
            "password": password.value
        }

        try:
            r = requests.post(f"{API_BASE}/login", json=data)
            if r.status_code == 200:
                user = r.json()["user"]
                page.client_storage.set("username", user["username"])
                page.client_storage.set("is_active", str(user["is_active"]))
                page.go("/home")
            else:
                status.value = r.json()["detail"]
        except Exception as err:
            status.value = f"Error: {err}"
        finally:
            loading.value = ""
            login_button.disabled = False
            page.update()

    message = page.client_storage.get("signup_success")
    if message:
        success_message.value = message
        page.client_storage.remove("signup_success")
            

    # Attach on_change to input fields
    username.on_change = check_fields
    password.on_change = check_fields
    login_button.on_click = handle_login
    #holds the route of the page and how the layout of the page should be.
    return ft.View(
        "/login",
        controls=[
            ft.AppBar(title=ft.Text("SWIFTBANK APP"), center_title=True, bgcolor=ft.Colors.RED, color=ft.Colors.ON_PRIMARY, surface_tint_color=ft.Colors.ON_SURFACE_VARIANT),
            ft.Text("Login", size=30, color=ft.Colors.RED, weight=ft.FontWeight.W_500),
            success_message,
            username,
            password,
            login_button,
            loading,
            status,
            ft.TextButton("Don't have an account? Sign up", on_click=lambda e: page.go("/signup"))
        ],
        vertical_alignment="center",
        horizontal_alignment="center"
    )
