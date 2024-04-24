# Изучить что такое множественное наследование и миксины,
# привести пример использования данных концепций ООП

# Python поддерживает множественное наследование,
# то есть один класс может наследовать свойства и методы сразу от нескольких классов-родителей.

class A:
    def method_A(self):
        print('Этот метод находится в классе A!')


class B:
    def method_B(self):
        print('Этот метод находится в классе B!')

class C(A, B): # Класс C наследуюет методы и атрибуты сразу двух других классов
    pass

if __name__ == '__main__':
    c = C()
    c.method_A()
    c.method_B()