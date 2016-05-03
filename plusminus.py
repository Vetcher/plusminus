from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivymd.card import MDCard
from kivymd.list import ILeftBodyTouch, IRightBodyTouch
from kivymd.selectioncontrols import MDCheckbox, MDSwitch
from kivymd.list import *
from kivymd.textfields import SingleLineTextField
import expression_tree as et


class RightPanel(MDCard):
    pass


class PlusMinusMain(Widget):
    pass


class SettingsListItem(OneLineRightIconListItem, ToggleButtonBehavior):
    active = False
    def on_state(self, widget, value):
        for each in self.walk(restrict=True):
            if isinstance(each, RightCheckbox):
                each.active = not each.active
                self.active = each.active

class MathTextField(SingleLineTextField):
    def on_text(self, instance, value):
        if self.auto_ev:
            self.evaluate()

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass

colornames = ['Pink', 'Blue', 'Indigo', 'BlueGrey', 'Brown', 'LightBlue',
         'Purple', 'Grey', 'Yellow', 'LightGreen', 'DeepOrange',
         'Green', 'Red', 'Teal', 'Orange', 'Cyan', 'Amber',
         'DeepPurple', 'Lime']

colornums = ['50', '100', '200', '300', '400', '500', '600', '700',
         '800', '900', 'A100', 'A200', 'A400', 'A700']

class PlusMinusApp(App):
    theme_cls = ThemeManager()
    settoggled = False
    rightpaneltoggled = False

    def build(self):
        self.theme_cls.theme_style = 'Light'
        #self.theme_cls.primary_palette = self.curname = 'DeepPurple'
        #self.theme_cls.primary_hue = self.curnum = '400'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '600'
        #self.theme_cls.accent_palette = 'LightGreen'
        #self.theme_cls.accent_hue = '600'
        self.rightpanel = RightPanel()
        main_widget = PlusMinusMain()
        return main_widget

    def btn_input_text(self, value, second=False):
        self.root.ids.inputline.insert_text(value)
        if second and self.root.ids.set_check_1.active:
            self.toggle_right_panel()

    def btn_del_symb(self):
        self.root.ids.inputline.do_backspace()

    def btn_clc(self):
        self.root.ids.inputline.text = ''
        self.root.ids.outputline.text = ''

    def btn_evaluate(self, change=False):
        text = self.root.ids.inputline.text
        ans = None
        try:
            arr = et.make_expression_array(text)
            tree = et.make_expression_tree(arr)
            ans = tree.calc()
        except ZeroDivisionError:
            ans = 'Division on zero!'
        except:
            ans = 'Runtime Error'
        if ans is None:
            ans = 'Input Error'
            if not change:
                return
        self.root.ids.outputline.text = str(ans)

    def toggle_right_panel(self):
        if self.rightpaneltoggled:
            self.root.ids.numboard.remove_widget(self.rightpanel)
        else:
            self.root.ids.numboard.add_widget(self.rightpanel)
            self.rightpanel.size = self.root.ids.numboard.width, self.root.ids.numboard.height * 4 / 5
        self.rightpaneltoggled = not self.rightpaneltoggled

    def toggle_set_screen(self, event=None):
        if self.settoggled:
            self.root.ids.maintoolbar.right_action_items = [['settings', lambda x: self.toggle_set_screen()]]
            self.root.ids.scr_mngr.transition.direction = 'right'
            self.root.ids.scr_mngr.current = 'main_screen'
        else:
            self.root.ids.maintoolbar.right_action_items = [['check', lambda x: self.toggle_set_screen()]]
            self.root.ids.scr_mngr.transition.direction = 'left'
            self.root.ids.scr_mngr.current = 'settings_screen'
        self.settoggled = not self.settoggled

    def nextcolorname(self):
        try:
            next_num = colornames.index(self.curname) + 1
            if next_num == len(colornames):
                next_num = 0
            self.curname = colornames[next_num]
            self.theme_cls.primary_palette = self.curname
            self.root.ids['clrname'].text = self.curname
        except KeyError:
            self.nextcolorname()
    def nextcolornum(self):
        try:
            next_num = colornums.index(self.curnum) + 1
            if next_num == len(colornums):
                next_num = 0
            self.curnum = colornums[next_num]
            self.theme_cls.primary_hue = self.curnum
            self.root.ids['clrnum'].text = self.curnum
        except KeyError:
            self.nextcolorname()
