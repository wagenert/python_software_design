class Attributes:
    
    @staticmethod
    def _equal_ignore_case(target_str, other_str):
        if len(target_str) == 0:
            return True
        else:
            return target_str.casefold() == other_str.casefold()
        
    def __init__(self, title, last, first, year):
        self.__title = title
        self.__last = last
        self.__first = first

    @property
    def title(self):
        return self.__title
    
    @property
    def last(self):
        return self.__last
    
    @property
    def first(self):
        return self.__first
    
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
        )
    
    def __str__(self):
        return (f"TITLE: '{self._title}, LAST: '{self._last}, FIRST: '{self._first}'")


