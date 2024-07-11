class Bank:
    def __init__(self, name, pin, money):
        self.name = name
        self._pin = pin
        self.__money = money

    def __str__(self):
        return f'{self.name}:{self.__money}'

    def setpin(self, pin):
        self._pin = pin

    def getpin(self):
        print(self._pin)

    # @property
    # def money(self):


beka = Bank('beka', '2525', 10_000)

print(beka)
# beka.printpin()
# beka._pin = 1111
#
# beka.name = 'калыс'
# beka.__money = 10_000_000
# beka.fullname='бекболот'
#
# beka.printpin()

beka.setpin(4343)
beka.getpin()

beka.setmoney(5000)
print(beka)
# print(beka)
print(dir(beka))
# print(dir(o))