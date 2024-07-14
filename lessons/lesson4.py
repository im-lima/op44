# Дектораторы, множественное наследование, ветки в гите
# Инкапсуляция


class ABC:
    def __init__(self,a,b,c):
        self.a=a
        self._b=b
        self.__c=c
    def isB(self,a):
        self._setB(a)
        self._getsB()
    def _getsB(self):
        print(self._b)
    def _setB(self,b):
        self._b=b
    def __str__(self):
        return self._b
a=ABC('a','_b',"__c")
a.isB('великий')
print(a)
# a._b='newB'
# print(a._b)
#
#
# print(dir(a))
# a.__c='ложный си'
# a._ABC__c='истинный си'
# print(a.__c)
# print(a)
# print(a)