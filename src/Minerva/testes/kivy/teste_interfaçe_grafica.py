from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from src.Minerva.testes.teste_geral import run_minerva

class Tela(BoxLayout):
    def zerar(self):

        run_minerva()


class kivy_interface(App):
    def build(self):
        return Tela()



kivy_interface().run()