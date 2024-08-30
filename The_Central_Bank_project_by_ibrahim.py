# Project

### The Central Bank contacted our technical team and asked it to develop a program suitable for all banks, with the addition of some advantages for certain banks
# Task 1 : 
#### task 1.1 Make Class(User) with attributes:
    # name 
    # age 
    # gender 
    # balance
#### task 1.2 Make method to show previous data 
class User:
    
    ## Attributes
    def __init__(self, name, age, gender, balance):
        self.name = name 
        self.age = age 
        self.gender = gender 
        self.__balance = balance
    
    def show_data(self):
        print(f"User \'{self.name}\' is \'{self.gender}\' has age of \'{self.age}\' and balance of \'{self.__balance}\'")
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        if type(new_balance) in [int, float] and new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Please enter postive numeric values only")
user_ahmed = User("Ahmed Ayman", 12, 'Male', 2000)
user_ahmed.get_balance()
user_ahmed.show_data()
# Task 2 : 
# Make Child Class(Bank) which inherite from Class(user) with Mehods:
    #### task 2.1 deposite : which take parameter(amount) and add it to balance and print new balance.  
    #### task 2.2 withdraw : which take parameter(amount) and check if user have enough money. 
    #### task 2.3 view balance : to show current balance. 

class Bank(User):
    
    ## Attributes
    def __init__(self, name, age, gender, balance):
        User.__init__(self, name, age, gender, balance) # create parent class
    
    ## Methods
    def deposit(self, amount):
#         self.balance = self.balance + amount 
        if type(amount) in [int, float] and amount >= 0:
            self.set_balance(self.get_balance() + amount)
        else:
            print("Please enter postive numeric values only")
    
    def withdraw(self, amount):
        
        if amount <= self.get_balance():
            self.balance = self.balance #amount
            self.set_balance(self.get_balance() amount)
        else:
            print(f"Not Enough Amount of Money ({amount}) in your account ({self.get_balance()})")
    
    def view_balance(self):
        print(f"Your Balance = {self.get_balance()}")
# Task 3 : 
# #### task 3.1 Make Child Class(CIB) which inherite from Class(Bank) with Mehods:
#       Loan application: which take parameter(amount) and  (Duration) >max loan is one million
# #### task 3.2 Make Child Class(QNB) which inherite from Class(Bank) with Mehods:
#       Loan application: which take parameter(amount) and  (Duration) >max loan is one 2 million
class CIB(Bank):
    
    ## Attributes
    def __init__(self, name, age, gender, balance):
        super().__init__(name, age, gender, balance)
        print("loan amounts is in million units and duration amounts is in years unit")
    
    def loan_application(self, loan_amount, duration):
        if loan_amount <= 1e6 and duration <= 1:
#             self.balance = self.balance + amount
            self.deposit(loan_amount)
        elif loan_amount 1e6:
            print("Maximum amount allowed for loan is 1 million")
        else:
            print("Maximum duration allowed for loan is 1 Year")
class QNB(Bank):
    
    ## Attributes
    def __init__(self, name, age, gender, balance):
        super().__init__(name, age, gender, balance)
        print("loan amounts is in million units and duration amounts is in years unit")
    
    def loan_application(self, loan_amount, duration):
        if loan_amount <= 2e6 and duration <= 2:
#             self.balance = self.balance + amount
            self.deposit(loan_amount)
        elif loan_amount 2e6:
            print("Maximum amount allowed for loan is 2 million")
        else:
            print("Maximum duration allowed for loan is 2 Year")
qnb_user = QNB('Ahmed Ayman', 24, "Male", 5000)
qnb_user.show_data()
qnb_user.view_balance()
qnb_user.withdraw(100)
qnb_user.view_balance()
qnb_user.deposit(5000)
qnb_user.view_balance()
qnb_user.loan_application(0.9e6, 0.5)
qnb_user.view_balance()
qnb_user.loan_application(0.1e6, 1)
qnb_user.view_balance()
qnb_user.loan_application(1.1e6, 1)
qnb_user.view_balance()
qnb_user.loan_application(2.1e6, 1)
qnb_user.view_balance()
qnb_user.loan_application(1.99e6, 1.5)
qnb_user.view_balance()
qnb_user.loan_application(1.99e6, 2.5)
qnb_user.view_balance()