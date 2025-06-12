from enum import Enum


class Region(Enum):
    UNSPECIFIED = 0
    CHINA = 1
    FRANCE = 2
    INDIA = 3
    ITALY = 4
    MEXICO = 5
    PERSIA = 6
    US = 7

    def __str__(self):
        return self.name.capitalize()
