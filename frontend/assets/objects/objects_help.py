import flet as ft

header_text = ft.Text(
    "Возникли вопросы или проблемы? Оставьте заявку и администрация обязательно вам ответит!",
    size = 33,
    color = "white",
    weight = "bold",
    text_align = "center",
)

header_text_container = ft.Container(
    content = header_text,
    alignment = ft.alignment.center,
    padding = ft.padding.only(bottom = 20),
)

title_label = ft.Text("Заголовок:", color = "white", size = 16)
title_input = ft.TextField(
    hint_text = "Введите заголовок...",
    border_color = "#1C1C1C",
    color = "white",
    bgcolor = "#1C1C1C",
    border_radius = 8,
    width = 1570,
)

description_label = ft.Text("Описание:", color = "white", size = 16,)
description_input = ft.TextField(
    hint_text = "Введите описание...",
    multiline = True,
    min_lines = 3,
    max_lines = 5,
    border_color = "#1C1C1C",
    color = "white",
    bgcolor = "#1C1C1C",
    border_radius = 8,
    width = 1570,
)

submit_button = ft.Container(
    content = ft.Text("Отправить", color = "white", size = 16, weight = "bold"),
    bgcolor = "#850000",
    border_radius = 8,
    alignment = ft.alignment.center,
    # on_hover = on_hover,
    padding = ft.padding.symmetric(vertical = 10, horizontal = 20),
    width = 150,
)

input_form = ft.Container(
    content=ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        [
                            title_label,
                            title_input,
                        ],
                        alignment = ft.MainAxisAlignment.START,
                        spacing = 8,
                    ),
                ],
                spacing = 20,
                alignment = ft.MainAxisAlignment.START,
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            description_label,
                            description_input,
                        ],
                        alignment = ft.MainAxisAlignment.START,
                        spacing = 8,
                    ),
                ],
                spacing = 20,
                alignment = ft.MainAxisAlignment.START,
            ),
            ft.Row(
                [
                    submit_button,
                ],
                alignment = ft.MainAxisAlignment.END,
            ),
        ],
        spacing = 20,
    ),
    padding = ft.padding.all(20),
    border_radius = 15,
    bgcolor = "#151515",
    width = 1610,
)

centered_form_container = ft.Container(
    content = input_form,
    alignment = ft.alignment.center,
)

faq_title = ft.Text(
    "Часто задаваемые вопросы (FAQ)",
    size = 33,
    color = "white",
    weight = "bold",
    text_align = "center",
)

faq_title_container = ft.Container(
    content = faq_title,
    alignment = ft.alignment.center,
    padding = ft.padding.only(top = 20, bottom = 10),
)

panel_data = [
    ("Как зарегистрироваться на форуме?", "Для регистрации на форуме Whizz нажмите кнопку \"Регистрация\" на главной странице. Заполните необходимые поля, подтвердите свой email и следуйте инструкциям на экране."),
    ("Как изменить мой профиль?", "Чтобы изменить свой профиль, войдите в свой аккаунт и перейдите в раздел \"Настройки профиля\". Там вы можете изменить свое имя, аватар, подпись и другую информацию."),
    ("Как восстановить забытый пароль?", "Нажмите на ссылку \"Забыли пароль?\" на странице входа и следуйте инструкциям для восстановления пароля. Вам будет отправлено письмо с инструкциями на указанный при регистрации email."),
    ("Как создать новую тему?", "Чтобы создать новую тему, выберите соответствующий раздел форума \"Посты\" и нажмите кнопку \"Создать\". Введите заголовок и содержание поста, затем нажмите \"Отправить\"."),
    ("Как ответить на пост?", "Чтобы ответить на пост, откройте тему и нажмите кнопку \"Ответы других комментаторов\". Введите свой ответ в поле для ввода текста и нажмите \"Отправить\"."),
    ("Какие правила поведения на форуме?", "Правила поведения на форуме включают: уважение к другим участникам, запрет на спам, соблюдение тематики обсуждений, безопасность личных данных и соблюдение законодательств Республики Беларусь и СНГ. Подробнее на вкладке \"Правила\"."),
    ("Что делать, если у меня возникли технические проблемы на форуме?", "Если у вас возникли технические проблемы, попробуйте очистить кэш браузера и обновить страницу. Если проблема не решается, обратитесь в службу поддержки через форму на вкладке \"Помощь\"."),
    ("Как вставить изображение или файл в сообщение?", "При создании или ответе на пост используйте кнопку \"Вставить файл\", чтобы прикрепить необходимые файлы или изображения к вашему сообщению."),
    ("Что делать, если я обнаружил нарушение правил форума?", "Если вы обнаружили нарушение правил форума, нажмите кнопку \"Помощь\" и оставьте заявку. Модераторы форума рассмотрят ваше обращение и примут меры."),
    ("Как связаться с модератором или администратором?", "Чтобы связаться с модератором или администратором, отправьте личное сообщение через форум или используйте контактную форму на сайте."),
]

left_column = ft.Container(
    content = ft.Column([ft.ExpansionPanelList(
        expand_icon_color = "white",
        # controls = left_column_panels,
    ),],
    scroll = ft.ScrollMode.ADAPTIVE,
    height = 500),
    width = 800,
    padding = ft.padding.only(right = 20),
    height = 500,
)

right_column = ft.Container(
    content = ft.Column([ft.ExpansionPanelList(
        expand_icon_color = "white",
        # controls = right_column_panels,
    ),
    ],
    scroll = ft.ScrollMode.ADAPTIVE,
    height = 500),
    width = 800,
    padding = ft.padding.only(left = 20),
    height = 500
)

two_columns_row = ft.Row(
    [
        left_column,
        right_column,
    ],
    alignment = ft.MainAxisAlignment.CENTER,
)

help = ft.Column(
    [
        header_text_container,
        centered_form_container,
        faq_title_container,
        two_columns_row,
    ],
    spacing = 30,
    alignment = ft.MainAxisAlignment.CENTER,
)