# Создать класс “Человек” с полями: имя, город проживания и год рождения.
# Написать метод, который будет возвращать возраст человека в годах

from datetime import datetime

class Human:
    def __init__(self, name: str, city: str, year_of_birth: int) -> None:
        self.name = name
        self.city = city
        self.year_of_birth = year_of_birth

    def get_age(self) -> int:
        return int(datetime.now().year) - self.year_of_birth

    def __str__(self) -> str:
        return f'{self.name}, город {self.city}, {self.get_age()} лет'

if __name__ == '__main__':
    ivan = Human('Иван', 'Нефтекамск', 2004)
    print(ivan)
