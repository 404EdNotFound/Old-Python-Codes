class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
    
    def deposit(self):
        money = int(input("How much money do you want to add: "))
        self.balance += money
        return f"Your balance is: {self.balance}" #Foo bar
    
    def withdraw(self):
        money = int(input("How much money do you want to withdraw: "))
        if money > self.balance: #Bonus solution
            print("Insufficient")
        
        else:
            self.balance -= money
        return f"Your balance is: {self.balance}"
    
    def get_balance(self):
        return f"Your balance is: {self.balance}"
    
class SavingsAccount:
    def __init__(self, interest_rate, interest, balance):
        self.interest_rate = interest_rate
        self.interest = interest
        self.balance = balance
    def setInterest(self):
        self.interest = self.balance * self.interest_rate
        return f"The interest based on the interest rate is: {self.interest}"
        
    def addInterest(self):
        self.balance += self.interest
        return f"Your Balance with the added interest rate is: {self.balance}"
    
account_number = ""
balance = 0.0
account_holder = ""
interest_rate = 0.0
interest = 0

account_number = input("Enter your account number: ")
balance = float(input("Input your balance: "))
account_holder = input("What is the name of this account: ")
interest_rate = float(input("Enter the interest rate as a decimal: "))

bank = BankAccount(account_number, balance, account_holder)
i = SavingsAccount(interest_rate, interest, balance)
bank.deposit()
bank.withdraw()
print(bank.get_balance())
print(i.setInterest())
print(i.addInterest())

#Alternate Solution
class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} into account {self.account_number}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} from account {self.account_number}. New balance: {self.balance:.2f}")

    def get_balance(self):
        return self.balance

# Create an instance of the BankAccount class and test its methods
print("\n")
print("Different Account with an instance")
account = BankAccount("123456789", 1000.0, "Alice")
account.deposit(500.0)
account.withdraw(200.0)
print(f"Current balance: {account.get_balance():.2f}")