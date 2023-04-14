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

    def __eq__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        result = [[0] * len(self.data[0]) for i in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)

    # def __mul__(self, other):
    #     if len(self.data[0]) != len(other.data):
    #         return -1
    #     result = [[0] * len(other.data[0]) for i in range(len(self.data))]
    #     for i in range(len(self.data)):
    #         k = 0
    #         for j in range(other.data):
    #             k += self.data[i][j] * other.data[j][i]
    #         result[i][]


if __name__ == '__main__':
    m = Matrix([[2, 3, 4, 5], [5, 6, 7, 8], [10, 11, 12, 14]])
    print(m)
    n = Matrix([[2, 3, 6, 3], [5, 6, 7, 6], [10, 11, 12, 10]])
    print(n)
    print(m == n)
    print(m + n)
