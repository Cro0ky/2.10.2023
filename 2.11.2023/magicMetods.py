# class Point:
#     def __new__(cls, *args, **kwargs):
#         print(f'Метод __new__ для класса {str(cls)}')
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print(f'Метод __init__ для класса {str(self)}')
#         self.x = x
#         self.y = y
#
#
# p = Point(1, 5)

# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def __del__(self):
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f'соединение с БД с настройками: user = {self.user}\npassword = {self.psw}\nport = {self.port}')
#
#     def close(self):
#         print(f'Соединение разорвано')
#
#     def read(self):
#         print('Чтение данных')
#
#     def write(self, data):
#         print(f"Запись данных: {data}")
#
#
# d1 = DataBase('user1', 'psw1', 3000)
# d1.connect()
# d2 = DataBase('user1', 'psw1', 3000)
# d2.connect()

class Test:
    def __repr__(self):
        return 'REPR'

    def __str__(self):
        return 'str'

    def __bool__(self):
        return True


print(Test())
t = Test()
print(str(1231))
test = Test()
if test:
    print('adadasdasd')


