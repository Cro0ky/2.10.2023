class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не опредедено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'


class Printer(Equipment):
    def __init__(self, name, make, year, seria):
        super().__init__(name, make, year)
        self.seria = seria

    def action(self):
        return 'Печатает'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}, {self.seria}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Ксеракопирует'


eq = Equipment('Name', 'Make 1231', 2023)
printer1 = Printer('printer', 'model1', 2021, 123123)
print(eq.__str__())
print(printer1.__str__())

xerox1 = Xerox('Xerox', 'Model2', 2019)
print(xerox1.__str__())

scaner = Scaner('Scaner', 'Model3', 2018)
print(scaner.__str__())

sklad = []
sklad.append(scaner)
sklad.append(xerox1)
sklad.append(printer1)


def info(sklad):
    print('\nНа скале имеется')
    for i in sklad:
        print(f'- {i}')
        print(i.action())


info(sklad)


def filter(sklad, obj):
    print("\nФильтрация по классам:")
    for i in sklad:
        if isinstance(i, obj):
            print(i)


filter(sklad, Printer)


def remove(sklad, obj):
    print("\nФильтрация по классам:")
    for i in sklad:
        if isinstance(i, obj):
            sklad.remove(i)


remove(sklad, Printer)
info(sklad)
