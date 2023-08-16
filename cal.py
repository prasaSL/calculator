import kivy
kivy.require('2.1.0')
import re
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
        elif self.ids.input.text[-1] in ['+', '-', '*', '/'] and button == 0:
            pass
        else:
            self.ids.input.text += str(button)
    def pressBtnSign(self, sign):
        if self.ids.input.text[-1] in ['+', '-', '*', '/']:
            pass
        else:
            self.ids.input.text += sign
    def pressBtnminus(self):
        text = self.ids.input.text
        if "-" in text:
            self.ids.input.text = text.replace("-", "")
        else:
            self.ids.input.text = '-' + self.ids.input.text
    def pressBtnDot(self):
        list1=re.split('\+|\-|\*|\/|\%',self.ids.input.text)
        if len(list1)!=0  and not '.' in list1[-1] :
            self.ids.input.text += '.'
        elif "." not in self.ids.input.text and self.ids.input.text[-1] != ['+', '-', '*', '/']:
            self.ids.input.text += '.'
        else:
            pass
    def pressBtnEqual(self):
        answer = eval(self.ids.input.text)
        self.ids.input.text = str(answer)
class calApp(App):
    def build(self):
        return calLayout()

if __name__ == '__main__':
    calApp().run()