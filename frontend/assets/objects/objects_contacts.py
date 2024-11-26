import flet as ft

left = ft.Image(
        src = "left.png",
        width = 270,
    )

center = ft.Image(
    src = "center.png",
    width = 698,
)

right = ft.Image(
    src = "right.png",
    width = 270,
)

telegram = ft.Image(
    src = "telegram.png",
    width = 50,
    fit = ft.ImageFit.CONTAIN,
)

discord = ft.Image(
    src = "discord.png",
    width = 50,
    fit = ft.ImageFit.CONTAIN,
)

instagram = ft.Image(
    src = "instagram.png",
    width = 50,
    fit = ft.ImageFit.CONTAIN,
)

text_container = ft.Container(
    content = ft.Column(
        [
            
            ft.Text(
                "Прямые контакты",
                size = 16,
                weight = "bold",
                color = "#FFFFFF",
                font_family = "WeblySleek UI",
            ),

            ft.Text(
                "katyatelanchenko@gmail.com\nmorph07112020@gmail.com\nowner@tanoshi.space\nhhungh07@gmail.com",
                size = 12,
                color = "#FFFFFF",
                font_family = "Uni Neue Thin",
            ),

            ft.Text(
                "Социальные сети",
                size = 16,
                weight = "bold",
                color = "#FFFFFF",
                font_family = "WeblySleek UI",
            ),

            ft.Row(
                [
                    ft.Row([
                        telegram,
                    ft.Column(
                        [
                            ft.Text(
                                "@ccCwNnn",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "@Roob1e",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "@knownraw",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "@Zeefren",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                        ],
                        spacing = 5,
                        alignment = "start",
                    )],width = 170),

                    
                    ft.Row([ discord,
                        ft.Column([
                            ft.Text(
                                "_cwn__belka__",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "roob1e",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "pacanchik",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "Zeefren",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                        ],
                        spacing = 5,
                        alignment = "start",
                        )
                    ],width = 170),
                    ft.Row([
                        instagram,
                    ft.Column(
                        [
                            ft.Text(
                                "@hachu_domoi",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "@_assxmblxr_",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "@tanoshi.space",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                            ft.Text(
                                "@Zeefren_VV",
                                size = 12,
                                color = "#FFFFFF",
                                font_family = "Uni Neue Thin",
                            ),
                        ],
                        spacing = 5,
                        alignment = "start",
                    )]),
                ],
                spacing = 50,
                
            ),
        ],
        spacing = 20,
        alignment = "start",
    ),
    padding = ft.padding.all(20),
    alignment = ft.alignment.center,
    width = 700,
    height = 300,
    bgcolor="#151515",
    border_radius = 26,
)

center_column = ft.Column(
    [
        text_container,
        ft.Container(
            content=center,
            alignment = ft.alignment.center,
            height = 450, 
        )
    ],
    spacing = 10,
    alignment = ft.MainAxisAlignment.CENTER
)

contacts = ft.Container(
    content = ft.Row(
        [
            ft.Container(content=left, alignment = ft.alignment.center, margin = ft.margin.only(right = 40)),
            ft.Container(content=center_column, alignment = ft.alignment.center, margin = ft.margin.only(top = 30)),
            ft.Container(content=right, alignment = ft.alignment.center, margin = ft.margin.only(left = 40)),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    ),
    padding=ft.padding.only(top = 20, left = 20, right = 20),
    margin = ft.margin.only(top = 50),
    scale = 1.2
)