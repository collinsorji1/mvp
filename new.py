from flet import *

class App(UserControl):
    def __init__(self):    super().__init__()
    def build(self):
        return Container(    content=Text("Hello, World!"),    bgcolor=Colors.BLUE,    padding=20,    border_radius=10,    alignment=alignment.center,    width=300,    height=200,    ink=True,    on_click=lambda e: print("Container clicked!"),)