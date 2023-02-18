# Полиморфизм --- выполнять один и тот же код по разному,
# при утиной типизации не важен класс наследования, важно действие,
#которое делает объект

class Animal:
    def make_noise(self):
        print('shh')

class Cat(Animal):
    def make_noise(self):
        print("meow")

class Dogs(Animal):
    def make_noise(self):
        print('gav-gav')


class Duck(Animal):
    def make_noise(self):
        print('crya-crya')


def noise(animal: Animal):
    animal.make_noise()


if __name__ == '__main__':
   noise(Duck())
