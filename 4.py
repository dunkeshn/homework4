# Изучить метод  __str__, создать класс с данным методом, продемонстрировать его выполнение

class StrMethod:
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f'''С помощью метода __str__ мы можем, к примеру, 
отобразить какие-либо атрибуты класса просто 
применив print() к экземпляру класса!
                
{self.message}'''

if __name__ == '__main__':
    m = input('Ввидет любое сообщение: ')
    a = StrMethod(m)
    print(a)
