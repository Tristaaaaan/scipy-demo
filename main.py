from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from scipy.special import factorial

# KivyMD Design String
kv = """
BoxLayout:
    orientation: 'vertical'
    
    MDTextField:
        id: input_text
        hint_text: "Enter a number"
        input_filter: 'int'
        input_type: 'number'
        pos_hint: {'center_x': 0.5}
        size_hint_x: None
        width: "200dp"
    
    Button:
        text: "Calculate Factorial"
        on_release: app.calculate_factorial()
"""


class MyApp(MDApp):
    def build(self):
        self.title = "KivyMD with SciPy"
        return Builder.load_string(kv)

    def calculate_factorial(self):
        try:
            input_text = self.root.ids.input_text.text
            n = int(input_text)
            result = factorial(n)
            self.show_result(f"The factorial of {n} is {result}")
        except ValueError:
            self.show_result("Invalid input. Please enter a valid integer.")

    def show_result(self, message):
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDRaisedButton

        self.dialog = MDDialog(
            title="Factorial Calculator",
            text=message,
            buttons=[MDRaisedButton(
                text="Close", on_release=self.close_dialog)],
        )
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()


if __name__ == "__main__":
    MyApp().run()
