import flet as ft
import os

from assets.objects import objects_main
from assets.objects import objects_contacts
from assets.objects import objects_rules
from assets.objects import objects_about_us
from assets.objects import objects_help

from assets.actions import actions_main
from assets.actions import auth
from assets.actions import tokens
from assets.actions import threads_container
from assets.actions import likes
from assets.actions.threads_ import create_theme

page_theme = ft.Theme( 
    color_scheme=ft.ColorScheme( 
        primary = "#FFFFFF",
        background = "#1C1C1C",
        primary_container = "#151515"
    )
)

def main(page: ft.Page):
    def update_page():
        page.update()
    
    def alert_liked():
        alert = ft.AlertDialog(content = ft.Container(content = ft.Text("Вы уже лайкнули этот пост", size = 20), padding = ft.padding.all(10)), open = False)
        page.overlay.append(alert)
        alert.open = True
        page.update()
    
    def main_page(*args):
        page.clean()
        page.title = "Whizz"
        page.window.maximized = True
        page.bgcolor = "#1C1C1C"
        page.theme = page_theme
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.scroll = ft.ScrollMode.AUTO
        #page.adaptive = ft.Auto
        page.padding = None
        
        if os.path.exists("frontend/assets/session.whz"):
            objects_main.profile_btn.content = ft.Text(tokens.read_login(), size = 20)
            page.appbar = objects_main.appbar_logged
        else:
            page.appbar = objects_main.appbar_unlogged
        
        page.update()
        
        def on_hover_1(event: ft.HoverEvent):
            if event.data == "true":
                objects_main.liked.scale = 1.03
                page.window.on_event
            else: 
                objects_main.liked.scale = 1.0
            page.update()
        
        def on_hover_2(event: ft.HoverEvent):
            if event.data == "true":
                objects_main.conf.scale = 1.03
            else:
                objects_main.conf.scale = 1.0
            page.update()
            
        def on_hover_3(event: ft.HoverEvent):
            if event.data == "true":
                objects_main.online.scale = 1.03
            else:
                objects_main.online.scale = 1.0
            page.update()
        
        def open_lgn(e):
            objects_main.lgn_popup.open = True
            page.update()
            
        def open_reg(e):
            objects_main.reg_popup.open = True
            page.update()
            
        def open_writer(e):
            objects_main.post_popup.open = True
            page.update()
            
        def close_writer(e):
            objects_main.post_popup.open = False
            page.update()
        
        def redirect_to_reg(e):
            objects_main.lgn_popup.open = False
            objects_main.reg_popup.open = True
            page.update()
            
        def redirect_to_lgn(e):
            objects_main.reg_popup.open = False
            objects_main.lgn_popup.open = True
            page.update()
            
        def login(*args):
            login = objects_main.lgn_login_field.value
            password = objects_main.lgn_pass_field.value
            
            response = auth.login(login, password)
            
            if response == 200:
                tokens.write_login(objects_main.lgn_login_field.value) 
                objects_main.lgn_login_field.value = ""
                objects_main.lgn_pass_field.value = ""
                page.appbar = objects_main.appbar_logged
                objects_main.profile_btn.text = tokens.read_login()
                alert = ft.AlertDialog(content = ft.Text("Вы успешно вошли в учётную запись", size = 20, width = 360), open = False, bgcolor = "#1C1C1C")   
            elif response == 400:
                objects_main.lgn_login_field.value = ""
                objects_main.lgn_pass_field.value = ""
                alert = ft.AlertDialog(content = ft.Text("Неверный логин или пароль", size = 20, width = 300), open = False, bgcolor = "#1C1C1C")

            objects_main.lgn_popup.open = False
            page.overlay.append(alert)
            alert.open = True
            page.update()
                
        def register(*args):
            login = objects_main.reg_login_field.value
            password = objects_main.reg_pass_field.value
            
            response = auth.register(login, password)
            
            if response == 200:
                objects_main.reg_login_field.value = ""
                objects_main.reg_pass_field.value = ""
                page.appbar = objects_main.appbar_logged
                objects_main.profile_btn.text = tokens.read_login()
                
                alert = ft.AlertDialog(content = ft.Text("Вы успешно зарегистрировали учётную запись", size = 20, width = 360), open = False, bgcolor = "#1C1C1C")
            elif response == 400:
                objects_main.reg_login_field.value = ""
                objects_main.reg_pass_field.value = ""
                alert = ft.AlertDialog(content = ft.Text("Такой логин уже существует", size = 20, width = 300), open = False, bgcolor = "#1C1C1C")
            
            objects_main.reg_popup.open = False
            page.overlay.append(alert)
            alert.open = True
            page.update()
                          
        def write_post(*args):
            title = objects_main.post_header_field.value
            topic = objects_main.theme_picker.value
            text = objects_main.post_text_field.value
            response = create_theme(topic, title, text)
            print(response)
            print(topic, title, text)
            
            if response[0] == 200:
                alert = ft.AlertDialog(content = ft.Container(content = ft.Text("Ваша тема была опубликована", size = 20, width = 360, text_align = ft.TextAlign.CENTER, height = 25), alignment = ft.alignment.center, height = 30), open = False, bgcolor = "#1C1C1C")
            else:
                alert = ft.AlertDialog(content = ft.Text("Ошибка публикации!", size = 20, width = 360), open = False, bgcolor = "#1C1C1C")
            page.overlay.append(alert)
            alert.open = True
            page.update()
        
        objects_main.liked.on_hover = on_hover_1
        objects_main.conf.on_hover = on_hover_2
        objects_main.online.on_hover = on_hover_3
        
        objects_main.login.on_click = open_lgn
        objects_main.register.on_click = open_reg
        objects_main.contacts.on_click = contacts
        objects_main.home.on_click = main_page
        objects_main.rules.on_click = rules
        objects_main.about.on_click = about_us
        objects_main.help_.on_click = help
        objects_main.posts.on_click = open_writer
        
        objects_main.lgn_redirect.on_click = redirect_to_reg
        objects_main.reg_redirect.on_click = redirect_to_lgn
        objects_main.cancel_post.on_click = close_writer
        
        objects_main.login_btn.on_click = login
        objects_main.reg_btn.on_click = register
        objects_main.send_post.on_click = write_post
        
        categories_container = ft.Container(
            content = objects_main.categories_column,
            width = 300,
            bgcolor = "#151515",
            padding = ft.padding.all(50),
            margin = ft.margin.only(right = 50),
            border_radius = 20
        )
        
        main_container = ft.Container(
            content = ft.Column(
                [
                    objects_main.main_column,
                    threads_container.get_main_threads(page)
                ], scroll = ft.ScrollMode.ADAPTIVE,
                spacing = 50  
            ),
            margin = ft.margin.only(right = 50),
            height = 930,
            padding = ft.padding.only(top = 30)
        )
        final_container = ft.Container(
            content = ft.Row(
                [
                    categories_container, 
                    main_container
                ]
            ),
            padding = ft.padding.only(left = 100),
            #alignment = ft.alignment.top_center
        )
        
        page.overlay.append(objects_main.lgn_popup)
        page.overlay.append(objects_main.reg_popup)
        page.overlay.append(objects_main.post_popup)
        page.add(final_container)
        page.update()
    
    def contacts(*args):
        page.clean()
        page.title = "Контакты"
        page.padding = ft.padding.only(right = 300, left = 280, top = 0)
        
        page.add(objects_contacts.contacts)
        page.update()
    
    def rules(*args):
        page.clean()
        page.scroll = ft.ScrollMode.AUTO
        page.padding = None
        page.title = "Правила"
        
        page.add(objects_rules.final)
        page.update()
        
    def about_us(*args):
        page.clean()
        page.padding = None
        page.title = "О нас"
        objects_about_us.right_container_image_button.on_click = actions_main.open_telegram_link
        
        def on_hover(event: ft.HoverEvent):
            if event.data == "true":
                objects_about_us.right_container_image_button.scale = 1.03
            else:
                objects_about_us.right_container_image_button.scale = 1.0
            page.update
            
        objects_about_us.right_container_image_button.on_hover = on_hover
        page.add(objects_about_us.about_us)
        page.update()



    def help(page: ft.Page):
        page.title = "Помощь"
        page.padding = ft.padding.only(right = 300, left = 280, top = 0)
        
        page.padding = ft.padding.only(right = 100, left = 100, top = 80)

        def on_hover(event):
            if event.data == "true":
                event.control.scale = 1.03
            else:
                event.control.scale = 1.0 
            page.update()

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
            on_hover = on_hover,
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

        def create_panel(index, title, content):
            return ft.ExpansionPanel(
                header = ft.Container(
                    content = ft.Text(title, size = 16, color = "white"),
                    padding = ft.padding.symmetric(horizontal = 15, vertical = 10),
                    bgcolor = "#151515",
                    border = ft.border.all(0, "transparent"),
                    border_radius = 15,
                ),
                content = ft.Container(
                    content = ft.Column(
                        [
                            ft.Divider(height = 1, color = "#850000"),
                            ft.Text(content, size = 16, color = "white"),
                        ],
                        spacing = 35,
                    ),
                    padding = ft.padding.all(10),
                    bgcolor = "#151515",
                    border_radius = 15,
                ), bgcolor = "#151515",
            )

        left_column_panels = [create_panel(i, *panel_data[i]) for i in range(len(panel_data) // 2)]
        right_column_panels = [create_panel(i, *panel_data[i]) for i in range(len(panel_data) // 2, len(panel_data))]

        left_column = ft.Container(
            content = ft.Column([ft.ExpansionPanelList(
                expand_icon_color = "white",
                controls = left_column_panels,
            ),],
            scroll = ft.ScrollMode.ADAPTIVE,
            height = 500),
            width = 800,
            padding = ft.padding.only(right = 20),
            height = 500
        )

        right_column = ft.Container(
            content = ft.Column([ft.ExpansionPanelList(
                expand_icon_color = "white",
                controls = right_column_panels,
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
        page.add(help)
        page.update()
    threads_container.set_callback_main(main_page)
    threads_container.set_callback_update(update_page)
    threads_container.set_callback_liked(alert_liked)
    main_page()

if __name__ == "__main__":
    ft.app(target = main)