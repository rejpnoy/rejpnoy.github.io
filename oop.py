class User:
    def __init__(self, user, email="placeholder@gmail.com", password="12345pass") -> None:
        self.username = user
        self.passs = password
        self.emailadd = email

    #methods
    def say_hi(self, person):
        print(f"hi {person} my name is {self.username}")

    def changepass(self, pass_secure):
        print(f"hi {pass_secure} my name is {pass_secure.username}")
happy = User("John", "john@gmail.com", "123password123")
mad = User("Mary")

happy.say_hi("Mary")

happy.changepass(mad)



