from cep import buscar_endereco
import flet as ft
def main(page: ft.Page):
   pass

def main(page: ft.Page):
   page.theme_mode = ft.ThemeMode.DARK
   page.window_width = 350
   page.window_height = 600
   page.title = 'buscador de CEP'
   page.bgcolor= ft.colors.BLUE_200

   campo_cep= ft.TextField(
      label='Digite seu cep'
   )
      
   page.add(campo_cep
    

ft.app(main)