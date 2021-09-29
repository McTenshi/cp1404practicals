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
        self.output = str(float(miles) * MILES_TO_KILOMETERS)

    def handle_miles_increase(self, miles):
        """Increases miles by one"""
        self.root.ids.input_miles.text = str(float(miles) + 1)

    def handle_miles_decrease(self, miles):
        """Decreases miles by one"""
        self.root.ids.input_miles.text = str(float(miles) - 1)
        pass

# Run the app
ConvertMilesApp().run()
