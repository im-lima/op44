# Инкапсуляция
# 1 публичный, 2 _защищенный,3 __скрытый


# супер класс\родительский класс
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def go(self):
        print(self.a, self.b)


a = A('a', 'b')


# дочерний класс
class B(A):
    def __str__(self):
        return f'a:{self.a} b:{self.b}'

    def go(self):
        print('метод класса B')
        super().go()


b = B('a', 'b')


# b.go()
# print(b)
# print(a)


class Bank:
    def __init__(self, name, pin, money):
        self.name = name
        self._pin = pin
        self.__money = money

    def __str__(self):
        return f'{self.name}:{self.__money}'


    def setpin(self,pin):
        self._pin = pin
    def getpin(self):
        print(self._pin)

    @property
    # getter
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money
    @money.deleter
    def money(self):
        del self.__money


beka = Bank('beka', '2525', 10_000)

print(beka)
beka.setpin(12432)
beka.getpin()
beka._pin=4444
beka.getpin()


# beka.setmoney(20000)
beka._Bank__money=0
print(beka)
beka.money=10000
print(beka.money)
del beka.money
beka.money=1
print(beka)
# print(dir(beka))