import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 600)

Builder.load_file('cal.kv')

class calLayout(Widget):
    def clear(self):
        self.ids.input.text = '0'
    
    def pressBtnNumber(self, button):
        if self.ids.input.text=='0':
            self.ids.input.text=''
            self.ids.input.text += str(button)
        else:
            self.ids.input.text += str(button)

class calApp(App):
    def build(self):
        return calLayout()

if __name__ == '__main__':
    calApp().run()