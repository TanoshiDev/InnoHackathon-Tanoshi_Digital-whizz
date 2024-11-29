import flet as ft
from .threads_ import *
from .tokens import *
from .likes import *
from .auth import user_info
from datetime import datetime, timedelta

comment_field = ft.TextField(hint_text = "Введите комментарий...", multiline = True, width = 900, border_radius = 15, border_color = "#1C1C1C", focused_border_color = "#850000")

callback_function = None
callback_update = None
callback_liked = None

def set_callback_main(callback): 
    global callback_function 
    callback_function = callback
    
def set_callback_update(callback):
    global callback_update
    callback_update = callback
    
def set_callback_liked(callback):
    global callback_liked
    callback_liked = callback

def call_main_function():
    if callback_function:
        callback_function()
        
def call_update_function():
    if callback_update:
        callback_update()
        
def call_liked_function():
    if callback_liked:
        callback_liked()
    
def send_comment(e: ft.TapEvent):
    post_id = getattr(e.control, "data")
    page = e.page
    token = read_token()
    print(type(page))
    text = comment_field.value
    print(post_id)
    response = create_comment(post_id, token, text)
    print(response)
    comment_field.value = ""
    call_main_function()
    
    
def like(e):
    obj = e.control
    id = getattr(obj, "data")[0]
    
    response = like_thread(id)
    if response == True:
        e.control.text = str(int(e.control.text) + 1)
        call_update_function()
    elif response == False:
        call_liked_function()
   
def init_thread(title: str, topic: str, text: str, likes: str, date: str, id: int, author_id: int, page: ft.Page) -> ft.Container:
    time = date[date.find("T") + 1:]
    time_obj = datetime.strptime(time, "%H:%M:%S")
    time_obj = time_obj + timedelta(hours = 3)
    time = time_obj.time().strftime("%H:%M:%S")
    date = date[:date.find("T")] + " " + time
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
                content = comments
            )
        ]
    )

    date = date.replace("-", ".")
    date = date.replace("T", " | ")
    return ft.Container(
        content = ft.Column([
            ft.Column([
                ft.Row([
                    ft.Text(f"{user_info(author_id)["login"]}", size = 20, color = "#850000"),
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
            res = init_comment(user_info(comment["user_id"])["login"], comment["text"])
            final_list.append(res)
            
        return [final_list, len(final_list)]
    return [(ft.Container()), 0]

def get_main_threads(page: ft.Page):
    threads_list = []
    response = read_themes(30)
    
    if response[0] == 200:
        threads_list = read_themes(30)[1]

        final_list = []
        for thread in threads_list:
            res = init_thread(thread["title"], thread["topic"], thread["text"], thread["likes"], thread["date"], thread["ID"], thread["author_id"], page)
            final_list.append(res)
            
        return ft.Column(final_list, scroll = ft.ScrollMode.AUTO)
    else:
        return ft.Column([ft.Text("Вы не авторизовались")])