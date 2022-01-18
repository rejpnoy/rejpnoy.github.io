#TIP:  what return self is doing?
# return self = referance the actualy instance of the method .. self = john/guido
# PRESET PERAMATER of the user class and basically gets an update of the changes

# instances the methods or the variables connected to the class
# the variables are connected to the class
# the class and the class has attributes there are the methods relate to the class

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0
    #adding the deposit method
    def make_deposit(self, amount): # takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self
        #self.account_balance = self.account balance + amount
#want to use the user functions methods .. need to make a withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount # -= operator actually turns account_balance to a varable and short hands for
        #self.account_balance = self.account balance - amount
        return self
#display_user_balance  - have this method print the user's name and account balance to the terminal
#want to run this function withhout manually putting account balance
    def display_user_balance(self):
        print(f"{self.name} has $ {self.account_balance} in their account.")
        return self
#print f the idea is called string interpulation every modern string so you can put varibales ito your strings
#so you can define what you want to look like in values.

#without "print(f" it will print out no value .. it will print out
#"{self.name} has {self.account_balance} in their account."



# BONUS : transfer_money(self,other_user,amount) - have this method decrease the user's
#balance  by the amount and add that amount to other other_user's balance
#    def transfer_money(self, other_user,amount):
#        self.other_user = 0
#        self.account_balance -= amount
#        self.other_user += amount
#
#        print(f"{self.name} will be transferring {self.other_user}")
#        print(f"{self.name} now has {self.account_balance} remaining in account")
#        print(f"Other Bank now has {self.other_user} remaining in account")

#otherversion code

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount) # you can make and call the functions
        other_user.make_deposit(amount)
        return self


john  = User("John", "email@fake.com")
guido = User("Guido", "test@gmail.com")

print(john)

john.make_deposit(100).make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance().transfer_money(guido,5)
# john.display_user_balance()
# #john.make_withdrawal(6)
# #john.display_user_balance()
# john.transfer_money(guido,5)
# john.display_user_balance()
guido.display_user_balance()
