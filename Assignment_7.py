# #abstrace using encapsulation

# from abc import ABC, abstractmethod

# class Wallet(ABC):

#     def __init__(self, balance=0):
#         self._balance = balance 

#     @abstractmethod
#     def deposit(self, amount):
#         pass

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

# class MyWallet(Wallet):

#     def deposit(self, amount):
#         self._balance += amount
#         return f"Deposited {amount}"

#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#             return f"Withdrawn {amount}"
#         else:
#             return "Insufficient balance"


# amt=MyWallet()
# print(amt._balance)
# print(amt.deposit(1000))
# print(amt._balance)
# print(amt.withdraw(1200))
# print(amt._balance)
# print(amt.withdraw(100))
# print(amt._balance)


# class Coffieemachin:
#     def __init__(self):
#         self.water_level=100

# def makecoffiee(self):
#     self._heatwater()
#     self._griend_bean()
#     self._brew()
# def _heatwater(self):
#     print("heat water to 90 ")

class Login_system:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def username(self):
        return self.username
    def password(self):
        return self.password
    
    
    def check(self):
        if