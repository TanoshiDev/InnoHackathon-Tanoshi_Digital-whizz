import flet as ft

text = ft.Text(
        "Форум Whizz - это платформа для общения и обмена знаниями на самые разнообразные темы. Форум предлагает множество категорий, чтобы каждый мог найти интересующие его обсуждения, делиться опытом, задавать вопросы и находить ответы. Whizz - Вдохновляй и будь на высоте!",
        size = 17,
        color = "#FFFFFF",
        weight = "normal",
        font_family = "Uni Neue Thin",
        text_align = "start",
        max_lines = None,
        width = 1300,
)

text_with_image_background = ft.Container(
    content = ft.Container(
        content = text,
        padding = ft.padding.only(left = 190),
    ),
    padding = ft.padding.symmetric(horizontal = 20),
    alignment = ft.alignment.center,
    width = 1980,
    height = 200,
    image_src = "Whizz.png",
    image_fit = ft.ImageFit.COVER,
    border_radius = 25,
)

left_container = ft.Container(
    content = ft.Image(
            src="frontend/assets/image_about_us.png",
            width = 460,
            height = 340,
            fit = ft.ImageFit.CONTAIN,
    ),
    bgcolor="#151515",
    border_radius=25,
    width=940,
    height=530,
)


right_container_text = ft.Text(
    "Социальные сети",
    size = 26,
    color = "#FFFFFF",
    weight ="bold",
    font_family = "Uni Neue",
    text_align = "center",
)

right_container_image_button = ft.Container(
    content = ft.Image(
        src="tg_about_us.png",
        width = 440,
        height = 300,
    ),
    animate_scale = ft.Animation(duration=150, curve = ft.AnimationCurve.EASE_IN_OUT),
    border_radius = 15,
)


right_container = ft.Container(
    content = ft.Column(
        [
            right_container_text,
            right_container_image_button,
        ],
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        spacing = 20,
    ),
    bgcolor = "#151515",
    border_radius = 25,
    width = 520,
    height = 400,
    padding = ft.padding.all(20),
)

second_row = ft.Row(
    [
        left_container,
        right_container,
    ],
    alignment = ft.MainAxisAlignment.CENTER,
    vertical_alignment = ft.CrossAxisAlignment.CENTER,
    spacing = 60,
)


about_us = ft.Container(
    content = ft.Column(
        [
            text_with_image_background,
            second_row,
        ],
        spacing = 60,
        alignment = ft.MainAxisAlignment.CENTER,
    ),
    alignment = ft.alignment.center,
    padding = ft.padding.all(20),
)