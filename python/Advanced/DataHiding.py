class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# create an object of BankAccount class
my_account = BankAccount(1000)

# call public method to access private variable
print(my_account.get_balance())

# try to change private variable directly (this will not work)
my_account.__balance = 2000
print("Access private variable: ",my_account.get_balance(),"not changed")   # output: 1000

# call public method to change private variable
my_account.deposit(5000)
print(my_account.get_balance())   # output: 2000
