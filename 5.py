# Создать базовый класс сотрудник и два дочерних класса – менеджер и работник.
# В базовый класс добавить get_paid(),
# который в дальнейшем переопределить в дочерних,
# чтобы сотрудники разных должностей получали различную зарплату

class Employee:
    position = None
    salary = 0
    def __init__(self, name: str) -> None:
        self.name = name

    def get_paid(self) -> None:
        self.salary = 0

    def __str__(self) -> None:
        return f'Имя: {self.name}, должность: {self.position}, зарплата: {self.salary}'

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
    print(manager)
    worker = Worker('Иван')
    worker.get_paid()
    print(worker)


