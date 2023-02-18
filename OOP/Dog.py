# Инкапсуляция -сбор в одном классе данных и методов работы с ними
# '_' (protected)
# '__' вначале переменной -(private)


class Dog:
    def __init__(self, _name, age):
        self._name = _name
        self._age = age


    # def set__age(self, age):
    #     self.__age = age

    def get_age(self):
        return self._age


    def speak(self):
        print(f'{self._name} says: Gavv')

    def __add__(self, other):
        if isinstance(other, Dog):  # уточняем является ли другой обьект собакой - принцип наследования
            return Dog('Whelp', 0)



if __name__ == '__main__':
    kip = Dog('Kip', 2)
    lily = Dog('Lily', 1)
    print(kip)
    print(lily)
    kip.speak()
    lily.speak()
    print(kip._name)
    print(kip._age)
    print(lily._name)
    print(lily._age)
    whelp = kip + lily
    whelp.speak()
