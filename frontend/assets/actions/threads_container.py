import flet as ft
from .threads_ import *
from .tokens import *
from .likes import *

def like(e):
    obj = e.control
    id = getattr(obj, "data")[0]
    token = read_token()
    page = getattr(obj, "data")[1]
    
    response = like_thread(id, token)
    if response == 400:
        alert = ft.AlertDialog(content = ft.Text("Вы уже лайкнули этот тред!"))
        page.overlay.append(alert)
        alert.open = True
    page.update()
    
    
def init_thread(title: str, topic: str, text: str, likes: str, date: str, id: int, page: ft.Page) -> ft.Container:
    "Инициализирует объект треда с указанными параметрами и оформлением"
    date = date.replace("-", ".")
    date = date.replace("T", " | ")
    return ft.Container(
        content = ft.Column([
            ft.Row([
                ft.Text(title),
                ft.Text(topic),
            ]),
            ft.Text(text),
            ft.Row([
                ft.TextButton(text = likes, icon = ft.icons.THUMB_UP, data = [id, page], on_click = like),
                ft.Text(date),
            ], spacing = 50)
        ]),
        border = ft.border.all(2, "#850000"),
        width = 500,
    )

def get_main_threads(page: ft.Page):
    threads_list = []
    threads_list = read_themes(10, None)[1]

    final_list = []

    for thread in threads_list:
        res = init_thread(thread["title"], thread["topic"], thread["text"], thread["likes"], thread["date"], thread["ID"], page)
        final_list.append(res)
        
    return ft.Column(final_list, scroll = ft.ScrollMode.AUTO)