class BankAccount:

    def __init__(self):
        self.Balance = 0
        self.__privateVar = 100

    def deposit(self, amount):
        self.Balance += amount

    def _withdraw(self, amount):
        self.Balance -= amount

    def __total_bal(self):
        print("my balance is:", self.Balance)

    def publiq_var(self):
        print("my private var:", self.__privateVar)

    def account_auth(self, flag):
        if flag:
            print(self.Balance)
        else:
            print("Invalid user")

    def managerApproval(self, amount):
        self._withdraw(amount=amount)


raj = BankAccount()
raj.deposit(500)

raj.account_auth(True)

raj.managerApproval(10)
print(raj.Balance)
raj.publiq_var()
