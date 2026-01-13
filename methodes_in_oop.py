# # #class method
# # #static method(freee method inside the class )
# # #instance method
# # class Student:
# #     school_name="abc"

# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age

# #     #use class method
# #     @classmethod
# #     def change_school_name(cls,New_name):
# #         cls.school_name=New_name
    
# # #     #use staticmethod 
# # #     @staticmethod
# # #     def percentage_check(percentage):
# # #         if percentage>=50:
# # #             return "pass"
# # #         else:
# # #             return "fail"
        
# # # first_std=Student("asmin",23)

# # # print(first_std.percentage_check(40))

# # print(Student.school_name)
# # Student.change_school_name("xyz")
# # print(Student.school_name)


# class Vehical:
    
#     model="xyzzzz"
#     def __init__(self,drives):
#         self.drives=drives

#     @classmethod
#     def change_model(cls,new_model):
#         cls.model=new_model

#     @staticmethod
#     def check_speed(speed):
#         if speed>=60:
#             return "high speed"
#         else:
#             return "mormal speed"
    
#     def drive(self):
        
#         return self.drives
    
# print(Vehical.model)
# Vehical.change_model("12548")
# print(Vehical.model)

# print(Vehical.check_speed(50))
# v=Vehical("driving...")
# print(v.drive())

        
#make private repo and try to clone from https 