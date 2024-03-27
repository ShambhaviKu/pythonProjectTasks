
class custom_balanceCheck(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

amount = 100
withraw_amt = int(input("Enter amount: "))

if withraw_amt > amount:
    raise custom_balanceCheck('insufficiant balance')
else:
    print("balance =", amount-withraw_amt)
