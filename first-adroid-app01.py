from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.text.markup import MarkupLabel
import webbrowser

class MainApp(App):
    def open_web(self, instance, value):
        webbrowser.open("www.programaren.com/")

    def build(self):
        layout = GridLayout(rows=2)

        label = Label(text='Bienvenido al curso de aplicaciones android con Python!\n',
                      size_hint=(5, 5),
                      font_size='20sp',
                      pos_hint={'center_x': .5, 'center_y': .5})

        layout.add_widget(label)

        btn_continue = Button(text='Continuar!')
        btn_continue.bind(state=self.open_web)
        layout.add_widget(btn_continue)

        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()
