import flet as ft

update_button = ft.IconButton(icon = ft.icons.REFRESH, icon_color = "#850000")

# Для аппбара

home = ft.TextButton("Главная", scale = 1.3)
about = ft.TextButton("О нас", scale = 1.3)
posts = ft.TextButton("Посты", scale = 1.3)
rules = ft.TextButton("Правила", scale = 1.3)
contacts = ft.TextButton("Контакты", scale = 1.3)
help_ = ft.TextButton("Помощь", scale = 1.3)
profile = ft.IconButton(ft.icons.ACCOUNT_CIRCLE)
login = ft.TextButton("Войти", scale = 1.3, style = ft.ButtonStyle(bgcolor = "#850000"))
register = ft.TextButton("Зарегистироваться", scale = 1.3)

# Для категорий
news = ft.TextButton("Новости и события")
techs = ft.TextButton("Технологии и инновации")
health = ft.TextButton("Здоровье и фитнесс")
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
login_btn = ft.TextButton("Войти")
lgn_login_field = ft.TextField(width = 400, border_radius = 10, bgcolor = "#1C1C1C", hint_text = "Логин...", focused_border_color = "#850000", border_color = "#1C1C1C", height = 50)
lgn_pass_field = ft.TextField(password = True ,width = 400, border_radius = 10, bgcolor = "#1C1C1C", hint_text = "Пароль...", focused_border_color = "#850000", border_color = "#1C1C1C", height = 50)

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
    ], height = 450),
    padding = ft.padding.only(top = 50),
    bgcolor = "#151515"
)

appbar_unlogged = ft.AppBar(
        actions=[
            ft.Container(ft.Row(
                            [
                                ft.Container(ft.Image("assets/logo.png", scale = 0.6), margin = ft.margin.only(right = 75)),
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
    toolbar_height = 80,
    center_title = False,
    bgcolor = "#151515",
    shape = ft.OutlinedBorder,
    )

dialog = ft.AlertDialog(
    content = lgn_panel,
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

categories_column = ft.Column(
    [
        ft.Text("Основные категории", color = "#850000", scale = 1.1),
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
        other
    ]
)