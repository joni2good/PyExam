# Encapsulation, @Propeties


class Person:

    def __init__(self, name, nickname):
        self.__name = name
        self.__nickname = nickname
        test = 'test'

    @property
    def name(self):
        return self.__name

    @property
    def nickname(self):
        return self.__nickname

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @nickname.setter
    def nickname(self, nickname):
        self.__nickname = nickname

    # __________________________ metoder

    def who(self):
        print('name :', self.__name)
        print('nickname: ', self.__nickname)


p = Person("Nick", "Nicker")
p2 = Person("Jonas", "Lil lort")


p.who()
print(p.name)
