# виртуальное окружение,модули библиотеки фреймворки
import random,time,sqlite3
# 1 вид встроенные\внутренний модули

import math
# print(math.pi)

from math import e,pi,sin,sqrt
# print(e)



# собвственные модули

from lesson4_2 import Remanga
import colorama
print(colorama.Back.LIGHTYELLOW_EX,colorama.Fore.RED)

n=Remanga('огненный кулак')
n.manga_upp()


# venv
# внешние модули

import colorama
print('привет')