# Изучить что такое множественное наследование и миксины,
# привести пример использования данных концепций ООП

# Миксины представляют собой классы, которые содержат методы для использования другими классами,
# но не предназначены для самостоятельного использования.
# Методы, определённые в миксине, можно использовать в любом классе, который наследуется от миксина.

# Можно немного переделать программу из 5 задания, чтобы продемонстрировать концепцию миксинов

class Mixin:
    def print_info(self):
        print(f'Имя: {self.name}, должность: {self.position}, зарплата: {self.salary}')
    # Метод класса Mixin наследуется всеми остальными классами, но сам класс не может использовать
    # свой метод сам по себе

class Employee(Mixin): # Наследуем класс-миксигн
    position = None
    salary = 0
    def __init__(self, name: str) -> None:
        self.name = name

    def get_paid(self) -> None:
        self.salary = 0

class Manager(Employee):
    position = 'Управляющий'

    def get_paid(self) -> None:
        self.salary = 100000

class Worker(Employee):
    position = 'Рабочий'

    def get_paid(self) -> None:
        self.salary = 50000

if __name__ == '__main__':
    manager = Manager('Алексей')
    manager.get_paid()
    manager.print_info()
    worker = Worker('Иван')
    worker.get_paid()
    worker.print_info()

