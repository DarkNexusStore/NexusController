from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests

class NexusController(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        btn_up = Button(text='Volumen +', size_hint=(1, .5))
        btn_up.bind(on_press=self.subir_volumen)
        
        btn_down = Button(text='Volumen -', size_hint=(1, .5))
        btn_down.bind(on_press=self.bajar_volumen)
        
        layout.add_widget(btn_up)
        layout.add_widget(btn_down)
        return layout

    def subir_volumen(self, instance):
        print("Subiendo volumen...")
        # Aquí irá la lógica de red más adelante

    def bajar_volumen(self, instance):
        print("Bajando volumen...")

if __name__ == '__main__':
    NexusController().run()

