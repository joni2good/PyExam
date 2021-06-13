import random


class ParentClass:

    classVar = 'This is the class var'

    def __init__(self, name, age):
        self.name = name
        self.calc_age(age)

    def speak(self):
        return f'I am the parent'

    def calc_age(self, i):
        self.age = 2 * i

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class ChildClassOne(ParentClass):
    def speak(self, *args):
        if len(args) != 0:
            return f'I am a {args[0]} {self.personal()} child'
        return f'I am a {self.personal()} child'

    def personal(self):
        return random.choice(['bratty', 'smart', 'spoiled', 'weird', 'pretty', 'dumb'])


class ChildClassTwo(ParentClass):

    def calc_age(self, i):
        self.age = 3 * i


parent = ParentClass('Jonas', 10)
childOne = ChildClassOne('George', 15)
childTwo = ChildClassTwo('Nick', 15)

print(parent.speak())
print(childOne.speak('not'))
print(parent.age)
print(childOne.age)
print(childTwo.age)

print(isinstance(parent, ParentClass))
print(isinstance(childOne, ParentClass))
print(parent.classVar)
print(childOne.classVar)
