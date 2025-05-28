from cep import buscar_endereco
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 300
    page.window_height = 400
    page.title = 'Buscador de CEP'
    page.bgcolor = ft.Colors.BLACK
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    icone = ft.Icon(
        name=ft.Icons.LOCATION_ON,
        size=70,
        color=ft.Colors.YELLOW
    )

    campo_cep = ft.TextField(
        hint_text='Digite seu CEP',
        width=250,
        text_align=ft.TextAlign.LEFT,
        hint_style=ft.TextStyle(color=ft.Colors.YELLOW),
        color=ft.Colors.YELLOW,
        border_color=ft.Colors.YELLOW,
        on_submit=lambda e: buscar_endereco(campo_cep.value, campo_resposta)
    )

    btn_buscar = ft.ElevatedButton(
        text='Buscar',
        bgcolor=ft.Colors.YELLOW,
        color=ft.Colors.BLACK,
        width=150,
        icon=ft.Icons.SEARCH,
        on_click=lambda evento: buscar_endereco(campo_cep.value, campo_resposta)
    )

    campo_resposta = ft.Text(
        value='',
        text_align=ft.TextAlign.CENTER,
        width=250,
        color=ft.Colors.YELLOW
    )

    page.controls = [
        ft.Container(
            content=icone,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=campo_cep,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=btn_buscar,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=campo_resposta,
            alignment=ft.alignment.center,
        ),
    ]
    page.update()

ft.app(main)

