import flet as ft
import os, sys, subprocess

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
from assets.actions.help import send_feedback

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
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, "assets", "session.whz")
        page.overlay.append(objects_main.lgn_popup)
        page.overlay.append(objects_main.reg_popup)
        if os.path.exists(path):
            objects_main.profile_btn.content = ft.Text(tokens.read_login(), size = 20)
            page.appbar = objects_main.appbar_logged
            page.overlay.append(objects_main.post_popup)
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
                
            def open_writer(e):
                objects_main.post_popup.open = True
                page.update()
                
            def close_writer(e):
                objects_main.post_popup.open = False
                page.update()
                            
            def write_post(*args):
                title = objects_main.post_header_field.value
                topic = objects_main.theme_picker.value
                text = objects_main.post_text_field.value
                
                print(topic, title, text)
                
                response = create_theme(topic, title, text)
                print(f"--------------{response}")
                
                if response[0] == 200:
                    alert = ft.AlertDialog(content = ft.Container(content = ft.Text("Ваша тема была опубликована", size = 20, width = 360, text_align = ft.TextAlign.CENTER, height = 25), alignment = ft.alignment.center, height = 30), open = False, bgcolor = "#1C1C1C")
                else:
                    alert = ft.AlertDialog(content = ft.Text("Ошибка публикации!", size = 20, width = 360), open = False, bgcolor = "#1C1C1C")
                page.overlay.append(alert)
                alert.open = True
                page.update()
            
            def open_profile_popup(*args):
                objects_main.username.value = tokens.read_login()
                page.overlay.append(objects_main.profile_popup)
                objects_main.profile_popup.open = True
                page.update()
            
            objects_main.liked.on_hover = on_hover_1
            objects_main.conf.on_hover = on_hover_2
            objects_main.online.on_hover = on_hover_3
            
            objects_main.contacts.on_click = contacts
            objects_main.home.on_click = main_page
            objects_main.rules.on_click = rules
            objects_main.about.on_click = about_us
            objects_main.help_.on_click = help
            objects_main.posts.on_click = open_writer
            
            objects_main.cancel_post.on_click = close_writer
            
            objects_main.send_post.on_click = write_post
            objects_main.profile_btn.on_click = open_profile_popup
            
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
            
            page.add(final_container)
            
            
            
        else:
            page.appbar = objects_main.appbar_unlogged
            
            def open_lgn(e):
                objects_main.lgn_popup.open = True
                page.update()
                
            def open_reg(e):
                objects_main.reg_popup.open = True
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
                    page.window.destroy()
                    subprocess.Popen([sys.executable] + sys.argv)
                    
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
                    page.window.destroy()
                    subprocess.Popen([sys.executable] + sys.argv)
                    
                elif response == 400:
                    objects_main.reg_login_field.value = ""
                    objects_main.reg_pass_field.value = ""
                    alert = ft.AlertDialog(content = ft.Text("Такой логин уже существует", size = 20, width = 300), open = False, bgcolor = "#1C1C1C")
                
                objects_main.reg_popup.open = False
                page.overlay.append(alert)
                alert.open = True
                page.update()
                
            objects_main.login.on_click = open_lgn
            objects_main.register.on_click = open_reg
            objects_main.lgn_redirect.on_click = redirect_to_reg
            objects_main.reg_redirect.on_click = redirect_to_lgn
            objects_main.login_btn.on_click = login
            objects_main.reg_btn.on_click = register
        
        page.overlay.append(objects_main.reg_popup)
        page.overlay.append(objects_main.lgn_popup)
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
            page.update()
            
        objects_about_us.right_container_image_button.on_hover = on_hover
        page.add(objects_about_us.about_us)
        page.update()

    def help(*args):
        page.clean()
        page.title = "Помощь"
        page.padding = ft.padding.only(right = 100, left = 100, top = 80)

        def on_hover(event):
            if event.data == "true":
                event.control.scale = 1.03
            else:
                event.control.scale = 1.0 
            page.update()
        
        def send_report(*args):
            title = objects_help.title_input.value
            description = objects_help.description_input.value
            
            response = send_feedback(title, description)
            
            objects_help.description_input.value = ""
            objects_help.title_input.value = ""
            
            if response == 200:
                alert = ft.AlertDialog(content = ft.Text("Отчёт отправлен!"), open = False)
                page.overlay.append(alert)
                alert.open = True
                page.update()
            
            
        
        objects_help.submit_button.on_hover = on_hover
        objects_help.submit_button.on_click = send_report
        
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

        left_column_panels = [create_panel(i, *objects_help.panel_data[i]) for i in range(len(objects_help.panel_data) // 2)]
        right_column_panels = [create_panel(i, *objects_help.panel_data[i]) for i in range(len(objects_help.panel_data) // 2, len(objects_help.panel_data))]

        objects_help.left_column.content = ft.Column([ft.ExpansionPanelList(
        expand_icon_color = "white",
        controls = left_column_panels,),],)
        objects_help.right_column.content = ft.Column([ft.ExpansionPanelList(
        expand_icon_color = "white",
        controls = right_column_panels)])

        page.add(objects_help.help)
        page.update()
        
    threads_container.set_callback_main(main_page)
    threads_container.set_callback_update(update_page)
    threads_container.set_callback_liked(alert_liked)
    main_page()

if __name__ == "__main__":
    ft.app(target = main)