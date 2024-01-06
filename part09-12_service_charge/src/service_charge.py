# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self,name: str, acc: str, balance: float):
        self.__name = name
        self.__acc = acc
        self.__balance = balance

    def deposit(self,amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self,amount: float):
        self.__balance -= amount
        self.__service_charge()

    def __service_charge(self):
        self.__balance -= (1/100)*self.__balance

    @property
    def balance(self):
        return self.__balance

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
