from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from . import teste_geral

class Tela(BoxLayout):
    def zerar(self):

        teste_geral.run_minerva()


class kivy_interface(App):
    def build(self):
        return Tela()



kivy_interface().run()
