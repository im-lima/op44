class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False

    def nameprint(self):
        print('Имя героя:', self.name)

    def умножить_здоровье_на_2(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}, Летает: {self.fly}"

    def __len__(self):
        return len(self.catchphrase)

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.air_property = "Air-based"

    def умножить_здоровье_на_2(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.earth_property = "Earth-based"

    def умножить_здоровье_на_2(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, target):
        if hasattr(target, 'damage'):
            target.damage **= 2


harley_quinn = AirHero('Harleen Frances Quinzel', 'Harley Quinn', 'immunity to poisons', 100, 'My love scares you, but no gun?', 50)
batman = EarthHero('Bruce Wayne', 'Batman', 'intellect', 200, 'I am Batman!', 30)


harley_quinn.nameprint()
harley_quinn.умножить_здоровье_на_2()
print(harley_quinn)
harley_quinn.true_phrase()

batman.nameprint()
batman.умножить_здоровье_на_2()
print(batman)
batman.true_phrase()


joker = Villain('Unknown', 'Joker', 'chaos', 150, 'Why so serious?', 40)


joker.crit(harley_quinn)
print("Урон Harley Quinn после применения метода crit:", harley_quinn.damage)