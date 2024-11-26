import flet as ft

update_button = ft.IconButton(icon = ft.icons.REFRESH, icon_color = "#850000")

# Для аппбара

home = ft.TextButton("Главная", scale = 1.3)
about = ft.TextButton("О нас", scale = 1.3)
posts = ft.TextButton("Написать пост", scale = 1.3, style = ft.ButtonStyle())
rules = ft.TextButton("Правила", scale = 1.3)
contacts = ft.TextButton("Контакты", scale = 1.3)
help_ = ft.TextButton("Помощь", scale = 1.3)
profile = ft.IconButton(ft.icons.ACCOUNT_CIRCLE)
login = ft.CupertinoButton(content = ft.Text("Войти", size = 20), bgcolor = "#850000", color = "#ffffff", border_radius = 15, height = 50)
register = ft.TextButton("Регистрация", scale = 1.3)

# Для категорий
news = ft.TextButton("Новости и события", style = ft.ButtonStyle(elevation = None, shape = None))
techs = ft.TextButton("Технологии и инновации")
health = ft.TextButton("Здоровье и фитнес")
hobbies = ft.TextButton("Хобби и увлечения")
literature = ft.TextButton("Книги и литература")
cinema = ft.TextButton("Кино и телевидение")
games = ft.TextButton("Игры")
education = ft.TextButton("Образование и карьера")
trips = ft.TextButton("Путешествия и отдых")
services = ft.TextButton("Сервисы")
social = ft.TextButton("Социальные вопросы")
other = ft.TextButton("Другое")

# Кнопки-картинки
liked = ft.Container(
    content = ft.Image("assets/liked.png"),
    on_click = lambda e: None,
    animate_scale = ft.Animation(duration = 150, curve = ft.AnimationCurve.EASE_IN_OUT)
)

conf = ft.Container(
    content = ft.Image("assets/conf.png"),
    on_click = lambda e: None,
    animate_scale = ft.Animation(duration = 150, curve = ft.AnimationCurve.EASE_IN_OUT)
)

online = ft.Container(
    content = ft.Image("assets/online.png"),
    on_click = lambda e: None,
    animate_scale = ft.Animation(duration = 150, curve = ft.AnimationCurve.EASE_IN_OUT)
)

# Панель входа
login_btn = ft.TextButton("Войти", width = 400, style = ft.ButtonStyle(bgcolor = "#850000"))
lgn_login_field = ft.TextField(width = 400, border_radius = 10, bgcolor = "#1C1C1C", hint_text = "Логин...", focused_border_color = "#850000", border_color = "#1C1C1C", height = 50)
lgn_pass_field = ft.TextField(password = True ,width = 400, border_radius = 10, bgcolor = "#1C1C1C", hint_text = "Пароль...", focused_border_color = "#850000", border_color = "#1C1C1C", height = 50)
lgn_redirect = ft.TextButton("Зарегистрироваться", style = ft.ButtonStyle(color = "#850000"), scale = 1.1)

lgn_panel = ft.Container(
    content = ft.Column([
        ft.Container(
            content=ft.Text("Войти", color = "#850000", scale = 1.8, width = 400, text_align = ft.TextAlign.CENTER),
            padding = ft.padding.only(bottom = 30),
            border = ft.border.only(bottom = ft.BorderSide(width = 2, color = "#850000")),
            width = 400,
        ),
        ft.Image("banner.png", width = 400),
        lgn_login_field,
        lgn_pass_field,
        login_btn,
        ft.Container(
            content = ft.Row([
                ft.Text("Нет аккаунта?", scale = 1.1),
                lgn_redirect
            ],
            width = 400,
            alignment = ft.MainAxisAlignment.CENTER),
            margin = ft.margin.only(top = 30),
            padding = ft.padding.only(top = 30),
            border = ft.border.only(top = ft.BorderSide(width = 2, color = "#850000"))
        )   
    ], height = 450),
    padding = ft.padding.only(top = 30),
    bgcolor = "#151515"
)

lgn_popup = ft.AlertDialog(
    content = lgn_panel,
    actions = [],
    open = False,
    bgcolor = "#151515"
)

