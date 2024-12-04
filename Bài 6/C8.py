class Bank:
    Account_type = "Savings"
    location = "Guntur"
    def __init__(self, name, Account_Number,balance):
        self.name = name
        self.Account_Number = Account_Number
        self.Account_type=Bank.Account_type
        self.location=Bank.location

    def __repr__(self):
        print ("welcome to the SBI ATM Machine ")
        print("--------------------------------")
        account_pin = int(input("please enter your pin number "))
        if(account_pin==123):
            Account(self)
        else:
            print("Pin Incorrect. Please try again")
            Error(self)
        return ' '.join([self.name,self.Account_Number])
def Error(self):


    account_pin = int(input("please enter your pin number "))
    if(account_pin==123):
        Account(self)
    else:
        print("Pin Incorrect. Please try again")
        Error(self)
def Account(self):
    print ("your Card Number is : XXXX XXXX XXXX 1357")
    print ("would you like to deposit/withdraw/Check balance")
    print("""
1)         Balance
2)         Withdraw
3)         Deposit
4)         quit
""")
    option=int(input("Plese enter your choise:"))
    if(option==1):
        Balance(self)
    elif(option==2):
        Withdraw(self)
    elif(option==3):
        Deposit(self)
    elif(option==4):
        Exit()
def Balance(self):
    print("balance:",self.balance)
    Account(self)
def Withdraw(self):
    w=int(input("please enter desired amount: "))
    if(self.balance>0 and self.balance>=w):
        self.balance=self.balance-w
        print("your transaction is successfull")
        print("your Balance:",self.balance)
        print("")
    else:
        print("your transaction is cancelled due to")
        print("Amount í not sufficient in your account")
    Account(self)
def Deposit(self):
    d=int(input("Please enter desired amount: "))
    self.balance=self.balance+d
    print("your transaction is successfull")
    print("Balance:",self.balance)
    Account(self)
def Exit():
    print ("Exit")
t1 = Bank('mahesh', 1453210145,5000)

print (t1)
    
    
    
