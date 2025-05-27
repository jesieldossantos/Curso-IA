from cep import buscar_endereco
import flet as ft


def main(page: ft.Page):
   page.theme_mode = ft.ThemeMode.DARK
   page.window_width = 100
   page.window_height = 200
   page.title = 'buscador de CEP'
   page.bgcolor= ft.Colors.BLUE_200
   page.window.always_on_top= True
   page.vertical_alignment= ft.MainAxisAlignment.CENTER
   page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
   
   campo_cep= ft.TextField(
      label='Digite seu cep'
   )
      
   icone = ft.Icon(
      name=ft.Icons.LOCATION_ON ,
      size=70,
      color=ft.Colors.RED_300
   )

   campo_resposta = ft.Text(
      value='',
      text_align=ft.TextAlign.CENTER
   )


   btn_buscar = ft.ElevatedButton(
      text='Buscar',
      bgcolor=ft.Colors.GREEN,
      color=ft.Colors.WHITE,
      width=150,
      icon=ft.Icons.SEARCH,
      on_click=lambda evento: buscar_endereco(campo_cep.value, campo_resposta)
   )
   page.add(
      icone,
      campo_resposta,
      campo_cep,
      btn_buscar
   )

ft.app(main)