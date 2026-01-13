# # # #Duck typing
# # # class Dog:
# # #     def speak(self):
# # #         return "hau hau"
# # # class Cat:
# # #     def speak(self):
# # #         return "mew mew"
# # # dog=Dog()
# # # cat=Cat()
# # # for animal in (dog,cat):
# # #     print(animal.speak())



# # # # #monkey patching


# # # ##type of method


# # #abstract

# # from abc import ABC,abstractmethod

# # class Shape(ABC):
# #     @abstractmethod
# #     def Area(self):
# #         pass
# # class Circle(Shape):
    
# #     def Area(self,radius):
# #         return 3.14*radius*radius

# # print(Circle().Area(10))

# from abc import ABC,abstractmethod
# # class coffieemachin(ABC):
# #     @abstractmethod
# #     def make_coffiee(self):
# #         pass

# # class latteMAchin(coffieemachin):
# #     def make_coffiee(self):
        
# #         return "make lattee"
# # class mochaMAchin(coffieemachin):
# #     def make_coffiee(self):
# #         return "make mocha"
    

    
# # print(latteMAchin().make_coffiee())
# # print(mochaMAchin().make_coffiee())

# class calc:
#     @abstractmethod
#     def _Add(self):
#         pass 

