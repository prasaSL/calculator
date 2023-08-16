import kivy
kivy.require('2.1.0')
import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

#set window size
Window.size = (400, 600)

#load kv file
Builder.load_file('cal.kv')

#main class
class calLayout(Widget):

    #clear input
    def clear(self):
        self.ids.input.text = '0'
    #press number button
    def pressBtnNumber(self, button):
        if self.ids.input.text=='0':
            self.ids.input.text=''
            self.ids.input.text += str(button)
        elif self.ids.input.text[-1] in ['+', '-', '*', '/'] and button == 0:
            pass
        else:
            self.ids.input.text += str(button)


    #press sign button       
    def pressBtnSign(self, sign):
        if self.ids.input.text[-1] in ['+', '-', '*', '/']:
            pass
        else:
            self.ids.input.text += sign

     #press Mainers button       
    def pressBtnminus(self):
        if self.ids.input.text[-1] in ['+', '-', '*', '/'] or self.ids.input.text=='0':
            pass
        elif "-" in self.ids.input.text:
            self.ids.input.text = self.ids.input.text.replace('-','')
        else:
            self.ids.input.text = f'-{self.ids.input.text}'

    #press decimal place  button
    def pressBtnDot(self):
        list1=re.split('\+|\-|\*|\/|\%',self.ids.input.text)
        if len(list1)!=0  and not '.' in list1[-1] :
            self.ids.input.text += '.'
        elif "." not in self.ids.input.text and self.ids.input.text[-1] != ['+', '-', '*', '/']:
            self.ids.input.text += '.'
        else:
            pass


    #press equal button
    def pressBtnEqual(self):
        answer = eval(self.ids.input.text)
        self.ids.input.text = str(answer)

    #press backspace button
    def backspace(self):
        if len(self.ids.input.text)==1:
            self.ids.input.text = '0'
        else:
            self.ids.input.text = self.ids.input.text[:-1]

#main app
class calApp(App):
    def build(self):
        return calLayout()

#run app

if __name__ == '__main__':
    calApp().run()