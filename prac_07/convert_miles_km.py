"""
CP1404 - Practical
Joshua Quidlat
Convert Miles to Kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934


class ConvertMilesApp(App):
    output = StringProperty()

    def build(self):
        """Construct the app"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles):
        """Converts miles into kilometers"""
        try:
            self.output = str(float(miles) * MILES_TO_KILOMETERS)
        except ValueError:
            self.output = '0.0'

    def handle_miles_increment(self, miles, increment):
        try:
            self.root.ids.input_miles.text = str(float(miles) + increment)
        except ValueError:
            self.root.ids.input_miles.text = str(0 + increment)


# Run the app
ConvertMilesApp().run()
