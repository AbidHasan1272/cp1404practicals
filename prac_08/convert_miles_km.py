from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (1000, 600)


class MilesToKmApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.output_text = "0.0"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        try:
            miles = float(value)
            km = miles * 1.60934
            self.output_text = f"{km:.5f}"
        except ValueError:
            self.output_text = "Invalid input"

    def handle_increment(self, value, change):
        try:
            miles = float(value) + change
            self.root.ids.input_miles.text = str(miles)
            self.handle_convert(miles)
        except ValueError:
            self.root.ids.input_miles.text = "0"
            self.output_text = "0.0"


MilesToKmApp().run()
