# # #task 1

# # def palindrome(s):
    
# #     if len(s) <= 1:         
# #         return True
# #     if s[0] != s[-1]:        
# #         return False
    
# #     return palindrome(s[1:-1])
# # print(palindrome("racecar"))
# # print(palindrome("level"))

# # #task 2

# # def sum_of_digits(n):
# #     if n < 10:
# #         return n
    
# #     return (n % 10) + sum_of_digits(n // 10)


# # number = int(input("Enter a number: "))
# # result = sum_of_digits(number)
# # print("Sum of digits:", result)


# #next leap year

# def leap(year):
#     while True:
        
#         if(year%4==0) or (year%100!=0 and year%400==0):
#             return year
#         year+=1
         
# year=2025
# print(leap(year))


# def logger(func): #student
#     def wrapper():
        
        
#     return wrapper


# @logger
# def student(name):
#     return name

# student("asminnn")

#nested loop

# def outer(a):
#     def inner():
#         if(a==1234):
           
#             return  print("access granted")
#         else:
#             return print("access denied")
#     return inner()

# outer(1238)

# num=10
# a=(lambda x: "even" if x%2==0 else"odd")(num)
# print(a)
a=30
b=20
print((lambda x,y: "a is gratter" if x>y else "b is greatest  " "a is smallest" if x<b else"b is smallest")(a,b))