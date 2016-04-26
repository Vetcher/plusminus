from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
# from kivy.properties import ObjectProperty, ListProperty
import expression_tree as et


class RightPanel(Button):
    isopened = False

    def on_press(self):
        if self.isopened:
            self.x = self.parent.width - self.parent.width / 10
            self.width = self.parent.width - self.x
            for each in self.walk(restrict=True):
                if each is not self:
                    each.disabled = True

        else:
            self.x = self.parent.width / 3 * 2 - self.parent.width / 10
            self.width = self.parent.width - self.x
            for each in self.walk(restrict=True):
                if each is not self:
                    each.disabled = False
        self.isopened = not self.isopened


class BaseBtn(Button):
    def on_press(self):
        self.parent.textline.input(self.value)


class BasePanBtn(BaseBtn):
    def on_press(self):
        self.parent.parent.textline.input(self.value)
        self.parent.on_press()


class ControlBtn(BaseBtn):
    def on_press(self):
        if self.typebtn is 'eval':
            text = self.parent.textline.text
            try:
                ans = self.parent.evaluator.evaluate(text)
                if ans is None:
                    self.parent.answerline.text = 'Input Error'
                else:
                    self.parent.answerline.text = str(ans)
            except TypeError:
                self.parent.answerline.text = 'Input Error'

        elif self.typebtn is 'del':
            self.parent.textline.text = self.parent.textline.text[:-1]
        elif self.typebtn is 'clc':
            self.parent.answerline.text = ''
            self.parent.textline.text = ''


class MathInput(TextInput):
    def input(self, value):
        self.insert_text(value)


class Evaluator(object):
    @staticmethod
    def evaluate(text):
        return et.make_expression_tree(et.make_expression_array(text)).calc()


class CalculatorGui(Widget):
    evaluator = Evaluator()


class CalcApp(App):
    def build(self):
        gui = CalculatorGui()
        return gui


if __name__ in ('__android__', '__main__'):
    w = 1080 / 4
    h = 1920 / 4
    Config.set('graphics', 'width', '1280')
    Config.set('graphics', 'height', '720')
    Config.set('graphics', 'window_state', 'maximized')
    CalcApp().run()