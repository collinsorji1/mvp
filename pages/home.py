from flet import *

def home_view(page):
    def toggle_sidebar(e):
        sidebar.left = 0 if sidebar.left == -220 else -220
        page.update()

    sidebar = Container(
    content=Column(
        [
            TextButton(
                text="Transfer",
                style=ButtonStyle(color=Colors.RED, overlay_color=Colors.RED_100),
                on_click=lambda e: print("Transfer clicked")
            ),
            Container(height=1, bgcolor=Colors.GREY_400),
            TextButton(
                text="Transactions",
                style=ButtonStyle(color=Colors.RED, overlay_color=Colors.RED_100),
                on_click=lambda e: print("Transactions clicked")
            ),
            Container(height=1, bgcolor=Colors.GREY_400),
            TextButton(
                text="Settings",
                style=ButtonStyle(color=Colors.RED, overlay_color=Colors.RED_100),
                on_click=lambda e: print("Settings clicked")
            ),
            Container(height=1, bgcolor=Colors.GREY_400),
            TextButton(
                text="Logout",
                style=ButtonStyle(color=Colors.RED, overlay_color=Colors.RED_100),
                on_click=lambda e: page.go("/login")
            )
        ],
        spacing=30
    ),
    bgcolor="white",
    width=200,
    height=page.height,
    padding=10,
    left=-220,
    top=0,
    animate_position=300,
    border_radius=0,
    visible=True
)


    def create_icon_with_text(icon, text):
        return Column(
            [
                IconButton(
                    icon,
                    icon_size=24,
                    icon_color=Colors.BLUE,
                    tooltip=text,
                    on_click=lambda e: print(f"{text} button clicked")
                ),
                Text(value=text, size=12, text_align="center", color=Colors.RED, weight="bold")
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=2
        )

    def bottom_nav_icon(icon, text):
        return Column(
            [
                IconButton(
                    icon,
                    icon_size=24,
                    icon_color=Colors.BLUE,
                    tooltip=text,
                    on_click=lambda e: print(f"{text} button clicked")
                ),
                Text(value=text, size=12, text_align="center", color=Colors.RED, weight="bold")
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=2
        )

    bottom_navbar = Container(
        content=Row(
            [
                bottom_nav_icon(Icons.HOME, "Overview"),
                bottom_nav_icon(Icons.PHONE, "Airtime"),
                bottom_nav_icon(Icons.SWAP_HORIZ, "Transfer"),
                bottom_nav_icon(Icons.WALLET, "Bills"),
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY
        ),
        bgcolor="white",
        height=70,
        border=border.only(top=BorderSide(1, "lightgrey")),
        padding=padding.only(top=5),
        shadow=BoxShadow(blur_radius=5, color="gray", offset=Offset(0, 0)),
        width=100000000
    )

    balance_holder = Container(
        content=Stack(
            [
                Text("TOTAL BALANCE", size=15, color=Colors.WHITE, left=0, top=9),
                Text("$1000.00", size=30, color=Colors.WHITE, left=0, top=30),
            ]
        ),
        bgcolor="#F34C4C",
        height=100,
        width=100000000,
        padding=10,
        alignment=alignment.center,
        border_radius=10,
        expand=True
    )

    main_content = Column(
        [
            balance_holder,
            Container(height=10),
            Text("0123456789 - ACTIVE", size=15, color=Colors.RED, weight="bold"),
            Container(width=100000000, height=1, bgcolor="black"),

            Container(
                content=Text("      Ledger Balance", size=18, color=Colors.WHITE),
                height=30, bgcolor=Colors.BROWN, width=100000000
            ),
            Container(height=10),
            Text("eaZyLinks", size=13, color=Colors.BLACK),
            Container(width=100000000, height=1, bgcolor="black"),
            Container(height=8),
            Row(
                [
                    create_icon_with_text(Icons.QR_CODE_2, "QR Payment"),
                    create_icon_with_text(Icons.AIRPLANEMODE_ACTIVE, "Travel & Leisure"),
                    create_icon_with_text(Icons.TV, "Cable TV"),
                    create_icon_with_text(Icons.CREDIT_CARD, "Cards"),
                ],
                alignment=MainAxisAlignment.SPACE_EVENLY
            ),
            Container(width=100000000, height=1, bgcolor="black"),
            Container(height=8),
            Row(
                [
                    create_icon_with_text(Icons.FINGERPRINT, "MyBVN"),
                    create_icon_with_text(Icons.REPEAT, "Scheduled Payments"),
                    create_icon_with_text(Icons.SETTINGS, "Customize eaZYlinks"),
                    create_icon_with_text(Icons.BUILD, "Settings"),
                ],
                alignment=MainAxisAlignment.SPACE_EVENLY,
            ),
            Container(width=100000000, height=1, bgcolor="black"),
            Container(height=20),

            # ⬇️ Non-sticky navbar added here at the bottom of the scrollable content
            bottom_navbar
        ],
        scroll=ScrollMode.AUTO,
        expand=True,
    )

    return View(
        "/home",
        controls=[
            AppBar(
                title=Text("SwiftPay"),
                bgcolor="#F34C4C",
                center_title=True,
                leading=IconButton(Icons.MENU, on_click=toggle_sidebar),
                actions=[IconButton(icon=Icons.LOGOUT, on_click=lambda e: page.go("/login"))]
            ),
            Stack(
                controls=[
                    Container(
                        content=main_content,
                        expand=True,
                    ),
                    sidebar,
                ],
                expand=True
            )
        ]
    )
