from enum import Enum

class Genre(Enum):
    UNSPECIFIED = 0
    ADVENTURE = 1
    CLASSICS = 2
    DETECTIVE = 3
    FANTASY = 4
    HISTORIC = 5
    HORROR = 6
    ROMANCE = 7
    SCIFI = 8

    def __str__(self): return self.name.lower()

class Attributes:
    
    @staticmethod
    def _equal_ignore_case(target_str, other_str):
        if len(target_str) == 0:
            return True
        else:
            return target_str.casefold() == other_str.casefold()
        
    def __init__(self, title, last, first, year, genre):
        self._title = title
        self._last = last
        self._first = first
        self._year = year
        self._genre = genre

    @property
    def title(self):
        return self._title
    
    @property
    def last(self):
        return self._last
    
    @property
    def first(self):
        return self._first
    
    @property
    def year(self):
        return self._year
    
    @property
    def genre(self):
        return self._genre

    def is_match(self, target_attrs):
        return (
            Attributes._equal_ignore_case(self.title, target_attrs.title)
            and Attributes._equal_ignore_case(self.last, target_attrs.last)
            and Attributes._equal_ignore_case(self.first, target_attrs.first)
            and (target_attrs.year == 0 or target_attrs.year == self._year)
            and (target_attrs.genre == Genre.UNSPECIFIED or target_attrs.genre == self._genre)
        )
    
    def __str__(self):
        return (f"{{TITLE: '{self._title}, LAST: '{self._last}, FIRST: '{self._first}', YEAR: {self._year}, GENRE: {self._genre}}}")


