from enum import Enum


class Kind(Enum):
    FICTION = 1
    COOKBOOK = 2
    HOWTO = 3

    def __str__(self):
        return self.name.lower()
