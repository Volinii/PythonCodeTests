class Cat:
    def __init__(self):
        print('cat')

    def say(self):
        print('I\'m a cat!')


class Dog:
    def __init__(self):
        print('dog')

    def say(self):
        print('dog,dog!')


class Animal:
    @staticmethod
    def set_animal(animal_name):
        animal_list = dict(dog=Dog, cat=Cat)
        print(animal_list)
        return animal_list[animal_name]

cat = Animal.set_animal('cat')
cat_test = cat()
cat_test.say()
a = [x for x in dir(cat_test) if '__' not in x]
b = a[0]
c = eval('cat_test.' + b)

print(b)
print(a)
c()