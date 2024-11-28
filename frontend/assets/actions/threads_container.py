import flet as ft
from .threads_ import *
from .tokens import *
from .likes import *

def send_comment(e: ft.TapEvent):
    post_id = getattr(e.control, "data")
    token = read_token()
    text = comment_field.value
    print(post_id)
    response = create_comment(post_id, token, text)
    print(response)
    comment_field.value = ""
    
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

comment_field = ft.TextField(hint_text = "Введите комментарий...", multiline = True, width = 900, border_radius = 15, border_color = "#1C1C1C", focused_border_color = "#850000")
    
def init_thread(title: str, topic: str, text: str, likes: str, date: str, id: int, page: ft.Page) -> ft.Container:
    "Инициализирует объект треда с указанными параметрами и оформлением"
    result = get_comments(id)
    result[0].append(
        ft.Container(
            content = ft.Row([
                comment_field,
                ft.TextButton(text = "Отправить", icon = ft.icons.SEND, style = ft.ButtonStyle(bgcolor = "#850000"), width = 200, on_click = send_comment, data = id)
            ])
        )
    )
    comments = ft.Container(content = ft.Column(result[0], spacing = 20))
    
    panel = ft.ExpansionPanelList(
        expand_icon_color = "#850000",
        elevation=8,
        divider_color = "#850000",
        controls=[
            ft.ExpansionPanel(
                header = ft.Container(content = ft.Text(f"Комментарии ({result[1]})", size = 20, color = "#850000"), padding = ft.padding.all(20)),
                bgcolor = "#151515",
                expanded = False,
                content = comments,
                left = 5,
                right = 5,
                top = 5,
                bottom = 5
            )
        ]
    )

    date = date.replace("-", ".")
    date = date.replace("T", " | ")
    return ft.Container(
        content = ft.Column([
            ft.Column([
                ft.Row([
                    ft.Text("Здесь будет имя автора...", size = 20, color = "#850000"),
                    ft.Text(date, size = 18)
                ], alignment = ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Text(f"{topic}. {title}", size = 24),
            ]),
            ft.Container(
                content = ft.Text(text, size = 16, selectable = True),
                padding = ft.padding.only(bottom = 15),
                border = ft.border.only(bottom = ft.BorderSide(2, "#850000")),
                width = 1220
            ),
            ft.Row([
                ft.TextButton(text = likes, icon = ft.icons.THUMB_UP, data = [id, page], on_click = like),
            ], spacing = 50),
            panel
        ]),
        border = None,
        width = 1280,
        bgcolor = "#151515",
        border_radius = 15,
        padding = ft.padding.all(30)
    )

def init_comment(user_id: int, text: str):
    return ft.Container(
        content = ft.Column([
            ft.Text(user_id, size = 20, color = "#850000"),
            ft.Text(text, size = 18)
        ]),
        bgcolor = "#1C1C1C",
        border_radius = 15,
        padding = ft.padding.all(10),
        width = 1200
    )
    
def get_comments(post_id: int) -> list[list | int]:
    final_list = []
    response = read_comments(post_id)
    
    if response[0] == 200:
        comments_list = response[1]
        
        for comment in comments_list:
            res = init_comment(comment["user_id"], comment["text"])
            final_list.append(res)
            
        return [final_list, len(final_list)]
    return [(ft.Container()), 0]

def get_main_threads(page: ft.Page):
    threads_list = []
    threads_list = read_themes(100, None)[1]

    final_list = []

    for thread in threads_list:
        res = init_thread(thread["title"], thread["topic"], thread["text"], thread["likes"], thread["date"], thread["ID"], page)
        final_list.append(res)
        
    return ft.Column(final_list, scroll = ft.ScrollMode.AUTO)