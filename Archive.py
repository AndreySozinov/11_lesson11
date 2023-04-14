# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков- архивов
# 📌 list-архивы также являются свойствами экземпляра
class Archive:
    """Contain number & string. Saving them in lists while create new Archive."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_numbers = []
            cls._instance.list_strings = []
        else:
            cls._instance.list_numbers.append(cls._instance.arch_number)
            cls._instance.list_strings.append(cls._instance.arch_string)
        return cls._instance

    def __init__(self, arch_number: int | float, arch_string: str):
        self.arch_number = arch_number
        self.arch_string = arch_string

    def __str__(self):
        return f'number = {self.arch_number} string = {self.arch_string}'

    def __repr__(self):
        return f'Archive({self.arch_number}, {self.arch_string}\n' \
               f'{self._instance.list_numbers}\n{self._instance.list_strings}'
