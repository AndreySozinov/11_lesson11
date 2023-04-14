# Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyString(str):
    """String class containing author's name & create time in sec"""

    def __new__(cls, value: str, author_name: str):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.create_time = time.time()

    def __str__(self):
        return f'{self}; author name = {self.author_name}; create time = {self.create_time}'

    def __repr__(self):
        return f'MyString({self.author_name}, {self.create_time}'
