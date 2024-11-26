import flet as ft

from assets.objects import objects_main
from assets.objects import objects_contacts
from assets.objects import objects_rules

from assets.actions import actions_main

page_theme = ft.Theme( 
    color_scheme=ft.ColorScheme( 
        primary = "#FFFFFF",
        background = "#1C1C1C",
        primary_container = "#151515"
    )
)
def main(page: ft.Page):
    def main_page(*args):
        page.clean()
        page.title = "Whizz"
        page.window.maximized = True
        page.bgcolor = "#1C1C1C"
        page.theme = page_theme
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.appbar = objects_main.appbar_unlogged
        page.padding = None
        
        def on_hover_1(event: ft.HoverEvent):
            if event.data == "true":
                objects_main.liked.scale = 1.03
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
        
        def redirect_to_reg(e):
            objects_main.lgn_popup.open = False
            objects_main.reg_popup.open = True
            page.update()
            
        def redirect_to_lgn(e):
            objects_main.reg_popup.open = False
            objects_main.lgn_popup.open = True
            page.update()
        
        objects_main.liked.on_hover = on_hover_1
        objects_main.conf.on_hover = on_hover_2
        objects_main.online.on_hover = on_hover_3
        
        objects_main.login.on_click = open_lgn
        objects_main.register.on_click = open_reg
        objects_main.contacts.on_click = contacts
        objects_main.home.on_click = main_page
        objects_main.rules.on_click = rules
        
        objects_main.lgn_redirect.on_click = redirect_to_reg
        objects_main.reg_redirect.on_click = redirect_to_lgn
        
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
                    objects_main.main_column
                ],    
            ),
            margin = ft.margin.only(right = 50),
            height = 800
        )
        
        final_container = ft.Container(
            content = ft.Row(
                [
                    categories_container, 
                    main_container
                ]
            ),
            padding = ft.padding.only(left = 100),
            margin = ft.margin.only,
            alignment = ft.alignment.top_center
        )
        
        page.overlay.append(objects_main.lgn_popup)
        page.overlay.append(objects_main.reg_popup)
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
        
    main_page()

if __name__ == "__main__":
    ft.app(target = main)