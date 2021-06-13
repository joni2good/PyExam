class Bank:
    def __init__(self):
        self.accounts = []

    def __str__(self):
        ret = ''
        for acc in self.accounts:
            ret += f'{str(acc)}\n'
        return f'Accounts:\n {ret}'

    def __repr__(self):
        return f'{self.__dict__}'

    def __len__(self):
        return len(self.accounts)

    def __getitem__(self, item):  # we can now call Bank[item] and use for loops
        return self.accounts[item]


class Account:
    def __init__(self, accNo, amount, cust):
        self.accNo = accNo
        self.amount = amount
        self.cust = cust

    def __str__(self):
        return f'Account number: {self.accNo}, Amount: {self.amount}, {self.cust}'

    def __repr__(self):
        return f'{self.__dict__}'


class Customer:
    def __init__(self, name, age):
        # self.name = name
        # self.age = age
        self.customer_dict = {'name': name, 'age': age}

    def __str__(self):
        return f'Customer name: {self.customer_dict.get("name")}, Age: {self.customer_dict.get("age")}'

    def __repr__(self):
        return f'{self.__dict__}'


c1 = Customer('Nick', 27)
c2 = Customer('Mads', 24)
c3 = Customer('Jonas', 25)

a1 = Account(1, 100, c1)
a2 = Account(2, 150, c2)
a3 = Account(3, 2000, c3)

b = Bank()
if '__len__' in dir(b):
    print(True)
else:
    print(False)

b.accounts.append(a1)
print(b[0])
b.accounts.append(a2)
b.accounts.append(a3)

for a in b:
    print(a)

print(c1)
print(repr(c1))

print(a1)
print(repr(a1))

print(b)
print(repr(b))

