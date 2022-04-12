from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Calc(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        o_label = Label(size_hint_y = 0.75, font_size=50)
        button_symbols = ('1', '2', '3', '*',
                          '4', '5', '6', '/',
                          '7', '8', '9', '-',
                          '0', '+', '/', '=')
        bgrid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            bgrid.add_widget(Button(text=symbol))

        clear = Button(text = 'Clear', size_hint_y=None, height=100)
        def print(instance):
            o_label.text += instance.text
        for button in bgrid.children[1:]:
            button.bind(on_press=print)
        def resize(label, new_height):
            label.fontsize = 0.5*label.height
        o_label.bind(height=resize)

        def evaluate_result(instance):
            try:
                o_label.text = str(eval(o_label.text))
            except SyntaxError:
                o_label.text = 'Python Syntax error!'
        bgrid.children[0].bind(on_press=calresult)

        def clear_label(instance):
            o_label.text = " "
        clear.bind(on_press=clear_label)

        root_widget.add_widget(o_label)
        root_widget.add_widget(bgrid)
        root_widget.add_widget(clear)
        return root_widget
Calc().run()