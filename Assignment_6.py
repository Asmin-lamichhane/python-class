# # # '''
# # # Docstring for my_project.Assignment_6
# # # Task 1: The "Digital Wallet" (Basic Encapsulation)
# # # Goal: Practice using private variables to prevent unauthorized changes to a balance.
# # # The Problem:Create a class called Wallet.
# # # Private Attributes: ownerName (String) and balance (Double).
# # # The Logic:
# # # Constructor: Set the owner's name and start the balance at 0.
# # # deposit(amount): If the amount is greater than 0, add it to the balance.
# # # withdraw(amount): If the amount is less than or equal to the balance, subtract it. Otherwise, print: "Insufficient funds!"
# # # getBalance(): A getter method to see the current money.
# # # '''

# # # class Wallet:
# # #     def __init__(self,name):
# # #         self.__name=name
# # #         self.__balance = 0.0
# # #     def deposit(self,amount):
# # #         if amount>0:
# # #             self.__balance+=amount
# # #             return self.__balance
# # #     def withdraw(self,amount):
# # #         if amount<=self.__balance:
# # #             self.__balance-=amount
# # #             return self.__balance
# # #         else:
# # #             return "insuficient balance "
# # #     def getbalance(self):
# # #         return self.__balance
    
# # # wallet1=Wallet("asmin")

# # # wallet1.deposit(100)
# # # print(wallet1.getbalance())
# # # wallet1.withdraw(50)
# # # print(wallet1.getbalance())


# # '''
# # Docstring for my_project.Assignment_6
# # Task 2: The "Smart Light Bulb" (State Management)
# # Goal: Understand how methods change the "internal state" of an object without the user touching variables directly.
# # The Problem:Create a class called SmartBulb.
# # Private Attributes: brightness (Integer) and isOn (Boolean).
# # The Logic:
# # Constructor: The bulb should start "Off" (false) and brightness at 0.
# # turnOn(): Sets isOn to true and sets brightness to 100.
# # turnOff(): Sets isOn to false and sets brightness to 0.
# # dim(value): * If the bulb is Off, print: "Cannot dim a bulb that is off!"
# # If the bulb is On, decrease the brightness by the value, but don't let it go below 0.
# # getStatus(): Print whether the bulb is on/off and its current brightness level.
# # '''
# # class SmartBulb:
# #     def __init__(self):
# #         self.__brightness=0
# #         self.__isOn=False
# #     def turnOn(self):
# #         self.__isOn=True
# #         self.__brightness=100
# #     def turnOff(self):
# #         self.__brightness=0
# #         self.__isOn=False
# #     def dim(self,value):
# #         if self.__isOn==False:
# #             return "cannot dim a bulb that is off"
# #         if self.__isOn==True:
# #             self.__brightness-=value
# #             return self.__brightness
# #         if self.__brightness<0:
# #             self.__brightness=0
# #     def getStatus(self):
# #         status = "on " if self.__isOn ==True  else "off" 
# #         return f"ststus is {status} and brightnesslevel is {self.__brightness}"
# # bulb=SmartBulb()
# # print(bulb.getStatus())
# # bulb.turnOn()
# # print(bulb.getStatus())
# # bulb.dim(20)
# # print(bulb.getStatus())

# '''
# Docstring for my_project.Assignment_6
# Task 3: The "Car Fuel System" (Validation Logic)
# Goal: Practice using "Setters" to validate data before saving it to an object.
# The Problem:Create a class called Car.
# Private Attributes: modelName (String) and fuelLevel (Integer).
# The Logic:
# Constructor: Set the modelName and set fuelLevel to 50 (percent).
# drive(): Each time this is called, decrease fuelLevel by 10.
# If fuelLevel reaches 0, print: "Out of fuel! Cannot drive."
# refuel(amount):
# If amount + fuelLevel is more than 100, print: "Tank is overflowing! Setting fuel to 100%." and set it to 100.
# Otherwise, add the amount to the current fuel.
# displayFuel(): Show the remaining percentage of fuel.
# '''
# class Car:
#     def __init__(self,modelName):
#         self.__modelname=modelName
#         self.__fuellevel=50
#     def drive(self):
#         if self.__fuellevel==0:
#             return "out of fuel"
#         else:
#             self.__fuellevel-=10
#             if self.__fuellevel<0:
#                 self.__fuellevel=0
#             return self.__fuellevel
#     def refuel(self, amount):
        
#         if self.__fuellevel + amount > 100:
#             print("Tank is overflowing!")
#             self.__fuellevel = 100
#         else:
#             self.__fuellevel += amount

#     def displayFuel(self): 
#         return f"remaining fuel is {self.__fuellevel}"

# car1=Car("bmw")
# print(car1.displayFuel())
# print(car1.drive())
# print(car1.drive())
# print(car1.drive())

# car1.refuel(110)
# print(car1.displayFuel())


#task 4 
class TemperatureConverter:
    def __init__(self, value, unit):
        
        if unit == "celsius":
            self.celsius = value
        elif unit == "fahrenheit":
            self.celsius = (value - 32) * 5 / 9
        elif unit == "kelvin":
            self.celsius = value - 273.15
        else:
            print("Invalid unit")

    def convert(self, to_unit):
        if to_unit == "celsius":
            return self.celsius
        elif to_unit == "fahrenheit":
            return (self.celsius * 9 / 5) + 32
        elif to_unit == "kelvin":
            return self.celsius + 273.15
        else:
            print("Invalid conversion unit")

t1=TemperatureConverter(40,"celsius")
print(t1.convert("celsius"))
print(t1.convert("fahrenheit"))
print(t1.convert("kelvin"))

t2=TemperatureConverter(104,"fahrenheit")
print(t2.convert("celsius"))
print(t2.convert("kelvin"))

t3=TemperatureConverter(313.15,"kelvin")
print(t3.convert("celsius"))
print(t3.convert("fahrenheit"))