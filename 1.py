# Создать класс для геометрической фигуры на выбор и добавить
# в него два метода – первый для расчета площади, второй для расчета периметра

class Rectangle:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def get_square(self) -> int:
        return self.a * self.b

    def get_perimeter(self) -> int:
        return 2 * self.a + 2 * self.b

    def __str__(self):
        return f'Площадь фигуры: {self.get_square()}\nПериметр фигуры: {self.get_perimeter()}'

if __name__ == '__main__':
    figure = Rectangle(1080, 1920)
    print(figure)

