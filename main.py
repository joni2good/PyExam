class Customer:
    def __init__(self, name='null'):
        self.name = name


class Account:
    def __init__(self, acc_num=0, customer=Customer()):
        self.acc_num = acc_num
        self.customer = customer


class Bank:
    def __init__(self, name='Static bank name', accList=[Account()]):
        self.name = name
        self.accList = accList

    def getAcc(self):
        toRet = ()
        for acc in self.accList:
            toRet += (acc.acc_num, acc.customer.name)
        return toRet


cus1 = Customer('Jens')
cus2 = Customer('Hans')
cus3 = Customer('Bent')
acc1 = Account(123, cus1)
acc2 = Account(456, cus2)
acc3 = Account(789, cus3)
acc_list = [acc1, acc2, acc3]
bank = Bank('Bank of denmark', acc_list)

print('Name: ' + bank.name + ' Accounts: ' + str(bank.getAcc()))
acc4 = Account(147, cus3)
bank.accList.append(acc4)
print('Name: ' + bank.name + ' Accounts: ' + str(bank.getAcc()))
