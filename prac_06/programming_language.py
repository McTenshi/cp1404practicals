"""
CP1404 - Practical
Joshua Quidlat
Programming Language
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return name, typing, reflection and first appearance"""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if typing is Dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