reg_btn = ft.TextButton("Зарегистрироваться", width = 400, style = ft.ButtonStyle(bgcolor = "#850000"))
reg_login_field = ft.TextField(width = 400, border_radius = 10, bgcolor = "#1C1C1C", hint_text = "Логин...", focused_border_color = "#850000", border_color = "#1C1C1C", height = 50)
reg_pass_field = ft.TextField(password = True ,width = 400, border_radius = 10, bgcolor = "#1C1C1C", hint_text = "Пароль...", focused_border_color = "#850000", border_color = "#1C1C1C", height = 50)
reg_redirect = ft.TextButton("Войти", style = ft.ButtonStyle(color = "#850000"), scale = 1.1)
reg_panel = ft.Container(
    content = ft.Column([
        ft.Container(
            content=ft.Text("Регистрация", color = "#850000", scale = 1.8, width = 400, text_align = ft.TextAlign.CENTER),
            padding = ft.padding.only(bottom = 30),
            border = ft.border.only(bottom = ft.BorderSide(width = 2, color = "#850000")),
            width = 400,
        ),
        ft.Image("banner.png", width = 400),
        reg_login_field,
        reg_pass_field,
        reg_btn,  
        ft.Container(
            content = ft.Row([
                ft.Text("Есть аккаунт?", scale = 1.1),
                reg_redirect
            ],
            width = 400,
            alignment = ft.MainAxisAlignment.CENTER),
            margin = ft.margin.only(top = 30),
            padding = ft.padding.only(top = 30),
            border = ft.border.only(top = ft.BorderSide(width = 2, color = "#850000"))
        )    
    ], height = 450),
    padding = ft.padding.only(top = 30),
    bgcolor = "#151515"
)

reg_popup = ft.AlertDialog(
    content = reg_panel,
    actions = [],
    open = False,
    bgcolor = "#151515"
)



appbar_unlogged = ft.AppBar(
        actions=[
            ft.Container(ft.Row(
                            [
                                ft.Container(ft.Image("assets/logo.png", scale = 1), margin = ft.margin.only(right = 75)),
                                home,
                                about,
                                posts,
                                rules,
                                contacts,
                                help_,
                                ft.Container(
                                    content = ft.Row([
                                        login,
                                        register 
                                    ], spacing = 60),
                                    margin = ft.margin.only(left = 100)
                                ),
                                
                            ],
                            alignment = ft.MainAxisAlignment.START,
                            spacing = 70,
                        ),
                        padding = ft.padding.only(left = 220, right = 20),
                        width = 1920,
                        )
        ],
    toolbar_height = 60,
    center_title = False,
    bgcolor = "#151515",
    shape = ft.OutlinedBorder,
    )

send_post = ft.TextButton("Отправить", icon = ft.icons.SEND, style = ft.ButtonStyle(bgcolor = "#850000"))
cancel_post = ft.TextButton("Отмена")
post_header_field = ft.TextField(width = 400, hint_text = "Заголовок поста...", focused_border_color = "#850000", border_color = "#1C1C1C")
post_text_field = ft.TextField(width = 660, height = 200,hint_text = "Текст поста...", focused_border_color = "#850000", border_color = "#1C1C1C", expand = False, multiline = True, adaptive = False, min_lines = 8)

theme_picker = ft.Dropdown(
    width = 250,
    options = [
        ft.dropdown.Option("Новости и события"),
        ft.dropdown.Option("Технологии и инновации"),
        ft.dropdown.Option("Здоровье и фитнес"),
        ft.dropdown.Option("Хобби и увлечения"),
        ft.dropdown.Option("Книги и литература"),
        ft.dropdown.Option("Кино и телевидение"),
        ft.dropdown.Option("Игры"),
        ft.dropdown.Option("Образование и карьера"),
        ft.dropdown.Option("Путешествия и отдых"),
        ft.dropdown.Option("Сервисы"),
        ft.dropdown.Option("Социальные вопросы"),
        ft.dropdown.Option("Другое")
    ],
    bgcolor = "#1C1C1C",
)

post_writer = ft.Container(
    content = ft.Column([
        ft.Row([
            post_header_field,
            theme_picker
        ]),
        post_text_field,
        ft.Row([
            send_post,
            cancel_post
        ])
    ]),
    width = 660,
    height = 300
)

post_popup = ft.AlertDialog(
    content = post_writer,
    actions = [],
    open = False,
    bgcolor = "#151515"
)

main_column = ft.Column([
    ft.Image(src = "assets/banner.png"),
    ft.Row([
        liked,
        conf,
        online
    ],
    spacing = 115)
])

categories_column = ft.Container(
    content = ft.Column([
        ft.Text("Основные категории\n", color = "#850000", scale = 1.4, width = 200, text_align = ft.TextAlign.CENTER),
        news,
        techs,
        health,
        hobbies, 
        literature,
        cinema,
        games,
        education, 
        trips,
        services,
        social,
        other,
    ])  
)                       