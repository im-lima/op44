# классы - git
# ООП -обьектно ориентированное программирование ОБЬЕКТЫ
p=1,True,'10',1.1,{},[],(),None
p1=1,1,'ertyu'
print(type(p1))

l='etyu'
# print(l.)
def a(name):
    print('привет', name)

a('бека')

# 1
class Person:
    # магический метод
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # метод -функция деф
    def __str__(self):
        return f'{self.name} {self.age}'

    def __len__(self):
        return len(self.name)
    def nameprint(self):
        print('мое имя:', self.name)

#обьект\экземпляр
beka=Person('beka',21)
beka2=Person('бека',99)
print(beka)
print(len(beka))
beka.nameprint()
beka2.nameprint()

