class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Нужно число!')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{h} : {m} : {s}'

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Неверный формат')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Не тот тип')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise AttributeError('Можно складывать только целые числа')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise AttributeError('Можно складывать только целые числа')

        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc
        self.seconds = self.seconds % self.__DAY

        return self


c1 = Clock(3548)
print(c1.get_time())
c2 = Clock(3548)

c3 = Clock(800)

c1 = c1 + c2 + c3
print(c1.get_time())

# print(c1 < c2)
# c1 = c1.__add__(500)
