# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# 📌 Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
class Matrix:
    """Matrix class contains 2D list of list. Can print, equals, adding."""
    def __init__(self, data: [[int | float]]):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            for el in row:
                result = f'{result} {el:>5}'
            result = f'{result}\n'
        return result

    def __repr__(self):
        result = ''
        for row in self.data:
            for el in row:
                result = f'{result} {el:>5}'
        return f'Matrix({result})'

    def __eq__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        result = [[0] * len(self.data[0]) for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data) and len(other.data[0]) != len(self.data):
            return -1
        if len(other.data[0]) != len(self.data):
            a, b = other, self
        else:
            a, b = self, other
        result = [[0] * len(b.data[0]) for _ in range(len(a.data))]
        for i in range(len(a.data)):
            for j in range(len(b.data[0])):
                summa = 0
                for k in range(len(a.data[0])):
                    summa += a.data[i][k] * b.data[k][j]
                result[i][j] = summa
        return Matrix(result)


if __name__ == '__main__':
    m = Matrix([[2, 3, 4, 5], [5, 6, 7, 8], [10, 11, 12, 14]])
    print(m)
    n = Matrix([[2, 3, 6, 3], [5, 6, 7, 6], [10, 11, 12, 10]])
    print(n)
    print(m == n)
    print(m + n)
    p = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(m * p)
