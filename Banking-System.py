#Parent Class is User
#Should Hold details about the User
#Has a function to show user details


#Child Class: Bank
#Stores Details about the account balance
#Stores details about the amount
#Allows for deposits, withdrawals, view_balance

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        print('Details: ')
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        print('Your Account Balance is:  $',self.balance)
    def withdrawal(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficent Funds. Your Balance is: ', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('Withdrawal Successful. Your new balance is:  $', self.balance)
    def view_balance(self):
        self.user_details()
        print('Your Account Balance is:  $',self.balance)
    





Dabby = Bank('Dabby', 22, 'Male')
Dabby.deposit(500)
Dabby.view_balance()