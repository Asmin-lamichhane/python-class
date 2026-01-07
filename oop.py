# # class Phone:
# #     def __init__(self,brand):
# #         self.brand=brand

# # class smartphone(Phone):
# #     def __init__(self, brand,memory):
# #         super().__init__(brand)
# #         self.memory=memory
# #     def photo(self):
# #         return "take photo"
    
# # p1=smartphone("samsung",4)
# # print(p1.photo())

# #multiple inheritance

# class Employee:
#     def __init__(self,name):
#         self.name=name

# class Salary:
#     def __init__(self,salary):
#         self.salary=salary
# class Payroll(Employee,Salary):
#     def __init__(self, name,salary):
#         Employee.__init__(self,name)
#         Salary.__init__(self,salary)
    
#     def get_salary(self):
#         return self.name
# emp1=Payroll("asmin",478888888)
# print(emp1.get_salary())
# print(emp1.name,emp1.salary)


class Employee:
    def __init__(self,name):
        self.name=name
class Functional_desiganation:
    def __init__(self,type):
        self.type=type
class Department:
    def __init__(self,department_name):
        self.department_name=department_name
class Internship(Employee,Functional_desiganation,Department):
    def __init__(self, name,type,department_name,intern_duration):
        Employee.__init__(self,name)
        Functional_desiganation.__init__(self,type)
        Department.__init__(self,department_name)
        self.intern_duration=intern_duration
       

i1  = Internship("Amit Sharma", "Software Intern", "IT", 3)
i2  = Internship("Rohan Gupta", "Web Developer Intern", "Web Development", 3)
i3  = Internship("Anjali Thapa", "UI/UX Intern", "Design", 4)
i4  = Internship("Rita Pandey", "QA Intern", "Quality Assurance", 3)
i5  = Internship("Suman Adhikari", "Software Intern", "IT", 4)
i6  = Internship("Kiran Shrestha", "Web Developer Intern", "Web Development", 4)
i7  = Internship("Mina Gurung", "UI/UX Intern", "Design", 3)
i8  = Internship("Komal Shah", "QA Intern", "Quality Assurance", 4)
i9  = Internship("Neha Singh", "Software Intern", "IT", 3)
i10 = Internship("Prakash Joshi", "Web Developer Intern", "Web Development", 3)
i11 = Internship("Pooja Rawat", "UI/UX Intern", "Design", 4)
i12 = Internship("Arjun Mehta", "QA Intern", "Quality Assurance", 3)
i13 = Internship("Bikash Rai", "Software Intern", "IT", 4)
i14 = Internship("Vivek Mishra", "Web Developer Intern", "Web Development", 4)
i15 = Internship("Nisha KC", "UI/UX Intern", "Design", 3)
i16 = Internship("Deepak Yadav", "QA Intern", "Quality Assurance", 4)
i17 = Internship("Sunita Lama", "Software Intern", "IT", 3)
i18 = Internship("Rahul Verma", "Web Developer Intern", "Web Development", 3)
i19 = Internship("Neha Karki", "UI/UX Intern", "Design", 4)
i20 = Internship("Sita Sharma", "QA Intern", "Quality Assurance", 3)


internship_list = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10,
                   i11, i12, i13, i14, i15, i16, i17, i18, i19, i20]







#method resolution order
#poli
