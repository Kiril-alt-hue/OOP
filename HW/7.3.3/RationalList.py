from Rational_copy import *
from RationalValueError import *

class RationalList:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = []
            for item in data:
                try:
                    if isinstance(item, (Rational, int)):
                        self.data.append(Rational(item) if isinstance(item, int) else item)
                    else:
                        raise RationalValueError(self, item, "ініціалізація",
                                               "Елементи списку повинні бути типу Rational або int")
                except (ValueError, TypeError) as e:
                    raise RationalValueError(self, item, "ініціалізація", str(e))

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        try:
            if isinstance(value, (Rational, int)):
                self.data[index] = Rational(value) if isinstance(value, int) else value
            else:
                raise RationalValueError(self, value, "присвоєння",
                                       "Елементи списку повинні бути типу Rational або int")
        except (ValueError, TypeError) as e:
            raise RationalValueError(self, value, "присвоєння", str(e))

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        try:
            if isinstance(other, RationalList):
                new_data = self.data + other.data
                return RationalList(new_data)
            elif isinstance(other, (Rational, int)):
                new_data = self.data + [Rational(other) if isinstance(other, int) else other]
                return RationalList(new_data)
            else:
                raise RationalValueError(self, other, "додавання",
                                       "Можна додавати лише Rational, int або RationalList")
        except (ValueError, TypeError) as e:
            raise RationalValueError(self, other, "додавання", str(e))

    def __iadd__(self, other):
        try:
            if isinstance(other, RationalList):
                self.data += other.data
            elif isinstance(other, (Rational, int)):
                self.data.append(Rational(other) if isinstance(other, int) else other)
            else:
                raise RationalValueError(self, other, "+=",
                                       "Можна додавати лише Rational, int або RationalList")
            return self
        except (ValueError, TypeError) as e:
            raise RationalValueError(self, other, "+=", str(e))

    def __str__(self):
        return str([str(item) for item in self.data])

    def __repr__(self):
        return f"RationalList({self.data})"

#########################################################

if __name__ == "__main__":
    try:
        rlist = RationalList([1, 2, "3/4", "abc"])
    except RationalValueError as e:
        print(e)  # Виведе детальну інформацію про помилку