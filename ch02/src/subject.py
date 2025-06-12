from enum import Enum


class Subject(Enum):
    UNSPECIFIED = 0
    PAINTING = 1
    WRITING = 2

    def __str__(self):
        return self.name.lower()
