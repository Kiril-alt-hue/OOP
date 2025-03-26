class ProtectedDictInt(dict):
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ValueError("Ключ має бути цілого типу")

        if key in self:
            raise ValueError("Такий ключ вже є у словнику")

        super().__setitem__(key, value)  # Викликаємо __setitem__ батьківського класу (dict)


if __name__ == '__main__':
    p = ProtectedDictInt()
    p[4] = "Hello"
    print(p)  # {4: 'Hello'}

    try:
        p[4] = "World"  # Виключення: ValueError: Такий ключ вже є у словнику
    except ValueError as e:
        print(e)

    try:
        p["Hello"] = "World"  # Виключення: ValueError: Ключ має бути цілого типу
    except ValueError as e:
        print(e)