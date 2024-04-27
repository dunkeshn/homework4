# Создать класс калькулятор и описать в нём методы
# для базовых математических операций для двух чисел

class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        print(f'Операции над числами {a} и {b}\n')

    def addition(self) -> None:
        print(f'Сложение: {self.a + self.b}')
    def difference(self) -> None:
        print(f'Вычитание: {self.a - self.b}')
    def division(self) -> None:
        if b == 0:
            print('Деление: деление на 0 невозможно!')
        else:
            print(f'Деление: {self.a / self.b}')
    def multiplication(self) -> None:
        print(f'Умножение: {self.a * self.b}')

if __name__ == '__main__':
    print('Введите 2 числа:')
    a = int(input())
    b = int(input())
    two_nums = Calculator(a, b)
    two_nums.addition()
    two_nums.difference()
    two_nums.division()
    two_nums.multiplication()
